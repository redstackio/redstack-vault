---
id: proc-streamlabs-test-restricted-001
tags:
  - api-test
  - access-denied
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.832Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Restricted-API-Access

## Summary

This procedure tests a restricted API endpoint to confirm that some access controls are enforced for moderators, highlighting the selective bypass in other endpoints.

## Description

While in the parent context, directly access the v5 user endpoint via browser to verify denial. This step validates the environment before exploiting the vulnerable path. Expected outcome: Unauthorized response, confirming partial security.

## Requirements

1. Switched to parent context as moderator
2. Web browser with direct URL access
3. Developer tools optional for inspection

## Defense

Defensive measures and detection strategies:

- Consistent permission checks across all API versions
- Rate-limit and log failed API requests
- Use consistent auth tokens with role embedding

## Objectives

1. Attempt access to restricted user info
2. Observe denial to contrast with vulnerable endpoint
3. Confirm moderator limitations on standard APIs

## Instructions

### Step 1: Access the v5 Endpoint

**Context**: Directly browse to the restricted API while in parent context.

Enter https://streamlabs.com/api/v5/user/ in the browser address bar and load.

**Expected Output**: HTTP response with "Request Unauthorized" message.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-test]]
- [[access-denied]]
