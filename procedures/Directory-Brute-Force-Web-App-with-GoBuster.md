---
id: 905b31b9-e98a-40fe-886d-206b65c4b50b
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T04:55:06.453822+00:00'
updated_at: '2023-05-26T01:27:16.281918+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - enumeration
  - web-applications
platforms:
  - Web
commands:
  - '[[commands/Gobuster-Directory-Brute-Force]]'
tools:
  - '[[tools/Gobuster]]'
validated: true
---

# Directory-Brute-Force-Web-App-with-GoBuster

## Summary

Use GoBuster to perform dictionary-based brute force on a web application's directories and files, uncovering hidden endpoints like upload forms or CGI directories essential for exploits such as ImageTragick or Shellshock.

## Description

GoBuster sends HTTP requests for common paths from a wordlist, identifying accessible resources based on response codes. This reveals structure without source code access, targeting misconfigurations in web apps on Linux hosts.

## Requirements

1. Target web server URL (from port scan)
2. Wordlist (e.g., /usr/share/wordlists/dirb/common.txt)
3. GoBuster installed

## Defense

- Implement web application firewall (WAF) to block brute force patterns
- Use rate limiting on directories
- Hide sensitive paths with authentication

## Objectives

1. Discover administrative or upload directories
2. Identify CGI bins for Shellshock
3. Map application structure for targeted exploits

## Instructions

### Step 1: Run Basic Directory Brute Force

**Context**: Start with common paths to find entry points.

**Command** ([[commands/Gobuster-Directory-Brute-Force]]):
```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP
```

> Output shows status codes; 200/301 indicate finds. If /cgi-bin/ appears, note for Shellshock.

### Step 2: Follow Up on Discoveries

**Context**: Manually verify found paths in browser or curl.

If upload dir found, test file upload capabilities for ImageTragick.
