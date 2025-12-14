---
id: proc-uuid-2
name: Verify-No-Public-Content-on-GitLab
tags:
  - discovery
  - public-exposure-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:28:44.331Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Verify No Public Content on GitLab

## Summary

This procedure checks the GitLab explore page to confirm that no public projects, groups, or snippets are visible, indicating the instance is configured as private but potentially vulnerable to credential-based access.

## Description

GitLab instances can be misconfigured to expose content publicly, but in private setups, the explore page should be empty. This step validates the instance's privacy status before attempting credential exploitation. Targets are GitLab EE instances behind nginx on standard web ports.

## Requirements

1. HTTPS access to the GitLab URL
2. Web browser
3. Target hostname from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce strict visibility settings on all projects and groups
- Monitor access logs for explore page visits from unknown IPs
- Use GitLab's audit logs to detect anomalous browsing

## Objectives

1. Confirm absence of public repositories
2. Validate private instance configuration
3. Identify potential for authenticated access

## Instructions

### Step 1: Navigate to Explore Page

**Context**: Access the explore endpoint to inspect for public content.

Use a web browser to visit:

https://[target-hostname]/explore

> The page loads showing no projects, groups, or snippets if properly private.

### Step 2: Inspect Page Elements

**Context**: Verify no hidden or default public items.

Examine the page source or UI for any listed items.

> Expected: Empty lists confirming no exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Discovery]]
- [[public-exposure-check]]
