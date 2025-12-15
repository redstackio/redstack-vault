---
tags:
  - information-disclosure
  - reconnaissance
type: procedure
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:03.256Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5dc74178-eda2-4ec3-a5db-c85ae6376380
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-CCM-CID-Values-for-Site-Structure

## Summary

This procedure extracts internal collection IDs (CCM_CID) disclosed in script tags across Concrete CMS pages, enabling attackers to map the site structure and select precise parentIDs for targeted page placement in CSRF attacks.

## Description

Concrete CMS exposes CCM_CID values—unique identifiers for pages and collections—in <script> tags on every page, revealing the internal site map without authentication. This information disclosure allows attackers to identify non-obvious or high-traffic locations for injecting malicious content. The procedure involves browsing target pages and parsing source code. Prerequisites: Public access to the CMS site. Outcomes: A list of exploitable parentIDs for chaining with CSRF.

## Requirements

1. Publicly accessible Concrete CMS site
2. Browser with dev tools for source inspection
3. Basic HTML parsing skills

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove CCM_CID from client-side scripts
- Implement server-side rendering to avoid exposure
- Use web application firewalls (WAF) to detect scraping patterns

## Objectives

1. Gather site hierarchy for targeted exploitation
2. Identify valid parentIDs for unauthorized page creation
3. Enable precise placement to maximize impact

## Instructions

### Step 1: Browse Target Pages

**Context**: Access multiple pages to collect diverse CCM_CID values.

Navigate to the site's homepage, blog sections, and subpages using a standard browser.

> Focus on areas where new pages can be parented, like blog roots.

### Step 2: Inspect Script Tags

**Context**: Extract IDs from embedded JavaScript.

Right-click and view page source. Search for 'CCM_CID' in <script> blocks, noting values like var CCM_CID = '123'; for parent candidates.

> Compile a list: e.g., parentID: 456 for high-traffic section. This reveals the tree structure for non-blog areas too.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[site-recon]]
