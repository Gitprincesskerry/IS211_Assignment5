#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 5 Assignment

import csv
import Queue
import urllib2

amazon_url_csv = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'

def downloadData(url=str):
    """This function reads and prints the contents located at the url."""
    response = urllib2.urlopen(url)
    html = response.read()

    html = html.split("\r\n")
    for x in range(0, len(html)):
        html[x] = html[x].split(',')
    return html

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


class Server:
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_processing_time()

class Request:
    def __init__(self, time, file, pt):
        self.timestamp = time
        self.filename = file
        self.processingtime = pt

    def get_stamp(self):
        return self.timestamp

    def get_filename(self):
        return self.filename

    def get_processing_time(self):
        return self.processingtime

def simulateOneServer(filename):
    temp_server = Server()
    temp_queue = Queue()
    waiting_times = []

    kerry_temp_list = downloadData(filename)

    for current_task in kerry_temp_list:
        task = Request(int(current_task[0]), current_task[1], int(current_task[2]))
        temp_queue.enqueue(task)

        if (not temp_server.busy()) and (not temp_queue.is_empty()):
            next_task = temp_queue.dequeue()

            waiting_times.append(next_task.processingtime)
            temp_server.start_next(next_task)

        temp_server.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."
        %(average_wait, temp_queue.size()))

def simulateManyServers(filename, servers):
    kerry_temp_list = downloadData(filename)

    tempservers = []
    tempqueues = []
    tempwaitingtimes = []

    for x in range(servers):
        tempservers.append(Server())
        tempqueues.append(Queue())
        tempwaitingtimes.append([])

    counter = 0
    for current_task in kerry_temp_list:
        task = Request(int(current_task[0]), current_task[1], int(current_task[2]))
        tempqueues[counter%servers].enqueue(task)

        if (not tempservers[counter%servers].busy()) and (not tempqueues[counter%servers].is_empty()):
            next_task = tempqueues[counter%servers].dequeue()

            tempwaitingtimes[counter%servers].append(next_task.processingtime)
            tempservers[counter%servers].start_next(next_task)

        tempservers[counter%servers].tick()
        counter += 1
    for x in range(servers):
        average_wait = sum(tempwaitingtimes[x]) / len(tempwaitingtimes[x])
        print("Average Wait %6.2f secs %3d tasks remaining on server %d."
        %(average_wait, tempqueues[x].size(), x))

def main(file = amazon_url_csv, servers=6):
    if servers==1:
        simulateOneServer(file)
    else:
        simulateManyServers(file, servers)

if __name__ == "__main__":
    main()

#Answer to Question from Part 3: As the amount of servers increase, the processing time decreases.
