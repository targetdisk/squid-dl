"""
Fancy parallel downloader for a pre-
retrieved YoutubeDL() info_dict JSON.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡤⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠀⡀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠘⡆⡜⠁⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⣀⣤⡂⠀⠇⠱⠀⡀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⡀⢠⣟⢭⣥⣤⠽⡆⠀⡶⣊⣉⣲⣤⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⡀⠀⠐⠂⠘⠄⣈⣙⡡⡴⠀⠀⠙⣄⠙⣛⠜⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠄⠊⠀⠀⠀⠀⡸⠛⠀⠀⠀⢸⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⢄⣘⣄⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⣇⡀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠈⡟⠒⠲⣄⠀⠀⡰⠇⠖⢄⠀⠀⡹⡇⢀⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⡇⠀⠀⠹⠀⡞⠀⠀⢀⠤⣍⠭⡀⢱⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⠞⠀⠀⢠⡇⠀⠀⠀⠀⠁⠀⢴⠥⠤⠦⠦⡼⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣤⣴⣶⣿⣿⡟⠁⠀⠋⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠑⣠⢤⠐⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠬⠥⣄⠀⠀⠈⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⢀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠦⠤⢤⣄⣀⣠⠤⢿⣶⣶⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀

NOTE: Not my fault if your IP gets rate-
limited or throttled by YouTube.  With
great power comes great responsibility!

ALSO NOTE: Have yet to test on other
video sites besides YouTube...
"""
import argparse
import json as j
from multiprocessing import cpu_count, Process, Queue
from multiprocessing.queues import Empty, Full
import os
from random import randint
from time import sleep
import typing
from yt_dlp import YoutubeDL
from yt_dlp.utils import encodeFilename, sanitize_filename
from yt_dlp.extractor.common import InfoExtractor as IE

from .linode import LinodeProxy
from .proxy import Proxy
from .socks import SocksProxy
from .util import die, eprint, runcmd


def do_download(
    entry_q: Queue,
    opts: argparse.Namespace,
    sub_langs: [str],
    proxy: Proxy = None,
):

    sub_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
    }
    if sub_langs[0] == "all":
        sub_opts["allsubtitles"] = True
    else:
        sub_opts["subtitleslangs"] = sub_langs

    yt_opts = {
        "noprogress": True,
        "http_chunk_size": 10485760,
        "writethumbnail": True,
        "ignoreerrors": True,
        "format_sort": IE.FormatSort.ytdl_default,
        "extractor_args": {
            "youtube": {"player_skip": ["webpage"]},
            "youtubetab": {"skip": ["webpage"]},
        },
    }
    if proxy is not None:
        yt_opts["proxy"] = proxy.proxy_url
    if opts.all_thumbnails:
        yt_opts["write_all_thumbnails"] = True

    y = YoutubeDL({**yt_opts, **sub_opts})
    y_nosubs = YoutubeDL(yt_opts)

    while True:
        try:
            try:
                entry = entry_q.get(block=True, timeout=0.5)
            except Empty:
                break

            try:
                id_dir = entry["id"]
            except TypeError:
                continue

            try:
                os.mkdir(id_dir)
            except FileExistsError:
                pass

            try:
                os.chdir(id_dir)
            except OSError as oserr:
                eprint("[WARN]: Skipping {} due to {}".format(id_dir, oserr))
                continue

            nfo_path = "playlist_entry.json"
            if not (os.path.exists(nfo_path) and os.path.isfile(nfo_path)):
                nfo_file = open(nfo_path, mode="w")
                nfo_file.write(j.dumps(entry, sort_keys=True, indent=2))
                nfo_file.close()

            desc_path = "description"
            if not (os.path.exists(desc_path) and os.path.isfile(desc_path)):
                desc_file = open(desc_path, mode="w")
                desc_file.write(entry["description"])
                desc_file.close()

            dl_url = "https://www.youtube.com/watch?v=" + entry["id"]
            try:
                if entry["tux_get_subs"] is True:
                    y.download([dl_url])
                else:
                    y_nosubs.download([dl_url])
            except KeyError:
                y.download([dl_url])

            os.chdir("..")
            sleep(2)
        except KeyboardInterrupt:
            break

    if proxy is not None:
        if proxy.exclusive:
            print(
                "[INFO]: Cleaning up worker {}'s exclusive proxy".format(
                    os.getpid()
                )
            )
            proxy.cleanup()

    print("[INFO]: Worker {} done...".format(os.getpid()))


