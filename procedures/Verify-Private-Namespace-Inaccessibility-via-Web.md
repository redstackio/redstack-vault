---
tags:
  - recon
  - web
  - privacy-check
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:59.917Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d55fd477-beb0-4e9f-8f51-274e28d6a8d6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Private-Namespace-Inaccessibility-via-Web

## Summary

This procedure confirms that a GitLab user or group namespace is configured as private and inaccessible via the web interface, setting the stage for testing API bypasses.

## Description

In GitLab, private profiles and groups restrict visibility to authorized users only. This step involves manually accessing profile URLs to verify restrictions, such as seeing a 'Private' indicator without project details. It targets public instances like gitlab.com and assumes knowledge of the namespace fullPath (e.g., username). Expected outcomes include confirmation of web-level privacy, which the subsequent GraphQL exploitation will bypass.

## Requirements

1. Web browser access to GitLab instance
2. Known target namespace fullPath (e.g., 'rpadovani' for user, 'secret-group-213' for group)
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Monitor access logs for repeated failed profile views
- Enforce strict visibility settings and audit private namespaces

## Objectives

1. Establish baseline privacy via web interface
2. Identify restricted contributed projects
3. Validate setup for API testing

## Instructions

### Step 1: Access User Profile

**Context**: Check the main profile page for privacy indicators.

No command needed; use browser to visit https://gitlab.com/rpadovani.

> Browser shows 'This profile is private' or similar, with no details visible.

### Step 2: Check Contributed Projects

**Context**: Verify restrictions on project listings.

No command needed; attempt https://gitlab.com/users/rpadovani/contributed.

> Page restricted, confirming privacy extends to contributions.

### Step 3: Verify Group Access

**Context**: Repeat for groups to ensure broad applicability.

No command needed; visit https://gitlab.com/secret-group-213.

> Displays 'You don't have access' message.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- recon
- web
- privacy-check
