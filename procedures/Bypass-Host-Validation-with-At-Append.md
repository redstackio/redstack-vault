---
id: proc-bypass-at-append
tags:
  - ssrf
  - bypass
  - header-manipulation
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
updated_at: '2025-12-14T17:30:46.892Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Host Validation with @ Append

## Summary

This procedure exploits a parsing flaw in Slack's host validation by appending '@' to the hostname in the X-Forwarded-Host header, allowing redirection to arbitrary domains while mimicking the legitimate host.

## Description

The header `X-Forwarded-Host: files.slack.com@your-controlled-domain.com` tricks the server into forwarding requests internally to the attacker's domain. The backend processes this as a valid override, resulting in a 302 redirect. This bypasses validation that checks only the prefix, enabling SSRF to external or internal targets on AWS. Requires a controlled domain and prior request interception.

## Requirements

1. Controlled domain/server for receiving requests
2. Burp Repeater with modified request ready
3. Understanding of HTTP header parsing

## Defense

Defensive measures and detection strategies:

- Parse and validate hostnames strictly, rejecting '@' characters
- Implement regex checks to block appended segments in headers
- Monitor for redirects to unauthorized domains

## Objectives

1. Achieve SSRF by bypassing host checks
2. Redirect requests to attacker-controlled endpoint
3. Confirm exploitation feasibility

## Instructions

### Step 1: Modify Header with @ Append

**Context**: Update the header to exploit the parsing vulnerability.

No command required; edit in Burp:

- Set X-Forwarded-Host: files.slack.com@your-controlled-domain.com
- Click Send

> Expected output: 302 redirect to http://your-controlled-domain.com/files-pri/...

### Step 2: Follow Redirect

**Context**: Observe the redirected path to verify bypass.

No command required; use Burp:

- Enable follow redirects in Repeater if needed

> Expected output: Request path preserved but host changed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[bypass]]
- [[header-manipulation]]
