---
id: proc-slack-share-gist-001
tags:
  - xss
  - slack
  - integration
  - delivery
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.757Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Gist-in-Slack-Channel

## Summary

This procedure shares a malicious GitHub Gist link in a Slack channel with Gist integration enabled, setting up the vector for XSS exploitation in Slack's rendering.

## Description

Slack's Gist integration automatically embeds and processes shared Gist links, creating preview views on its domain. By posting the link from the previous procedure, the malicious filename is ingested into Slack's system. This step assumes access to a Slack workspace and relies on the integration being active. The outcome is the Gist becoming available for vulnerable views.

## Requirements

1. Slack workspace with GitHub Gist integration enabled (admin-configured)
2. Permission to post in a channel
3. The malicious Gist URL from prior step

## Defense

Defensive measures and detection strategies:

- Disable or restrict third-party integrations like Gist in Slack
- Implement URL scanning for shared links to detect suspicious payloads
- Educate users on verifying shared content before interaction

## Objectives

1. Deliver the malicious Gist to the target environment
2. Trigger Slack's processing of the Gist
3. Position for payload execution in subsequent views

## Instructions

### Step 1: Access Slack Workspace

**Context**: Ensure the workspace has Gist integration active.

Log in to Slack and navigate to the target channel. Verify integration via Slack's app directory if needed.

### Step 2: Post the Gist Link

**Context**: Share the link to initiate embedding.

Type or paste the Gist URL (e.g., https://gist.github.com/username/abc123) into the message and send.

**Expected Output**: Slack posts the message and generates an embedded preview of the Gist.

### Step 3: Confirm Integration Processing

**Context**: Check that Slack has created domain-specific views.

Interact with the embedded Gist to see options like 'raw' or 'open in new window' appear.

**Expected Output**: Preview shows without immediate errors, indicating successful ingestion.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[slack]]
- [[integration]]