def get_entries(entries: dict, entry_q: Queue):
    try:
        for entry in entries:
            while True:
                try:
                    entry_q.put(entry, block=True, timeout=0.2)
                    break
                except Full:
                    pass

    except KeyboardInterrupt:
        pass

    entry_q.close()


def check_subs_done(entry: dict, basename: str, langs: [str] = None) -> bool:
    if langs is None:
        langs = entry["automatic_captions"].keys()

    for lang in langs:
        subbase = basename + "." + lang

        lang_sub_exists = False
        for subentry in entry["automatic_captions"][lang]:
            sfname = subbase + "." + subentry["ext"]
            if os.path.exists(sfname) and os.path.isfile(sfname):
                lang_sub_exists = True
                break
        if not lang_sub_exists:
            return False

    return True


def check_video_done(entry: dict, basename: str) -> bool:
    for ext in (".mp4", ".webm", ".mkv"):
        vfname = basename + ext

        if os.path.exists(vfname) and os.path.isfile(vfname):
            return True

    return False


def check_dl(in_q: Queue, out_q: Queue):
    while True:
        try:
            try:
                entry = in_q.get(block=True, timeout=0.5)
            except Empty:
                break

            try:
                id_dir = entry["id"]
            except TypeError:
                continue

            if os.path.isdir(id_dir):
                try:
                    os.chdir(id_dir)
                except OSError as oserr:
                    eprint(
                        "[WARN]: Skipping {} due to {}".format(id_dir, oserr)
                    )
                    continue
            elif os.path.exists(id_dir):
                eprint(
                    "[WARN]: Not downloading https://youtube.com/watch?v={} "
                    + "because {} exists and is not a directory!"
                )
                continue
            else:
                out_q.put(entry)
                continue

            nfo_path = "playlist_entry.json"
            if not (os.path.exists(nfo_path) and os.path.isfile(nfo_path)):
                os.chdir("..")
                out_q.put(entry)
                continue

            desc_path = "description"
            if not (os.path.exists(desc_path) and os.path.isfile(desc_path)):
                desc_file = open(desc_path, mode="w")
                desc_file.write(entry["description"])
                desc_file.close()

            y = YoutubeDL({"ignoreerrors": True})
            basename = os.path.splitext(
                sanitize_filename(encodeFilename(y.prepare_filename(entry)))
            )[0]
            try:
                if check_subs_done(entry, basename):
                    entry["tux_get_subs"] = False
                else:
                    entry["tux_get_subs"] = True
            except KeyError:
                eprint(
                    "[WARN]: Couldn't find auto subs for {} in info".format(
                        entry["id"]
                    )
                )
                entry["tux_get_subs"] = False

            if not (check_video_done(entry, basename)):
                out_q.put(entry)
                os.chdir("..")
                continue

            os.chdir("..")
        except KeyboardInterrupt:
            break


def testworker(in_q: Queue):
    i = 0
    while not in_q.empty():
        try:
            entry = in_q.get(block=True, timeout=0.5)
        except Empty:
            break
        try:
            i += 1
            print("{}: ".format(i), end="")
            print(entry["id"])
            acs = entry["automatic_captions"]
        except KeyError:
            eprint("couldn't get caps on vid {}".format(entry["id"]))


def workers_alive(workers: [Process]):
    for worker in workers:
        if worker.is_alive():
            return True

    return False


def resume_cleanup(workers: [Process], q_worker: Process):
    print("\n[CLEANUP]: Cleaning up...")

    for worker in workers:
        if worker.is_alive():
            print("[CLEANUP]: Terminating resume worker {}".format(worker.pid))
        worker.terminate()

    print("[CLEANUP]: Terminating queue worker {}".format(worker.pid))
    q_worker.terminate()


