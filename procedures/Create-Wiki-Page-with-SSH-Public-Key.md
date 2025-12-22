---
tags:
  - gitlab
  - key-injection
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: c0d61680-f24c-4160-abd2-9dab32ad7d27
created_at: '2025-12-11T03:47:47.591Z'
updated_at: '2025-12-11T03:47:47.591Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Wiki Page with SSH Public Key

## Summary

This procedure creates a wiki page with the SSH public key as the commit message for injection.

## Description

Similar to the initial wiki creation, this sets the commit to the public key content, enabling its injection into authorized_keys.

## Requirements

1. GitLab API token
2. Public key content

## Defense

Defensive measures and detection strategies:

- Audit commit messages
- Restrict wiki commits

## Objectives

1. Embed key in commit
2. Prepare for RCE

## Instructions

### Step 1: Create the Wiki Page

**Context**: Set commit message to public key.

> Use GitLab UI or API to create the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/curl-gitlab-search-api]]
- #key-injection
