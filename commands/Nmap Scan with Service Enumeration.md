---
id: b8f280a3-8838-4a76-9a1e-4d7cf8cb3ed4
name: Nmap Scan with Service Enumeration
type: command
executor: bash
data: nmap -sV $_TARGET_IP -oN $_OUTPUT
output: 'root@kali:~# nmap -sV 10.10.10.10 -oN default

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 14:56 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00025s latency).

  Not shown: 990 closed ports

  PORT      STATE SERVICE      VERSION

  135/tcp   open  msrpc        Microsoft Windows RPC

  139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn

  445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)

  5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

  49152/tcp open  msrpc        Microsoft Windows RPC

  49153/tcp open  msrpc        Microsoft Windows RPC

  49154/tcp open  msrpc        Microsoft Windows RPC

  49155/tcp open  msrpc        Microsoft Windows RPC

  49156/tcp open  msrpc        Microsoft Windows RPC

  49159/tcp open  msrpc        Microsoft Windows RPC

  MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)

  Service Info: Host: VICTIM-PC; OS: Windows; CPE: cpe:/o:microsoft:windows


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 60.51 seconds'
created_at: '2019-10-11T19:37:17.057364+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan with Service Enumeration

```bash
nmap -sV $_TARGET_IP -oN $_OUTPUT
```

## Expected Output

```
root@kali:~# nmap -sV 10.10.10.10 -oN default
Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 14:56 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00025s latency).
Not shown: 990 closed ports
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)
Service Info: Host: VICTIM-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.51 seconds
```


