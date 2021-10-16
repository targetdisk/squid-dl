#!/usr/bin/env python3
from squid_dl.linode import LinodeProxy
from squid_dl.util import die, eprint
from time import sleep


def main():
    """
    A simple LinodeProxy class example.  This should work once you have setup
    linode-cli.  Only tested with Linode CLI settings that select Arch Linux
    image by default.  YMMV with other distro images.
    """
    proxy = LinodeProxy(debug=True)
    while proxy.get_status() != "running":
        sleep(1)

    if not proxy.start(headless=False):
        proxy.cleanup()
        print(proxy.proxy_proc.stdout.read().decode())
        eprint(proxy.proxy_proc.stderr.read().decode())
        die("BAD PROXY!")

    sleep(10)
    # proxy.cleanup()
    proxy.proxy_proc.terminate()
    print(proxy.proxy_proc.stdout.read().decode())
    eprint(proxy.proxy_proc.stderr.read().decode())


if __name__ == "__main__":
    main()
