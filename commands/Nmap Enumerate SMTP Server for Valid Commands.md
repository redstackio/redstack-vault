---
id: 35ee0080-3210-434c-8728-e068c86868e9
name: Nmap Enumerate SMTP Server for Valid Commands
type: command
executor: null
data: nmap -p25 -script smtp-commands $_TARGET_IP
output: "root@kali:~# nmap -p25 -script smtp-commands 10.10.10.10\nStarting Nmap 7.70\
  \ ( https://nmap.org ) at 2019-09-24 14:50 EDT\nNmap scan report for 10.10.10.10\n\
  Host is up (0.00079s latency).\n\nPORT   STATE SERVICE\n25/tcp open  smtp\n|_smtp-commands:\
  \ host.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES,\
  \ 8BITMIME, DSN, \nMAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)\n\
  \nNmap done: 1 IP address (1 host up) scanned in 0.30 seconds"
created_at: '2019-09-24T19:45:11.092104+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap Enumerate SMTP Server for Valid Commands

```bash
nmap -p25 -script smtp-commands $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -p25 -script smtp-commands 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-24 14:50 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00079s latency).

PORT   STATE SERVICE
25/tcp open  smtp
|_smtp-commands: host.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 0.30 seconds
```


