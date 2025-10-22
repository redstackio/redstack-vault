---
id: 7b5609ae-c4fc-482e-a93f-2be00490d107
name: Nmap Ping Sweep
type: command
executor: bash
data: nmap -sn $_TARGET_IP/$_CIDR
output: "root@kali:~# nmap -sn 10.10.10.0/24\nStarting Nmap 7.70 ( https://nmap.org\
  \ ) at 2019-09-11 16:44 EDT                                         \nNmap scan\
  \ report for 10.10.10.1  \nHost is up (0.016s latency).       \nNmap scan report\
  \ for 10.10.10.2"
created_at: '2019-09-11T20:46:03.382284+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Ping Sweep

```bash
nmap -sn $_TARGET_IP/$_CIDR
```

## Expected Output

```
root@kali:~# nmap -sn 10.10.10.0/24
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-11 16:44 EDT                                         
Nmap scan report for 10.10.10.1  
Host is up (0.016s latency).       
Nmap scan report for 10.10.10.2
```
