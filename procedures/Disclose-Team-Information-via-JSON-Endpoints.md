---
id: proc-hackerone-info-disclosure-001
tags:
  - information-disclosure
  - hackerone
  - web
  - json
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
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:30:58.441Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Disclose Team Information via JSON Endpoints

## Summary

This procedure leverages insufficient authorization on HackerOne's JSON endpoints to disclose sensitive team data, including user IDs, names, groups, and permissions, accessible even to readonly or low-privilege users, revealing internal structures without proper checks.

## Description

HackerOne's /teams.json and /TEAM/groups.json endpoints return full team details without adequate permission validation. Readonly users can access /teams.json, while any valid permission allows /groups.json, exposing identical sensitive information. This information disclosure can aid further attacks by mapping team hierarchies and identifying high-value targets. The root cause is missing authorization middleware in the Ruby on Rails controllers for these API-like endpoints.

## Requirements

1. Any valid authenticated session (even readonly permission)
2. Web browser or API client to access endpoints
3. Team slug for /groups.json URL
4. No elevated privileges needed

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization on all JSON/API endpoints based on user roles
- Rate-limit and log accesses to sensitive endpoints like /teams.json
- Mask or filter sensitive fields (e.g., user IDs) in responses for low-privilege users
- Implement content security policies to prevent unauthorized endpoint scraping

## Objectives

1. Access unprotected JSON endpoints
2. Extract team and group details
3. Identify users, permissions, and structures
4. Use disclosed data for targeted follow-on attacks

## Instructions

### Step 1: Access Teams JSON Endpoint

**Context**: Retrieve global team information with minimal privileges.

Navigate to:

```plaintext
https://hackerone.com/teams.json
```

> JSON response with team data. Expected output: Array of teams with details.

### Step 2: Access Group JSON Endpoint

**Context**: Get specific team group info, including users and permissions.

Navigate to:

```plaintext
https://hackerone.com/TEAM/groups.json
```

> JSON with groups, users, IDs, and permissions. Expected output: Detailed group objects.

### Step 3: Parse and Analyze Data

**Context**: Review exposed sensitive information.

Use browser dev tools or save JSON to file for analysis.

> Identify user names, IDs, and permission mappings.

### Step 4: Validate Disclosure

**Context**: Confirm data sensitivity and completeness.

Cross-reference with known team members.

> Matches internal structures, confirming leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- json
- web
