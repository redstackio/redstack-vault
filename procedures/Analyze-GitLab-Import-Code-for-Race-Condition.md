---
tags:
  - recon
  - code-review
  - race-condition
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Linux
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: cd2a3f8d-d7de-4acd-97b2-b9c8c7dc386f
created_at: '2025-12-14T17:24:19.291Z'
updated_at: '2025-12-14T17:24:19.291Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-GitLab-Import-Code-for-Race-Condition

## Summary

This procedure involves reviewing GitLab's source code to identify a race condition in the project import feature, focusing on file upload paths that lack uniqueness, enabling potential overwrites in shared storage.

## Description

In a GitLab instance, the import process copies uploaded tar.gz files to a shared temporary directory using the original filename (e.g., 'import.tar.gz') without adding entropy, project IDs, or namespaces. Combined with asynchronous Sidekiq processing, this creates a window for concurrent uploads to collide and overwrite files. This analysis confirms the vulnerability in app/controllers/import/gitlab_projects_controller.rb and related methods, allowing attackers to predict and exploit the behavior for information disclosure.

## Requirements

1. Access to GitLab source code (e.g., public GitHub mirror or decompiled instance files).
2. Basic Ruby on Rails knowledge for code interpretation.
3. Text editor or IDE for reviewing specific lines (15-18 in the controller).

## Defense

Defensive measures and detection strategies:

- Implement file path randomization or project-specific subdirectories for uploads.
- Add uniqueness checks or locks during file operations to prevent overwrites.
- Monitor Sidekiq queues for anomalous import jobs and concurrent uploads from multiple accounts.

## Objectives

1. Confirm the use of original_filename in import_upload_path without safeguards.
2. Identify the processing delay introduced by Sidekiq.
3. Document the shared directory path (/var/opt/gitlab/gitlab-rails/shared/tmp/project_exports/uploads/) for exploitation planning.

## Instructions

### Step 1: Locate and Review Controller Code

**Context**: Examine the create endpoint to understand file handling logic.

No specific command; manually review app/controllers/import/gitlab_projects_controller.rb lines 15-18, where the file is copied using Gitlab::ImportExport.import_upload_path(original_filename).

> Expected: Code shows direct use of filename without hashing or UUIDs, storing in shared tmp/uploads/.

### Step 2: Check Import Path Method

**Context**: Verify path generation lacks uniqueness.

Review the Gitlab::ImportExport.import_upload_path method definition.

> Expected: Path construction relies solely on original_filename, e.g., /uploads/#{original_filename}, prone to collisions in multi-tenant environments.

### Step 3: Simulate Timing Window

**Context**: Understand the async gap by noting Sidekiq enqueue after upload.

Observe that the controller enqueues a job but does not process immediately, creating the race window.

> Expected: Confirmation of delay, testable by monitoring file system post-upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[recon]]
- [[code-review]]
