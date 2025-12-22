---
id: f2b0e3c0-859b-43f6-b99f-578c072fa957
name: nmap-fetch-robots-txt
type: command
executor: bash
data: nmap -p80 --script http-robots.txt $_TARGET_IP
output: |-
  Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:29 IST
  Nmap scan report for 192.168.1.3
  Host is up (0.00048s latency).

  PORT   STATE SERVICE
  80/tcp open  http
  | http-robots.txt: 5 disallowed entries 
  |_/images/ /admin/ /img/ /js/ /bin/
created_at: '2020-09-01T17:18:29.803350+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - nmap
  - web
verified: true
validated: true
---

# nmap-fetch-robots-txt

## Command

```bash
nmap -p80 --script http-robots.txt $_TARGET_IP
```

## Description

This command uses Nmap to scan a target web server on port 80 and execute the http-robots.txt script, which fetches the /robots.txt file and extracts disallowed directories. It is useful for initial web reconnaissance to identify hidden or sensitive paths without manual effort.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p80 | Specifies the port to scan (change to -p443 for HTTPS) | Yes |
| --script http-robots.txt | Runs the Nmap script to parse robots.txt | Yes |
| $_TARGET_IP | IP address or hostname of the target web server | Yes |

## Examples

### Basic Usage

```bash
nmap -p80 --script http-robots.txt 192.168.1.3
```

### Advanced Usage

```bash
nmap -p80,443 --script http-robots.txt -sV 192.168.1.3
```

This adds service version detection (-sV) for more context on the web server.

## Expected Output

Description of what output to expect when the command runs successfully.

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:29 IST
Nmap scan report for 192.168.1.3
Host is up (0.00048s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-robots.txt: 5 disallowed entries 
|_/images/ /admin/ /img/ /js/ /bin/
```

The output shows the port status and lists disallowed paths from robots.txt. If no file exists, it will note that.

## Related

- [[procedures/Enumerate-Directories-from-Robots-Txt-using-Nmap]]
- [[tools/Nmap]]
