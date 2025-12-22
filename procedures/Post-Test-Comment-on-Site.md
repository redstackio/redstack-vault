---
tags:
  - posting
  - comment
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 07fe5aaf-9c4f-4167-9ffb-3e87ec84c728
created_at: '2025-12-14T17:28:28.723Z'
updated_at: '2025-12-14T17:28:28.724Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Post-Test-Comment-on-Site

## Summary

This procedure describes posting a sample comment on an IntenseDebate-integrated site to create a target for the subsequent spam reporting attack, demonstrating normal user interaction before exploitation.

## Description

After site setup, users can post comments via the embedded IntenseDebate widget. This step simulates legitimate content addition, which becomes vulnerable to deletion once reporting is enabled. The target environment is any webpage with IntenseDebate comments; no special tools needed. Expected outcome: A visible comment that can be reported.

## Requirements

1. Configured IntenseDebate site from previous procedure
2. Access to the site's comment section
3. Web browser

## Defense

Defensive measures and detection strategies:

- Limit comment posting to authenticated users
- Moderate new comments before visibility
- Log all post actions for anomaly detection

## Objectives

1. Introduce target content for abuse demonstration
2. Verify site functionality post-configuration
3. Set stage for report spamming

## Instructions

### Step 1: Navigate to Site

**Context**: Load the page with the comment section.

Visit the site's URL where IntenseDebate is integrated.

> Page loads with comment form visible.

### Step 2: Post Comment

**Context**: Add a test comment to target.

Enter text like "Test comment for reporting demo" in the form and submit.

> Comment appears below posts, with report button adjacent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[posting]]
- [[comment]]
- [[web]]
