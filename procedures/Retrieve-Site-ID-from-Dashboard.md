---
tags:
  - discovery
  - web
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
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:15:05.468Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bec647ac-3476-4223-b3d0-0fea55cbcd17
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve-Site-ID-from-Dashboard

## Summary

This procedure extracts the numeric site ID from the IntenseDebate user dashboard, which is crucial for constructing the vulnerable comment history URL in a SQL injection attack.

## Description

The site ID is exposed in dashboard URLs and lists after creation. Navigating to the site's overview page reveals it in the path (e.g., /dash/12345). This reconnaissance step identifies the parameter for injection without triggering alerts, as it's standard user navigation.

## Requirements

1. Authenticated session with at least one site created
2. Web browser
3. Ability to inspect URLs

## Defense

Defensive measures and detection strategies:

- Obfuscate or avoid exposing internal IDs in client-side URLs
- Implement role-based access to dashboard views
- Log frequent dashboard accesses for potential reconnaissance

## Objectives

1. Obtain the exact site ID value
2. Map the parameter for targeted injection
3. Maintain low-profile discovery

## Instructions

### Step 1: Access User Dashboard

**Context**: View the list of managed sites.

Navigate to https://intensedebate.com/user-dashboard.

> Site list displays on the right side.

### Step 2: Select and View Site Overview

**Context**: Trigger the URL that embeds the site ID.

Select your site from the list and click 'Overview'.

> Redirects to https://intensedebate.com/dash/$YourSiteId; copy the ID from the URL bar.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[id-retrieval]]
- [[recon]]
