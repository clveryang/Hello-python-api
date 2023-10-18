# coding:utf-8
import threading
from queue import Queue
"""
    Queue的使用
"""

def job(l, q):
    try:
        for i in range(5):
            l[i] = l[i] ** 2
        q.put(l)
    except:
        q.put(l)
        print('error')


def multithreading():
    # 创建队列
    q = Queue()
    # 线程列表
    threads = []
    # 二维列表
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [6, 6, 6]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    #对所有线程进行阻塞
    for thread in threads:
        thread.join()
    results = []
    # 将新队列中的每个元素挨个放到结果列表中
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == "__main__":
    multithreading()
