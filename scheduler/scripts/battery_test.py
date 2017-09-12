""" script to test battery life by change txt file every minute """
import time
import os

def get_curr_time():
    """ get current time formatted """
    return time.asctime(time.localtime(time.time()))

def start_timer():
    """ log inital start time """
    print("start timer")
    with open('../time/start.txt', 'w') as input_file:
        input_file.write(get_curr_time())

def stop_timer():
    """ log stop time """
    print("stop timer")
    with open('../time/end.txt', 'w') as input_file:
        input_file.write(get_curr_time())

def main():
    """ main routine """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    start_timer()
    while True:
        time.sleep(10) # wait 60 secs / 1 min
        stop_timer()

if __name__ == '__main__':
    main()
