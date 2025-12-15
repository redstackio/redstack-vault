---
id: proc-access-unikrn-history-1
tags:
  - web-access
  - session-handshake
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-transaction-history]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.259Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Unikrn-Transaction-History-Endpoint

## Summary

This procedure initiates access to the Unikrn cashier transaction history endpoint during session handshake, setting up the context for IDOR exploitation by establishing an authenticated session.

## Description

In the Unikrn cashier system, the transaction history page at https://cashier.unikrn.com/cashier/transaction-history performs a session handshake that can be intercepted and manipulated. This step ensures the attacker has a valid session before attempting unauthorized access. The target environment is a web application requiring authentication, and success leads to a baseline response that can be altered for IDOR attacks. Expected outcomes include receiving the attacker's own transaction data, confirming the endpoint's accessibility.

## Requirements

1. Authenticated session cookie from a valid Unikrn account
2. Network access to https://cashier.unikrn.com
3. Browser or command-line tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on session handshakes
- Log all access to transaction endpoints and monitor for anomalous patterns

## Objectives

1. Establish a valid session on the transaction history endpoint
2. Confirm endpoint responsiveness for further exploitation
3. Prepare request template for IDOR manipulation

## Instructions

### Step 1: Authenticate and Access Endpoint

**Context**: Log in to Unikrn and navigate to the transaction history to capture the session cookie, then use curl to replicate the access.

**Command** ([[commands/curl-access-transaction-history]]):
```bash
curl -H "Cookie: session=your_session_cookie" https://cashier.unikrn.com/cashier/transaction-history
```

> This command sends a GET request with the session cookie, initiating the handshake. Expected output is a JSON response with transaction data or a 200 OK status.

### Step 2: Verify Session Handshake

**Context**: Check the response for session confirmation indicators, such as a handshake token.

**Command** ([[commands/curl-access-transaction-history]]):
```bash
curl -v -H "Cookie: session=your_session_cookie" https://cashier.unikrn.com/cashier/transaction-history
```

> The verbose flag (-v) shows headers; look for successful handshake in the body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-transaction-history]]

## Tools Used


## Tags

- web-access
- session-handshake
