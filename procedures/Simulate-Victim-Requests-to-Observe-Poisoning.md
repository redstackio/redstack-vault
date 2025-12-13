---
tags:
  - http-request-smuggling
  - simulation
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-signin-victim-simulation]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 35023c6c-ed17-4e49-9e89-c4acbe928a64
created_at: '2025-12-13T09:01:21.726Z'
updated_at: '2025-12-13T09:01:21.726Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate Victim Requests to Observe Poisoning

## Summary

This procedure simulates normal user requests to the /signin endpoint to observe the effects of socket poisoning, such as redirections from the smuggled request.

## Description

After sending the desync request, queue multiple GET requests to verify if any are affected by the poisoned socket, leading to redirection to the malicious domain.

## Requirements

1. Turbo Intruder configured
2. Prior desync request sent
3. Network access to target

## Defense

Defensive measures and detection strategies:

- Use connection pooling monitoring
- Detect unexpected redirections in server logs

## Objectives

1. Verify socket poisoning
2. Observe redirection impact
3. Confirm exploit success

## Instructions

### Step 1: Queue Victim Simulation Requests

**Context**: Send multiple GET requests to simulate visitors.

**Command** ([[commands/get-signin-victim-simulation]]):
```bash
GET /signin HTTP/1.1
Host: launchpad.37signals.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,la;q=0.8
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D

```

> This simulates normal traffic; expect one request to be redirected if poisoning succeeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/get-signin-victim-simulation]]

## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- [[http-request-smuggling]]
- [[simulation]]
