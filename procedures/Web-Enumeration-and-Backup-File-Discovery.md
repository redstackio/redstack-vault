---
id: 48c5c5e1-956b-4f3a-827a-2d9648dd9e8e
name: Web-Enumeration-and-Backup-File-Discovery
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.819302+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - '[[techniques/Active Scanning|T1595 - Active Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Active recon]]'
  - '[[tags/Bug Hunting Methodology and Enumeration]]'
  - '[[tags/Web discovery]]'
commands:
  - '[[commands/gobuster-directory-enumeration]]'
  - '[[commands/bfac-scan-single-url]]'
  - '[[commands/bfac-scan-from-file-list]]'
platforms:
  - Web
tools:
  - '[[tools/Gobuster]]'
  - '[[tools/BFAC]]'
validated: true
---

# Web-Enumeration-and-Backup-File-Discovery

## Summary

This procedure performs web enumeration to discover hidden directories, files, and backup artifacts on a target web server. Using tools like Gobuster for brute-force directory and file discovery and BFAC for identifying exposed backup files, it helps uncover potential sensitive information such as configuration files, source code backups, or administrative interfaces that could lead to further exploitation.

## Description

Web enumeration involves systematically probing a web application to map its structure and identify non-public resources. Attackers use this during reconnaissance to gather information about the target's architecture, technologies, and potential entry points. Gobuster employs wordlist-based brute forcing to request common paths, analyzing server responses (e.g., HTTP status codes) to detect existence. BFAC specifically targets backup file patterns (e.g., .bak, ~, .old) across common extensions and depths, which often contain unredacted sensitive data like credentials or API keys. This procedure is applicable in external reconnaissance against public-facing web servers and requires no authentication, making it low-risk for detection if rate-limited. Success reveals the attack surface for subsequent techniques like vulnerability scanning or exploitation.

## Requirements

1. Network access to the target web server (e.g., HTTP/HTTPS ports 80/443 open).
2. A wordlist file for brute-forcing (e.g., common directories like /usr/share/wordlists/dirb/common.txt).
3. Installed tools: Gobuster and BFAC.
4. Basic command-line proficiency and a Linux/Unix-like environment for execution.

## Defense

- Disable directory listing and implement proper access controls (e.g., .htaccess rules or web server configurations) to hide non-public paths.
- Use web application firewalls (WAFs) like ModSecurity to detect and block anomalous request patterns from brute-force tools.
- Regularly audit server file systems to remove unnecessary backups and monitor access logs for suspicious 200/403 responses to uncommon paths.
- Employ content security policies and rate limiting to mitigate enumeration attempts.

## Objectives

1. Identify hidden directories and files that expose application structure or sensitive data.
2. Locate backup files containing potentially valuable information like credentials or source code.
3. Map the web server's attack surface for targeted follow-up reconnaissance or exploitation.

## Instructions

### Step 1: Enumerate Directories and Files with Gobuster

**Context**: Begin by using Gobuster to brute-force common directories and files on the target URL. This step uncovers the web application's structure by testing paths against a wordlist and identifying valid resources based on server responses. Use a standard wordlist and adjust threads for performance without overwhelming the target.

**Command** ([[commands/gobuster-directory-enumeration]]):
```bash
gobuster dir -u http://example.com/ -w /usr/share/wordlists/dirb/common.txt -t 10 -x php,html,txt
```

> This command scans the root of the target site using the dirb common wordlist, with 10 threads for efficiency, and checks for extensions like PHP, HTML, and TXT files. Expected output includes a list of discovered paths with status codes (e.g., 200 for found, 404 for not found). Monitor for 403 responses, which may indicate protected but existent directories. If HTTPS is used, replace http with https and add --no-tls-validation if self-signed certs are present.

### Step 2: Scan for Backup Files on a Single URL with BFAC

**Context**: After initial enumeration, use BFAC to probe a specific URL or discovered path for backup artifacts. This tool appends common backup suffixes and depths to the base URL, checking for exposed files that might contain sensitive data. Start with a moderate level to balance thoroughness and speed.

**Command** ([[commands/bfac-scan-single-url]]):
```bash
bfac --url http://example.com/test.php --level 4
```

> The --url flag targets the specific path, and --level 4 sets the scan depth for backup pattern variations. Expected output lists any found backup files with their full URLs and HTTP status. If backups are discovered, download them immediately for analysis, as they may reveal source code or configs. Increase level for deeper scans if initial results are sparse.

### Step 3: Scan Multiple URLs from a File List with BFAC

**Context**: For broader coverage, feed BFAC a list of URLs (e.g., from prior enumeration or subdomain scans) to check for backups across multiple endpoints. This is efficient for large targets and helps identify patterns of misconfigurations.

**Command** ([[commands/bfac-scan-from-file-list]]):
```bash
bfac --list urls.txt
```

> The --list flag reads URLs from the specified file (one per line). Expected output aggregates findings across all URLs, flagging any backup discoveries. Prepare urls.txt with discovered paths from Step 1. If no backups are found, refine the list to focus on dynamic files like .php or .asp.
