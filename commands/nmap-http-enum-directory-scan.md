---
id: e5789d21-768f-469b-b946-73d9a8cf52e4
name: nmap-http-enum-directory-scan
type: command
executor: bash
data: nmap -p80 --script http-enum $_TARGET_IP
output: |-
  PORT   STATE SERVICE
  80/tcp open  http
  | http-enum: 
  |   /icons/: Potentially interesting folder w/ directory listing
  |   /img/: Potentially interesting folder w/ directory listing
  |_  /webalizer/: Potentially interesting folder w/ directory listing
created_at: '2020-09-01T17:09:05.183875+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Web
tags:
  - reconnaissance
  - web
  - nmap
verified: true
validated: true
---

# nmap-http-enum-directory-scan

## Command

```bash
nmap -p80 --script http-enum $_TARGET_IP
```

## Description

This command uses Nmap's http-enum NSE script to enumerate common directories and files on a web server by sending HTTP GET requests to a built-in wordlist of paths. It identifies potentially interesting resources based on response codes (e.g., 200, 403) or content patterns like directory listings. Use this during web reconnaissance to uncover hidden endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target web server | Yes |
| -p80 | Specifies the port to scan (use -p443 for HTTPS) | Yes |
| --script http-enum | Loads the http-enum script for directory brute-forcing | Yes |

## Examples

### Basic Usage

```bash
nmap -p80 --script http-enum 192.168.1.3
```

### Advanced Usage

```bash
nmap -p80,443 --script http-enum --script-args http-enum.basepath=/custom/ $_TARGET_IP -v
```

This adds verbosity (-v) and a custom base path for the wordlist.

## Expected Output

```
PORT   STATE SERVICE
80/tcp open  http
| http-enum: 
|   /icons/: Potentially interesting folder w/ directory listing
|   /img/: Potentially interesting folder w/ directory listing
|_  /webalizer/: Potentially interesting folder w/ directory listing
```

The output lists discovered paths under the http-enum section, flagging interesting ones with descriptions like 'directory listing' or status codes.

## Related

- [[procedures/Nmap-Directory-Enumeration-in-Web-Application]]
- [[tools/Nmap]]
