---
type: code
language: yaml
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - gitlab-ci
  - yaml
  - execution
validated: true
---

# GitLab-CI-YAML-for-Parallel-Command-Execution

## Code

```yaml
stages:
    - test

test:
    stage: test
    script:
        - |
            whoami
    parallel:
        matrix:
            - RUNNER: VM1
            - RUNNER: VM2
            - RUNNER: VM3
    tags:
        - ${RUNNER}
```

## Description

This YAML configuration defines a GitLab CI pipeline that executes the 'whoami' command in parallel across three virtual machine runners, allowing simultaneous reconnaissance on multiple environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ${RUNNER} | Runner tag for selecting specific VMs | VM1, VM2, VM3 |

## Usage

Save as .gitlab-ci.yml in the repository root, commit, and push to trigger. Useful for scaling command execution in compromised repos with tagged runners.

## Detection

- Anomalous pipeline jobs with parallel matrix usage.
- Logs showing unexpected commands like whoami in test stages.
- Increased runner utilization without corresponding code changes.

## Related

- [[procedures/Arbitrary-Command-Execution-via-GitLab-and-GitHub-CI-CD-Pipelines]]
