#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 5 Assignment

import csv
import Queue
import time

amazon_url_csv = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'

def downloadData(url=str):
    """This function reads and prints the contents located at the url."""
    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()
    print(html)

downloadData(amazon_url_csv)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# class Server:
#     def __init__(self, ppm):
#         self.page_rate = ppm
#         self.current_task = None
#         self.time_remaining = 0
#
#     def tick(self):
#         if self.current_task != None:
#             self.time_remaining = self.time_remaining - 1
#             if self.time_remaining <= 0:
#                 self.current_task = None
#
#     def busy(self):
#         if self.current_task != None:
#             return True
#         else:
#             return False
#
#     def start_next(self, new_task):
#         self.current_task = new_task
#         self.time_remaining = new_task.get_pages() * 60/self.page_rate
#
# class Request:
#     def __init__(self, time):
#         self.timestamp = time
#         self.pages = random.randrange(1, 21)
#
#     def get_stamp(self):
#         return self.timestamp
#     def get_pages(self):
#         return self.pages
#     def wait_time(self, current_time):
#         return current_time - self.timestamp
#
#     def simulation(num_seconds, pages_per_minute):
#         lab_printer = Printer(pages_per_minute)
#         print_queue = Queue()
#         waiting_times = []
#         for current_second in range(num_seconds):
#             if new_print_task():
#                 task = Task(current_second)
#                 print_queue.enqueue(task)
#
#             if (not lab_printer.busy()) and (not print_queue.is_empty()):
#                 next_task = print_queue.dequeue()
#                 waiting_times.append(next_task.wait_time(current_second))
#                 lab_printer.startNext(next_task)
#
#             lab_printer.tick()
#
#         average_wait = sum(waiting_times) / len(waiting_times)
#         print("Average Wait %6.2f secs %3d tasks remaining."
#             %(average_wait, print_queue.size()))
#
#     def new_print_task():
#         num = random.randrange(1, 181)
#         if num == 180:
#             return True
#         else:
#             return False
#
#         for i in range(10):
#             simulation(3600, 5)

#simulateOneServer() = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'


#start = time.time()
# end = time.time()
# return end-start


#def simulateOneServer():
#"""This function prints the average wait time a request was on the server before it was processed."""


#def main(--file, --servers = int):


#if __name__ == "__main__":
    #main()