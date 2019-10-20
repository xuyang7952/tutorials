# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import threading

# def main():
#     ## 线程数，线程池，当前的线程
#    print(threading.active_count())
#    print(threading.enumerate()) # see the thread list
#    print(threading.current_thread())

def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job,)
    thread.start()
if __name__ == '__main__':
    main()
