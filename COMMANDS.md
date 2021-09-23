cat wc - l /etc/
cat /etc/ssh/ssh_config | sort | unique | grep IdentityFile | wc -l
cd ~; du -hs
