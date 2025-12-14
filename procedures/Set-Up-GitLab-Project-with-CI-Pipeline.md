---
id: proc-gitlab-setup-ci
tags:
  - gitlab
  - ci-pipeline
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-before-script]]'
  - '[[commands/echo-after-script]]'
  - '[[commands/echo-build-script]]'
  - '[[commands/echo-test-script]]'
  - '[[commands/echo-deploy-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:46.086Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-GitLab-Project-with-CI-Pipeline

## Summary

This procedure sets up a GitLab project and configures a CI/CD pipeline using a .gitlab-ci.yml file with placeholder echo commands to trigger subsequent integration tests.

## Description

In the context of exploiting SSRF in GitLab's GitHub integration, this procedure authenticates to GitLab, creates a new project, and commits a YAML file that defines CI stages (build, test, deploy) with simple echo scripts. This ensures pipelines are generated, providing the context for the integration test. The target is any GitLab instance; prerequisites include a valid user account. Expected outcome: Active pipelines ready for integration triggering.

## Requirements

1. Valid GitLab user credentials
2. Access to GitLab UI via web browser
3. Control over a Git repository for committing the YAML file

## Defense

Defensive measures and detection strategies:

- Monitor for unusual project creations and CI configurations in GitLab logs
- Enforce CI YAML validation to prevent suspicious scripts
- Use web application firewalls to detect anomalous pipeline triggers

## Objectives

1. Establish a project environment to test integrations
2. Generate pipelines that simulate normal CI activity
3. Prepare for GitHub integration configuration

## Instructions

### Step 1: Authenticate and Create Project

**Context**: Sign in to the GitLab instance and create a new repository to host the CI configuration.

No specific command; use GitLab UI to authenticate and create a project named e.g., 'test-ssrf'.

> Successful authentication redirects to the dashboard; project creation shows a new empty repo.

### Step 2: Commit .gitlab-ci.yml with Echo Scripts

**Context**: Add a .gitlab-ci.yml file using image: busybox:latest and echo commands in various stages to trigger pipelines.

**Command** ([[commands/echo-before-script]]):
```yaml
before_script:
  - echo "Before script section"
  - echo "For example you might run an update here or install a build dependency"
  - echo "Or perhaps you might print out some debugging details"
```

> This sets up pre-execution logging; expected output: Messages printed in pipeline logs.

**Command** ([[commands/echo-after-script]]):
```yaml
after_script:
  - echo "After script section"
  - echo "For example you might do some cleanup here"
```

> Post-execution cleanup simulation; expected output: Cleanup messages in logs.

**Command** ([[commands/echo-build-script]]):
```yaml
build1:
  stage: build
  script:
    - echo "Do your build here"
```

> Placeholder build; expected output: Build message.

**Command** ([[commands/echo-test-script]]):
```yaml
test1:
  stage: test
  script:
    - echo "Do a test here"
    - echo "For example run a test suite"

test2:
  stage: test
  script:
    - echo "Do another parallel test here"
    - echo "For example run a lint test"
```

> Test stage with parallel jobs; expected output: Test messages.

**Command** ([[commands/echo-deploy-script]]):
```yaml
deploy1:
  stage: deploy
  script:
    - echo "Do your deploy here"
```

> Deploy placeholder; expected output: Deploy message.

### Step 3: Wait for Pipeline Processing

**Context**: Allow GitLab to parse the YAML and create pipelines.

No command; wait ~1 minute and check the CI/CD pipelines tab.

> Expected output: Pipelines listed as pending or running.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/echo-before-script]]
- [[commands/echo-after-script]]
- [[commands/echo-build-script]]
- [[commands/echo-test-script]]
- [[commands/echo-deploy-script]]

## Tools Used

-

## Tags

- [[gitlab]]
- [[ci-pipeline]]
- [[setup]]
