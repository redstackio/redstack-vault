---
id: proc-uuid-1
tags:
  - ssrf
  - reconnaissance
type: procedure
tools:
  - '[[tools/irb]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.159Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Investigate-Integrations-SSRF-Protections

## Summary

This procedure involves analyzing the SSRF protections in HackerOne's Integrations feature to identify reliance on the private_address_check gem and Ruby's Resolv.getaddresses for URL resolution and private IP filtering.

## Description

In a web application like HackerOne, the Integrations panel at https://hackerone.com/{BBP}/integrations allows users to input URLs that are resolved server-side. The private_address_check gem uses Resolv.getaddresses to parse hostnames and checks resolved IPs against a blacklist of private ranges. This reconnaissance step uncovers these mechanisms, setting the stage for targeted exploitation. Prerequisites include authenticated access to the panel and basic knowledge of Ruby ecosystem.

## Requirements

1. Authenticated HackerOne account with access to Integrations
2. Web browser or API access to submit test URLs
3. Local Ruby environment for offline analysis of the gem

## Defense

Defensive measures and detection strategies:

- Implement comprehensive URL validation beyond IP blacklists, including hostname parsing
- Monitor for anomalous URL patterns in application logs
- Use WAF rules to flag encoded or suspicious IP formats in requests

## Objectives

1. Map out SSRF filtering logic in the Integrations feature
2. Identify dependencies like private_address_check gem
3. Establish baseline for bypass testing

## Instructions

### Step 1: Access and Review Integrations Panel

**Context**: Log in to HackerOne and navigate to the Integrations section to observe URL input fields and any visible error handling for invalid URLs.

No specific command; manually inspect the UI at https://hackerone.com/{BBP}/integrations.

> Submit benign test URLs to observe resolution behavior and any filtering feedback.

### Step 2: Analyze private_address_check Gem

**Context**: Review the gem's source code to understand its use of Resolv.getaddresses for IP resolution and blacklist checking.

Use a code editor or browser to examine the gem at https://github.com/jtdowney/private_address_check.

> Confirm that empty resolution results (e.g., []) are not treated as private, allowing bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/irb]]

## Tags

- ssrf
- reconnaissance
