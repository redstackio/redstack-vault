---
tags:
  - deserialization
  - rce-trigger
  - session-cookie
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: fff03315-24fa-4ddf-bc8f-4f5df322ca67
created_at: '2025-12-11T03:48:06.036Z'
updated_at: '2025-12-11T03:48:06.036Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Trigger Deserialization Payload via Session Cookie

## Summary

This procedure triggers the injected deserialization payload in GitLab by sending a request with a crafted session cookie, leading to arbitrary command execution.

## Description

The injected session in Redis is loaded via Marshal.load when the cookie is presented, executing the gadget chain. This achieves full RCE on the GitLab server.

## Requirements

1. Successful prior injection
2. Matching session key (e.g., 'gggg')
3. Access to GitLab web endpoint

## Defense

Defensive measures and detection strategies:

- Use safe deserialization methods or avoid Marshal.load
- Monitor for anomalous session loads and command executions
- Implement WAF rules for suspicious cookies

## Objectives

1. Load injected session
2. Execute deserialization gadget
3. Achieve RCE

## Instructions

### Step 1: Send Trigger Request

**Context**: GET request with crafted cookie to trigger Marshal.load.

**Command** ([[commands/curl-trigger-session-payload]]):
```bash
curl -v 'http://gitlab.wbowling.info/root' -H 'Cookie: _gitlab_session=gggg'
```

> This executes the payload on the server.

### Step 2: Verify Execution

**Context**: Check server for evidence (e.g., /tmp/vakzz22 file).

No command; manual verification on compromised system.

> Command output indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-trigger-session-payload]]

## Tools Used

- #curl

## Tags

- #deserialization
- #rce-trigger
