---
id: proc-shopify-xss-distribute-001
tags:
  - phishing
  - social-engineering
  - url-distribution
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
  - '[[Phishing]]'
updated_at: '2025-12-13T23:56:03.522Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Distribute Malicious URL to Authenticated Staff

## Summary

This procedure covers sending the crafted malicious URL to a Shopify staff member via social engineering or phishing to prompt visitation while authenticated.

## Description

Delivery relies on trusted communication channels to bypass suspicion. The URL appears as a legitimate internal link to marketing reports, exploiting the victim's role. Prerequisites include identifying a staff contact. Expected outcomes: Victim clicks the link in an admin session, setting up the reflection.

## Requirements

1. Contact information for authenticated staff (e.g., email, Slack)
2. Pretext for delivery (e.g., urgent report review)
3. Crafted URL from prior procedure

## Defense

Defensive measures and detection strategies:

- Train staff on phishing recognition and URL verification
- Implement email filtering for suspicious admin links
- Log and alert on unusual parameter values in inbound links

## Objectives

1. Deliver URL without raising suspicion
2. Ensure victim is authenticated during access
3. Maximize click-through rate

## Instructions

### Step 1: Prepare Delivery Message

**Context**: Craft a convincing pretext to encourage clicking.

Write an email or message like: "Hi, please review this marketing report for the campaign: [MALICIOUS-URL]. Let me know your thoughts."

### Step 2: Send the URL

**Context**: Transmit via appropriate channel.

Use email, internal chat, or shared document to send the link. Ensure the victim is likely logged into Shopify admin.

**Expected Output**: Message delivered; victim potentially navigates to the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[shopify]]
