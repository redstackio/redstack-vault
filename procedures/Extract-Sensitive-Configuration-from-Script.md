---
id: proc-uuid-002
name: Extract Sensitive Configuration from Script
tags:
  - information-disclosure
  - sensitive-config
  - mautic
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
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:20.282Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Extract Sensitive Configuration from Script

## Summary

This procedure involves analyzing the contents of an accessed script file to identify and extract hardcoded sensitive information, such as secret keys from configurations like Mautic's test setup.

## Description

Once an exposed script is retrieved, attackers review it for embedded sensitive data. In the Unikrn case, the CRM application's source code included Mautic configuration values like 'mautic.secret_key', which were not redacted from test environments. This disclosure can lead to further exploitation, such as API access or session hijacking, in PHP/Symfony-based web applications.

## Requirements

1. Access to the script content from prior retrieval
2. Text editor or grep for pattern matching
3. Knowledge of common config patterns (e.g., secret_key)

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding secrets in source code; use environment variables or secure vaults
- Perform code reviews and static analysis to detect exposed configs
- Monitor logs for unusual file access patterns

## Objectives

1. Locate hardcoded sensitive values in the script
2. Assess the validity and exploitability of disclosed secrets
3. Document potential impacts like further unauthorized operations

## Instructions

### Step 1: Review Script Content

**Context**: Manually or programmatically search the retrieved script for configuration blocks.

**Command**:

> Save the curl output to a file (e.g., script.txt) and open in a text editor. Look for lines containing 'secret_key', 'api_key', or Mautic-specific configs.

### Step 2: Extract and Validate Secrets

**Context**: Isolate the sensitive strings for potential use in other attacks.

**Command**:
```bash
grep -i 'secret_key' script.txt
```

> This greps for secret keys. Expected output: Lines like 'mautic.secret_key = somevalue', confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[sensitive-config]]
