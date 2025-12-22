---
id: 2e8bbb09-0a24-438c-b21f-d4ec81933fde
type: procedure
verified: true
submitted: true
created_at: '2019-10-10T21:55:34.655033+00:00'
updated_at: '2023-05-26T18:07:21.556975+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - data-exposure
  - network
  - web-enumeration
commands:
  - '[[commands/gobuster-directory-brute-force-with-extensions]]'
platforms:
  - Web
tools:
  - '[[tools/Gobuster]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Directory Brute Force Web App with Extensions Gobuster

## Summary

This procedure uses Gobuster to brute force hidden directories and files on a web application, specifying extensions based on server technology to uncover sensitive paths like CGI scripts.

## Description

Directory brute forcing reveals unprotected resources. Extensions are chosen from recon (e.g., .sh for CGI on Apache) to target likely files. This aids in finding exploitable endpoints.

## Requirements

1. Target web server URL
2. Wordlist like SecLists common.txt
3. Gobuster installed

## Defense

Implement web application firewalls (WAF), directory listing disablement, and monitor for anomalous requests.

## Objectives

1. Discover hidden directories
2. Identify files with specific extensions
3. Expose potential vulnerabilities

## Instructions

### Step 1: Manual Recon for Extension Selection

**Context**: Browse the site to note technologies (e.g., Apache headers suggest .sh for CGI).

**Command**: Use browser or curl for headers.

> Gather info on file types to inform brute force targets.

### Step 2: Run Gobuster with Extensions

**Context**: Brute force using selected extensions to find paths like /cgi-bin/.

**Command** ([[commands/gobuster-directory-brute-force-with-extensions]]):
```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -f -e -x '$_EXT1,$_EXT2,$_EXT3'
```

> Use extensions like 'sh,php,html'. Look for 403 on /cgi-bin/ indicating access but restriction.
