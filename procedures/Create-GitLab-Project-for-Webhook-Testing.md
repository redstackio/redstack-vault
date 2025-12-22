---
tags:
  - gitlab
  - project-creation
  - initial-access
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
updated_at: '2025-12-14T04:39:18.565Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d6f23d9-8848-4d14-b2e9-a769afd8ff76
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-GitLab-Project-for-Webhook-Testing

## Summary

This procedure outlines logging into a GitLab account and creating a new project to enable configuration of webhook integrations for testing SSRF vulnerabilities.

## Description

In the context of exploiting SSRF in GitLab's webhook feature, an authenticated user must first establish a project environment. This involves accessing GitLab.com, authenticating, and creating a project under the user's namespace. The project serves as the foundation for navigating to settings and configuring integrations without restrictions on URL inputs.

## Requirements

1. Valid GitLab account credentials
2. Web browser with internet access
3. No additional permissions beyond standard user access

## Defense

Defensive measures and detection strategies:

- Monitor for unusual project creation patterns from new or suspicious accounts
- Implement rate limiting on project and integration configurations
- Log all authentication and project creation events for anomaly detection

## Objectives

1. Establish authenticated access to GitLab
2. Create a project for webhook testing
3. Prepare environment for SSRF payload submission

## Instructions

### Step 1: Authenticate to GitLab

**Context**: Log in to gain access to project creation features.

Access GitLab at https://gitlab.com and enter credentials to authenticate.

> Successful login redirects to the dashboard.

### Step 2: Create New Project

**Context**: Set up a project namespace for integrations.

From the dashboard, select 'New project' and choose 'Create blank project', providing a name and visibility settings.

> Project creation completes with a unique URL like https://gitlab.com/{username}/{project}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[project-creation]]
- [[initial-access]]
