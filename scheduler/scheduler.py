import time

def current_hour(): 
    return time.localtime(time.time())[3]

def time_blocks():
    return_me = None
    with open('/home/hotdog-soup/Documents/scheduler/times.txt') as file:
        for line in file: 
            return_me = [li.split('-') for li in line.split(',')]
            # print(TIME)
    return return_me

def main():
    begin_time = None
    end_time = None
    test = 0 # test thing
    for duration in time_blocks(): 
        begin_time = duration[0]
        end_time = duration[1]

        while int(begin_time) <= int( current_hour() ) and int( current_hour() ) <= int(end_time):
            test += 1

if __name__ == '__main__':
    main()