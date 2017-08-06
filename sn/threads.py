import threading
import time
max_threads = 10

carwl_url = ['www.baidu.com','www.google.com']
threads = []

def dowmLoad():
    pass

def process_queue():
    while True:
        try:
            url = carwl_url.pop()
        except IndexError :
            break
        else:
            html = dowmLoad()
            pass
def threaded_crawler():
    while threads or carwl_url:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
            while len(threads) < max_threads and carwl_url:
                thread = threading.Thread(target=process_queue)

                thread.setDaemon(True)
                thread.start()
                threads.append(thread)
            time.sleep(1)

