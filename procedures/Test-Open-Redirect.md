---
id: proc-uuid-4
name: Test Open Redirect
tags:
  - phishing
  - redirect
  - testing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-open-redirect]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:27.106Z'
sub_techniques:
  - '[[T1566.002]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Test Open Redirect

## Summary

This procedure tests the open redirect vulnerability by sending a crafted HTTP request to the hekto server, verifying the 307 redirect to a protocol-relative URL that enables phishing.

## Description

With the server running and trigger file in place, a GET request to '//hackerone.com' causes the server to check for 'hackerone.com.html', find it, and redirect to '//hackerone.com/' without validation. This can be abused to redirect to malicious domains. The test uses curl to inspect headers. Prerequisites: running server on port 3000. Outcome: confirmation of the redirect, highlighting phishing risk.

## Requirements

1. Hekto server active on localhost:3000
2. Trigger file present
3. curl installed
4. Local network access

## Defense

Defensive measures and detection strategies:

- Implement redirect URL whitelisting and validation
- Log all 3xx redirects for anomaly detection
- Use CSP headers to block untrusted redirects in browsers

## Objectives

1. Trigger the vulnerable redirection
2. Verify arbitrary domain redirect
3. Demonstrate phishing potential

## Instructions

### Step 1: Send Test Request

**Context**: Use curl to request the double-slash path and include headers.

**Command** ([[commands/test-open-redirect]]):
```bash
curl -i http://127.0.0.1:3000//hackerone.com
```

> Returns headers showing HTTP/1.1 307 Temporary Redirect and Location: //hackerone.com/, plus an HTML redirect body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.002]] Spearphishing Link

## Commands Used

- [[commands/test-open-redirect]]

## Tools Used

- [[tools/curl]]

## Tags

- phishing
- redirect
- testing
