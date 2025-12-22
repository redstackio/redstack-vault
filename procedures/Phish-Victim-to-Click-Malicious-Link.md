---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Phish-Victim-to-Click-Malicious-Link
tags:
  - phishing
  - social-engineering
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
updated_at: '2025-12-14T03:16:02.438Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Phish-Victim-to-Click-Malicious-Link

## Summary

This procedure simulates a phishing attack to lure a victim user of a Cisco ASA/FTD web interface into clicking a link that loads the malicious HTML page, initiating the CVE-2020-3580 XSS exploit chain.

## Description

Targeting users authenticated or intending to access AnyConnect or WebVPN services, this involves crafting deceptive communications (e.g., emails) that appear legitimate from Cisco or the organization. The link points to the hosted HTML, tricking the victim into browser-based interaction. No technical exploits occur here; success relies on social engineering. Expected outcomes: victim loads the page, triggering subsequent auto-submission.

## Requirements

1. Hosted malicious HTML page URL
2. Access to communication channels (email, chat) targeting victims
3. Knowledge of victim personas (e.g., IT admins using Cisco VPN)

## Defense

Defensive measures and detection strategies:

- User training on phishing recognition
- Email filters for suspicious links and domains
- Browser warnings for cross-origin redirects

## Objectives

1. Gain victim interaction without raising suspicion
2. Ensure link appears relevant to Cisco services
3. Track click-through for chain progression

## Instructions

### Step 1: Craft Phishing Message

**Context**: Design a convincing lure referencing Cisco updates or login issues to prompt clicking.

Example email body:

```
Subject: Urgent Cisco VPN Security Update Required

Dear User,

Your Cisco AnyConnect session requires immediate verification due to a security alert. Please click here to renew: http://fake-cisco.com/update.html

Best,
IT Security Team
```

Replace with your hosted URL. Use spoofed sender if possible.

> The message exploits trust in Cisco branding to drive clicks.

### Step 2: Distribute the Phishing Link

**Context**: Send to targeted victims via email lists or other vectors.

Send the message to potential users of the Cisco interface. Monitor server access logs for hits.

> Success is indicated by increased traffic to the hosted page from victim IPs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- victim-luring
