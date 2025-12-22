---
id: 97f02023-0cc3-48f3-9931-fe989c40ca6e
type: command
executor: bash
data: nmap -A $_TARGET_IP
output: >
  root@kali:~# nmap -A 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:43 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00073s latency).

  Not shown: 977 closed ports

  PORT     STATE SERVICE     VERSION

  21/tcp   open  ftp         vsftpd 2.3.4

  |_ftp-anon: Anonymous FTP login allowed (FTP code 230)

  | ftp-syst: 

  |   STAT: 

  | FTP server status:

  |      Connected to 10.10.10.13

  |      Logged in as ftp

  |      TYPE: ASCII

  |      No session bandwidth limit

  |      Session timeout in seconds is 300

  |      Control connection is plain text

  |      Data connections will be plain text

  |      vsFTPd 2.3.4 - secure, fast, stable

  |_End of status

  MAC Address: 00:0C:29:66:97:CB (VMware)

  Device type: general purpose

  Running: Linux 2.6.X

  OS CPE: cpe:/o:linux:linux_kernel:2.6

  OS details: Linux 2.6.9 - 2.6.33

  Network Distance: 1 hop

  Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs:
  Unix, Linux; CPE: cpe:/o:linux:linux_kernel


  Host script results:

  |_clock-skew: mean: -6s, deviation: 0s, median: -6s

  |_ms-sql-info: ERROR: Script execution failed (use -d to debug)

  |_nbstat: NetBIOS name: METASPLOITABLE, NetBIOS user: <unknown>, NetBIOS MAC:
  <unknown> (unknown)

  |_smb-os-discovery: ERROR: Script execution failed (use -d to debug)

  |_smb-security-mode: ERROR: Script execution failed (use -d to debug)

  |_smb2-time: Protocol negotiation failed (SMB2)


  TRACEROUTE

  HOP RTT     ADDRESS

  1   0.73 ms 10.10.10.10


  OS and Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 35.76 seconds
created_at: '2019-09-12T18:44:52.374985+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - nmap
  - aggressive-scan
verified: true
validated: true
---

# nmap-aggressive-scan-with-version-detection

## Command

```bash
nmap -A $_TARGET_IP
```

## Description

Performs aggressive scanning including port scan, version detection, OS fingerprinting, and script scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -A | Aggressive mode (sV, sC, O, traceroute) | Built-in |
| $_TARGET_IP | Target IP/hostname | Yes |

## Examples

### Basic Usage

```bash
nmap -A 192.168.1.1
```

### With Output

```bash
nmap -A 192.168.1.1 -oN scan.txt
```

## Expected Output

Detailed port list with services, versions, OS, and script results.

## Related

- [[procedures/Perform-Aggressive-Port-Scan-with-Nmap]]
- [[tools/Nmap]]
