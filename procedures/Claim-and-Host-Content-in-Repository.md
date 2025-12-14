---
id: proc-uuid-003
tags:
  - github
  - supply-chain
  - rce
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
updated_at: '2025-12-14T17:33:06.708Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
---
# Claim-and-Host-Content-in-Repository

## Summary

This procedure covers claiming a specific GitHub repository under a newly registered organization and hosting proof-of-concept or malicious content to demonstrate takeover, potentially leading to RCE in downstream users.

## Description

Once the organization is controlled, the attacker creates or transfers the targeted repository (e.g., 'macrosan-csi-driver') and uploads content like a takeover notice or malicious driver code. Users following the official docs would download from this compromised repo, risking RCE during CSI driver installation in Kubernetes. Prerequisites: Control of the parent org. Expected outcomes: Repository under attacker control, visible via docs link, enabling supply chain attack.

## Requirements

1. Ownership of the GitHub organization
2. GitHub repository creation access
3. Basic Markdown or code editing skills

## Defense

Defensive measures and detection strategies:

- Validate all documentation links point to verified, owned repos
- Implement code signing for drivers
- Monitor for unexpected repo activity on project names

## Objectives

1. Create and claim the target repository
2. Host demonstration content
3. Verify accessibility via original documentation link

## Instructions

### Step 1: Create Repository

**Context**: Initialize the repo under the org.

No command required; from the org dashboard, click 'New repository' and name it 'macrosan-csi-driver'.

> Select public visibility to match docs expectation.

### Step 2: Upload Takeover Content

**Context**: Add files to prove control.

No command required; edit README.md with content like "This repository has been taken over as a proof-of-concept for dangling link vulnerability."

> Commit and push changes.

### Step 3: Verify Takeover

**Context**: Test the link from docs.

No command required; click the docs link https://github.com/macrosan-csi/macrosan-csi-driver.

> Expected output: Takeover message displayed, confirming compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Compromise Software Dependencies and Development Tools]] Compromise Software Dependencies and Development Tools

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- GitHub web interface

## Tags

- [[github]]
- [[supply-chain]]
- [[rce]]
