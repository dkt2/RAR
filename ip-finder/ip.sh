# while [ true ]; do
 
#  sleep 30
# done

IP="$(ip route get 8.8.8.8 | awk '{print $NF; exit}')"
dweet_id_ip="elegant-songs"
wget --post-data="IP=${IP}" http://dweet.io/dweet/for/${dweet_id_ip} -O /home/pi/Git/ip-finder/log2.txt
echo "${IP}" >> /home/pi/Git/ip-finder/log.txt