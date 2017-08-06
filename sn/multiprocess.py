import multiprocessing
import threads

def process_link_crawler(args,**kwargs):
    num_cpus = multiprocessing.cpu_count()
    print( 'Starting {} processes'.format(num_cpus))
    process = []
    for i in range(num_cpus):
        p = multiprocessing.Process(target=threads.threaded_crawler,
                                    args=[args],kwargs=kwargs)
        p.start()
        process.append(p)
    for p in process:
        p.join()
