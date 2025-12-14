---
tags:
  - setup
  - gitlab
  - test-environment
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T00:11:09.728Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: cc6f48be-4258-4411-a574-e481c884019a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-GitLab-Test-Instance

## Summary

This procedure establishes a controlled GitLab 10.0.0 CE test environment to replicate and exploit the stored XSS vulnerability in the Markdown parser without risking production systems.

## Description

The GitLab 10.0 Markdown parser is vulnerable to stored XSS via character encoding bypasses. This setup involves deploying an isolated instance, creating a project with Wiki enabled, and preparing for payload injection during Wiki editing. It ensures the environment matches the vulnerable configuration, allowing safe testing of persistent JavaScript execution when viewing affected content.

## Requirements

1. Access to a VPS or local VM for installing GitLab CE 10.0.0
2. Administrative privileges to configure the instance
3. Web browser for initial access and project creation

## Defense

Defensive measures and detection strategies:

- Use updated GitLab versions (post-10.0 patches) to mitigate known parser flaws
- Implement content security policies (CSP) to block inline JavaScript execution
- Monitor Wiki edit logs for anomalous URL-encoded payloads with non-printable characters

## Objectives

1. Deploy a functional GitLab 10.0 instance with Project Wiki
2. Verify Markdown rendering capabilities
3. Prepare for authenticated editing sessions

## Instructions

### Step 1: Install GitLab 10.0.0 CE

**Context**: Download and configure the specific vulnerable version on a test server.

Follow official GitLab installation guides for version 10.0.0 CE, ensuring Omnibus package is used for simplicity. Access the instance via browser at http://your-gitlab-ip.

### Step 2: Create Project and Enable Wiki

**Context**: Set up a project to access the Wiki feature.

Log in as admin, create a new project, and navigate to Settings > General to enable Wiki. Go to the Project Wiki section and select 'Edit' on the homepage or create a new page.

**Expected Output**: Editable Wiki interface loaded, ready for content input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[setup]]
- [[gitlab]]
- [[test-environment]]
