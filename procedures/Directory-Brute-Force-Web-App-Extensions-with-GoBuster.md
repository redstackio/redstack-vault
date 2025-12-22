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
platforms:
  - Web
commands:
  - '[[commands/Gobuster-Directory-Brute-Force-with-Extensions]]'
tools:
  - '[[tools/Gobuster]]'
validated: true
---

# Directory-Brute-Force-Web-App-Extensions-with-GoBuster

## Summary

Extend GoBuster brute force to target specific file extensions based on server tech, discovering scripts (.sh for Shellshock) or images (.jpg for ImageTragick uploads) that enable exploitation.

## Description

After basic enumeration, specify extensions to probe for backend files. For Apache with CGI, target .sh; for image processing apps, look for .php handling uploads. This narrows focus on exploitable artifacts.

## Requirements

1. Base URL and initial recon findings
2. Extensions list (e.g., php,sh,jpg based on headers)
3. Common wordlist

## Defense

- Serve only necessary extensions
- Validate and sanitize uploads
- Log and monitor unusual extension requests

## Objectives

1. Find executable scripts or upload handlers
2. Confirm tech stack for exploit selection
3. Uncover misconfigured file access

## Instructions

### Step 1: Manual Recon for Extensions

**Context**: Inspect headers or existing files to choose extensions.

Use curl -I http://$_TARGET_IP to get Server header.

### Step 2: Brute Force with Extensions

**Context**: Run extended scan.

**Command** ([[commands/Gobuster-Directory-Brute-Force-with-Extensions]]):
```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -x 'php,sh,jpg,png'
```

> Look for 200 responses on .sh or .php; indicates potential RCE vectors.
