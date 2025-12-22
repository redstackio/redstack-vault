---
tags:
  - path-traversal
  - access-control
  - cve-2020-3452
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-direct-file-access]]'
verified: false
platforms:
  - Web
  - Cisco ASA
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:05.623Z'
sub_techniques: []
id: 4764cf40-7134-444a-970d-d1904731a9b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Direct-File-Access-Protection

## Summary

This procedure tests direct access to sensitive files like portal_inc.lua in Cisco ASA/FTD to confirm they are protected, underscoring the value of the path traversal bypass in CVE-2020-3452.

## Description

Direct file access to paths like /+CSCOE+/portal_inc.lua is blocked by the application's access controls, resulting in errors. This step validates the protection mechanism before exploiting traversal. Targets the HTTPS web server on port 443 of vulnerable Cisco devices.

## Requirements

1. Network access to the target's HTTPS port 443
2. Knowledge of the sensitive file path (e.g., /+CSCOE+/portal_inc.lua)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Enforce strict URL access controls in Cisco ASA/FTD configurations
- Log and alert on 500 errors or 'Wrong URL' responses to protected paths
- Regularly audit webroot file permissions

## Objectives

1. Confirm direct access denial to sensitive files
2. Highlight the traversal vulnerability's bypass capability
3. Baseline normal failure behavior

## Instructions

### Step 1: Attempt Direct File Access

**Context**: Send a straightforward GET request to the sensitive file path to observe the protection response.

**Command** ([[commands/curl-direct-file-access]]):
```bash
curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' $'https://target.example.com/%2bCSCOE%2b/portal_inc.lua'
```

> The command mimics a browser request. Expected output is HTTP/1.1 500 Internal Server Error with a message like 'Wrong URL' or access denied, confirming protection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-direct-file-access]]

## Tools Used

- [[tools/curl]]

## Tags

- access-control
- verification
- cve-2020-3452
