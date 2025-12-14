---
tags:
  - gitlab
  - issue-creation
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
updated_at: '2025-12-13T23:52:43.616Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 568058a5-5b18-4f8d-8b6a-798bb1ba90d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Issue-in-GitLab-Repository

## Summary

This procedure outlines creating a new issue in a GitLab repository using the web interface, serving as the initial vector for embedding malicious payloads in subsequent attack stages.

## Description

In the context of exploiting vulnerabilities like prototype pollution in GitLab's rendering components, creating an issue provides a persistent storage mechanism for injected content. This targets GitLab's issue tracking feature, which allows authenticated users to post markdown-formatted descriptions that can include diagrams. Prerequisites include a valid GitLab account with write permissions to the target project. Expected outcomes include a new issue URL that can be shared or viewed by other users to trigger the exploit.

## Requirements

1. Authenticated GitLab session with project write access
2. Web browser with JavaScript enabled
3. Access to the target GitLab instance via HTTPS

## Defense

Defensive measures and detection strategies:

- Enforce role-based access controls to limit issue creation to trusted users
- Monitor for unusual issue creation patterns or rapid edits in audit logs
- Implement content scanning for issues before rendering

## Objectives

1. Establish a persistent injection point for malicious content
2. Generate a shareable URL for the vulnerable issue
3. Prepare for payload embedding without triggering immediate alerts

## Instructions

### Step 1: Navigate to Project Issues

**Context**: Access the GitLab project to initiate issue creation.

Log in to GitLab and navigate to the target repository. Click on the "Issues" section in the left sidebar.

> This positions you in the issue management interface.

### Step 2: Create New Issue

**Context**: Use the UI to generate a blank issue for payload insertion.

Click the "New issue" button. Enter a benign title (e.g., "Test Diagram") and leave the description empty. Click "Create issue".

> Successful creation results in a new issue page with an editable description field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[issue-creation]]
