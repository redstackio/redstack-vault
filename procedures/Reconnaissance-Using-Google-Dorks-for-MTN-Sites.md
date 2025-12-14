---
id: proc-mtn-dork-recon-001
tags:
  - recon
  - dorking
  - web
type: procedure
tools:
  - '[[tools/Google-Dorks]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/google-dork-mtn-site]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:05.511Z'
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
# Reconnaissance-Using-Google-Dorks-for-MTN-Sites

## Summary

This procedure uses Google dorking to locate MTN-related web pages on associated domains like admyntec.co.za, identifying potential endpoints with dynamic parameters for further testing.

## Description

In the context of targeting MTN Group assets, Google dorks help discover in-scope pages without direct scanning. By limiting to admyntec.co.za and searching for 'MTN' in titles, attackers uncover admin or customer portals vulnerable to injection. Prerequisites include a search engine; outcomes reveal URLs for SQLi testing.

## Requirements

1. Internet access and Google search capabilities
2. Knowledge of target domain associations (e.g., admyntec.co.za with mtn.co.za)
3. No special tools beyond a browser

## Defense

Defensive measures and detection strategies:

- Monitor search engine queries for domain-specific dorks via SIEM
- Implement robots.txt and meta tags to limit indexing of sensitive paths
- Use web application firewalls to block unusual access patterns

## Objectives

1. Discover public-facing endpoints with parameters
2. Confirm scope association for ethical hacking
3. Identify potential injection points

## Instructions

### Step 1: Execute Google Dork

**Context**: Search for MTN-titled pages on the target domain to find candidate URLs.

**Command** ([[commands/google-dork-mtn-site]]):
```bash
google search: site:admyntec.co.za intitle:"MTN"
```

> This dork restricts results to admyntec.co.za and pages with 'MTN' in the title, outputting a list of URLs like admin portals.

### Step 2: Review Results

**Context**: Manually inspect URLs for dynamic parameters like customerId.

**Command** (Manual):
```bash
# No command; browse URLs in browser
```

> Expected: Identification of paths like /path/customerId/value for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/google-dork-mtn-site]]

## Tools Used

- [[tools/Google-Dorks]]

## Tags

- recon
- dorking
