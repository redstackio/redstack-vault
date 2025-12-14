---
id: proc-send-message-burp
tags:
  - ssrf
  - burp
  - post-request
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.083Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Private-Message-with-Burp-Suite

## Summary

Intercept and send the private message POST request using Burp Suite to ensure the SSRF payload is properly encoded in the raw= parameter.

## Description

The message submission hits /posts with raw= containing the Markdown payload. Burp allows inspection/modification to bypass any client-side checks and confirm the exploit path.

## Requirements

1. Burp Suite configured as browser proxy
2. Completed message with payload
3. Target Discourse accessible

## Defense

Defensive measures and detection strategies:

- Server-side validation of raw= parameter for malicious URLs
- WAF rules to block suspicious POST payloads
- Proxy logs for anomalous traffic patterns

## Objectives

1. Submit payload without interception blocks
2. Verify request integrity

## Instructions

### Step 1: Configure Proxy

**Context**: Route browser traffic through Burp.

**Command** (Burp config):
Set browser proxy to 127.0.0.1:8080

> Burp intercepts requests. Expected: All site traffic captured.

### Step 2: Submit Message

**Context**: Fill and send the form.

**Command** (Browser/Burp action):
Click 'Send' on composer; intercept in Burp Proxy > HTTP history or Repeater.

> POST /posts with raw=%3CTEST%20%21%5B%5D(http%3A%2F%2F192.166.218.53%2Fmalicious3.php). Expected: Forward to get 200 OK.

### Step 3: Analyze Request

**Context**: Inspect for encoding issues.

**Command** (Burp action):
View raw= param in Inspector.

> Ensure URL not sanitized. Expected: Payload intact post-forward.

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

- ssrf
- submission
- interception
