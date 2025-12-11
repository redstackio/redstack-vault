---
id: b1bf1334-7d97-432a-a49c-d0dae1e00f7b
name: Intercept and Modify Project Creation Request in GitLab
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.620Z'
updated_at: '2025-12-11T03:47:47.620Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - request-manipulation
  - authorization-bypass
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Intercept and Modify Project Creation Request in GitLab

## Summary

This procedure uses Burp Suite to intercept and modify a GitLab project creation request, bypassing authorization to import private data from a restricted project template.

## Description

By manipulating parameters in the POST request to /projects, an attacker can force the use of a custom template from an unauthorized group, exploiting validation skips and missing checks in GitLab EE. This leads to the export and import of confidential data like repositories and issues. The procedure targets web-based GitLab instances and results in data exfiltration to the attacker's project.

## Requirements

1. Burp Suite installed and configured for proxying
2. Two GitLab accounts
3. Access to the project creation page

## Defense

Defensive measures and detection strategies:

- Implement strict validation in project creation services
- Monitor Sidekiq jobs for unauthorized exports

## Objectives

1. Bypass template validation
2. Import private data without authorization
3. Achieve data exfiltration

## Instructions

### Step 1: Navigate to Creation Page

**Context**: Prepare the request from the unauthorized account.

Sign into the second account and go to http://instance/projects/new.

> This initiates the project creation flow.

### Step 2: Intercept and Modify Request

**Context**: Use Burp to alter parameters.

Create a new project and intercept the POST /projects request with [[tools/Burp-Suite]]. Modify: set project[use_custom_template] to true, project[template_name] to 'test_project', project[group_with_project_templates_id] to 1.

Execute [[commands/curl-gitlab-project-create]] for equivalent:

```bash
curl -X POST "http://instance/projects" -d "project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1" -H "Authorization: Bearer [token]"
```

> This bypasses checks and triggers the import.

### Step 3: Forward and Wait

**Context**: Complete the import process.

Forward the modified request and wait for the server to process the import.

> Data will be copied after a few minutes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-gitlab-project-create]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[commands/curl-gitlab-project-create]]
- #request-manipulation
- #authorization-bypass
