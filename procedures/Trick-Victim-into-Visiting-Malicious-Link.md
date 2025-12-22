---
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
updated_at: '2025-12-13T23:52:25.174Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
id: aa321868-738b-4f55-84f6-6cb106a807e8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trick-Victim-into-Visiting-Malicious-Link

## Summary

This procedure involves social engineering to lure an authenticated user to the CSRF PoC site, triggering the exploit via their active session.

## Description

Phishing delivers the link to the malicious HTML, exploiting the victim's trust and session. No technical commands; focuses on delivery vectors like email or chat. Success relies on victim being logged in.

## Requirements

1. Access to victim's communication channels (email, messaging)
2. Crafted malicious site ready
3. Spoofed sender to appear legitimate

## Defense

Defensive measures and detection strategies:

- User training on phishing recognition
- Email filters for suspicious links
- Browser warnings for cross-site requests

## Objectives

1. Induce visit to attacker site
2. Leverage active session for CSRF
3. Trigger payload injection

## Instructions

### Step 1: Prepare Phishing Vector

**Context**: Create a convincing pretext (e.g., "Check this urgent alert update").

Embed the link to the hosted HTML in an email or message.

### Step 2: Monitor and Confirm Visit

**Context**: Track if the victim loads the page.

Use server logs or analytics to detect IP and user-agent matching victim.

> Expected: Log entry for page load and form submission.

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

- phishing
- social-engineering
