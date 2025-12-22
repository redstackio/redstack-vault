---
tags:
  - xss
  - credential-theft
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5600d4c3-166c-4c13-95ff-dd191b9c0a0b
created_at: '2025-12-11T06:10:22.363Z'
updated_at: '2025-12-11T06:10:22.363Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Execute JavaScript for Credential Theft

## Summary

This procedure covers the execution phase where the injected JavaScript runs in the victim's browser, capturing and exfiltrating credentials or session data.

## Description

Upon URL visit, the reflected XSS payload executes JS in the context of the OAUTH2 domain, allowing access to cookies, local storage, or form data. Data is sent to an attacker server, enabling theft or hijack. This exploits the trust in the login flow.

## Requirements

1. Attacker-controlled server to receive exfiltrated data.
2. Victim has visited the malicious URL.
3. Payload designed for exfiltration (e.g., via GET request).

## Defense

Defensive measures and detection strategies:

- Enable XSS protections like HttpOnly cookies and CSP.
- Monitor network traffic for unexpected outbound requests from login pages.

## Objectives

1. Run JS in victim browser.
2. Capture sensitive data.
3. Exfiltrate to attacker.

## Instructions

### Step 1: Monitor Exfiltration Server

**Context**: Set up a listener to capture incoming data.

Use a simple web server to log requests.

### Step 2: Confirm Theft

**Context**: Verify received data includes credentials or tokens.

Inspect logs for exfiltrated information like cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[credential-theft]]
- [[commands/curl-test-xss-url]]
