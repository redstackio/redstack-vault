---
id: 123e4567-e89b-12d3-a456-426614174001
name: Analyze-Smokescreen-Source-Code-for-Deny-List
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.789Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - recon
  - source-code-analysis
  - smokescreen
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Analyze-Smokescreen-Source-Code-for-Deny-List

## Summary

This procedure involves reviewing the open-source code of Stripe's Smokescreen library to identify flaws in the domain deny_list validation, specifically incomplete handling of bracket stripping in domain names.

## Description

In an attack scenario targeting applications using Smokescreen as an HTTP proxy, an attacker first analyzes the publicly available source code on GitHub to understand the deny_list enforcement. The target environment is any service integrated with Smokescreen for outbound request filtering. The expected outcome is pinpointing the vulnerability where only a single set of brackets is stripped from domain inputs, allowing nested brackets to evade filtering and enable SSRF.

## Requirements

1. Access to GitHub repository (public: github.com/stripe/smokescreen)
2. Basic knowledge of Go programming and HTTP proxy mechanics
3. Text editor or IDE for code review

## Defense

Defensive measures and detection strategies:

- Regularly audit open-source dependencies for vulnerabilities
- Implement code reviews for custom proxy logic
- Monitor for anomalous source code access patterns in logs

## Objectives

1. Identify bracket stripping logic in deny_list validation
2. Confirm limitation to single bracket sets
3. Document potential bypass techniques like double brackets

## Instructions

### Step 1: Access and Clone Repository

**Context**: Obtain the source code for detailed inspection.

Navigate to github.com/stripe/smokescreen and clone the repository using Git:

```bash
git clone https://github.com/stripe/smokescreen.git
```

> This downloads the Go codebase for local review. Expected output: Local copy of the repository.

### Step 2: Locate Deny List Implementation

**Context**: Search for domain validation functions to examine bracket handling.

Open the relevant files (e.g., proxy or validation modules) and review the code that processes domain names against the deny_list. Look for string replacement or stripping operations on brackets.

> Focus on functions that normalize domains by removing brackets. Expected output: Code snippet showing single bracket strip, e.g., replace("[", "", 1).

### Step 3: Analyze Flaw

**Context**: Verify the incomplete stripping allows evasion.

Trace the logic to confirm it fails on nested brackets like [[]]. Note how this leads to unfiltered domains passing validation.

> Expected output: Confirmation of vulnerability in handling multiple brackets.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[source-code-analysis]]
- [[smokescreen]]
