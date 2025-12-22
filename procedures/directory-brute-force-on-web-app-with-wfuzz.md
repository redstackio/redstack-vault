---
id: 25e3f6b9-1833-4eba-af0d-3b6d7be81ce6
name: directory-brute-force-on-web-app-with-wfuzz
type: procedure
verified: true
submitted: false
created_at: '2019-09-11T22:12:51.778764+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Discovery|TA0007]]'
techniques:
  - '[[techniques/File and Directory Discovery|T1083.002]]'
sub_techniques: []
tags:
  - enumeration
  - web-applications
commands:
  - '[[commands/wfuzz-directory-brute-force]]'
platforms:
  - Web
tools:
  - '[[tools/Wfuzz]]'
validated: true
---

# directory-brute-force-on-web-app-with-wfuzz

## Summary

This procedure uses dictionary-based brute-forcing to discover hidden directories and files on a web application, revealing administrative panels or sensitive resources like WordPress uploads.

## Description

Web servers often expose unintended paths due to misconfigurations. Wfuzz fuzzes URLs by replacing a placeholder (FUZZ) with wordlist entries, filtering out 404s to highlight valid responses. This is key after port scanning confirms a web service, targeting paths like /wp-content/ for CMS identification.

## Requirements

- Target web server IP and base URL (e.g., http://target.com)
- Wordlist file (e.g., common.txt with directories like admin, wp-admin)
- Wfuzz installed

## Defense

- Configure web servers to return consistent 404s for non-existent paths
- Use web application firewalls (WAF) to block fuzzing patterns
- Directory listing disabled in server config (e.g., Apache Options -Indexes)

## Objectives

- Uncover hidden web directories
- Identify CMS installation paths
- Locate exploitable files like images with stego

## Instructions

### Step 1: Prepare Wordlist and Target

**Context**: Select a comprehensive wordlist for common web paths; ensure the target URL ends with /FUZZ for substitution.

No command here; manually prepare $_WORDLIST and $_TARGET_IP.

### Step 2: Execute Directory Fuzzing

**Context**: Run Wfuzz to probe directories, hiding 404 responses (--hc 404) and showing progress (-c) for efficiency.

**Command** ([[commands/wfuzz-directory-brute-force]]):
```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP/FUZZ
```

> Filters invalid responses; success shown by 200/301 codes for paths like /wp-admin/ or /images/wallpaper.jpg.
