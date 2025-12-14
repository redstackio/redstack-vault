---
id: p-generate-gitlab-export
name: Generate-and-Download-Project-Export
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.261Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - gitlab
  - export
  - information-disclosure
platforms:
  - Web
tools: []
commands: []
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

# Generate-and-Download-Project-Export

## Summary

This procedure triggers GitLab's project export feature to generate a .tar.gz archive containing serialized project data, including unredacted user objects with authentication tokens, and downloads it via email link.

## Description

The GitLab export feature serializes the entire project, including the project_members array with full user details like authentication_token, hashed passwords, and OTP secrets, without any filtering. An attacker navigates to project settings to start the export, waits for an email notification, and downloads the archive from the provided URL. This exploits the information disclosure vulnerability in the export serialization process. Prerequisites: project with target member. Expected outcomes: downloadable archive with sensitive data.

## Requirements

1. Project with target user as member
2. Access to project settings in GitLab UI
3. Email access associated with attacker account

## Defense

Defensive measures and detection strategies:

- Redact sensitive fields (e.g., tokens) during export serialization
- Log and monitor export requests, alerting on frequent exports from new projects
- Disable or restrict export for non-admin users

## Objectives

1. Serialize project data including target user tokens
2. Obtain export archive for extraction
3. Enable credential access

## Instructions

### Step 1: Initiate Export

**Context**: Start the serialization process via UI.

No command; in project settings, select "Export project" to trigger background job.

> Export queued; process may take a few minutes.

### Step 2: Wait for Notification

**Context**: GitLab emails a download link once ready.

No command; check email inbox for notification from GitLab.

> Email received with link like http://gitlab-instance/account/repo/download_export.

### Step 3: Download Archive

**Context**: Retrieve the .tar.gz file.

No command; click the link in email to download the export archive to local machine (e.g., ~/Downloads).

> File downloaded, e.g., 2016-08-12_09-34-826_gitlab-org_gitlab-test_export.tar.gz.

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
- [[export]]
- [[information-disclosure]]
