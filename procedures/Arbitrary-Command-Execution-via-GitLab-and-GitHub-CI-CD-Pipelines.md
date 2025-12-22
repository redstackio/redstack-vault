---
type: procedure
description: >-
  Exploit CI/CD pipelines in GitLab and GitHub to execute arbitrary commands on
  build runners, bypassing local security controls.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/Unix Shell|T1059.004 - Unix
    Shell]]
tags:
  - gitlab-ci
  - github-actions
  - cicd-compromise
  - command-execution
commands:
  - '[[commands/git-add-file]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push-origin]]'
  - '[[commands/whoami-bash]]'
platforms:
  - Linux
  - Windows
  - Cloud
tools: []
validated: true
---

# Arbitrary-Command-Execution-via-GitLab-and-GitHub-CI-CD-Pipelines

## Summary

This procedure demonstrates how to execute arbitrary commands on CI/CD runners in GitLab or GitHub by creating and triggering pipeline configurations. By gaining write access to a repository, an attacker can inject scripts into the CI/CD workflow, allowing remote code execution on build environments, which often have elevated privileges or access to sensitive resources.

## Description

CI/CD pipelines in platforms like GitLab and GitHub automate build, test, and deployment processes using configurable YAML files. These pipelines run on shared or self-hosted runners with potentially broad permissions. An attacker with repository write access can modify the pipeline configuration to run malicious commands, such as reconnaissance (e.g., whoami), data exfiltration, or persistence establishment. This technique evades endpoint detection by executing in isolated build environments and can target multiple runners in parallel for broader impact. It requires no direct access to the target infrastructure, making it suitable for supply chain attacks or initial foothold establishment in cloud environments.

## Requirements

1. Write access to a GitLab or GitHub repository with CI/CD pipelines enabled.
2. Git installed on the attacker's machine for committing changes.
3. Knowledge of the target repository's branch (e.g., main) and runner tags if using GitLab.
4. For GitHub, the repository must allow GitHub Actions; for GitLab, runners must be configured.

## Defense

- Enforce least-privilege access to repositories and pipelines, using branch protection rules.
- Implement mandatory code reviews and static analysis for CI/CD configuration files.
- Monitor pipeline logs and executions for anomalous commands or runner usage.
- Use isolated, ephemeral runners without persistent access to sensitive data.
- Enable pipeline approval gates for production branches.

## Objectives

1. Execute arbitrary commands on CI/CD runners to perform reconnaissance or actions.
2. Establish persistence or lateral movement via runner access to internal resources.
3. Exfiltrate data or deploy payloads without direct target compromise.

## Instructions

### Step 1: Create GitLab CI Configuration

**Context**: Prepare a .gitlab-ci.yml file to define a pipeline stage that executes the desired command in parallel across multiple runners. This allows scaling the execution for broader reconnaissance.

**Code** ([[codes/GitLab-CI-YAML-for-Parallel-Command-Execution]]):

Embed the YAML configuration in the repository root.

> The stages define the pipeline flow, script runs the command (e.g., whoami for identity confirmation), parallel matrix targets multiple runners, and tags select specific environments.

### Step 2: Add and Commit the Configuration File

**Context**: Stage the .gitlab-ci.yml file and commit it to the repository to prepare for triggering the pipeline.

**Command** ([[commands/git-add-file]]):
```bash
git add .gitlab-ci.yml
```

> This stages the YAML file for commit. Expected output: No output if successful; error if file not found.

**Command** ([[commands/git-commit-message]]):
```bash
git commit -m "Add CI pipeline for testing"
```

> Commits the changes with a innocuous message to avoid suspicion. Expected output: Commit hash and summary.

### Step 3: Push Changes to Trigger Pipeline

**Context**: Push the commit to the target branch to initiate the GitLab CI pipeline execution on runners.

**Command** ([[commands/git-push-origin]]):
```bash
git push origin main
```

> Pushes to the main branch, triggering the pipeline. Expected output: Push summary with branch update.

### Step 4: Monitor Pipeline Execution

**Context**: Observe the pipeline in the GitLab UI to confirm command execution and capture outputs from runners.

**Instructions**: Navigate to the project's CI/CD > Pipelines section. If using whoami, check job logs for user identity on each runner.

**Command** ([[commands/whoami-bash]]):
```bash
whoami
```

> This command runs within the pipeline script. Expected output: The username of the runner process (e.g., gitlab-runner).

### Step 5: Create GitHub Actions Workflow

**Context**: For GitHub, create a .github/workflows/ directory and add a YAML workflow file to execute commands on a specified runner OS.

**Code** ([[codes/GitHub-Actions-Workflow-for-Command-Execution]]):

Embed the YAML in .github/workflows/test.yml.

> The on section triggers on dispatch, push, or PR; jobs specify the runner and steps run the command.

### Step 6: Commit and Push GitHub Workflow

**Context**: Repeat the add, commit, and push steps for the GitHub workflow file to trigger execution.

**Instructions**: Use the same git commands as Steps 2-3, replacing the file with the workflow YAML. For manual trigger, use workflow_dispatch and run via GitHub UI after push.

**Expected Output**: In GitHub Actions tab, job logs show command output (e.g., whoami on Windows runner returns the build user).
