---
id: proc-send-crafted-post-rce
name: Send-Crafted-POST-Request-for-RCE
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.783Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - rce
  - api-bypass
  - post-request
commands: []
platforms:
  - Web
  - PHP
  - WordPress
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
---

# Send-Crafted-POST-Request-for-RCE

## Summary

This procedure sends a POST request with the malicious sslsig to the Vaultpress API, bypassing validation due to the OpenSSL error and enabling unauthenticated RCE.

## Description

The POST includes serialized data for 'uri' and 'post', plus the crafted sslsig. The validate_api_signature method's loose check allows the -1 return to pass, granting API access for code execution on the server.

## Requirements

1. sslsig payload from key generation
2. Curl or HTTP client
3. Accessible API endpoint from previous steps

## Defense

Defensive measures and detection strategies:

- Use constant-time comparisons for signatures (e.g., hash_equals)
- Rate-limit API endpoints
- Log and alert on failed OpenSSL verifications

## Objectives

1. Bypass signature validation
2. Gain unauthenticated API access
3. Execute remote code via plugin functions

## Instructions

### Step 1: Prepare and Send POST Payload

**Context**: Include sslsig in POST to trigger bypass and RCE payload.

**Command** (curl-post-bypass):
```bash
curl -X POST "http://target.wordpress.com/wp-admin/admin-ajax.php" \
  -d "action=vaultpress_api" \
  -d "sslsig=<base64-sslsig>" \
  -d "data=<serialized-uri-post-rce-payload>"
```

> Submits the exploit. Expected output: Successful API response with RCE results, like command echo or file creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[PowerShell]] Command and Scripting Interpreter (PHP)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- api-bypass
- post-request
