---
id: 0d4b53ca-8aa9-4eed-9182-13d3d32e00ec
name: Nmap FIN Scan with Service Enumeration
type: command
executor: bash
data: nmap -sV -sF -p- $_TARGET_IP
output: 'root@kali:~# nmap -sV -sF 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:55 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.0026s latency).

  Not shown: 998 closed ports

  PORT     STATE SERVICE     VERSION

  21/tcp   open  ftp         vsftpd 2.3.4

  22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)

  MAC Address: 00:0C:29:66:97:CB (VMware)

  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 13.03 seconds

  '
created_at: '2019-09-12T19:01:25.583612+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap FIN Scan with Service Enumeration

```bash
nmap -sV -sF -p- $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -sV -sF 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:55 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0026s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
MAC Address: 00:0C:29:66:97:CB (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.03 seconds

```
