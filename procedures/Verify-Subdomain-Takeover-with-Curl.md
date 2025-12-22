---
id: proc-verify-takeover-curl
tags:
  - verification
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-verify-subdomain-takeover]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:51:26.589Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Subdomain Takeover with Curl

## Summary

This procedure uses curl to fetch and confirm the content on the taken-over subdomain, ensuring the custom content is served instead of the original error page.

## Description

Post-configuration, verify the takeover by requesting the subdomain URL. The response should show the injected 'Hello World!<!--FRANS ROSEN-->' instead of Modulus.io's error. This step validates the attack's success in a web environment. Prerequisites: Completed takeover steps. Expected outcome: Custom content in response, confirming control.

## Requirements

1. Command-line access with curl installed
2. Network connectivity to the subdomain
3. Knowledge of expected custom content

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected HTTP responses from subdomains
- Use web application firewalls (WAF) to detect anomalous content
- Regularly probe your own subdomains for takeover signs

## Objectives

1. Confirm subdomain serves attacker content
2. Provide proof-of-concept evidence
3. Validate full control before further exploitation

## Instructions

### Step 1: Execute Curl Request

**Context**: Fetch the subdomain to inspect the served content.

Run [[commands/curl-verify-subdomain-takeover]]:

```bash
curl https://api.legalrobot.com
```

> This retrieves the raw HTML. Expected output: 'Hello World!<!--FRANS ROSEN-->' or similar custom text.

### Step 2: Inspect Output

**Context**: Check for the identifying comment or content.

Review the response for absence of error page and presence of custom elements.

> Success if custom content appears, indicating takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-subdomain-takeover]]

## Tools Used

- [[tools/curl]]

## Tags

- [[verification]]
- [[subdomain-takeover]]
