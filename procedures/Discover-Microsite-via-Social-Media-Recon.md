---
tags:
  - reconnaissance
  - social-media
  - twitter
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-13T23:52:25.435Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 626413d4-ac19-4982-b86c-97047d65be8e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Microsite via Social Media Recon

## Summary

This procedure involves manual reconnaissance on social media platforms like Twitter to identify public mentions of target domains, uncovering microsites or shareable content that may contain vulnerabilities.

## Description

In the context of web application testing, attackers often scan public sources for recent activity. Here, searching Twitter for 'grab.com' reveals mentions of the Valentine's microsite at growth.grab.com/valentine/active/my.html, which features shareable cards for drivers. This step provides initial access to the attack surface without direct interaction with the target.

## Requirements

1. Access to Twitter search
2. Basic understanding of domain-related keywords
3. No special tools or credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor social media for mentions of internal tools or microsites
- Limit public sharing of promotional content
- Use brand monitoring tools to alert on domain mentions

## Objectives

1. Identify hidden or temporary microsites
2. Gather intelligence on shareable features
3. Establish reconnaissance baseline for further analysis

## Instructions

### Step 1: Perform Twitter Search

**Context**: Use keyword-based search to find recent relevant posts.

No command required; manually search Twitter for "grab.com" filtered by recent tweets.

> Focus on posts about Valentine's promotions or driver cards to locate the microsite URL.

### Step 2: Verify Shareable Content

**Context**: Confirm the presence of interactive elements like share buttons.

Visit identified URLs in a browser to inspect for shareable cards.

> Expected: Discovery of https://growth.grab.com/valentine/active/my.html with referral features.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[social-media]]
