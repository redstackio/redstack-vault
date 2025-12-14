---
tags:
  - google-dorking
  - information-disclosure
  - recon
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
id: 2ccda048-e6a3-4558-9326-275b85d2ad5a
created_at: '2025-12-14T17:33:24.377Z'
updated_at: '2025-12-14T17:33:24.377Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Leaked Confirmation Links Using Google Dorking

## Summary

This procedure uses Google dorking to identify publicly indexed confirmation links on Sorare.com that expose sensitive tokens for email and device verification, enabling subsequent exploitation for account takeover.

## Description

Attackers perform targeted searches to find URLs containing tokens that should not be publicly accessible. The root cause is inadequate robot.txt configurations or link sharing protections, allowing search engines to index sensitive endpoints. This reconnaissance step reveals tokens for random users, setting up auth bypass attacks. Expected outcomes include a list of exploitable URLs leading to PII exposure.

## Requirements

1. Internet access and [[tools/Google-Search]]
2. Knowledge of Google dorking syntax
3. Target domain with poor crawling protections (e.g., sorare.com)

## Defense

Defensive measures and detection strategies:

- Implement strict robots.txt to block /confirm_* paths
- Use noindex meta tags on confirmation pages
- Monitor search engine caches for sensitive URLs and request removals

## Objectives

1. Gather leaked tokens for targeting specific users
2. Identify vulnerable confirmation endpoints
3. Enable follow-on token manipulation for access

## Instructions

### Step 1: Execute Google Dork Query

**Context**: Craft a precise search to filter for token-containing URLs on the target site.

Use [[tools/Google-Search]] with the query:

```plaintext
site:sorare.com inurl:token
```

> This returns results limited to sorare.com domains with 'token' in the URL path or parameters. Expected output: SERP with links like https://sorare.com/confirm_email?token=...

### Step 2: Collect and Analyze Results

**Context**: Review and extract usable URLs from search results.

Manually copy URLs from the search engine results page, focusing on confirm_email and confirm_device endpoints.

> Expected output: A list of 10+ leaked links with visible tokens. Success if tokens show predictable patterns (e.g., underscores and digits).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- [[Vulnerability Scanning]]

## Commands Used


## Tools Used

- [[tools/Google-Search]]

## Tags

- [[google-dorking]]
- [[information-disclosure]]
