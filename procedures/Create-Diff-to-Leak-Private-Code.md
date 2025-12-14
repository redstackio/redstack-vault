---
tags:
  - idor
  - access-bypass
  - code-leak
  - github
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[T1213.003]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c82aa3ae-53c4-40a8-a678-e014d711e093
created_at: '2025-12-14T17:30:58.312Z'
updated_at: '2025-12-14T17:30:58.312Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Create-Diff-to-Leak-Private-Code

## Summary

This procedure exploits the IDOR vulnerability in GitHub Enterprise Server's diff/compare feature to retrieve limited code from a private repository by specifying it against an accessible repo.

## Description

Authenticated users can create diffs between any repositories, but the system fails to verify access to the target private repo, leading to disclosure of code snippets in the diff view. This affects versions before 3.18 and is triggered via the web UI by inputting the target repo name and known refs.

## Requirements

1. Authenticated access to at least one repository
2. Target private repo name and refs from prior steps
3. GitHub Enterprise Server instance with the vulnerable diff feature

## Defense

Defensive measures and detection strategies:

- Patch to fixed versions (3.14.17+, 3.15.12+, 3.16.8+, 3.17.5+)
- Enable access logging for diff operations
- Implement server-side authorization checks for all repo comparisons

## Objectives

1. Trigger unauthorized diff to expose private code
2. Capture and exfiltrate leaked snippets
3. Validate the IDOR for further exploitation

## Instructions

### Step 1: Access Diff Feature

**Context**: Use an accessible repo as base and input target details.

In the GitHub web UI, navigate to your repo's "Compare" or "Diff" tool.

> Expected output: Interface ready for repo/branch input.

### Step 2: Specify Target and Generate Diff

**Context**: Enter private repo name and refs to bypass checks.

Input format: Base repo (yours) vs. "target-user/private-repo" with branches/tags/SHAs; submit to generate diff.

> Expected output: Diff view showing limited code from private repo, e.g., file diffs with snippets.

### Step 3: Capture Leaked Content

**Context**: Document the unauthorized code exposure.

Screenshot or copy the diff output for analysis/exfiltration.

> Expected output: Saved code snippets confirming leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[github]]
