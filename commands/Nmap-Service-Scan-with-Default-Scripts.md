---
id: f8a860fd-f488-4bba-bd23-84e2dd9c2c7c
name: Nmap-Service-Scan-with-Default-Scripts
type: command
executor: bash
data: nmap -sV -sC $_TARGET_IP
output: >-
  root@kali:~# nmap -sV -sC 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:32 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00057s latency).

  Not shown: 999 closed ports

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


  Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 34.97 seconds
created_at: '2019-09-12T18:35:43.264851+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - enumeration
  - network
  - reconnaissance
verified: true
validated: true
---

# Nmap-Service-Scan-with-Default-Scripts

## Command

```bash
nmap -sV -sC $_TARGET_IP
```

## Description

This command performs a TCP SYN scan (default) on the target IP, detects service versions on open ports using -sV, and executes default NSE scripts with -sC to gather additional service details like configuration or vulnerability hints. Use it for initial reconnaissance to identify exploitable services without full handshakes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target (e.g., 10.10.10.10 or example.com) | Yes |
| -sV | Enable service version detection (probes open ports for software details) | Built-in |
| -sC | Run default set of NSE scripts (safe enumeration like banner grabbing) | Built-in |

## Examples

### Basic Usage

```bash
nmap -sV -sC 10.10.10.10
```

### Advanced Usage

```bash
nmap -sV -sC -p 1-1000 -T4 10.10.10.10
```

This limits ports to 1-1000 and uses aggressive timing (-T4) for faster scans.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# nmap -sV -sC 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:32 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00057s latency).
Not shown: 999 closed ports
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

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.97 seconds
```

Look for open ports, versions (e.g., vsftpd 2.3.4), and script outputs indicating weaknesses.

## Related

- [[commands/Nmap-Host-Discovery]]
- [[procedures/Basic-Port-Scan-and-Scripted-Service-Enumeration]]
