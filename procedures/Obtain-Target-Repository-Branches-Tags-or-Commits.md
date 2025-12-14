---
tags:
  - recon
  - github
  - commit-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b0038881-f4a5-4201-98a0-44178e8e32d6
created_at: '2025-12-14T17:30:58.318Z'
updated_at: '2025-12-14T17:30:58.318Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Obtain-Target-Repository-Branches-Tags-or-Commits

## Summary

This procedure gathers branch names, tags, or commit SHAs from a target private GitHub repository to enable triggering the diff functionality in an IDOR exploit.

## Description

Without direct access, attackers collect these identifiers from indirect sources like public commit references in issues, webhooks, or external data leaks. This step is crucial as the diff feature requires specific refs to compare repositories, bypassing access checks on the private repo content.

## Requirements

1. Knowledge of the target repository name from prior recon
2. Access to ancillary GitHub features or external sources
3. Authenticated session for any API or UI queries

## Defense

Defensive measures and detection strategies:

- Sanitize commit SHAs and refs in public-facing GitHub elements
- Audit logs for unusual ref queries
- Limit exposure of tags/branches in shared contexts

## Objectives

1. Collect usable branches, tags, or SHAs for the private repo
2. Validate identifiers without alerting defenses
3. Enable diff trigger in the next step

## Instructions

### Step 1: Search Indirect References

**Context**: Scan shared GitHub areas for exposed refs.

Manually search issues, PRs, or notifications for mentions of branches/tags/SHAs linked to the target repo.

> Expected output: Identifiers like "main" branch or "abc123def" SHA.

### Step 2: Cross-Verify Identifiers

**Context**: Confirm the refs belong to the target without full access.

Use GitHub search or API (if partially permitted) to match refs; expect limited results.

> Expected output: Confirmed list of 1+ valid refs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[github]]
