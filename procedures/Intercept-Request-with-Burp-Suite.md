---
id: proc-intercept-burp-slack
tags:
  - ssrf
  - intercept
  - http-proxy
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
updated_at: '2025-12-14T17:30:46.897Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Request with Burp Suite

## Summary

This procedure captures an HTTP request to a Slack file URL using Burp Suite, allowing for inspection, modification, and replay in the Repeater module to confirm baseline functionality before SSRF exploitation.

## Description

Burp Suite acts as a proxy to intercept traffic to files.slack.com. By navigating to the direct file URL, the request is captured and forwarded to Repeater for testing. This establishes a working request that can be altered for header manipulation. Prerequisites include Burp Suite installation and browser proxy configuration. Outcomes include a verified request-response pair, essential for detecting server behavior in SSRF scenarios targeting AWS backends.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Direct Slack file URL from previous step

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning to block proxy interception
- Monitor for unusual proxy traffic patterns
- Use HSTS to prevent MITM in non-dev environments

## Objectives

1. Capture and verify the baseline file request
2. Prepare for header modifications
3. Ensure request integrity for exploitation

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept browser traffic.

No command required; configure in Burp:

- Launch Burp Suite, go to Proxy tab, ensure Intercept is on
- In browser, set proxy to 127.0.0.1:8080 and install Burp CA certificate

> Expected output: Browser traffic routes through Burp without errors.

### Step 2: Intercept and Replay

**Context**: Capture the request to the file URL and test in Repeater.

No command required; use Burp UI:

- Navigate to the Slack file URL in browser
- In Burp Proxy, intercept the GET request, forward it
- Send to Repeater tab and click Send

> Expected output: 200 OK response with file content in Repeater.

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
- [[intercept]]
- [[http-proxy]]
