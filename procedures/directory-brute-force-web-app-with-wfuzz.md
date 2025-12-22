---
id: 25e3f6b9-1833-4eba-af0d-3b6d7be81ce6
type: procedure
verified: true
submitted: false
created_at: '2019-09-11T22:12:51.778764+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
platforms:
  - Web
tags:
  - Enumeration
  - Web Applications
commands:
  - '[[commands/wfuzz-directory-brute-force]]'
tools:
  - '[[tools/Wfuzz]]'
validated: true
---

# Directory-Brute-Force-Web-App-with-Wfuzz

## Summary

Enumerate hidden files and directories on a web application like WordPress by performing a dictionary-based brute-force attack using Wfuzz, revealing admin panels or configuration files.

## Description

Wfuzz fuzzes the URL path with a wordlist to test for existing resources, filtering irrelevant responses like 404s. This is useful for discovering unprotected directories on CMS platforms, increasing the attack surface for credential brute-forcing or exploitation.

## Requirements

- Target web server IP or domain
- Wordlist file (e.g., common.txt with directories like admin, wp-admin)
- Wfuzz installed

## Defense

- Implement web application firewalls (WAF) to rate-limit fuzzing attempts
- Use directory listing protection in server config (e.g., Apache Options -Indexes)
- Monitor access logs for anomalous requests

## Objectives

1. Identify hidden directories like /wp-admin/
2. Uncover potential entry points for authentication bypass
3. Map the web app structure for targeted attacks

## Instructions

### Step 1: Prepare Wordlist and Target

**Context**: Select a comprehensive wordlist for common web directories and ensure the target URL is the web root.

No command; prepare $_WORDLIST path and $_TARGET_IP.

> Use directories focused on CMS like WordPress (e.g., /wp-content/, /wp-login.php).

### Step 2: Run Directory Brute-Force

**Context**: Fuzz the /FUZZ path to detect responses indicating existing resources, hiding 404s for cleaner output.

**Command** ([[commands/wfuzz-directory-brute-force]]):
```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP/FUZZ
```

> The --hc 404 filters out not-found pages; -c shows progress. Expect a table with status codes: 200 for files, 301 for directories like /wp-admin/.
