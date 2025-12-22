---
tags:
  - recon
  - version-check
  - ruby
type: procedure
tools:
  - '[[tools/rdoc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rdoc-version-check]]'
platforms:
  - Ruby
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 198c8587-5b9a-45d6-ab1f-c113a756b70e
created_at: '2025-12-14T17:23:42.461Z'
updated_at: '2025-12-14T17:23:42.461Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-RDoc-Version

## Summary

This procedure checks the installed version of RDoc to confirm vulnerability to unsafe YAML deserialization, a prerequisite for exploiting RCE in untrusted repository processing.

## Description

RDoc, Ruby's documentation generator, uses Psych YAML and Marshal serialization without restrictions in vulnerable versions (e.g., 6.3.1 with Psych <4.0.0). Verifying the version ensures the target environment is exploitable by running the verbose flag, which outputs the version without side effects. This is the initial reconnaissance step in a deserialization attack chain targeting developers or CI/CD pipelines processing external Ruby code.

## Requirements

1. Ruby environment with RDoc installed
2. Shell access (bash or equivalent)
3. No network access needed

## Defense

Defensive measures and detection strategies:

- Upgrade RDoc and Psych to latest versions with safe loading enabled
- Monitor for unusual rdoc executions in logs
- Use sandboxing for processing untrusted repos

## Objectives

1. Identify vulnerable RDoc version
2. Validate environment for exploitation
3. Ensure no version-specific mitigations

## Instructions

### Step 1: Run Version Check Command

**Context**: Execute the rdoc command with verbose flag to display the installed version, confirming if it's affected by CVE-like deserialization issues.

**Command** ([[commands/rdoc-version-check]]):
```bash
rdoc -v
```

> This command queries the RDoc installation and prints the version. Expected output: "rdoc 6.3.1" or similar, indicating vulnerability if pre-mitigation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/rdoc-version-check]]

## Tools Used

- [[tools/rdoc]]

## Tags

- recon
- ruby
- version-check
