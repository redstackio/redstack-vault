---
id: proc-enum-external-programs
tags:
  - enumeration
  - reconnaissance
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:53.474Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate External Programs from Directory

## Summary

This procedure scrapes or manually collects team handles of external programs from HackerOne's public directory, providing a target list for subsequent GraphQL queries.

## Description

HackerOne's public directory lists external programs with their team handles, which can be iterated over to probe for private programs. This reconnaissance step accesses the directory via a specific URL query and extracts handles, forming the basis for enumeration without requiring authentication.

## Requirements

1. Web browser or HTTP client for accessing the directory
2. Ability to parse HTML or use directory search
3. Internet access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Rate limit directory access and scraping attempts
- Obfuscate team handles in public listings
- Monitor for bulk directory queries

## Objectives

1. Compile list of external program handles
2. Identify potential targets for private program detection
3. Minimize detection during reconnaissance

## Instructions

### Step 1: Access Public Directory

**Context**: Load the external programs directory page.

Open https://hackerone.com/directory?query=type%3Aexternal&sort=name%3Aascending&page=1 in a browser.

> Expected output: Paginated list of external programs with team handles.

### Step 2: Extract Team Handles

**Context**: Collect handles from the directory listings.

Manually copy handles or use a script to scrape (e.g., via Python requests and BeautifulSoup) all visible team handles across pages.

> Expected output: Text file with handles like "example-team".

### Step 3: Paginate and Complete List

**Context**: Ensure full coverage by iterating pages.

Increment the page parameter (e.g., &page=2) until all results are gathered.

> Expected output: Comprehensive list of all external program handles.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- reconnaissance
