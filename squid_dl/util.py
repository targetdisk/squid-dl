#!/usr/bin/env python3
import subprocess
from sys import stderr as STDERR
import typing


def eprint(errmsg):
    print(errmsg, file=STDERR)


def die(errmsg, stat: int = 1):
    """Prints message and exits Python with a status of stat."""
    eprint(errmsg)
    exit(stat)


def runcmd(args):
    """
    Run a given program/shell command and return its output.

    Error Handling
    ==============
    If the spawned proccess returns a nonzero exit status, it will print the
    program's ``STDERR`` to the running Python iterpreter's ``STDERR``.
    """
    proc = subprocess.Popen(
        args,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        if proc.wait() == 1:
            print(proc.stdout.read().decode())
            eprint(proc.stderr.read().decode())

        return proc.stdout.read()
    except KeyboardInterrupt:
        proc.terminate()
        return b""

