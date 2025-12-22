---
tags:
  - initial-access
  - gitlab
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/login-to-gitlab]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:56:19.844Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b8ba9be4-b468-434f-8faf-e854de99ea26
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-GitLab-and-Create-Issue

## Summary

This procedure establishes initial access to a GitLab project by logging in with valid user credentials and creating a new issue, setting the stage for injecting stored XSS payloads in Markdown-rendered content.

## Description

In the context of exploiting GitLab's stored XSS vulnerability, logging in as a regular user allows access to project issues or wikis where HTML injection can occur via the Markdown renderer. This step requires no elevated privileges and targets GitLab.com or self-hosted instances. Expected outcomes include visibility of the issue creation interface, enabling subsequent payload storage that affects all viewers.

## Requirements

1. Valid GitLab user credentials (email and password)
2. Web browser with access to GitLab.com
3. Target project membership or public access

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to secure logins
- Monitor for unusual login patterns from new IPs
- Use session timeouts and IP whitelisting for sensitive projects

## Objectives

1. Gain authenticated access to a GitLab project
2. Navigate to the issues section
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Access GitLab Login Page

**Context**: Open the GitLab instance and authenticate to obtain a session.

**Command** ([[commands/login-to-gitlab]]):

No specific command; use browser form submission with credentials.

> Enter username/email and password on https://gitlab.com/users/sign_in. Successful login redirects to the dashboard.

### Step 2: Navigate to Project and Create Issue

**Context**: Select or create a project, then access the issues tab to start a new one.

**Command** ([[commands/create-new-issue]]):

No CLI; browser navigation: Click 'New issue' button.

> This opens the issue creation form with title and description fields. Fill minimally to proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/login-to-gitlab]]
- [[commands/create-new-issue]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- initial-access
- authentication
