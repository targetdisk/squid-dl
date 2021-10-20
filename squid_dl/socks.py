"""
Generic SOCKS proxy support.
      ⢀⣀⣤⣴⣶⣶⣾⣿⣷⣶⣶⣦⣄⡀⠀⠀⠀
   ⠀⢠⣴⣿⣿⣿⣿⣿⣭⣭⣭⣭⣭⣿⣿⣿⣿⣧⣀⠀
   ⢰⣿⣿⣿⣿⣿⣯⣿⡶⠶⠶⠶⠶⣶⣭⣽⣿⣿⣷⣆
   ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⠈⢿⣿⣿⡿⠋⠉⠁⠈⠉⠛⠉⠀⠀⠀⠈⠻⣿⡿⠃
   ⠀⠀⠀⠉⠁⠀⢴⣐⢦⠀⠀⠀⣴⡖⣦⠀⠀⠈⠀⠀
   ⠀⠀⠀⠀⠀⠀⠈⠛⠋⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⣀⠀⠀⠀⢀⡀⠀⠀⠀⠀
   ⠀⠀⢀⡔⣻⣭⡇⠀⣼⣿⣿⣿⡇⠦⣬⣟⢓⡄⠀⠀
   ⠀⠀⠀⠉⠁⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠉⠉⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠟⠁⠀⠀
"""

from getpass import getpass
import json as j
import typing
import os
import socket
import struct
from urllib.parse import unquote_plus, urlparse
from yt_dlp.socks import ProxyType, Socks4Error, Socks5Error, sockssocket

from .proxy import Proxy
from .util import die, eprint


class SocksUnknownSchemeError(Exception):
    pass


def test_proxy(host: str, port: int):
    sen = struct.pack("BBB", 0x05, 0x01, 0x00)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except ConnectionRefusedError as e:
        die(
            '[ERROR]: Got "{}" when connecting to {} on port {}'.format(
                e, host, port
            )
        )

    for n in range(3):
        s.sendall(sen)
        try:
            data = s.recv(2)
            break
        except socket.timeout:
            if n == 2:
                eprint("[ERROR]: SOCKS proxy timed out after three attempts!")
                exit(1)

    s.close()
    return struct.unpack("BB", data)  # (version, auth)


class SocksProxy(Proxy):
    """
    The ``params`` dict can either contain the single element ``url`` or:
      * ``host`` (string)
      * ``port`` (string)
      * ``scheme`` (string, optional)
      * ``user`` (string, optional)
      * ``password`` (string, optional)
    """

    def __init__(
        self, url: str = None, params: dict = None, debug: bool = False
    ):
        self.debug = debug

        if url is not None:
            self.init_from_url(url)
        else:
            self.init_from_params(params)

        self.setup()

    def get_socks_proxytype(self):
        if self.scheme.lower() == "socks5":
            return ProxyType.SOCKS5
        elif self.scheme.lower() in ("socks", "socks4"):
            return ProxyType.SOCKS4
        elif self.scheme.lower() == "socks4a":
            return ProxyType.SOCKS4A
        else:
            eprint("[ERROR]: Unknown scheme in proxy URL!")
            raise SocksUnknownSchemeError

    def init_from_url(self, url: str):
        self.proxy_url = url
        url_pieces = urlparse(url)

        self.scheme = url_pieces.scheme
        self.host = url_pieces.hostname
        self.port = url_pieces.port or 1080
        self.user = url_pieces.username
        self.password = url_pieces.password

    def init_from_params(self, params: dict):
        self.host = params["host"]
        self.port = params["port"] if "port" in params else 1080
        if "user" in params and "password" in params:
            self.user = params["user"]
            self.password = params["password"]
            authstr = self.user + ":" + self.password + "@"
        else:
            self.user = None
            self.password = None
            authstr = ""
        self.scheme = (
            params["scheme"].lower() if "scheme" in params else "socks5"
        )
        self.proxy_url = (
            self.scheme + "://" + authstr + self.host + ":" + str(self.port)
        )

    def get_creds(self):
        self.username = input("SOCKS username: ")
        self.password = getpass(prompt="SOCKS password: ")
        self.proxy_url = (
            self.scheme
            + "://"
            + self.username
            + ":"
            + self.password
            + "@"
            + self.host
            + ":"
            + str(self.port)
        )

    def setup(self):
        version, auth = test_proxy(host=self.host, port=self.port)
        if auth != 0 and (self.user is None or self.password is None):
            self.get_creds()

        def unquote_if_non_empty(s):
            if not s:
                return s
            return unquote_plus(s)

        proxy_args = (
            self.get_socks_proxytype(),
            self.host,
            self.port or 1080,
            True,  # Remote DNS
            unquote_if_non_empty(self.username),
            unquote_if_non_empty(self.password),
        )

        testsock = sockssocket()
        testsock.setproxy(*proxy_args)
        try:
            testsock.connect((self.host, self.port))
            testsock.close()
        except (Socks4Error, Socks5Error) as e:
            die("[ERROR]: {}: {}".format(type(e).__name__, e))
