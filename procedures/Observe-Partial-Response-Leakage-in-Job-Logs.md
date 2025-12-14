---
tags:
  - response-leak
  - logs
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Automated Collection]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4a8ea609-8719-4893-a501-a2f5595395ba
created_at: '2025-12-14T04:08:48.093Z'
updated_at: '2025-12-14T04:08:48.093Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Observe Partial Response Leakage in Job Logs

## Summary

This procedure examines GitLab CI job error logs for partial leakage of SSRF responses, such as the first character of tokens or full error bodies, confirming internal access.

## Description

The Docker client's JSON parsing fails on invalid redirect responses (e.g., plain text token), leaking snippets in error messages. Successful SSRF to metadata yields 'access_token...' but only 'a' may show; errors provide more. This achieves blind exfiltration without full response visibility.

## Requirements

1. Failed CI job from SSRF trigger
2. Access to GitLab job logs

## Defense

Defensive measures and detection strategies:

- Sanitize error logs to avoid data leaks
- Rate-limit internal metadata queries
- Alert on parsing errors in Docker client logs
- Use non-plain text metadata responses

## Objectives

1. Confirm SSRF execution
2. Exfiltrate partial sensitive data
3. Identify further exploitation paths

## Instructions

### Step 1: Review Job Logs

**Context**: Check for Docker API errors revealing responses.

Navigate to the failed job in GitLab UI, inspect console output for lines like "invalid character 'a' in JSON" from parsing the metadata token.

### Step 2: Analyze Leakage

**Context**: Extract and interpret leaked data.

Look for full error bodies on failed internal requests; correlate with expected metadata format to reconstruct info.

**Expected Output**: Partial token or error indicating internal hit.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Automated Collection]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- response-leak
- logs
- exfiltration
