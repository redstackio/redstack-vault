---
id: proc-detect-dangling-modulus
tags:
  - subdomain-takeover
  - reconnaissance
  - dns
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.600Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Detect Dangling Subdomain on Modulus.io

## Summary

This procedure identifies subdomain takeover vulnerabilities by accessing a target subdomain and checking for default error pages from hosting services like Modulus.io, indicating a dangling DNS record without an active application.

## Description

In a subdomain takeover attack, DNS records point to third-party services (e.g., Modulus.io) but lack corresponding configurations, allowing attackers to claim them. This step focuses on reconnaissance: visiting the subdomain https://api.legalrobot.com/ reveals the Modulus.io error 'NO APPLICATION WAS FOUND FOR api.legalrobot.com', confirming vulnerability. Prerequisites include internet access and basic web browsing or curling capabilities. Expected outcome: confirmation of dangling status, setting up for exploitation.

## Requirements

1. Internet access to the target subdomain
2. Browser or command-line tool like curl
3. Knowledge of common hosting service error pages

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like dnsdumpster or subjack
- Implement DNS monitoring alerts for changes or unresolved records
- Use services like SecurityTrails to track historical DNS changes

## Objectives

1. Confirm the subdomain points to an unconfigured service
2. Identify the hosting provider (Modulus.io) for targeted exploitation
3. Assess potential for takeover without alerting the target

## Instructions

### Step 1: Access the Subdomain

**Context**: Visit the target subdomain to observe the response, looking for provider-specific error pages.

No specific command required; use a browser or [[commands/curl-verify-subdomain-takeover]] for verification:

```bash
curl https://api.legalrobot.com
```

> This fetches the page content. Expected output includes the Modulus.io error message indicating no application found.

### Step 2: Analyze Response

**Context**: Inspect the HTML or text for indicators of dangling status.

Manually review the output for phrases like 'NO APPLICATION WAS FOUND'.

> Success if the error page matches Modulus.io's default template.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[subdomain-takeover]]
- [[Reconnaissance]]
