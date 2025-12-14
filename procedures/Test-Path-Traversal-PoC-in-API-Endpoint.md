---
id: proc-test-path-traversal-poc-api
tags:
  - path-traversal
  - poc
  - github-api
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
updated_at: '2025-12-14T03:47:23.423Z'
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
# Test Path Traversal PoC in API Endpoint

## Summary

This procedure tests a PoC for path traversal in the JSONP script loading, manipulating 'user' and 'repo' to load an arbitrary GitHub API endpoint.

## Description

By setting parameters to include traversal sequences, the script src is altered to request unintended paths on api.github.com. This demonstrates the flaw but notes limited impact without further GitHub vulns.

## Requirements

1. Web browser with Network tab
2. Target URL
3. Basic URL crafting

## Defense

Defensive measures and detection strategies:

- Sanitize path components in API calls
- Rate-limit anomalous requests
- Log traversal attempts

## Objectives

1. Alter script src via parameters
2. Load non-standard endpoint
3. Confirm no blocking

## Instructions

### Step 1: Craft Traversal URL

**Context**: Include ../ in parameters.

Use: http://nutty.ubnt.com/github-btn.html?#&user=../../another/endpoint&repo=../../another/endpoint&type=fork.

**Expected Output**: URL with traversal payload.

### Step 2: Load and Monitor Network

**Context**: Observe script request.

Enter URL, open DevTools Network tab, and reload.

**Expected Output**: Request to https://api.github.com/another/endpoint?callback=callback.

### Step 3: Verify Execution

**Context**: Check if script loads.

See if JSONP callback executes without error.

**Expected Output**: 200 response or partial load from manipulated path.

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
- [[poc]]
- [[github-api]]
