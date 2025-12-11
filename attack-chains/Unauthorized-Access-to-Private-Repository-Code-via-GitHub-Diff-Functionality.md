---
tags:
  - github
  - idor
  - access-control
  - repository
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - GitHub Enterprise Server
complexity: medium
procedures:
  - '[[procedures/Gather-Private-Repository-Intelligence]]'
  - '[[procedures/Initiate-Cross-Repository-Diff]]'
  - '[[procedures/Exploit-Diff-for-Code-Retrieval]]'
step_count: 3
techniques:
  - '[[Data from Information Repositories]]'
description: >-
  Exploits improper access control in GitHub Enterprise Server to retrieve
  limited code from private repositories using the compare/diff feature
skill_level: intermediate
impact_level: high
id: 64fbc2c7-1698-4706-8305-d7b9f6744125
created_at: '2025-12-11T03:47:39.357Z'
updated_at: '2025-12-11T03:47:39.357Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Unauthorized Access to Private Repository Code via GitHub Diff Functionality

## Overview

This attack chain exploits an improper access control vulnerability in GitHub Enterprise Server, allowing attackers with access to any repository to retrieve limited code content from another private repository without authorization. By knowing the private repository's name and details like branches, tags, or commit SHAs, attackers can trigger a diff between repositories using the compare/diff functionality, leading to unauthorized code access. The vulnerability is classified as an IDOR and was assigned a CVE, fixed in later versions.

## Attack Flow

```mermaid
graph LR
    A[Gather Intelligence] --> B[Initiate Diff] --> C[Retrieve Code]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specified; web browser or API client for GitHub interactions

### Target Environment

- GitHub Enterprise Server (vulnerable versions)
- Web-based access to GitHub interface

### Initial Access Requirements

- Access to at least one repository on the server
- Knowledge of target private repository name and details (branches, tags, or SHAs)

## Step 1: Gather Intelligence - [[procedures/Gather-Private-Repository-Intelligence]]

### Objective

Identify the target private repository and collect necessary details such as its name, branches, tags, or commit SHAs to prepare for the diff exploitation.

### Instructions

Obtain the name of the private repository through reconnaissance or prior knowledge. Collect branch names, tags, or commit SHAs, which might be guessed, leaked, or obtained via other means. No specific commands are used; this step relies on intelligence gathering.

### Validation

Confirm you have accurate repository details ready for the diff request.

## Step 2: Initiate Cross-Repository Diff - [[procedures/Initiate-Cross-Repository-Diff]]

### Objective

Use the compare/diff functionality to request a diff between an accessible repository and the target private one.

### Instructions

Navigate to the compare/diff endpoint in GitHub Enterprise Server (e.g., via URL like /compare/<base>...<head> where base and head reference the private repo details). Submit the request to trigger the diff across repositories.

### Validation

Observe if the diff request processes without immediate authorization errors.

## Step 3: Retrieve Code via Diff - [[procedures/Exploit-Diff-for-Code-Retrieval]]

### Objective

Exploit the improper access control to access and retrieve limited code content from the diff output.

### Instructions

Review the diff output generated from the previous step, which exposes limited code from the private repository due to missing authorization checks.

### Validation

Successfully view code snippets from the private repository in the diff results.

## Attack Chain Summary

### Key Achievements

1. Gathered necessary intelligence on private repository
2. Triggered unauthorized cross-repository diff
3. Retrieved limited private code content

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]
