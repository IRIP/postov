import urllib2
from os.path import join, exists, isfile, splitext
import sys
import logging

def download(urllist, root_dir):
    """
        Загрузка файлов по ссылке
    """
    for url, name, subdir in urllist:
        if name is None:
            name = url.split('/')[-1]
        dir = join(root_dir, subdir)
        fname = join(dir, name)
        u = urllib2.urlopen(url)

        #file might exist, so add (1) or (2) etc
        counter = 1
        if exists(fname) and isfile(fname):
            name, ext = splitext(fname)
            fname = name + " ({})".format(counter) + ext
        while exists(fname) and isfile(fname):
            counter += 1
            name, ext = splitext(fname)
            fname = name[:-4] + " ({})".format(counter) + ext
        logging.info(u"Start dl: {}".format(fname))
        f = open(fname, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        sys.stdout.write("Загружаю: %s (%s kb)\n" % (fname.encode('ascii', 'ignore'),
                                              file_size/1024))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            sys.stdout.write(status)

        f.close()
        logging.info(u" End  dl: {}".format(fname))


def make_dir(base_dir, name):
    """Make new dir into base dir, return concatenation"""
    if path.exists(base_dir) and path.isdir(base_dir):
        directory = path.join(base_dir, name)
        if path.exists(directory) and path.isdir(directory):
            #raise RuntimeError("Directory already exists: {}".format(directory))
            return directory
        else:
            makedirs(directory)
            return directory
    else:
        raise RuntimeError("Directory does not exist: {}".format(base_dir))
