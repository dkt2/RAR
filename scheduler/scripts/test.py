""" script playground area to test code """
import time
import json

def parse_json():
    """ parsing json into arrays """
    with open('schedule.json') as input_file:
        schedule = json.load(input_file)
        for key, value in schedule.items():
            schedule[key] = value.split(';')
            for val in range(0, len(schedule[key])):
                schedule[key][val] = schedule[key][val].split(',')
        print(schedule)

def timemaker():
    """ parsing time into input json style """
    localtime = time.localtime(time.time())
    formated_ltime = time.asctime(localtime)
    hourmin = "{:0>2}{:0>2}".format(localtime[3], localtime[4])
    print(hourmin == "0010")
    print(formated_ltime)

def main():
    """ main """
    with open('./time/start.txt', 'w') as input_file:
        # input_file.write(get_curr_time())
        pass

if __name__ == '__main__':
    main()
