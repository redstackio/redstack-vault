---
tags:
  - xss
  - chaining
  - redirect
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[T1566.001]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: cc8d2533-c492-4ca3-a38b-7f3806170515
created_at: '2025-12-14T03:47:12.596Z'
updated_at: '2025-12-14T03:47:12.596Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[T1566.001]]'
---
# Execute-Chained-XSS-Redirects

## Summary

This procedure chains XSS execution with open redirects in a javascript: payload to alert data and redirect to malicious sites, facilitating phishing as demonstrated in the Semrush bypass.

## Description

In the attack scenario, a double-encoded payload executes JS to steal info (e.g., domain) and then redirects sequentially (e.g., to google.com and facebook.com). Targets web redirect endpoints. Prerequisites: Successful basic XSS. Expected: Multi-action execution for session hijacking.

## Requirements

1. Valid XSS bypass payload
2. External sites for chaining (e.g., google.com)
3. Browser for testing redirects

## Defense

Defensive measures and detection strategies:

- Validate redirect destinations against whitelist
- Detect chained JS actions via anomaly monitoring
- Use referrer checks to block unauthorized redirects

## Objectives

1. Collect data via alerts
2. Perform unintended redirects
3. Enable phishing or hijacking

## Instructions

### Step 1: Build Chained Payload

**Context**: Combine alert and location assignments with double-encoding.

Craft: javascript://%250Aalert(document.location="https://google.com",document.location="https://www.facebook.com").

> Expected: Payload that alerts then redirects twice.

### Step 2: Deploy and Verify

**Context**: Inject into endpoint and observe chain.

URL: https://www.semrush.com/redirect?url=javascript://%250Aalert(document.domain) for domain test, or full chain. Visit.

> Expected: Alert shows domain; redirects occur sequentially.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[chained-xss]]
- [[open-redirect]]
