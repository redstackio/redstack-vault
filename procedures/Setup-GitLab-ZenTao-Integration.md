---
tags:
  - gitlab
  - integration-setup
type: procedure
tools:
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Self-hosted GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 68f22861-9b67-4672-aefb-36844bd658ae
created_at: '2025-12-11T03:47:48.762Z'
updated_at: '2025-12-11T03:47:48.762Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup GitLab ZenTao Integration

## Summary

This procedure guides the configuration of GitLab's ZenTao integration with a malicious server URL, setting the stage for fetching and rendering unvalidated API responses that lead to stored XSS.

## Description

By logging into a self-hosted GitLab instance, creating a project, and configuring the ZenTao integration to point to a malicious server, the attacker ensures that GitLab will request data from the controlled endpoint. This exploits the lack of URL validation and insufficient encoding in the integration's serializer.

## Requirements

1. Valid credentials on a premium self-hosted GitLab instance
2. Access to project creation and integration settings
3. Malicious ZenTao server already hosted

## Defense

Defensive measures and detection strategies:

- Restrict integration configurations to trusted URLs
- Audit integration changes in GitLab
- Enable strict CSP on self-hosted instances

## Objectives

1. Establish a link between GitLab and malicious server
2. Prepare for payload delivery via API fetches
3. Enable subsequent XSS triggering

## Instructions

### Step 1: Login to GitLab

**Context**: Access the GitLab instance as a user.

Log in with user1 credentials on the premium self-hosted instance.

> Navigate to the dashboard after login.

### Step 2: Create New Project

**Context**: Set up a project for the integration.

Create a project named project1.

> Confirm project creation and access settings.

### Step 3: Configure Integration

**Context**: Point the integration to the malicious server.

Navigate to /-/integrations/zentao/edit, set server URL to https://joaxcar.com, leave API field empty, add any username and password, and save.

> Verify integration is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- [[procedures/Setup-GitLab-ZenTao-Integration]]
