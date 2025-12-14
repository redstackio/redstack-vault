---
id: proc-id-bruteforce-001
tags:
  - bruteforce
  - enumeration
  - idor
  - discovery
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:29.397Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
---
# Bruteforce-ID-to-Enumerate-User-Servers

## Summary

This procedure systematically bruteforces the ID parameter in the DoD FTP push server URLs to discover and access multiple users' server configurations, scaling the IDOR exploitation for comprehensive credential harvesting.

## Description

The sequential nature of IDs in the /filepush/ftp/<ID>/ endpoint allows attackers to iterate through values (e.g., 1 to 1000+) and identify valid servers via response differences (e.g., HTTP 200 with data vs. 404). Each hit exposes FTP/sFTP credentials, enabling mass compromise. This targets the lack of rate limiting or access controls, amplifying the vulnerability's impact on confidential data.

## Requirements

1. Authenticated session on DoD website
2. Web browser or scripting tool for automated iteration (manual for small ranges)
3. List of potential ID ranges (assume 1-5000 based on user count)

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting on endpoint requests to prevent enumeration
- Implement logging of sequential ID accesses and alert on patterns
- Randomize or hash object IDs to break sequential bruteforcing

## Objectives

1. Identify all accessible user server IDs
2. Collect credentials from multiple configurations
3. Assess scope of exposure for reporting or further exploitation

## Instructions

### Step 1: Prepare Iteration Range

**Context**: Define the scope for bruteforcing based on expected user base.

Start with IDs from 1 upwards; use browser bookmarks or a simple loop in developer console.

> Assume up to 10,000 users; begin small to avoid detection.

### Step 2: Iterate and Request URLs

**Context**: Send requests for each ID and observe responses.

Manually or via console: For each ID, construct and load https://████████/█████/filepush/ftp/<ID>/.

> Valid IDs return populated forms with credentials; invalid ones may 404 or show empty pages. Note successes.

### Step 3: Harvest and Validate Data

**Context**: Compile exposed information from valid responses.

For each successful load, extract hostname, username, password, and path; test connectivity if possible.

> Output: Spreadsheet or notes with harvested credentials, confirming enumeration success.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- bruteforce
- enumeration
- idor
- ftp-discovery
- dod
