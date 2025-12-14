---
id: 0ce6796e-3826-4c17-ad73-00a6b1e76cf7
name: Identify-Hardcoded-Zombie-Endpoints
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.899Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - zombie-endpoint
  - code-review
  - api-discovery
commands: []
platforms:
  - Android
  - Mobile
tools:
  - '[[tools/Grep]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Identify-Hardcoded-Zombie-Endpoints

## Summary

This procedure scans decompiled Android app code for hardcoded, unused API endpoints (zombie endpoints) that can be accessed despite being legacy, enabling discovery of insecure references like IDOR in trip management APIs.

## Description

Applied to the Bykea app, this involves static code analysis to find strings or methods defining API paths that are not invoked in active flows but remain in the binary. The target environment is the decompiled source on a local machine. Outcomes include pinpointing endpoints lacking validation, such as those for driver data retrieval, facilitating unauthorized access.

## Requirements

1. Decompiled app source from prior reverse engineering step.
2. Text search tools like grep or IDE with search functionality.
3. Basic understanding of Java/Android networking code.

## Defense

Defensive measures and detection strategies:

- Remove or disable legacy code during app updates.
- Use API gateways to validate all endpoints server-side.
- Employ code scanning tools in CI/CD to detect hardcoded secrets/endpoints.

## Objectives

1. Locate inactive API paths in the codebase.
2. Assess for missing security controls like ownership checks.
3. Prepare for exploitation testing.

## Instructions

### Step 1: Search for API Patterns

**Context**: Use string matching to find potential endpoint URLs related to trips or drivers.

Execute a grep search in the decompiled directory:

```bash
grep -r "api.*trip" jadx_output/ --include="*.java"
```

> Outputs lines with API constructions; look for hardcoded bases like "/legacy/trip/".

### Step 2: Review for Zombie Status

**Context**: Manually inspect methods to confirm endpoints are unused but accessible.

No specific command; open files in an editor and trace method calls for activity.

> Check if the endpoint handler lacks @Deprecated or removal, and note parameters like trip ID without user binding.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Grep]]

## Tags

- [[zombie-endpoint]]
- [[code-review]]
