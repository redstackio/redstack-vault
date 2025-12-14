---
tags:
  - file-upload
  - gitlab
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-import-file]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2260c85b-d785-4abe-973a-be2779565eb1
created_at: '2025-12-14T17:24:19.288Z'
updated_at: '2025-12-14T17:24:19.288Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Import-File-to-GitLab

## Summary

This procedure demonstrates uploading a project import file (tar.gz) to a GitLab instance via the web API or UI, scheduling a Sidekiq job for asynchronous processing, which sets up the race condition window.

## Description

GitLab's import feature allows users to upload repository exports for restoration into new projects. Files are POSTed to /import/gitlab_projects/create, copied to a shared tmp directory, and enqueued for Sidekiq unpacking. Using a common filename like 'import.tar.gz' maximizes collision potential. This step is performed under one account to prepare for overwrite.

## Requirements

1. Valid GitLab personal access token for the account.
2. A prepared tar.gz file (e.g., gitlab export archive).
3. Access to the GitLab API endpoint.
4. New project created in GitLab for import targeting.

## Defense

Defensive measures and detection strategies:

- Rate-limit concurrent imports per user/IP.
- Validate filenames for entropy or restrict to project-specific names.
- Log all upload attempts with timestamps for anomaly detection.

## Objectives

1. Successfully upload and store the file in shared uploads.
2. Enqueue Sidekiq job without immediate processing.
3. Confirm file uses predictable path for later collision.

## Instructions

### Step 1: Prepare the Import File

**Context**: Create or obtain a tar.gz file named 'import.tar.gz' for upload.

Use GitLab's export feature or manually create a sample archive.

> Expected: File ready with contents to be imported.

### Step 2: Execute Upload via API

**Context**: POST the file to the import endpoint to trigger storage and job enqueue.

**Command** ([[commands/curl-upload-import-file]]):
```bash
curl -X POST -H "Authorization: Bearer $GITLAB_TOKEN" -F "file=@import.tar.gz" https://gitlab.example.com/api/v4/import/gitlab_projects/create
```

> This sends the file, copies it to /var/opt/gitlab/gitlab-rails/shared/tmp/project_exports/uploads/import.tar.gz, and schedules Sidekiq. Expected output: JSON response with job ID or success status.

### Step 3: Verify Pending Status

**Context**: Check that the job is enqueued but not processed.

Monitor the project's import page in GitLab UI for 'Pending' status.

> Expected: File exists in tmp directory; Sidekiq queue shows unprocessed job.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-upload-import-file]]

## Tools Used



## Tags

- [[file-upload]]
- [[api]]
