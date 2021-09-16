import gzip
import shutil
import os
import argparse
from typing import Optional


def gzip_compress(fileroot: str, fileurl: str, outroot: str, delete: bool) -> Optional[str]:
    # nekomprimuj uz zkomprimovane
    if '.gz' in fileurl:
        return
    fullurl = rf'{fileroot}/{fileurl}'
    outurl = rf'{outroot}/{fileurl}.gz'
    # nejefektivnejsi zpusob primo z dokumentace
    with open(fullurl, 'rb') as f_in:
        with gzip.open(outurl, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    # smaz original
    if delete:
        os.remove(fullurl)
    return outurl


if __name__ == '__main__':
    # parser pro versatilni argumenty pri volani skriptu
    parser = argparse.ArgumentParser(description='Gzips all files in a given directory.')
    parser.add_argument('zipdir', metavar='zipdir', type=str, default='',
                        help='The directory to gzip up (Default is root).')
    parser.add_argument('--list', '-l', dest='listprint', action='store_const', const=True, default=False,
                        help='List out the gzipped files (Default is no).')
    parser.add_argument('--ndel', '-nd', dest='delete', action='store_const', const=False, default=True,
                        help='Don\'t delete the original files (Default is yes).')
    parser.add_argument('--outdir', '-o', metavar='outdir', type=str,
                        help='Specify an output directory (Default is same as zipdir).')
    args = parser.parse_args()
    # zkontroluj, ze vstupni slozka existuje
    if not os.path.isdir(args.zipdir):
        print('Error: That directory doesn\'t exist.')
    else:
        # deklaruj vystupni slozku
        if not args.outdir:
            outdir = args.zipdir
        else:
            outdir = args.outdir
            # pokud slozka neexistuje, zaloz
            if not os.path.isdir(outdir):
                os.mkdir(outdir)
        # projde vsechny soubory ve slozce a na kazdem provede funkci
        for r, d, f in os.walk(args.zipdir):
            for file in f:
                gzipurl = gzip_compress(r, file, outdir, args.delete)
                if gzipurl and args.listprint:
                    print(gzipurl)
