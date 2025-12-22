---
id: 1c33746f-dc64-44c2-8618-561c9c476599
name: Enumerate-Web-Directories-with-Dirb
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:05:51.550989+00:00'
updated_at: '2023-05-26T15:56:44.496394+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - directory-enumeration
  - web-reconnaissance
  - directory-listing
  - web-applications
commands:
  - '[[commands/dirb-directory-brute-force]]'
platforms:
  - Web
tools:
  - '[[tools/dirb]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-Web-Directories-with-Dirb

## Summary

This procedure uses the Dirb tool to perform brute-force enumeration of hidden directories and files on a web application server. It helps identify potential entry points such as administrative panels, upload directories, or backup files that may not be linked from the main site, aiding in reconnaissance for further exploitation.

## Description

Directory enumeration is a key reconnaissance technique in web application testing, where attackers systematically guess common directory paths to uncover hidden resources. Dirb automates this by using wordlists to send HTTP requests for potential paths against the target URL. This procedure is applicable in scenarios where initial browsing reveals limited site structure, such as content management systems or custom web apps. It targets HTTP/HTTPS services and can reveal directories like /admin, /uploads, or /backups. Success depends on the quality of the wordlist and server response codes (e.g., 200 for found, 403 for forbidden). This maps to MITRE ATT&CK technique T1083 for discovering file and directory structures on remote systems.

## Requirements

1. Network access to the target web server (HTTP/HTTPS ports 80/443 open).
2. Dirb tool installed (pre-installed on Kali Linux).
3. A wordlist file containing common directory names (e.g., /usr/share/wordlists/dirb/common.txt).
4. Basic command-line knowledge and a terminal environment.

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAFs) like ModSecurity to rate-limit or block repeated requests to non-existent paths.
- Use directory listing protections in web servers (e.g., Options -Indexes in Apache) and monitor access logs for patterns of brute-force attempts (e.g., high volume of 404 errors from a single IP).
- Employ intrusion detection systems (IDS) to flag anomalous HTTP traffic matching reconnaissance signatures.

## Objectives

1. Identify hidden directories and files on the web server to expand the attack surface.
2. Verify the existence of enumerated paths through manual access.
3. Gather intelligence on the web application's structure for subsequent testing phases.

## Instructions

### Step 1: Execute Directory Brute-Force Scan

**Context**: Launch Dirb to scan the target URL using a wordlist, focusing on non-recursive mode to avoid deep crawling and reduce noise. This step probes for directories by sending requests and analyzing response codes.

**Command** ([[commands/dirb-directory-brute-force]]):
```bash
dirb http://$_TARGET_IP $_WORDLIST -r
```

> This command starts the scan against the specified target IP and wordlist. The -r flag prevents recursion into discovered directories. Monitor the output for lines starting with '==>' indicating directories (typically 200 or 301 responses) or '+' for files. Adjust the URL to HTTPS if needed by changing 'http://' to 'https://'. Expected runtime depends on wordlist size; use a smaller list for initial tests.

### Step 2: Verify Discovered Directories

**Context**: Manually access the enumerated directories in a web browser or using a tool like curl to confirm their existence and content. This validates the scan results and checks for accessible resources like login pages or sensitive files.

**Command** (Use browser or [[commands/curl-basic-get]] for verification):
```bash
curl -I http://$_TARGET_IP/$_DISCOVERED_PATH
```

> Replace $_DISCOVERED_PATH with a path from the Dirb output (e.g., /admin). Look for 200 OK responses indicating accessibility. If the directory lists contents, note any files for further enumeration. Document findings, such as exposed backups or config files, which could lead to privilege escalation or data exposure.
