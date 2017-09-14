#!/bin/bash
IP="$(ip route get 8.8.8.8 | awk '{print $NF; exit}')"
dweet_id_ip="elegant-songs"
cwd="$HOME/Git/RAR/logs"

touch "${cwd}/ip_log.txt"
touch "${cwd}/dweet_log.txt"
wget --post-data="IP=${IP}" http://dweet.io/dweet/for/${dweet_id_ip} -O ${cwd}/dweet_log.txt
echo "`date` | ${IP}" >> ${cwd}/ip_log.txt
