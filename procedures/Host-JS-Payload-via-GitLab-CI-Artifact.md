---
tags:
  - csp-bypass
  - gitlab-ci
type: procedure
tools:
  - '[[tools/GitLab-CI-CD]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-test-in-gitlab-ci]]'
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 87d105c4-3924-4977-8f8a-8d22b0230fc4
created_at: '2025-12-13T23:52:24.586Z'
updated_at: '2025-12-13T23:52:24.586Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-JS-Payload-via-GitLab-CI-Artifact

## Summary

This procedure uses GitLab CI/CD to host a malicious JavaScript file as a downloadable artifact, served from gitlab.com for CSP-compliant loading.

## Description

GitLab CI artifacts are hosted on the same domain, allowing script-src loads. The job creates a raw JS file accessible via a predictable URL, expiring in 4 weeks for persistence.

## Requirements

1. GitLab account with project creation
2. Repository access for commits
3. Basic YAML knowledge

## Defense

Defensive measures and detection strategies:

- Restrict CI artifact public access
- Monitor for suspicious job artifacts
- Scan CI pipelines for malicious files

## Objectives

1. Generate and host JS payload
2. Obtain accessible URL
3. Ensure correct Content-Type

## Instructions

### Step 1: Create Project and Files

**Context**: Set up hosting environment.

Create new project via UI; add `payload.js`:

```javascript
alert(document.cookie);
```

### Step 2: Configure CI YAML

**Context**: Define job to produce artifact.

Add `.gitlab-ci.yml`:

```yaml
js:
  script: '[[commands/echo-test-in-gitlab-ci]]'
  artifacts:
    paths:
      - payload.js
    expire_in: 4 weeks
```

### Step 3: Trigger and Retrieve

**Context**: Run pipeline and get URL.

Commit/push; go to CI/CD > Jobs > Artifacts > raw/payload.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/echo-test-in-gitlab-ci]]

## Tools Used

- [[tools/GitLab-CI-CD]]

## Tags

- [[csp-bypass]]
- [[gitlab-ci]]
