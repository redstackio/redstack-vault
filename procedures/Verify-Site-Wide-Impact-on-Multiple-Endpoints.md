---
id: p-verify-site-wide-impact
tags:
  - xss
  - enumeration
  - site-wide
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:24.933Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Site-Wide Impact on Multiple Endpoints

## Summary

This procedure enumerates and tests additional endpoints on the target site to confirm the XSS vulnerability's scope, identifying over 80 affected paths with pagination features.

## Description

Attackers use search engines to map site structure and replicate the exploit across endpoints, assessing overall risk. Scenario: PHP site like data.gov with consistent templating. Outcomes: Quantified impact for reporting. Prerequisites: Working payload and search tool access.

## Requirements

1. [[tools/Google-Search]] for endpoint discovery
2. List of potential paths (e.g., /food/, /consumer/)
3. Time for manual testing

## Defense

Defensive measures and detection strategies:

- Centralize pagination templating with uniform escaping
- Scan for similar reflection patterns across site
- Rate-limit query parameter testing

## Objectives

1. Enumerate vulnerable endpoints
2. Confirm consistent exploitation
3. Quantify site-wide risk

## Instructions

### Step 1: Enumerate Endpoints

**Context**: Find paths with pagination.

Use [[tools/Google-Search]] with "site:data.gov inurl:pagination" or similar to list 80+ endpoints like /local/, /food/.

> Expected: List of URLs with <div class="pagination">

### Step 2: Test Payload Replication

**Context**: Apply exploit to each.

For each endpoint, append ?&q&zzz'onmou<seover=1&ale<rt('xsp'<)<;1; //, load, and hover pagination links.

> Success: Alert triggers on majority of tested paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Search]]

## Tags

- enumeration
- impact
