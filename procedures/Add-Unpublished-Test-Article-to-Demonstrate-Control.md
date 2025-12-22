---
id: proc-uuid-6
tags:
  - zendesk
  - poc
  - content-demonstration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.584Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add Unpublished Test Article to Demonstrate Control

## Summary

This procedure adds a proof-of-concept article in Zendesk's Help Center to verify full subdomain control without public exposure.

## Description

Final step in takeover: insert unpublished content to show ownership, which can be extended to malicious pages for credential theft or file sharing in phishing scenarios.

## Requirements

1. Existing unpublished guide in Help Center
2. Zendesk admin access
3. Target subdomain fully mapped and SSL-enabled

## Defense

Defensive measures and detection strategies:

- Regularly review unpublished drafts for anomalies
- Implement content moderation and logging
- Use subdomain monitoring tools for unexpected changes

## Objectives

1. Prove control over subdomain content
2. Set stage for malicious use (e.g., phishing)
3. Validate takeover success

## Instructions

### Step 1: Access Article Creation

**Context**: Open the guide for article addition.

In Help Center, select the draft guide and add new article.

> Expected: Article editor loads.

### Step 2: Add and Save Test Article

**Context**: Create POC content and keep unpublished.

Title the article 'POC', add test text, and save as draft.

> Expected: Article in unpublished state, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[zendesk]]
- [[poc]]
- [[content-demonstration]]
