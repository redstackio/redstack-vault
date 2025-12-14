---
id: proc-gitlab-github-config
tags:
  - gitlab
  - github
  - integration
type: procedure
tools:
  - '[[tools/Octokit-Ruby-Gem]]'
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
updated_at: '2025-12-14T04:08:46.083Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-GitHub-Integration-in-GitLab

## Summary

This procedure configures the GitHub integration in a GitLab project settings using an attacker-controlled external repository URL, triggering a test request to the fake endpoint.

## Description

To exploit the SSRF, configure the integration with a URL like http://remote_ip/1/2 where the attacker hosts a mock GitHub API. Clicking 'Test settings and save changes' causes GitLab to send a POST request via Octokit, setting up for interception. Target: GitLab project settings page. Prerequisites: Active project with pipelines. Outcome: Outgoing request to external endpoint.

## Requirements

1. Configured GitLab project from prior procedure
2. Attacker-controlled server hosting fake GitHub repo
3. Web browser access to GitLab

## Defense

Defensive measures and detection strategies:

- Validate integration URLs against allowlists
- Log and monitor external API calls from integrations
- Disable auto-testing for third-party integrations

## Objectives

1. Trigger GitLab's outbound request to external API
2. Prepare for request interception and manipulation
3. Simulate legitimate integration setup

## Instructions

### Step 1: Access Project Settings

**Context**: Navigate to the project's integrations section in GitLab UI.

Use GitLab UI to go to Settings > Integrations > GitHub.

> Expected output: Integration configuration form loaded.

### Step 2: Enter Attacker-Controlled URL

**Context**: Input the external repository URL under attacker control.

Enter URL: http://remote_ip/1/2 (where remote_ip is your server).

> This sets the target for the test POST.

### Step 3: Trigger Test and Save

**Context**: Initiate the validation request.

Click 'Test settings and save changes'.

> Expected output: GitLab sends POST to /api/v3/repos/1/2/statuses/... using Octokit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Octokit-Ruby-Gem]]

## Tags

- [[gitlab]]
- [[github]]
- [[integration]]
