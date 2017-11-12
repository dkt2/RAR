# RAR
RAR stands for Remote Acoustic Recording device. This repository holds all the code necessary... 
- To run the hydrophone (underwater microphone)
- Schedule recording (based on a time range using 24h time)

This repo also contains a simple battery-testing script and a script to send the pi's ip address on boot for easy ssh access. 

## File/Folder Tree Breakdown 

### scheduler
- `record.py` is the script that handles recording 
- `times.txt` is the text file to input scheduling of recording 
- `recordings` folder is an empty folder to hold recordings produced by the `record.py` script 

#### Dependecies
The dependencies for the `record.py` script is as follows... 

**Python**:
- Python3, pip3 
- pyaudio (using pip (e.g. sudo pip3 install pyaudio) or package manager (e.g. sudo apt install python3-pyaudio))

**Linux**:
- portaudio19-dev (portaudio library developement package) (e.g. sudo apt install portaudio19-dev)
- python-all-dev (python development package) 

refer to this pages for other OS: 
https://people.csail.mit.edu/hubert/pyaudio/

### ip-finder
- `ip.sh` is the script that sends the local ip address of the ip for easy ssh access if it is connected to the Internet (Go to this website: dweet.io/follow/elegant-songs)
- `crontab_instructions.txt` are instructions for setting up the `ip.sh` script to run on boot
- `logs` folder is an empty folder to hold logs

### battery-tester
- `battery_test.py` is a script that simply prints out the time every minute (the idea being that once the pi runs out of power, the script will be killed when the pi shuts down)