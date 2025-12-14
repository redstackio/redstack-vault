---
id: proc-craft-phishing-links
tags:
  - phishing
  - social-engineering
  - open-redirect
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-phishing-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:34.943Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Craft-Phishing-Links-for-Social-Engineering

## Summary

This procedure creates and tests phishing links that exploit the open redirect, tricking users into visiting malicious sites via Expedia interactions like logout or login.

## Description

By sending crafted links (e.g., expedia.com/?logout=1&rurl=phish-site), attackers enable social engineering. Victims believe they're interacting with legitimate Expedia flows but end up on fake sites for credential theft or malware. This works across affected domains and bypasses via user actions.

## Requirements

1. Attacker-controlled phishing domain
2. Means to distribute links (email, social media)
3. Testing with curl/browser

## Defense

Defensive measures and detection strategies:

- Educate users on verifying URLs before clicking
- Use URL scanners in email gateways
- Monitor for mass distribution of suspicious Expedia-like links

## Objectives

1. Generate deceptive phishing URLs
2. Validate end-to-end redirect to malicious site
3. Achieve credential compromise or malware spread

## Instructions

### Step 1: Build Phishing URL

**Context**: Combine Expedia endpoint with malicious rurl for deception.

**Command** ([[commands/curl-phishing-test]]):
```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://fake-expedia-phish.com/steal-creds" -v
```

> Tests the link; output confirms redirect to phishing site.

### Step 2: Distribute and Monitor

**Context**: Send links to targets and observe interactions.

No command; use email tools to send.

> Expected: Victims redirected, potential data exfil.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-phishing-test]]

## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
