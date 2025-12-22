---
id: proc-uuid-4
tags:
  - workhorse
  - metadata-stripping
  - eval-injection
type: procedure
tools:
  - '[[tools/ExifTool]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:24:14.942Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
---
# Trigger-ExifTool-Processing-on-Upload

## Summary

Submit the upload to GitLab Workhorse, which automatically invokes ExifTool to remove metadata from the attached image, parsing the DjVu content and executing the injected Perl code.

## Description

Upon submission, Workhorse uses ExifTool with specific flags to strip non-whitelisted tags (e.g., -all= --IPTC:all). The DjVu parser in ExifTool's DjVu.pm (line 233) evals metadata tokens insecurely, allowing the backslash-newline bypass to inject qx{command}.

## Requirements

1. Successful file attachment in snippet
2. Target GitLab using vulnerable ExifTool integration
3. Server-side access for verification (optional)

## Defense

Defensive measures and detection strategies:

- Patch ExifTool to avoid eval on user metadata
- Isolate Workhorse processes with seccomp or containers
- Audit logs for ExifTool errors or unusual command executions

## Objectives

1. Invoke the vulnerable parsing path
2. Execute the payload silently during metadata handling
3. Achieve RCE without crashing the process

## Instructions

### Step 1: Confirm Submission

**Context**: Ensure the form submits the attachment.

Click 'Create snippet' after attaching.

> Expected: HTTP 200; no upload errors.

### Step 2: Monitor Backend (If Accessible)

**Context**: Observe Workhorse invoking ExifTool.

On server, tail logs for exiftool processes:

```bash
tail -f /var/log/gitlab/gitlab-workhorse/current | grep exiftool
```

> Expected: Invocation with flags like -all= -tagsFromFile @ -ResolutionUnit.

### Step 3: Await Processing Completion

**Context**: Processing happens asynchronously.

Wait 10-30 seconds for eval to trigger.

> Expected: No visible errors; payload executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Windows Command Shell]] Command and Scripting Interpreter: Perl

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ExifTool]]

## Tags

- backend-trigger
- perl-eval
