---
tags:
  - rce-trigger
  - http-injection
  - deserialization
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/http-get-openam-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:18.971Z'
sub_techniques: []
id: bb6bbc64-7261-4bf8-902e-7e5344aa9a70
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-HTTP-Request-to-Trigger-RCE

## Summary

This procedure sends a crafted HTTP GET request to the vulnerable ForgeRock OpenAM endpoint, injecting the deserialization payload to trigger remote code execution without authentication.

## Description

The Jato framework in OpenAM deserializes user-supplied input in the specified endpoint parameter without validation, allowing the Click1 gadget to execute system commands. The request targets a redacted path (specific to CVE-2021-35464, e.g., an authentication or session endpoint) and uses the encoded payload as the parameter value. This achieves pre-auth RCE on the server.

## Requirements

1. Generated payload.txt from previous step
2. Access to target OpenAM server on port 443
3. HTTP client like curl, Burp Suite, or netcat

## Defense

Defensive measures and detection strategies:

- Patch OpenAM to fixed version (post-CVE-2021-35464)
- Implement web application firewall (WAF) rules to block suspicious base64 in parameters
- Log and alert on 302 redirects to AMInvalidURL
- Restrict deserialization to trusted sources

## Objectives

1. Deliver payload to vulnerable endpoint
2. Trigger deserialization gadget chain
3. Achieve arbitrary command execution

## Instructions

### Step 1: Craft and Send GET Request

**Context**: Replace the redacted endpoint and inject the payload to exploit the deserialization flaw.

**Command** ([[commands/http-get-openam-exploit]]):
```bash
GET /openam/██████████=contents-of-payload.txt HTTP/1.1
Host: target-server:443
```

> Use curl or Burp Repeater: `curl -X GET "https://target:443/openam/██████████=\$(cat payload.txt)" -k`. The redacted path is the specific parameter-vulnerable endpoint. Expected output: HTTP 302 with Location: https://target:443/openam/base/AMInvalidURL and Content-Length: 0.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-get-openam-exploit]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- rce-trigger
- http-injection
- deserialization
