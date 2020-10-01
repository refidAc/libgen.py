import argparse

import requests

from exceptions import NoAvailableMirror
from mirrors import MIRRORS

from multiprocessing.pool import ThreadPool
from threading import Thread


class MirrorFinder(object):
    def __init__(self) -> None:
        self.mirrors = MIRRORS
        self.pool = ThreadPool(processes=50)

    def run(self, search_term: str, non_interactive: bool, zip_file : bool, do_upload : bool, do_convert: bool):
        """Tries to find an active mirror and runs the search on it."""
        try:
            mirror = self.find_active_mirror()
            if mirror is None:
                raise NoAvailableMirror
            mirror(search_term).run(non_interactive,zip_file, do_upload, do_convert)
        except NoAvailableMirror as e:
            print(e)

    # TODO: eliminate this method
    # Maybe use the chain of responsability pattern
    def find_active_mirror(self):
        for (homepage, mirror) in self.mirrors.items():
            r = requests.get(homepage)
            if r.status_code == 200:
                return mirror
        return None


def main():
    p = argparse.ArgumentParser(description='Read more, kids.')
    p.add_argument('-s', '--search', dest='search', required=True, help='search term')
    p.add_argument('-n', '--non-interactive', dest='non_interactive', help='non interactive mode, download first available choice', action='store_true', default=False)
    p.add_argument('-z', '--zip', dest='zip_file', help='archive all downloads into a zipfile', default=False)
    p.add_argument('-u', '--upload', dest='do_upload', help='upload files at the end', default=False)
    p.add_argument('-c', '--convert', dest='do_convert', help='convert all downloads into a zipfile', default=False)
    args = p.parse_args()
    MirrorFinder().run(args.search, args.non_interactive, args.zip_file, args.do_upload, args.do_convert)


if __name__ == '__main__':
    main()
