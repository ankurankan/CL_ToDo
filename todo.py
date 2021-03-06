import argparse
import os
import sys

MONTH_MAP = {
            '01':'Jan',
            '02':'Feb',
            '03':'Mar',
            '04':'Apr',
            '05':'May',
            '06':'June',
            '07':'July',
            '08':'Aug',
            '09':'Sep',
            '10':'Oct',
            '11':'Nov',
            '12':'Dec'
            }

class task:
    def __init__(self, text, date=None, time=None, complete=0):
        self.text = text
        self.date = date
        self.time = time
        self.complete = complete

    def asstring(self):
        return_string = self.text + " " + self.date + " " + self.time + " " + self.complete

def sort(li):
#Sorts a list of task objects by date and time
    

def parser(string):
    string = string.split(" ")
    return(task(string[0], string[1], string[2], int(string[3])))

#def value(string):
#    if not string:
#        print("here")

#def month(mon):
#    month = {
#            '01':'Jan',
#            '02':'Feb',
#            '03':'Mar',
#            '04':'Apr',
#            '05':'May',
#            '06':'June',
#            '07':'July',
#            '08':'Aug',
#            '09':'Sep',
#            '10':'Oct',
#            '11':'Nov',
#            '12':'Dec'
#            }
#    return(month[mon])

def parse_date(date):
    return(date.split('/'))

def add(args):
    date = parse_date(args.date)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'todo', date[2], MONTH_MAP[date[1]]) + '/'
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = date[0] + '.txt'

    to_write = args.add + ' ' + str(args.date) + ' ' + str(args.time) + '\n'

    with open(path+filename, 'a') as f:
        f.write(to_write)

def get(args):
    if args.date:
        date = parse_date(args.date)
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'todo' ,date[2], MONTH_MAP[date[1]]) + '/'
        filename = date[0] + '.txt'
        tasks = []
        try:
            with open(path+filename) as f:
                for i in f.readlines():
#                   print(i)
                    tasks.append(i)
        except IOError:
            print ("No tasks for this date")
            sys.exit()
        tasks_to_print = []
        if args.re:
            #Do a regular expression search on the tasks list
            return(tasks)
        if args.exact:
            for i in tasks:
                if args.exact in i:
                    tasks_to_print.append(i)
        for i in range(len(tasks_to_print)):
            print(i,":", tasks_to_print[i])
        return(tasks)
    else:
#        tasks = recursively get all the tasks
        if args.re:
            #Do a regular expression search on the tasks list
            return
        if args.exact:
            for i in tasks:
                if args.exact in i:
                    return (i)

def complete(args):
    if args.date:
        #tasks = get all the tasks for the date
        if args.re:
            #regular expression search
            return
        if args.exact:
            #for i in tasks
        return(tasks)
    else:
        #recursively find all the tasks
        return
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'To-do list manager')
    parser.add_argument('--add', '-a', nargs='?', help='add task')
    parser.add_argument('--get', '-g', action='store_true', help='get tasks')
    parser.add_argument('--rem', '-r', nargs='?', help='remove task')
    parser.add_argument('--re', '-e', action='store_true', help='search using regular expression')
    parser.add_argument('--exact', '-x', action='store_true', help='exact search')
    parser.add_argument('--mod', '-m', nargs='?', help='modify task')
    parser.add_argument('--comp', '-c', nargs='?', help='mark complete')
    parser.add_argument('--date', '-d', nargs='?', help='date')
    parser.add_argument('--time', '-t', nargs='?', help='time')
    args = parser.parse_args()

    print(args)
    #check for todo folder
    path = os.path.dirname(os.path.realpath(__file__))
    print(path)

    if args.add:
        add(args)
    if args.get:
        print(get(args))
    if args.comp:
        print(complete(args))
