---
id: f02c9d46-b38d-45cb-ba5d-9fc2e1de9012
name: Nmap Service Scan of All TCP Ports
type: command
executor: bash
data: nmap -p- -sV $_TARGET_IP
output: 'root@kali:~# nmap -p- -sV 10.10.10.10

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:25 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.000036s latency).

  Not shown: 65534 closed ports

  PORT      STATE SERVICE     VERSION

  21/tcp    open  ftp         vsftpd 2.3.4

  53227/tcp open  nlockmgr    1-4 (RPC #100021)

  MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

  Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux;
  CPE: cpe:/o:linux:linux_kernel


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 122.34 seconds'
created_at: '2019-09-13T22:29:10.912781+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Service Scan of All TCP Ports

```bash
nmap -p- -sV $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -p- -sV 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:25 EDT
Nmap scan report for 10.10.10.10
Host is up (0.000036s latency).
Not shown: 65534 closed ports
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         vsftpd 2.3.4
53227/tcp open  nlockmgr    1-4 (RPC #100021)
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)
Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 122.34 seconds
```


