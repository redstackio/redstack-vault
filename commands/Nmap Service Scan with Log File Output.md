---
id: 6e4354da-a240-4873-9b87-91042bac292c
name: Nmap Service Scan with Log File Output
type: command
executor: bash
data: nmap -sV -oA $_OUTPUT.log $_TARGET_IP
output: 'root@kali:~# nmap -sV -oA results.log 10.10.10.10

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:44 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.000098s latency).

  Not shown: 998 closed ports

  PORT     STATE SERVICE     VERSION

  21/tcp   open  ftp         vsftpd 2.3.4

  22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)

  MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

  Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux;
  CPE: cpe:/o:linux:linux_kernel


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 12.08 seconds'
created_at: '2019-09-13T22:29:10.930324+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
- '[[ssh]]'
---

# Nmap Service Scan with Log File Output

```bash
nmap -sV -oA $_OUTPUT.log $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -sV -oA results.log 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:44 EDT
Nmap scan report for 10.10.10.10
Host is up (0.000098s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)
Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.08 seconds
```


