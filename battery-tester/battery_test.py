""" script to test battery life by change txt file every minute """
import time
import os

def get_curr_time():
    """ get current time formatted """
    return time.asctime(time.localtime(time.time()))

def record_time():
    with open('../logs/time.txt', 'a') as input_file:
        input_file.write(get_curr_time() + '\n')

def clear_log():
    with open('../logs/time.txt', 'w') as input_file:
        input_file.write('')

def main():
    """ main routine """
    secs = 10
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clear_log()
    print("*** Timer Starts")
    while True:
        print(get_curr_time())
        record_time()
        time.sleep(secs) # wait 60 secs / 1 min

if __name__ == '__main__':
    main()
