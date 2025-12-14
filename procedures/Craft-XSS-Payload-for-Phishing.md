---
tags:
  - xss
  - phishing
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/open-xss-phishing-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e7874ed9-9224-4040-b157-592c5193b3fe
created_at: '2025-12-13T23:56:20.469Z'
updated_at: '2025-12-13T23:56:20.469Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Phishing

## Summary

This procedure crafts an XSS payload to render a phishing page within the Swagger-UI context, potentially capturing user credentials.

## Description

By injecting a base64-encoded YAML that loads HTML/JS for a fake login page, attackers can trick users into entering sensitive information.

## Requirements

1. Vulnerable Swagger-UI endpoint
2. Browser for testing
3. Custom phishing HTML encoded in base64

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP)
- Detect anomalous page renders in API docs

## Objectives

1. Render phishing interface
2. Capture user inputs
3. Escalate to credential theft

## Instructions

### Step 1: Craft and Open URL

**Context**: Build and test the phishing URL.

Execute [[commands/open-xss-phishing-url]] to open:

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-phishing-payload'
```

> The payload renders a phishing form via injected JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/open-xss-phishing-url]]

## Tools Used

- [[Browser]]

## Tags

- [[xss]]
- [[Phishing]]