def resume_preprocess(entries: [dict]) -> list:
    ncpus = cpu_count()
    n_workers = ncpus if len(entries) >= ncpus else len(entries)

    in_q = Queue(n_workers)
    out_q = Queue(len(entries))
    iq_builder = Process(target=get_entries, args=(entries, in_q))
    workers = []

    try:
        iq_builder.start()

        for n in range(n_workers):
            workers.append(Process(target=check_dl, args=(in_q, out_q)))

        while not in_q.full():
            sleep(0.2)

        for w in workers:
            w.start()

        unfinished_entries = []
        while workers_alive(workers):
            try:
                unfinished_entries.append(out_q.get(block=True, timeout=2))
            except Empty:
                continue
    except KeyboardInterrupt:
        resume_cleanup(workers, iq_builder)
        return []

    if iq_builder.is_alive():
        iq_builder.terminate()
        die("[BUG]: Workers didn't verify whole list! Exiting...")

    return unfinished_entries


def validate_linode_proxy(proxy: LinodeProxy) -> LinodeProxy:
    if not proxy.start():
        eprint(
            "[WARN]: "
            + "Proxy, validation failed, deleting and rebuilding Linode..."
        )
        port = proxy.proxy_port
        proxy.cleanup()
        proxy = LinodeProxy(proxy_port=port)
        return validate_linode_proxy(proxy)
    else:
        print(
            "[INFO]: SOCKS validation succeeded on port {} from ID {}".format(
                proxy.proxy_port, proxy.info["id"]
            )
        )
        return proxy


def cleanup(workers: [Process], linode_proxies: [LinodeProxy]) -> None:
    if len(workers) > 0:
        for worker in workers:
            if worker.is_alive():
                print(
                    "[CLEANUP]: Terminating download worker {}".format(
                        worker.pid
                    )
                )
                worker.terminate()

    if len(linode_proxies) > 0:
        print("[CLEANUP]: Deleting Linode proxies...")
        for proxy in linode_proxies:
            proxy.cleanup()


def parse_args(args: list, name: str):
    parser = argparse.ArgumentParser(prog=name)

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-L",
        "--linode-proxy",
        action="store_true",
        help="Give each worker a Linode SOCKS proxy.  Assumes you have already "
        + "setup the linode-cli with an API key and default settings.  See "
        + "https://www.linode.com/docs/guides/linode-cli/ "
        + "for more information.",
    )
    group.add_argument(
        "-S",
        "--socks-proxy",
        type=str,
        default=None,
        help="Run workers through a SOCKS proxy.  Requires a fully-qualified "
        + 'proxy URL (e.g. "socks5://user:pass@hostname:port" or '
        + '"socks5://hostname:port").\n'
        + "Be mindful of your shell's history file when entering passwords on "
        + "the command line.  If this script encounters a proxy that requires "
        + "authentication, it will prompt the user for a password "
        + "interactively, as well.",
    )
    parser.add_argument(
        "-p",
        "--proxy-base-port",
        type=int,
        default=1337,
        help="Port number that local Linode-powered proxy ports are derived "
        + "from, does nothing without "
        + "enabling --linode-proxy (aka. -L).",
    )
    parser.add_argument(
        "--resume-dump",
        action="store_true",
        help="Dump resume info_dict to JSON (for debugging).",
    )
    parser.add_argument(
        "-n",
        "--n-workers",
        type=int,
        default=8,
        help="Number of parallel download workers",
    )
    parser.add_argument(
        "-l",
        "--subtitle-langs",
        type=str,
        default="en",
        help="Comma-delimited list of subtitle languages to download; "
        + 'pass "all" to download all auto captions.  '
        + 'Downloads "en" subtitles by default.',
    )
    parser.add_argument(
        "-T",
        "--all-thumbnails",
        action="store_true",
        help="Download all thumbnails instead of just the best one.",
    )
    parser.add_argument(
        "playlist_json",
        type=argparse.FileType("r"),
        help="JSON-ified playlist file to download",
    )

    return parser.parse_args(args=args)

