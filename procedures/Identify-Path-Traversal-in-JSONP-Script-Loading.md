---
id: proc-identify-path-traversal-jsonp
tags:
  - path-traversal
  - jsonp
  - api-abuse
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
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:47:23.426Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify Path Traversal in JSONP Script Loading

## Summary

This procedure reviews the JSONP loading mechanism in the GitHub button script to identify path traversal vulnerabilities in API URL construction using user-controlled parameters.

## Description

The jsonp() function appends 'user' and 'repo' parameters directly to GitHub API paths without validation, enabling directory traversal (e.g., ../../) to access unintended endpoints. While limited by GitHub's security, it could chain with other vulns for abuse.

## Requirements

1. Browser DevTools for code inspection
2. Knowledge of URL path manipulation
3. Target script access

## Defense

Defensive measures and detection strategies:

- Validate and canonicalize API paths
- Use whitelists for allowed endpoints
- Monitor for traversal patterns in requests

## Objectives

1. Spot unvalidated concatenation in URL building
2. Assess traversal potential
3. Evaluate exploitation limits

## Instructions

### Step 1: Locate JSONP Function

**Context**: Find the script loading code.

In DevTools Sources, search for jsonp() or script src construction.

**Expected Output**: Function like loadScript('https://api.github.com/users/' + user + '?callback=...').

### Step 2: Analyze Parameter Usage

**Context**: Check for validation on 'user' and 'repo'.

Confirm direct string concat without path normalization or regex checks.

**Expected Output**: No filters, allowing ../../ insertion.

### Step 3: Hypothesize Exploitation

**Context**: Test mentally for path manipulation.

Note potential src: https://api.github.com/another/endpoint?callback=callback.

**Expected Output**: Traversal vector identified.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[path-traversal]]
- [[jsonp]]
- [[api-abuse]]
