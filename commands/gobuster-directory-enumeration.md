---
id: 21cc125b-0be7-4d96-9228-eb144900a21f
type: command
executor: bash
data: >-
  gobuster dir -w $_WORDLIST -u $_TARGET_URL -t $_THREADS -x $_EXTENSIONS
  --status-codes-blacklist $_BLACKLIST_CODES
output: |-
  root@kali:~# gobuster dir -w common.txt -u http://10.10.10.10
  ===============================================================
  Gobuster v3.0.1
  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
  ===============================================================
  [+] Url:            http://10.10.10.10
  [+] Threads:        10
  [+] Wordlist:       common.txt
  [+] Status codes:   200,204,301,302,307,401,403
  [+] User Agent:     gobuster/3.0.1
  [+] Timeout:        10s
  ===============================================================
  2019/09/13 20:20:35 Starting gobuster
  ===============================================================
  /.htpasswd (Status: 403)
  /.hta (Status: 403)
  /.htaccess (Status: 403)
  /api (Status: 301)
  /backups (Status: 301)
  /dev (Status: 301)
  /index.html (Status: 200)
  /server-status (Status: 403)
  /var (Status: 301)
  ===============================================================
  2019/09/13 20:20:36 Finished
  ===============================================================
created_at: '2019-09-14T01:56:14.216810+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-enum
  - brute-force
  - directory-enumeration
verified: true
validated: true
---

# Gobuster-Directory-Enumeration

## Command

```bash
gobuster dir -w $_WORDLIST -u $_TARGET_URL -t $_THREADS -x $_EXTENSIONS --status-codes-blacklist $_BLACKLIST_CODES
```

## Description

This command uses Gobuster in directory (dir) mode to brute-force and enumerate hidden directories, files, and endpoints on a target web server. It sends HTTP requests for each entry in the provided wordlist, reporting responses based on status codes to identify accessible or interesting paths. Ideal for web reconnaissance to uncover admin panels, backups, or configuration files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w, $_WORDLIST | Path to the wordlist file containing potential directory/file names | Yes |
| -u, $_TARGET_URL | Base URL of the target web application (e.g., http://example.com) | Yes |
| -t, $_THREADS | Number of concurrent threads for faster scanning (default: 10) | No |
| -x, $_EXTENSIONS | Comma-separated list of file extensions to append to wordlist entries (e.g., php,html,txt) | No |
| --status-codes-blacklist, $_BLACKLIST_CODES | Comma-separated HTTP status codes to exclude from output (e.g., 404,500) | No |
| --wildcard | Force treatment of wildcard responses (use if server returns 200 for non-existent paths) | No |
| -p, --proxy | Proxy server for routing traffic (e.g., http://127.0.0.1:8080) | No |

## Examples

### Basic Usage

```bash
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.10.10
```

This performs a basic directory scan using a medium-sized wordlist.

### Advanced Usage

```bash
gobuster dir -w /usr/share/wordlists/dirb/big.txt -u https://example.com -t 50 -x php,asp,jsp --status-codes-blacklist 404,403 -p http://127.0.0.1:8080
```

This scans with a large wordlist, 50 threads, specific extensions, blacklists common errors, and routes through a proxy for interception.

## Expected Output

The output lists discovered paths with their HTTP status codes, such as 200 (OK), 301 (redirect), or 403 (forbidden). Paths with 200 or 301 often indicate interesting content. Example:

```
/.htpasswd (Status: 403)
/api (Status: 301)
/backups (Status: 301)
/index.html (Status: 200)
```

A summary at the end shows the scan duration and total findings.

## Related

- [[tools/Gobuster]]
- [[procedures/Directory-Brute-Force-Web-App-with-GoBuster]]
