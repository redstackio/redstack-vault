---
id: proc-uuid-003
tags:
  - jsonp
  - path-traversal
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
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-13T23:52:24.314Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Discover-JSONP-Endpoint

## Summary

This procedure probes for internal endpoints supporting JSONP callbacks through XHR requests, focusing on the rockstargames.com application to find services like /comments_dal/users/getGlobalLoginSettings.json that can be abused for script injection.

## Description

By leveraging initial path traversal observations, this procedure iteratively tests internal paths via the tags parameter. The target environment exposes JSONP by wrapping JSON responses in user-supplied callback functions when ?callback= is detected in XHR requests, allowing escalation to XSS without proper validation.

## Requirements

1. Knowledge of base path from prior analysis
2. Browser tools for iterative URL testing
3. Patience for trial-and-error traversal

## Defense

Defensive measures and detection strategies:

- Restrict internal endpoints to same-origin requests only
- Validate and whitelist callback parameter values (e.g., alphanumeric only)
- Block traversal sequences in path construction

## Objectives

1. Locate JSONP-supporting internal services
2. Confirm callback wrapping behavior
3. Identify exploitable endpoints for chaining

## Instructions

### Step 1: Initiate Path Traversal Probing

**Context**: Use basic traversal to escape the intended directory.

Set #/?tags=../../../ and observe the XHR URL in Network tab. Increment '../' to reach root or internal dirs like /comments_dal/.

> Responses may 404 or reveal directory hints; persist until hitting JSON endpoints.

### Step 2: Test for JSONP Support

**Context**: Append ?callback=test to suspected endpoints.

For /comments_dal/users/getGlobalLoginSettings.json, use #/?tags=../../../comments_dal/users/getGlobalLoginSettings.json?callback=test. Check response for test({...}).

> If wrapped, the endpoint is vulnerable to arbitrary callback injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- jsonp
- path-traversal
- discovery
- web
