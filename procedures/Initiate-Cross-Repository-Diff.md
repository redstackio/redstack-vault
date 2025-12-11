---
tags:
  - github
  - diff
  - access-control
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9fe72de8-be8d-4b44-9ed4-92bc53a4129d
created_at: '2025-12-11T03:47:39.354Z'
updated_at: '2025-12-11T03:47:39.354Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Initiate Cross-Repository Diff

## Summary

This procedure uses the collected repository details to request a diff between an accessible repository and a private one, exploiting improper access controls.

## Description

By leveraging the compare/diff feature in GitHub Enterprise Server, this step triggers a cross-repository comparison without proper authorization checks, setting up for code retrieval. It targets the vulnerability in the diff functionality.

## Requirements

1. Access to at least one repository
2. Details from intelligence gathering
3. Web access to GitHub interface

## Defense

Defensive measures and detection strategies:

- Patch to fixed versions of GitHub Enterprise Server
- Monitor for unusual diff requests across repositories

## Objectives

1. Trigger diff request
2. Bypass authorization checks
3. Generate diff output

## Instructions

### Step 1: Access Compare Endpoint

**Context**: Navigate to the compare/diff URL in GitHub.

No specific command; use web interface (e.g., /<org>/<repo>/compare/<base>...<head>).

> Replace with actual repo details.

### Step 2: Submit Diff Request

**Context**: Input the private repo details to initiate the diff.

No specific command; submit via web form or API.

> Expect the server to process the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #github
- #diff
