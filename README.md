<p align="center">
  <img alt="squid-dl logo" src="./img/squid-dl.no-outline.web.svg">
  <h1 align="center">squid-dl</h1>
</p>

<p align="center">
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://github.com/tuxlovesyou/squid-dl/blob/main/LICENSE">
    <img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg">
  </a>
</p>

`squid-dl` is a massively parallel
[yt-dlp](https://github.com/yt-dlp/yt-dlp)-based YouTube downloader.

## Installation
Run the `setup.py`, which will install `squid-dl` and its two dependencies:
`linode-cli` and `yt-dlp`.
```
$ python3 setup.py install
```

### Linode Setup
If you want to use the Linode SOCKS proxy feature, be sure to configure the
`linode-cli` first:
```
$ linode-cli configure --token
```

Follow the onscreen instructions and be sure to set sensible defaults.  The
default region for new Linodes that you pick here is where your proxies will
live.  For more information, see
[this page](https://www.linode.com/docs/guides/linode-cli/) on Linode's website.

## Usage
To download a playlist, first fetch its metadata with `squidson`:
```
(.venv) $ squidson 'https://www.youtube.com/playlist?list=PLhI42_YpLVHvYqvjniSp7lhAM55K4fllO'
[youtube:tab] PLhI42_YpLVHvYqvjniSp7lhAM55K4fllO: Downloading webpage
[youtube:tab] PLhI42_YpLVHvYqvjniSp7lhAM55K4fllO: Downloading API JSON with unavailable videos
[download] Downloading playlist: Programming
[youtube:tab] playlist Programming: Downloading 12 videos
[download] Downloading video 1 of 12
[youtube] Wp9XD5FKZ2c: Downloading webpage
[youtube] Wp9XD5FKZ2c: Downloading android player API JSON
...
[download] Downloading video 12 of 12
[youtube] CIpfoMKqPAg: Downloading webpage
[youtube] CIpfoMKqPAg: Downloading android player API JSON
[youtube] CIpfoMKqPAg: Downloading MPD manifest
[youtube] CIpfoMKqPAg: Downloading MPD manifest
[download] Finished downloading playlist: Programming
[INFO]: Writing JSON-ified playlist info_dict to "Programming.json"
```

Now that you have the playlist `.json` file, you can download it with
`squid-dl`.  Use the `-n` flag to tell `squid-dl` how many workers you'd like to
spawn downloading videos at once (the default is 8 workers).  In this 12-video
playlist example, we'll spawn 12 workers:
```
(.venv) $ squid-dl -n 12 Programming.json

[INFO]: Starting squid-dl...
[INFO]: saving videos to "Programming" directory

...
[download] Download completed
[download] Download completed
[download] Download completed
[INFO]: Worker 80214 done...
[INFO]: Worker 80319 done...
[download] Download completed
[INFO]: Worker 80150 done...
[INFO]: Worker 80248 done...
[download] Download completed
[INFO]: Worker 80219 done...
[INFO]: Worker 80109 done...
[INFO]: Worker 80341 done...
[download] Download completed
[INFO]: Worker 80193 done...
[download] Download completed
[INFO]: Worker 80117 done...
[INFO]: All done!
```

For more information see the built-in help by running `squid-dl -h`.

## Linode Proxying
With the `-L` option, you can run each worker through its own Linode-powered
SSH-tunneled SOCKSv5 proxy!  `squid-dl` will make an temporary SSH key in
the current working directory and then get to work spinning up Linodes and
downloading your videos:
```
(.venv) anon@fire-crotch:~/butter/youtube/btr$ squid-dl -L Mem.json

[INFO]: Creating SSH key for Linode proxying...
Generating public/private rsa key pair.
Your identification has been saved in /home/anon/fuse/butter-anon/youtube/btr/proxy
_key
Your public key has been saved in /home/anon/fuse/butter-anon/youtube/btr/proxy_key
.pub
The key fingerprint is:
SHA256:cSns+aK0l7xS+fRSXRdqmc5DXkT5pIQsDV8/Ql526vg anon@fire-crotch
The key's randomart image is:
+---[RSA 3072]----+
|          .+ oo+o|
|       .  .o*.+*o|
|        + o..+*++|
|       . =   Oo.=|
|        S.  B.o..|
|        o.. .*.  |
|      .o.+.o  E  |
|     ..o+.o .    |
|      oo.. .     |
+----[SHA256]-----+

[INFO]: Starting squid-dl...
[INFO]: saving videos to "Mems" directory
[INFO]: Created Linode 30970792.
[INFO]: Waiting for Linodes to come online...........................

[INFO]: Starting proxy on port 1337 with Linode 30970792
Warning: Permanently added '45.79.47.110' (ED25519) to the list of known hosts.
[INFO]: SOCKS validation succeeded on port 1337 from ID 30970792
[youtube] fIdfGtG7Isg: Downloading android player API JSON
[youtube] fIdfGtG7Isg: Downloading iframe API JS
[youtube] fIdfGtG7Isg: Downloading player 03869671
[youtube] fIdfGtG7Isg: Downloading web player API JSON
[youtube] fIdfGtG7Isg: Downloading MPD manifest
[youtube] fIdfGtG7Isg: Downloading MPD manifest
[youtube] fIdfGtG7Isg: Downloading initial data API JSON
[info] fIdfGtG7Isg: Downloading 1 format(s): 22
[info] Downloading video thumbnail ...
[info] Writing video thumbnail to: Plankton goes to an anime convention [fIdfGtG7Is
g].webp
[download] Destination: Plankton goes to an anime convention [fIdfGtG7Isg].mp4
[download] Download completed
[INFO]: Cleaning up worker 83832's exclusive proxy
[CLEANUP]: Deleted Linode 30970792.
[INFO]: Worker 83832 done...
[INFO]: All done!
[CLEANUP]: Deleting Linode proxies...
```

## Bugs
If you encounter any issues running `squid-dl`, please create an issue
[on GitHub](https://github.com/tuxlovesyou/squid-dl/issues/new/choose).

This software has only tested on Linux so far (patches welcome).
