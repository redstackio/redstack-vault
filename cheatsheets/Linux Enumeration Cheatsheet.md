---
id: 13652278-5ce9-45c5-9b6c-55fe48a57895
name: Linux Enumeration Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:43.237763+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Linux Enumeration Cheatsheet

# Print all available system information (Kernel Version)



**Command** ([[description]]):

```bash
uname -a

```







**Command** ([[description]]):

```bash
uname -r

```







**Command** ([[description]]):

```bash
uname -n

```







**Command** ([[description]]):

```bash
hostname

```







**Command** ([[description]]):

```bash
uname -m

```







**Command** ([[description]]):

```bash
cat /proc/version	

```







**Command** ([[description]]):

```bash
cat /etc/*-release	

```







**Command** ([[description]]):

```bash
cat /etc/issue

```







**Command** ([[description]]):

```bash
cat /proc/cpuinfo	

```







**Command** ([[description]]):

```bash
df -a	File system

```







**Command** ([[description]]):

```bash
dmesg | grep Linux

```







**Command** ([[description]]):

```bash
rpm -q kernel
ls /boot | grep vmlinuz-

```





# Users & Groups:



**Command** ([[description]]):

```bash
cat /etc/passwd

```







**Command** ([[description]]):

```bash
cat /etc/shadow

```







**Command** ([[description]]):

```bash
cat /etc/group

```







**Command** ([[description]]):

```bash
finger

```







**Command** ([[description]]):

```bash
pinky

```







**Command** ([[description]]):

```bash
users

```







**Command** ([[description]]):

```bash
who -a

```







**Command** ([[description]]):

```bash
w

```







**Command** ([[description]]):

```bash
last

```







**Command** ([[description]]):

```bash
lastlog

```







**Command** ([[description]]):

```bash
lastlog –u %username%

```







**Command** ([[description]]):

```bash
lastlog |grep -v "Never"

```







**Command** ([[description]]):

```bash
for i in $(cat /etc/passwd 2>/dev/null| cut -d":" -f1 2>/dev/null);do id $i;done 2>/dev/null

```







**Command** ([[description]]):

```bash
grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}'	List all super user accounts

```





# User & Privilege Information:



**Command** ([[View your current user:]]):

```bash
whoami

```







**Command** ([[description]]):

```bash
id

```







**Command** ([[description]]):

```bash
cat /etc/sudoers

```







**Command** ([[description]]):

```bash
sudo -l

```







**Command** ([[description]]):

```bash
sudo -l 2>/dev/null | grep -w 'nmap\|perl\|'awk'\|'find'\|'bash'\|'sh'\|'man'\|'more'\|'less'\|'vi'\|'vim'\|'nc'\|'netcat'\|python\ |ruby\|lua\|irb' | xargs -r ls -la 2>/dev/null

```





# Environmental Information:



**Command** ([[command]]):

```bash
env

```







**Command** ([[command]]):

```bash
set

```







**Command** ([[command]]):

```bash
echo $PATH

```







**Command** ([[command]]):

```bash
history

```







**Command** ([[command]]):

```bash
pwd

```







**Command** ([[command]]):

```bash
cat /etc/profile

```







**Command** ([[command]]):

```bash
cat /etc/shells

```





# Interesting Files:



**Command** ([[command]]):

```bash
find / -perm -4000 -type f 2>/dev/null

```







**Command** ([[command]]):

```bash
find / -uid 0 -perm -4000 -type f 2>/dev/null

```







**Command** ([[command]]):

```bash
find / -perm -2000 -type f 2>/dev/null

```







**Command** ([[command]]):

```bash
find / -perm -2 -type f 2>/dev/null

```







**Command** ([[command]]):

```bash
find / ! -path "*/proc/*" -perm -2 -type f -print 2>/dev/null

```







**Command** ([[command]]):

```bash
find / -perm -2 -type d 2>/dev/null

```







**Command** ([[command]]):

```bash
find /home –name *.rhosts -print 2>/dev/null

```







**Command** ([[command]]):

```bash
find /home -iname *.plan -exec ls -la {} \; -exec cat {} 2>/dev/null \;

```







**Command** ([[command]]):

```bash
find /etc -iname hosts.equiv -exec ls -la {} 2>/dev/null \; -exec cat {} 2>/dev/null \;

```







**Command** ([[command]]):

```bash
ls -ahlR /root/

```







**Command** ([[command]]):

```bash
cat ~/.bash_history

```







**Command** ([[command]]):

```bash
ls -la ~/.*_history

```







**Command** ([[command]]):

```bash
ls -la /root/.*_history

```







**Command** ([[command]]):

```bash
ls -la ~/.ssh/

```







**Command** ([[Find SSH keys/host]]):

```bash
find / -name "id_dsa*" -o -name "id_rsa*" -o -name "known_hosts" -o -name "authorized_hosts" -o -name "authorized_keys" 2>/dev/null |xargs -r ls -la

```







**Command** ([[Check Configuration of inetd services]]):

```bash
ls -la /usr/sbin/in.*

```







**Command** ([[Check log files for keywords (‘pass’ in this example) and show positive matches]]):

```bash
grep -l -i pass /var/log/*.log 2>/dev/null

```







**Command** ([[	List files in specified directory (/var/log)]]):

```bash
find /var/log -type f -exec ls -la {} \; 2>/dev/null

```







**Command** ([[	List .log files in specified directory (/var/log)]]):

```bash
find /var/log -name *.log -type f -exec ls -la {} \; 2>/dev/null

```







**Command** ([[	List .conf files in /etc (recursive 1 level)]]):

```bash
find /etc/ -maxdepth 1 -name *.conf -type f -exec ls -la {} \; 2>/dev/null
ls -la /etc/*.conf

```







**Command** ([[	Find .conf files (recursive 4 levels) and output line number where the word ‘password’ is located]]):

```bash
find / -maxdepth 4 -name *.conf -type f -exec grep -Hn password {} \; 2>/dev/null

```







**Command** ([[no name conversion]]):

```bash
lsof -i -n

```







**Command** ([[Try to read root mail]]):

```bash
head /var/mail/root

```