def check_keys():
    key_path = os.path.abspath("./proxy_key")
    pubkey_path = os.path.abspath(key_path + ".pub")
    if not (
        os.path.isfile(pubkey_path)
        or os.path.isfile(os.path.splitext(pubkey_path)[0])
    ):
        print("[INFO]: Creating SSH key for Linode proxying...")
        print(runcmd('ssh-keygen -f "{}" -N ""'.format(key_path)).decode())

def main(args: [str], name: str) -> int:
    opts = parse_args(args=args, name=name)
    sub_langs = opts.subtitle_langs.split(",")
    n_workers = opts.n_workers

    info_dict = j.loads(opts.playlist_json.read())
    opts.playlist_json.close()

    print("[INFO]: Starting squid-dl...")

    dirname = sanitize_filename(info_dict["title"])
    print('[INFO]: saving videos to "{}" directory'.format(dirname))
    if not (os.path.exists(dirname) and os.path.isdir(dirname)):
        os.mkdir(dirname)
    else:
        playlist_size = len(info_dict["entries"])

        info_dict["entries"] = resume_preprocess(info_dict["entries"])
        if len(info_dict["entries"]) == 0:
            print("[WARN]: Nothing left to download, exiting...")
            return 1

        print(
            "Resuming download of {}/{} videos...".format(
                len(info_dict["entries"]), playlist_size
            )
        )
        if opts.resume_dump:
            rdump = open(info_dict["title"] + ".resume.json", mode="w")
            rdump.write(j.dumps(info_dict, sort_keys=True, indent=2))
            rdump.close()

    n_entries = len(info_dict["entries"])
    n_workers = n_workers if n_workers < n_entries else n_entries
    entry_q = Queue(n_workers)
    entry_getter = Process(
        target=get_entries, args=(info_dict["entries"], entry_q)
    )
    entry_getter.start()

    base_port = 1337
    workers = []
    linode_proxies = []
    if opts.socks_proxy is not None:
        socks_proxy = SocksProxy(url=opts.socks_proxy)
    try:
        for n in range(n_workers):
            port = base_port + n

            if opts.linode_proxy:
                check_keys()
                linode_proxies.append(
                    LinodeProxy(proxy_port=port, pubkey_path=pubkey_path)
                )
                worker_args = (entry_q, opts, sub_langs, linode_proxies[n])
            elif opts.socks_proxy is not None:
                worker_args = (entry_q, opts, sub_langs, socks_proxy)
            else:
                worker_args = (entry_q, opts, sub_langs)

            workers.append(
                Process(
                    target=do_download,
                    args=worker_args,
                )
            )

        if len(linode_proxies) > 0:
            if not (
                os.path.isfile(pubkey_path)
                or os.path.isfile(os.path.splitext(pubkey_path)[0])
            ):
                die(
                    '[ERROR]: SSH key file "{}" does not exist!'.format(
                        pubkey_path
                    )
                )
            print("[INFO]: Waiting for Linodes to come online", end="")
            nodes_to_ping = list(range(n_workers))
            while len(nodes_to_ping) > 0:
                print(".", end="")
                temp_list = []
                for proxy_idx in nodes_to_ping:
                    if linode_proxies[proxy_idx].get_status() != "running":
                        temp_list.append(proxy_idx)
                    sleep(0.2)
                nodes_to_ping = temp_list
        print()

        while not entry_q.full():
            sleep(0.2)

        os.chdir(dirname)

        for i in range(n_workers):
            if len(linode_proxies) > 0:
                linode_proxies[i] = validate_linode_proxy(linode_proxies[i])
                seconds = randint(0, 1)
            else:
                seconds = randint(1, 6)
            workers[i].start()
            sleep(seconds)

        while workers_alive(workers):
            sleep(0.2)

    except KeyboardInterrupt:
        eprint("\n[CLEANUP]: Interrupted, cleaning up...")
        cleanup(workers, linode_proxies)
        if entry_getter.is_alive():
            print(
                "[CLEANUP]: Terminating queue worker {}".format(
                    entry_getter.pid
                )
            )
            entry_getter.terminate()
        return 1

    print("[INFO]: All done!")
    cleanup(workers, linode_proxies)

    return 0
