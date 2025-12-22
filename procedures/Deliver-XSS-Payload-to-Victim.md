---
tags:
  - xss
  - phishing
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss-url]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 77fa1dc2-6af5-4355-b67d-6c0e45c651b3
created_at: '2025-12-11T06:10:22.366Z'
updated_at: '2025-12-11T06:10:22.366Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Deliver XSS Payload to Victim

## Summary

This procedure focuses on socially engineering a victim to visit the crafted malicious URL, triggering the reflected XSS vulnerability in the OAUTH2 flow.

## Description

Delivery relies on phishing tactics to lure the victim into clicking the link, such as disguising it as a legitimate login reset. Once clicked, the reflected payload executes without further interaction. This is effective in web environments where users are accustomed to clicking authentication links.

## Requirements

1. Crafted malicious URL from prior steps.
2. Method to send the URL (email, messaging).
3. Victim with access to the target application.

## Defense

Defensive measures and detection strategies:

- Educate users on phishing awareness.
- Use URL scanning tools in email gateways to detect script injections.

## Objectives

1. Induce victim click.
2. Trigger payload execution.
3. Set stage for data exfiltration.

## Instructions

### Step 1: Obfuscate URL

**Context**: Shorten or mask the URL to avoid suspicion.

Use a URL shortener service manually.

### Step 2: Send Phishing Message

**Context**: Craft and send a message containing the URL.

No command needed; example message: 'Your OAUTH2 login needs verification: [shortened-malicious-url]'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[Phishing]]
- [[commands/curl-test-xss-url]]
