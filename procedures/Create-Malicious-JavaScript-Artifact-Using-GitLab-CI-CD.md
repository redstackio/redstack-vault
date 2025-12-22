---
tags:
  - xss
  - gitlab
  - ci-cd
  - artifact
type: procedure
tools:
  - '[[tools/GitLab-CI-CD]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-gitlab-ci-yml]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bfe055cd-c98f-4d6f-b63a-aea45f5fb1c3
created_at: '2025-12-13T23:52:43.692Z'
updated_at: '2025-12-13T23:52:43.692Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-JavaScript-Artifact-Using-GitLab-CI-CD

## Summary

This procedure sets up a GitLab CI/CD pipeline to generate a malicious JavaScript file as an artifact, ensuring it is served with the correct MIME type (application/javascript) to bypass browser restrictions like X-Content-Type-Options: nosniff.

## Description

In a GitLab project, configure a CI/CD job that writes arbitrary JavaScript to a file named alert.js and exposes it as a downloadable artifact. This allows hosting the payload externally without direct file upload restrictions. The artifact URL can then be referenced in subsequent steps for XSS delivery. Requires authenticated GitLab access to create and run pipelines.

## Requirements

1. GitLab account with project creation and CI/CD execution rights
2. Access to a GitLab repository
3. Basic knowledge of YAML for .gitlab-ci.yml

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type validation on all artifact downloads
- Monitor CI/CD jobs for suspicious script outputs (e.g., echo to JS files)
- Implement content security policies (CSP) blocking external script loads

## Objectives

1. Host executable JavaScript externally via GitLab artifacts
2. Bypass MIME sniffing protections
3. Prepare payload for embedding in SVG

## Instructions

### Step 1: Initialize GitLab Project

**Context**: Create or use an existing GitLab project to host the CI/CD configuration.

No command needed; use GitLab UI to create a new project and clone it locally.

### Step 2: Create CI/CD Configuration

**Context**: Define a job that generates the malicious JS file using [[commands/create-gitlab-ci-yml]] to write the .gitlab-ci.yml file.

**Command** ([[commands/create-gitlab-ci-yml]]):
```bash
echo 'xss_job:
  script:
    - echo "alert(\'Hello: \' + window.parent.location.href);" > alert.js
  artifacts:
    paths:
      - alert.js
    expire_in: 4 weeks' > .gitlab-ci.yml
```

> This creates a YAML file configuring a job named 'xss_job' that echoes the alert script to alert.js and artifacts it for 4 weeks. Commit and push to trigger the pipeline.

### Step 3: Trigger Pipeline and Retrieve Artifact

**Context**: Run the CI/CD job to produce the artifact URL.

Use GitLab UI to commit .gitlab-ci.yml and start the pipeline. Once complete, download the artifact from the job page to verify.

**Expected Output**: Job succeeds; artifact URL available, e.g., https://gitlab.com/username/project/-/jobs/123/artifacts/raw/alert.js, served as application/javascript.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-gitlab-ci-yml]]

## Tools Used

- [[tools/GitLab-CI-CD]]

## Tags

- xss
- gitlab
- ci-cd
