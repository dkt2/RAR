#!/bin/bash
cd /home/pi/Git/RAR/ip-finder/
touch ip_log.txt
touch dweet_log.txt
IP="$(ip route get 8.8.8.8 | awk '{print $NF; exit}')"
dweet_id_ip="elegant-songs"
wget --post-data="IP=${IP}" http://dweet.io/dweet/for/${dweet_id_ip} -O dweet_log.txt
echo "`date` | ${IP}" >> ip_log.txt
