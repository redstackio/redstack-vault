---
id: proc-uuid-3
tags:
  - ssrf
  - directory-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-submit-url-to-validator]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.551Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-Internal-Directories-via-SSRF

## Summary

This procedure leverages SSRF to enumerate directories on open internal HTTP services, identifying accessible paths and confirming content availability through metatag presence or absence.

## Description

Once an HTTP port is identified, probe paths like /system/ (existing) and /test/ (non-existing) via the validator. Valid paths return metatags; invalid ones return errors. This maps internal web structure for vulnerability hunting. Requires prior port identification; outcomes: directory listings and potential file access points.

## Requirements

1. Open HTTP port confirmed (e.g., 4680)
2. Guesses for common paths (e.g., /system/, /test/)
3. SSRF-capable endpoint

## Defense

Defensive measures and detection strategies:

- Restrict directory listings on internal servers
- Implement path normalization to prevent traversal
- Monitor for unusual path requests in app logs

## Objectives

1. Identify accessible internal directories
2. Differentiate valid vs. invalid paths
3. Uncover potential entry points for escalation

## Instructions

### Step 1: Test Existing Directory

**Context**: Submit known or guessed valid path to extract metatags.

**Command** ([[commands/curl-submit-url-to-validator]]):
```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:4680/system/'
```

> Response includes metatags from the directory.

### Step 2: Test Non-Existing Directory

**Context**: Probe invalid path to confirm 404 behavior without metatags.

**Command** ([[commands/curl-submit-url-to-validator]]):
```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:4680/test/'
```

> Fetch succeeds but no metatags, indicating 404.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-url-to-validator]]

## Tools Used


## Tags

- ssrf
- directory-enumeration
