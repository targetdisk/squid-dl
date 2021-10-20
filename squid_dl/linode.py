"""
You ever wanted to spawn n proxies?
   ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠠⠤⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⣀⢤⡒⠉⠁⠀⠒⢂⡀⠀⠀⠀⠈⠉⣒⠤⣀⠀⠀⠀⠀
   ⠀⠀⣠⠾⠅⠈⠀⠙⠀⠀⠀⠈⠀⠀⢀⣀⣓⡀⠉⠀⠬⠕⢄⠀⠀
   ⠀⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠶⢦⡀⠑⠀⠀⠀⠀⠈⢧⠀
   ⠀⡇⠀⠀⠀⠀⠀⢤⣀⣀⣀⣀⡀⢀⣀⣀⠙⠀⠀⠀⠀⠀⠀⢸⡄
   ⠀⢹⡀⠀⠀⠀⠀⡜⠁⠀⠀⠙⡴⠁⠀⠀⠱⡄⠀⠀⠀⠀⠀⣸⠀
   ⠀⠀⠱⢄⡀⠀⢰⣁⣒⣒⣂⣰⣃⣀⣒⣒⣂⢣⠀⠀⠀⢀⡴⠁⠀
   ⠀⠀⠀⠀⠙⠲⢼⡀⠀⠙⠀⢠⡇⠀⠛⠀⠀⣌⣀⡤⠖⠉⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⢸⡗⢄⣀⡠⠊⠈⢦⣀⣀⠔⡏⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠈⡇⠀⢰⠁⠀⠀⠀⢣⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⣠⠔⠊⠉⠁⡏⠀⠀⠀⠀⠘⡆⠤⠿⣄⣀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⣧⠸⠒⣚⡩⡇⠀⠀⠀⠀⠀⣏⣙⠒⢴⠈⡇⠀⠀⠀⠀
   ⠀⠀⠀⠀⠈⠋⠉⠀⠀⢳⡀⠀⠀⠀⣸⠁⠈⠉⠓⠚⠁⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠛⠛
      Well, here you go.
"""

import json as j
from os.path import splitext
import socket
import struct
import subprocess
from time import sleep
import typing

from .proxy import Proxy
from .util import eprint, runcmd


class LinodeProxy(Proxy):
    user_made = False

    def __init__(
        self,
        pubkey_path: str = "proxy_key.pub",
        proxy_port: int = 1337,
        proxy_user: str = "boing",
        debug: bool = False,
        exclusive: bool = True,
    ):
        try:
            self.proxy_port = proxy_port
            self.proxy_user = proxy_user
            self.pubkey_path = pubkey_path
            self.debug = debug
            self.exclusive = exclusive

            self.proxy_url = "socks5://127.0.0.1:" + str(self.proxy_port)

            self.ssh_prefix = (
                'ssh -o "UserKnownHostsFile=/dev/null" '
                + '-o "StrictHostKeyChecking=no" -i '
                + splitext(self.pubkey_path)[0]
                + " "
            )
            pubfile = open(self.pubkey_path, mode="r")
            self.pubkey = pubfile.readline().rstrip()
            pubfile.close()

            self.passwd = runcmd(
                "echo $(cat /dev/random | strings | head -c 512 | "
                + "grep -oE '[a-zA-Z0-9#%!]') | sed 's/\s//g' | head -c 32;"
            ).decode()

            create_cmd = (
                "linode-cli --json linodes create "
                + "--image linode/arch "
                + "--authorized_keys "
                + '"'
                + self.pubkey
                + '"'
                + ' --root_pass "'
                + self.passwd
                + '"'
            )
            self.info = j.loads(runcmd(create_cmd).decode())[0]
            print("[INFO]: Created Linode {}.".format(self.info["id"]))
        except KeyboardInterrupt:
            self.cleanup()

    def find_linode(self) -> bool:
        linodes = j.loads(runcmd("linode-cli --json linodes list").decode())

        for linode in linodes:
            if linode["id"] == self.info["id"]:
                return True
        return False

    def cleanup(self) -> None:
        if hasattr(self, "proxy_proc"):
            self.proxy_proc.terminate()

        if hasattr(self, "info"):
            if self.find_linode():
                print(
                    runcmd(
                        "linode-cli --json linodes delete "
                        + str(self.info["id"])
                    ).decode(),
                    end="",
                )
                print("[CLEANUP]: Deleted Linode {}.".format(self.info["id"]))
                delattr(self, "info")

    def get_info(self) -> None:
        self.info = j.loads(
            runcmd(
                "linode-cli --json linodes view " + str(self.info["id"])
            ).decode()
        )[0]

    def get_status(self) -> str:
        self.get_info()
        return self.info["status"]

    def setup_user(self) -> None:
        """
        This will probably break on other distros that assign new accounts to
        the `users` primary group instead of one derived from their user name.
        (Patches welcome!)
        """
        user_cmd = (
            "useradd -m "
            + self.proxy_user
            + "; "
            + "mkdir /home/"
            + self.proxy_user
            + "/.ssh; "
            + "touch /home/"
            + self.proxy_user
            + "/.ssh/authorized_keys; "
            + "chown -R "
            + self.proxy_user
            + ":"
            + self.proxy_user  # change to "users" if using Red Hat/Fedora
            + " /home/"
            + self.proxy_user
            + "/.ssh; "
            + "chmod 700 /home/"
            + self.proxy_user
            + "/.ssh; "
            + "chmod 600 /home/"
            + self.proxy_user
            + "/.ssh/authorized_keys; "
            + "cat ~/.ssh/authorized_keys >> /home/"
            + self.proxy_user
            + "/.ssh/authorized_keys"
        )
        full_cmd = (
            self.ssh_prefix
            + "root@"
            + self.info["ipv4"][0]
            + " '"
            + user_cmd
            + "'"
        )
        if self.debug:
            print(full_cmd)

        print(runcmd(full_cmd).decode())
        self.user_made = True

    def test_proxy(self) -> bool:
        sen = struct.pack("BBB", 0x05, 0x01, 0x00)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        try:
            s.connect(("127.0.0.1", self.proxy_port))
        except ConnectionRefusedError as e:
            eprint(
                "[WARN]: Linode {} SOCKS proxy on {} got {}".format(
                    self.info["id"], self.proxy_port, e
                )
            )
            return False

        for n in range(3):
            s.sendall(sen)
            try:
                data = s.recv(2)
                break
            except socket.timeout:
                if n == 2:
                    eprint(
                        "[ERROR]: Linode SOCKS timed out after three attempts!",
                    )
                    return False

        version, auth = struct.unpack("BB", data)
        if version == 5 and auth == 0:
            return True
        else:
            eprint("[WARN]: SOCKSv5 proxy anomaly!")
            return False

    def start(self, headless: bool = True) -> bool:
        if not self.user_made:
            self.setup_user()

        verbose_ssh = ""
        if self.debug:
            verbose_ssh = "-v "

        proxy_cmd = (
            self.ssh_prefix
            + "-D "
            + str(self.proxy_port)
            + " -NT "
            + verbose_ssh
            + self.proxy_user
            + "@"
            + self.info["ipv4"][0]
        )
        if self.debug:
            print(proxy_cmd)

        print(
            "[INFO]: Starting proxy on port {} with Linode {}".format(
                self.proxy_port, self.info["id"]
            )
        )
        if headless is True:
            self.proxy_proc = subprocess.Popen(proxy_cmd, shell=True)
        else:
            self.proxy_proc = subprocess.Popen(
                proxy_cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        sleep(2)

        return self.test_proxy()
