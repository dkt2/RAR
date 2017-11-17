# RAR
RAR stands for Remote Acoustic Recording device. This repository holds all the code necessary... 
- To run the hydrophone (underwater microphone)
- Schedule recording (based on a time range using 24h time)

This repo also contains a simple battery-testing script and a script to send the pi's ip address on boot for easy ssh access. 

## Getting Files/Folders off of the Pi
To get files/folders off of the Pi, I recommend using sftp ([more info](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)). Briefly, 
1. On your local machine, `cd` into your `Downloads` folder (or into a folder that convient for you for holding the Pi files you want to download)
2. Type this command `sftp pi@<ip address of Pi>` (its just like the ssh command except replace `ssh` with `sftp`)
3. Now you can navigate the Pi like you can normally with `ssh`! 
4. If you want to download... 
    - a folder:  navigate to the parent folder of the folder you want to download and type `get -r <folder name> .`
    - a file: navigate to the folder (`cd` inside it) that contains the file you want and type `get <file name> .`
5. When it is finished downloading, type `exit`
6. You should now have the folder/file on your local machine (in your `Downloads` folder or the folder you were in when you type the `sftp` command)! 

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

### record (.py)
- pyaudio has this weird quirk where you need to pass `exception_on_overflow = False` to `stream.read(CHUNK, exception_on_overflow = False)` (its main audio recorder, [more info here](https://stackoverflow.com/questions/10733903/pyaudio-input-overflowed))

### ip-finder
- `ip.sh` is the script that sends the local ip address of the ip for easy ssh access if it is connected to the Internet (Go to this website: dweet.io/follow/elegant-songs)
- `crontab_instructions.txt` are instructions for setting up the `ip.sh` script to run on boot
- `logs` folder is an empty folder to hold logs

### battery-tester
- `battery_test.py` is a script that simply prints out the time every minute (the idea being that once the pi runs out of power, the script will be killed when the pi shuts down)