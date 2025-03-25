import threading
import urllib.request as urllib2
import time

class FetchUrls(threading.Thread):
    """
    Thread checking URL's
    """

    def __init__(self, urls, output, lock):
        """
        Constructor

        @param urls list of urls to check
        @param output file to write urls output
        """

        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock

    def run(self):
        """
        Thred run method. Check URLs one by one
        """
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            try:
                d = urllib2.urlopen(req)
            except (urllib2.URLError) as e:
                print(f'URL {url} failed: {e.reason}')
            self.lock.acquire()
            print(f'lock acquired by {self.name}')
            self.output.write(str(d.read()))
            print(f'write done by {self.name}')
            print(f'lock relased by {self.name}')
            self.lock.release()
            print(f'URL {url} feched by {self.name}')

def main():
    urls1 = ['http://www.google.com', 'http://www.facebook.com']
    urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']

    lock = threading.Lock()
    f = open('outputLock.txt', 'w+')
    t1 = FetchUrls(urls1, f, lock)
    t2 = FetchUrls(urls2, f, lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__ == '__main__':
    main()
