---
type: procedure
description: >-
  Use ffuf to perform directory enumeration and parameter fuzzing on web
  applications to discover hidden directories, files, and injection points.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - fuzzing
  - web-reconnaissance
  - directory-enumeration
  - parameter-discovery
commands:
  - '[[commands/ffuf-directory-fuzzing]]'
  - '[[commands/ffuf-get-parameter-fuzzing]]'
  - '[[commands/ffuf-post-data-fuzzing]]'
platforms:
  - Web
tools:
  - '[[tools/Ffuf]]'
skill_level: beginner
impact_level: low
detection_risk: medium
created_at: '2020-07-24T17:11:28.857057+00:00'
updated_at: '2023-05-26T18:35:23.816769+00:00'
validated: true
---

# Directory-and-Parameter-Fuzzing-with-Ffuf

## Summary

This procedure uses the ffuf tool to fuzz web applications for hidden directories, files, and parameters in GET and POST requests. It helps identify potential entry points for further exploitation, such as undisclosed admin panels or vulnerable endpoints, by brute-forcing against wordlists of common names.

## Description

Ffuf (Fuzz Faster U Fool) is a fast web fuzzer written in Go, designed for discovering content on web servers through dictionary attacks. This procedure covers directory fuzzing to find hidden paths, GET parameter fuzzing to uncover injectable parameters, and POST data fuzzing for form-based inputs. It is typically used during reconnaissance phases to map the attack surface of public-facing web applications. Success depends on quality wordlists and filtering false positives based on response sizes or status codes. This maps to MITRE ATT&CK techniques for active scanning and exploiting public-facing applications.

## Requirements

1. ffuf tool installed (see [[tools/Ffuf]] for installation).
2. Wordlists for directories (e.g., /usr/share/wordlists/dirb/common.txt), parameters (e.g., paramnames.txt), and POST data (e.g., postdata.txt).
3. Network access to the target web application.
4. Basic understanding of HTTP methods and response codes.

## Defense

Defensive measures include web application firewalls (WAFs) that rate-limit or block anomalous requests, server-side logging of unusual patterns, and directory listing disabled on web servers. Detection can involve monitoring for high volumes of 404/403 responses from the same IP or tools like Fail2Ban to block fuzzing attempts.

## Objectives

1. Discover hidden directories and files on the target website.
2. Identify potential GET and POST parameters for further testing.
3. Map the web application's structure for targeted attacks.
4. Filter out false positives to focus on valid discoveries.

## Instructions

### Step 1: Fuzz Directories

**Context**: Start by enumerating directories to find hidden or unprotected paths on the target domain. This step uses a common wordlist to probe for common directory names and filters out responses of a specific size to reduce noise.

**Command** ([[commands/ffuf-directory-fuzzing]]):
```bash
ffuf -w /usr/share/wordlists/dirb/common.txt -u https://target.com/FUZZ -fs 324
```

> This command sends GET requests to https://target.com/FUZZ, replacing FUZZ with words from the wordlist. The -fs 324 flag filters out responses of 324 bytes (often the default 404 page size). Expected output includes a list of discovered directories with their status codes and sizes.

### Step 2: Fuzz GET Parameters

**Context**: After identifying a script or endpoint, fuzz for additional GET parameters that might be injectable or reveal sensitive data. This tests parameters in query strings to find undocumented ones.

**Command** ([[commands/ffuf-get-parameter-fuzzing]]):
```bash
ffuf -w /path/to/paramnames.txt -u https://target.com/script.php?FUZZ=test_value -fs 4242
```

> Replace /path/to/paramnames.txt with a list of potential parameter names. The command fuzzes the FUZZ position in the URL and filters responses of 4242 bytes (common error page size). Look for changes in response size or content indicating valid parameters.

### Step 3: Fuzz POST Data

**Context**: For login forms or API endpoints, fuzz POST payloads to discover valid fields or injection points. This step simulates form submissions with varying data to identify weaknesses.

**Command** ([[commands/ffuf-post-data-fuzzing]]):
```bash
ffuf -w /path/to/postdata.txt -X POST -d "username=admin&password=FUZZ" -u https://target.com/login.php -fc 401
```

> Use a wordlist for POST values like passwords. The -X POST specifies the method, -d sets the data with FUZZ as the payload position, and -fc 401 filters out 401 Unauthorized responses. Success is indicated by 200 OK responses or varying content lengths suggesting valid inputs.
