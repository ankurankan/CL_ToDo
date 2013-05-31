import argparse
import os
import sys

def value(string):
    if not string:
        print("here")

def month(mon):
    month = {
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
    return(month[mon])               

def parse_date(date):
    return(date.split('/'))

def add(args):
    date = parse_date(args.date)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'todo', date[2], month(date[1])) + '/'
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = date[0] + '.txt'

    to_write = args.add + ' ' + str(args.date) + ' ' + str(args.time) + '\n'

    with open(path+filename, 'a') as f:
        f.write(to_write)

def get(args):
    date = parse_date(args.date)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'todo' ,date[2], month(date[1])) + '/'
    filename = date[0] + '.txt'
    try:
        with open(path+filename) as f:
            for i in f.readlines():
                print(i)
    except IOError:
        print ("No tasks for this date")
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'To-do list manager')
    parser.add_argument('--add', '-a', nargs='?', help='add task')
    parser.add_argument('--get', '-g', action='store_true', help='get tasks')
    parser.add_argument('--rem', '-r', nargs='?', help='remove task')
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
        get(args)
