---
tags:
  - tls
  - handshake
  - client-cert
type: procedure
tools:
  - '[[tools/OpenSSL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/openssl-s-client-auth-handshake]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:31.109Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 929629d7-c077-48e0-82b6-2c3a23c2adda
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Establish Authenticated TLS Session with Virtual Host A

## Summary

This procedure establishes a full TLS 1.3 handshake with the first NGINX virtual host (A) using a valid client certificate, obtaining a session ticket for later resumption.

## Description

In NGINX setups with shared IP/port virtual hosts and enabled TLS session tickets via OpenSSL, this step authenticates to host A to generate a ticket. The ticket is not isolated per host, enabling cross-host resumption. Prerequisites include a valid client certificate for host A and network access to the server.

## Requirements

1. Valid client certificate (client.crt) and private key (client.key) for host A
2. OpenSSL installed on the attacker's system
3. Network connectivity to the target's IP and port (e.g., 443)

## Defense

Defensive measures and detection strategies:

- Disable TLS session tickets or session cache on shared virtual hosts
- Isolate session keys per virtual host using NGINX ssl_session_cache directive
- Monitor for anomalous TLS resumptions via server logs

## Objectives

1. Complete authenticated TLS handshake with host A
2. Extract session ticket for resumption
3. Verify authentication success

## Instructions

### Step 1: Perform TLS Handshake with Client Certificate

**Context**: Initiate a full TLS 1.3 connection to host A, providing the client certificate for authentication.

**Command** ([[commands/openssl-s-client-auth-handshake]]):
```bash
openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com
```

> This command performs the handshake and outputs TLS messages, including the NewSessionTicket. Look for the ticket in the output and save the session state if needed (e.g., via -sess_out). Successful output shows "Verify return code: 0 (ok)" and HTTP access confirmation.

### Step 2: Verify Session Ticket Issuance

**Context**: Confirm the session ticket was issued during the handshake.

**Command** ([[commands/openssl-s-client-session-extract]]):
```bash
openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com -sess_out session_A.pem
```

> Extracts the session to a file for later use. Expected output includes the session ticket details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/openssl-s-client-auth-handshake]]
- [[commands/openssl-s-client-session-extract]]

## Tools Used

- [[tools/OpenSSL]]

## Tags

- [[tls]]
- [[nginx]]
- [[auth]]
