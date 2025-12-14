---
id: proc-lichess-review-001
tags:
  - code-review
  - ssrf
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:46:14.710Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-Lichess-Source-Code-for-SSRF

## Summary

This procedure involves analyzing the open-source Lichess codebase on GitHub to identify SSRF vulnerabilities in the game export API, focusing on unvalidated user input in the 'players' parameter.

## Description

Lichess is an open-source chess platform hosted on lichess.org. By reviewing the Scala code in the Play Framework, attackers can pinpoint where the 'players' query parameter is passed directly to an HTTP client without validation, allowing arbitrary URL fetches. This step is crucial for understanding the root cause before live testing and requires no special access, only public GitHub review.

## Requirements

1. Access to GitHub (public repository: lichess-org/lichess)
2. Basic knowledge of Scala and Play Framework
3. Git client for cloning the repo

## Defense

Defensive measures and detection strategies:

- Implement code scanning tools like Semgrep for SSRF patterns in CI/CD
- Monitor GitHub for vulnerability disclosures and apply patches promptly
- Use static analysis to detect unsanitized URL inputs in HTTP clients

## Objectives

1. Identify vulnerable code paths in GameApiV2 and RealPlayer modules
2. Confirm lack of URL validation or private IP blocking
3. Document technical details for exploitation planning

## Instructions

### Step 1: Clone the Repository

**Context**: Obtain the latest Lichess source code for analysis.

**Command** ([[git-clone]]):
```bash
git clone https://github.com/lichess-org/lichess.git
```

> This clones the repository locally. Expected output: Directory 'lichess' with source files.

### Step 2: Analyze Key Files

**Context**: Review specific Scala files for 'players' parameter handling.

Navigate to app/controllers/Game.scala and search for 'players' parameter. Trace it to GameApiV2.scala and RealPlayer.scala, where ws.url(url).withRequestTimeout(3.seconds).get() is called without validation.

**Expected Output**: Code snippets showing direct URL usage from query params.

### Step 3: Document Findings

**Context**: Note the vulnerability details for later steps.

Record paths: app/controllers/Game.scala -> GameApiV2.OneConfig.playerFile -> RealPlayer.apply(url).

**Expected Output**: Written notes on SSRF vector.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- ssrf
- scala
