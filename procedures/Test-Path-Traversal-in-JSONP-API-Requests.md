---
id: proc-test-path-traversal-jsonp
tags:
  - path-traversal
  - jsonp
  - api-manipulation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - JavaScript
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.851Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Path-Traversal-in-JSONP-API-Requests

## Summary

This procedure tests path traversal in the JSONP function of github-btn.html by using '../' payloads in 'user' and 'repo' parameters to redirect script src to arbitrary GitHub API endpoints, potentially enabling data exfiltration.

## Description

The jsonp function constructs script URLs like 'https://api.github.com/users/' + user or '/repos/' + user + '/' + repo + '?callback=callback' without validation. Path traversal payloads like ../../another/endpoint alter the path, loading JSONP from unintended endpoints. This could chain with other vulns for attacks, though GitHub API may limit impact.

## Requirements

1. Web browser with network inspection
2. Access to target URL
3. Knowledge of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and validate API path components (e.g., regex for valid usernames/repos)
- Use absolute paths or proxies for API calls
- Monitor for anomalous requests to api.github.com

## Objectives

1. Traverse to arbitrary API paths
2. Confirm JSONP loading from altered endpoints
3. Assess potential for exfiltration

## Instructions

### Step 1: Identify JSONP Construction

**Context**: Review code for script src building.

In DevTools, find the jsonp function and note concatenation of user/repo.

**Expected Output**: Vulnerable URL construction logic.

### Step 2: Craft Traversal Payload

**Context**: Build URL with '../' sequences.

Create: https://github.algolia.com/github-btn.html?user=../../another/endpoint&repo=../../another/endpoint&type=fork.

**Expected Output**: Payload URL prepared.

### Step 3: Execute and Monitor

**Context**: Load and inspect network.

Load the URL and check Network tab for script requests.

**Expected Output**: Request to https://api.github.com/another/endpoint?callback=callback.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[path-traversal]]
- [[jsonp]]
- [[api-manipulation]]
