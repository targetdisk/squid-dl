from setuptools import setup

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

# install_requires sucks, I don't know why and I really
# don't care, so I do this:
pipmain(["install", "-r", "requirements.txt"])

scripts = ["scripts/squid-dl", "scripts/squidson"]

setup(
    name="squid-dl",
    version="0.9",
    author="Andrea Rogers (@targetdisk)",
    description="Massively parallel YouTube downloader using yt-dlp",
    author_email="targetdisk one three nine four at g mail dot com",
    url="https://github.com/targetdisk/squid-dl",
    packages=["squid_dl"],
    include_package_data=True,
    scripts=scripts,
)
