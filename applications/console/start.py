# _*_ coding: utf-8 _*_
from multiprocessing import Process
from multiprocessing import Queue
import time
from psutil import cpu_count

queue = Queue()
message = Queue()


def child_process(q: Queue, msg: Queue):
    while True:
        i = q.get()
        msg.put(f"{i:10}\t{2**i:30}")


if __name__ == "__main__":
    for i in range(cpu_count() * 2):
        process = Process(
            target=child_process,
            args=(
                queue,
                message,
            ),
        )
        process.daemon = True
        process.start()

    for i in range(40):
        queue.put(i)

    time.sleep(100)
    while True:
        m = message.get(timeout=2)
        print(m)
        if message.empty():
            break
