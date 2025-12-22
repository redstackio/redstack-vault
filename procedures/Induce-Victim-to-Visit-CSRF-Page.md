---
tags:
  - phishing
  - drive-by
  - csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.292Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 22d3df99-4477-41d6-97cd-1ab97088ee4c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Victim-to-Visit-CSRF-Page

## Summary

This procedure describes methods to trick an authenticated user into visiting the hosted CSRF page, triggering the unauthorized request to UPchieve's vulnerable endpoints while their session cookie is active.

## Description

The core of CSRF relies on user interaction: loading the malicious page in a browser where the victim is logged into the target site. Since the page auto-submits, the victim may not notice anything beyond a brief load or redirect. Delivery often involves social engineering, such as phishing emails or links in trusted contexts. The attack succeeds because browsers send cookies cross-site without SameSite protection, but CORS prevents attacker from seeing responses.

## Requirements

1. Hosted CSRF page URL (e.g., http://attacker.com/csrf_poc.html)
2. Contact method with victim (email, chat, social media)
3. Lure tailored to victim (e.g., fake tutor update for UPchieve users)

## Defense

Defensive measures and detection strategies:

- Train users to recognize phishing and avoid clicking unknown links
- Implement SameSite=Strict on cookies to block cross-site usage
- Use referrer checks or token validation on sensitive endpoints
- Monitor user agents or referrers for suspicious submissions

## Objectives

1. Get victim to load the page while authenticated
2. Ensure silent execution without alerting the user
3. Maximize success via convincing delivery

## Instructions

### Step 1: Craft Delivery Mechanism

**Context**: Prepare a phishing vector to entice the victim.

Create an email or message: "Hey, check this new availability tool for UPchieve: http://attacker.com/csrf_poc.html" Ensure the link appears legitimate, perhaps mimicking UPchieve styling.

### Step 2: Send the Lure

**Context**: Deliver the link to the victim via email, SMS, or embedded in a compromised site.

Send the message when the victim is likely active and logged in. For drive-by, embed the iframe or script on a malicious site the victim visits.

No command; use email client or messaging app.

### Step 3: Monitor for Execution

**Context**: Indirectly confirm via later verification, as no response is readable.

Watch for timing of account changes post-delivery.

**Expected Output**: Victim clicks and loads page, submitting the form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[drive-by]]
- [[csrf]]
