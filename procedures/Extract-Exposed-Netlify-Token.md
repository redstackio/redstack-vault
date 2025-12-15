---
id: proc-002
tags:
  - token-leak
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:31:52.739Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Exposed-Netlify-Token

## Summary

This procedure searches public CI logs for leaked authentication tokens, specifically extracting a Netlify Bearer token from unmasked log output.

## Description

In CI/CD pipelines like Mozilla's TaskCluster, commands such as Netlify deployments may echo tokens in cleartext if not masked. This procedure uses text search to locate and capture the token, enabling unauthorized API access in a supply chain attack scenario.

## Requirements

1. Access to the CI log content from previous step
2. Text editor or browser search tools
3. Knowledge of token formats (e.g., Netlify's Bearer strings)

## Defense

Defensive measures and detection strategies:

- Enforce secret scanning in logs before public exposure
- Use environment variables with masking in CI tools
- Audit pipeline configurations for verbose logging

## Objectives

1. Locate the 'auth:' keyword in logs
2. Extract the full token string
3. Prepare for API validation

## Instructions

### Step 1: Search Log Content

**Context**: Scan the loaded log for indicators of leaked credentials.

No command required; manual search.

> In the browser, press Ctrl+F (or Cmd+F) and search for 'auth:'. The token appears in a line like 'netlify deploy --auth ████', where ████ is the exposed value. Copy the token carefully, redacting it for reports.

**Expected Output**: Isolated token string, e.g., a long alphanumeric Bearer token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-leak]]
- [[information-disclosure]]
