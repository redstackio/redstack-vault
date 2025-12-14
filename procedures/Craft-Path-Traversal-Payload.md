---
id: uuid-craft-payload
tags:
  - path-traversal
  - payload-craft
  - apache
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.778Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Path-Traversal-Payload

## Summary

This procedure constructs a path traversal payload exploiting the incomplete normalization in Apache's mod_alias for CVE-2021-42013, allowing access to files outside configured directories like /cgi-bin/.

## Description

The vulnerability stems from insufficient path normalization in the fix for CVE-2021-41773, permitting sequences like .%2e/ to bypass restrictions. In an attack scenario, payloads are crafted to map URLs to arbitrary files via Alias directives. Expected outcomes include valid traversal strings targeting sensitive files such as /etc/passwd. This requires understanding Apache's path handling and testing in a controlled environment.

## Requirements

1. Knowledge of target directory structure (e.g., Unix /etc/)
2. Awareness of Alias configurations (inferred from common setups like /cgi-bin/)
3. URL encoding tools or manual construction

## Defense

Defensive measures and detection strategies:

- Apply full Apache patch for CVE-2021-42013 (upgrade to 2.4.51+)
- Enforce 'require all denied' on non-standard paths
- Log and alert on suspicious URL patterns with multiple ../ or %2e

## Objectives

1. Build evasion payload using double-encoded dots and slashes
2. Target files outside protected Alias directories
3. Prepare for request delivery without triggering basic filters

## Instructions

### Step 1: Analyze Base Path

**Context**: Identify an entry point like /cgi-bin/ which uses Alias-like mapping.

No command; manually note the base URL from server config or defaults.

### Step 2: Construct Traversal Sequence

**Context**: Use CVE-2021-41773-style encoding: .%2e/ for ../, chaining multiple to reach root.

Example payload: /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd

> This traverses four levels up from /cgi-bin/ to /etc/passwd. Adjust depth based on Alias depth. Test encoding with tools like Burp Suite if available.

### Step 3: Encode for Evasion

**Context**: Ensure double encoding bypasses partial fixes.

Manual: Replace . with %2e, / with %2f where needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[path-traversal]]
- [[payload-craft]]
