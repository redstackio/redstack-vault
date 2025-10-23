---
id: 5e5b9a80-b278-4447-98d3-79ab9d9def4f
name: Nmap Full Port Scan with Service Enumeration
type: command
executor: bash
data: nmap -sV -p- $TARGET_IP -oN $OUTPUT
output: 'root@kali:~# nmap -sV -p- 10.10.10.10 -oN allports

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 15:32 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00034s latency).

  Not shown: 65524 closed ports

  PORT      STATE SERVICE         VERSION

  135/tcp   open  msrpc           Microsoft Windows RPC

  139/tcp   open  netbios-ssn     Microsoft Windows netbios-ssn

  445/tcp   open  microsoft-ds    Microsoft Windows 7 - 10 microsoft-ds (workgroup:
  WORKGROUP)

  5357/tcp  open  http            Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

  44444/tcp open  cognex-dataman?

  49152/tcp open  msrpc           Microsoft Windows RPC

  49153/tcp open  msrpc           Microsoft Windows RPC

  49154/tcp open  msrpc           Microsoft Windows RPC

  49155/tcp open  msrpc           Microsoft Windows RPC

  49156/tcp open  msrpc           Microsoft Windows RPC

  49158/tcp open  msrpc           Microsoft Windows RPC

  MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)

  Service Info: Host: VICTIM-PC; OS: Windows; CPE: cpe:/o:microsoft:windows


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 106.06 seconds'
created_at: '2019-10-11T19:37:17.062629+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Full Port Scan with Service Enumeration

```bash
nmap -sV -p- $TARGET_IP -oN $OUTPUT
```

## Expected Output

```
root@kali:~# nmap -sV -p- 10.10.10.10 -oN allports
Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 15:32 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00034s latency).
Not shown: 65524 closed ports
PORT      STATE SERVICE         VERSION
135/tcp   open  msrpc           Microsoft Windows RPC
139/tcp   open  netbios-ssn     Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds    Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
5357/tcp  open  http            Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
44444/tcp open  cognex-dataman?
49152/tcp open  msrpc           Microsoft Windows RPC
49153/tcp open  msrpc           Microsoft Windows RPC
49154/tcp open  msrpc           Microsoft Windows RPC
49155/tcp open  msrpc           Microsoft Windows RPC
49156/tcp open  msrpc           Microsoft Windows RPC
49158/tcp open  msrpc           Microsoft Windows RPC
MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)
Service Info: Host: VICTIM-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 106.06 seconds
```


