---
id: b6625a02-8416-464b-8fef-b42490e590f8
name: Nmap Service Scan with No Host Discovery
type: command
executor: bash
data: nmap -sV -Pn $_TARGET_IP
output: 'root@kali:~# nmap -sV -Pn 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:52 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.0017s latency).

  Not shown: 999 closed ports

  PORT     STATE SERVICE     VERSION

  21/tcp   open  ftp         vsftpd 2.3.4

  MAC Address: 00:0C:29:66:97:CB (VMware)

  Service Info: Hosts:  host.localdomain, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 11.72 seconds'
created_at: '2019-09-12T18:53:18.085226+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Service Scan with No Host Discovery

```bash
nmap -sV -Pn $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -sV -Pn 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:52 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0017s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
MAC Address: 00:0C:29:66:97:CB (VMware)
Service Info: Hosts:  host.localdomain, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.72 seconds
```


