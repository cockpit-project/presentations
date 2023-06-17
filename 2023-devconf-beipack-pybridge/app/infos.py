import getpass
import platform
import shlex
import sys


def user():
    return getpass.getuser()


def hostname():
    return platform.node()


def os_pretty_name():
    with open('/etc/os-release') as file:
        attrs = dict(line.split('=') for line in shlex.split(file))
        return attrs['PRETTY_NAME']


def pyver():
    return sys.version
