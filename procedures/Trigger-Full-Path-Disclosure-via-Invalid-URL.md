---
tags:
  - information-disclosure
  - full-path-disclosure
  - web-vulnerability
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-ooni-invalid-url]]'
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
id: a8133bf8-721b-4350-90a1-d309025642c5
created_at: '2025-12-14T17:26:12.119Z'
updated_at: '2025-12-14T17:26:12.119Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger Full Path Disclosure via Invalid URL

## Summary

This procedure exploits a full path disclosure (CWE-209) vulnerability in web applications by requesting an invalid URL path, causing the server to return a 404 error that inadvertently reveals internal filesystem paths. In the context of the Tor Project's OONI Explorer, this allows attackers to map server structure for reconnaissance without authentication.

## Description

Full path disclosure occurs when error handling in web servers or applications leaks sensitive filesystem information, such as absolute paths to directories and files. For OONI Explorer (https://explorer.ooni.torproject.org/), appending an invalid path like '//x' to the base URL triggers a 404 response that exposes the server's internal path (e.g., something like '/usr/local/share/ooni/...'). This information can aid in identifying the operating system, web server software, and directory structure, potentially chaining with path traversal (CWE-22) or other vulnerabilities for deeper compromise. The root cause is typically misconfigured error reporting or lack of input sanitization in the routing logic. Prerequisites include public access to the web app; no special privileges are needed.

## Requirements

1. Network access to the target web application (HTTPS on port 443)
2. A tool or browser capable of making HTTP GET requests (e.g., curl)
3. Basic understanding of HTTP status codes and URL structure

## Defense

Defensive measures and detection strategies:

- Disable detailed error messages in production (e.g., configure Apache/Nginx to return generic 404 pages)
- Implement proper input validation and sanitization for URL paths
- Use web application firewalls (WAF) to filter suspicious requests to invalid paths
- Monitor server logs for anomalous 404 requests and path probing patterns

## Objectives

1. Elicit a server response that discloses internal file paths
2. Gather reconnaissance data on the target's filesystem for attack planning
3. Validate the presence of information disclosure vulnerabilities

## Instructions

### Step 1: Construct and Send Invalid URL Request

**Context**: Craft a simple invalid path by duplicating the trailing slash and adding a non-existent endpoint (e.g., '//x'). This bypasses normal routing and hits the error handler, exposing the path in the response body.

**Command** ([[commands/curl-fetch-ooni-invalid-url]]):
```bash
curl https://explorer.ooni.torproject.org//x
```

> This command performs a GET request to the invalid URL. On success, the output will include a 404 status and an error message embedding the full server path, such as "No such file or directory: '/path/to/webroot//x'". Verify the response for path leakage; if no disclosure occurs, try variations like '/nonexistent' or observe browser dev tools for the same effect.

### Step 2: Analyze Response for Disclosure

**Context**: Inspect the returned HTML or text for absolute paths. This step confirms the vulnerability and extracts usable intelligence.

**Command** (Manual inspection or pipe to grep):
```bash
curl https://explorer.ooni.torproject.org//x | grep -i "path\|directory"
```

> Expected output: Lines containing filesystem paths (e.g., "/var/www/..."). If paths are revealed, document them for chaining with other exploits like local file inclusion.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-ooni-invalid-url]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[full-path-disclosure]]
- [[web-vulnerability]]
- [[Reconnaissance]]
