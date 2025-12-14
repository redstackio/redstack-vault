---
id: proc-sub-enum-001
tags:
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-browse]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:15.279Z'
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
# Enumerate-and-Analyze-Subdomains

## Summary

This procedure involves enumerating subdomains of a target domain like starbucks.com.sg to identify potentially vulnerable or inactive ones, then analyzing their responses for technology footprints such as custom CMS indicators.

## Description

In the attack on the Starbucks subdomain, enumeration revealed http://www.example.starbucks.com.sg/, which returned a 404 page hinting at an old custom CMS named 'xxxx' in the footer. This step is crucial for expanding the attack surface in web reconnaissance scenarios targeting legacy systems.

## Requirements

1. Network access to the target domain
2. Tools for subdomain brute-forcing or passive recon (e.g., subfinder, though manual here)
3. Browser or curl for page inspection

## Defense

Defensive measures and detection strategies:

- Implement wildcard DNS to hide inactive subdomains
- Remove or obscure technology hints in error pages
- Monitor for unusual enumeration traffic with WAF rules

## Objectives

1. Identify hidden or inactive subdomains
2. Gather initial intel on web technologies
3. Set stage for deeper path discovery

## Instructions

### Step 1: Perform Subdomain Enumeration

**Context**: Use passive or active techniques to list subdomains; in this case, standard methods uncovered the target.

**Command** ([[commands/curl-browse]]):
```bash
curl -i http://www.example.starbucks.com.sg/
```

> This fetches the page headers and body, revealing the 404 message and CMS footer. Expected output includes 'this website is not in use' and 'Copyright 2010 | Built on xxxx CMS'.

### Step 2: Analyze Page Source

**Context**: Inspect the response for clues on backend tech.

No specific command; manually view source or pipe curl output to grep:

```bash
grep -i "cms" response.html
```

> Confirms CMS presence, guiding next path guesses.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-browse]]

## Tools Used

- None specific

## Tags

- [[Reconnaissance]]
- [[subdomain-enumeration]]
