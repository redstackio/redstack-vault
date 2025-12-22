---
id: proc-submit-mr-xss-payload
tags:
  - xss
  - merge-request
  - gitlab
type: procedure
tools:
  - '[[tools/GDK-GitLab-Development-Kit]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.775Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Merge-Request-with-XSS-Payload

## Summary

This procedure submits a merge request in GitLab using a branch named with an XSS payload, ensuring the malicious string is included in the request for later email rendering.

## Description

After creating the malicious branch, navigate to the merge request creation page and select the payload branch as source, targeting the original repo's master. This persists the payload in the MR metadata, which is unsanitized in email templates (e.g., `new_merge_request_email.html.haml`). Tested on GDK; outcome: MR created with payload ready to trigger XSS on notification.

## Requirements

1. Malicious branch created in forked repo.
2. Access to merge request UI.
3. Original repo's branch (e.g., master) as target.

## Defense

Defensive measures and detection strategies:

- Sanitize branch names in MR source selection.
- Scan MRs for HTML/JS in branch names before processing.
- Disable MRs from untrusted forks without approval.

## Objectives

1. Associate XSS payload with a merge request.
2. Target original repo to reach its maintainers.
3. Set up for email trigger via reviewer assignment.

## Instructions

### Step 1: Navigate to MR Creation

**Context**: Access the form to create a new merge request.

Use GitLab UI:

- Go to `http://yourserver:3000/your-namespace/html5-boilerplate/merge_requests/new`.

> Form allows source/target branch selection.

**Expected Output**: MR new page loads.

### Step 2: Select Branches and Submit

**Context**: Choose malicious source and original target.

- Set source branch to `<script>alert(1)</script>` from your fork.
- Set target to original repo's master.
- Submit the form.

> Payload branch selectable; MR queued.

**Expected Output**: MR creation confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDK-GitLab-Development-Kit]]

## Tags

- merge-request
- xss-payload
- submission
