---
id: d0791778-87b6-4fca-adb1-694c98e2c994
name: Nmap Service Scan with OS Detection
type: command
executor: bash
data: nmap -O -sV $_TARGET_IP
output: 'root@kali:~# nmap -O -sV 10.10.10.10

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:41 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00059s latency).

  Not shown: 998 closed ports

  PORT     STATE SERVICE     VERSION

  22/tcp open  ssh           OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol
  2.0)

  80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))

  MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

  Device type: general purpose

  Running: Linux 2.6.X

  OS CPE: cpe:/o:linux:linux_kernel:2.6

  OS details: Linux 2.6.9 - 2.6.33

  Network Distance: 1 hop

  Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux;
  CPE: cpe:/o:linux:linux_kernel


  OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 13.72 seconds'
created_at: '2019-09-13T22:29:10.923723+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
- '[[ssh]]'
- '[[type]]'
---

# Nmap Service Scan with OS Detection

```bash
nmap -O -sV $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -O -sV 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:41 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00059s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE     VERSION
22/tcp open  ssh           OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop
Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.72 seconds
```


