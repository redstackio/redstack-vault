---
id: f2b0e3c0-859b-43f6-b99f-578c072fa957
name: Nmap Command to Find Directories From Robots.txt File
type: command
executor: ''
data: nmap -p80 --script http-robots.txt 192.168.1.3
output: "Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:29 IST\nNmap scan\
  \ report for 192.168.1.3\nHost is up (0.00048s latency).\n\nPORT   STATE SERVICE\n\
  80/tcp open  http\n| http-robots.txt: 5 disallowed entries \n|_/images/ /admin/\
  \ /img/ /js/ /bin/"
created_at: '2020-09-01T17:18:29.803350+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[find]]'
- '[[host]]'
---

# Nmap Command to Find Directories From Robots.txt File

```bash
nmap -p80 --script http-robots.txt 192.168.1.3
```

## Expected Output

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:29 IST
Nmap scan report for 192.168.1.3
Host is up (0.00048s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-robots.txt: 5 disallowed entries 
|_/images/ /admin/ /img/ /js/ /bin/
```


