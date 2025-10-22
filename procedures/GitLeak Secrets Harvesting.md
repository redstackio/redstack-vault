---
id: 8225b2e4-5ee1-4a09-bafc-1b86ed75ef8c
name: GitLeak Secrets Harvesting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.208419+00:00'
updated_at: '2023-04-10T20:33:56.268516+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
sub_techniques:
- '[[Domain Controller Authentication|T1556.001 - Domain Controller Authentication]]'
tags:
- '[[Git]]'
- '[[Gitleaks]]'
- '[[Harvesting secrets]]'
- '[[Insecure Source Code Management]]'
- '[[Tools]]'
commands:
- '[[Run gitleaks against a local repository]]'
- '[[Run gitleaks against a public repository]]'
- '[[Run gitleaks against a specific Github Pull request using Docker]]'
- '[[Run gitleaks against a specific Github Pull request using go get]]'
---

# GitLeak Secrets Harvesting

## Summary

GitLeak is a tool that searches through the code in a Git repository for secrets and other sensitive information. It can be used to identify hardcoded passwords, access tokens, and API keys that have been accidentally committed to a repository. Attackers can use this information to gain unauthorize

## Description

# Description

GitLeak is a tool that searches through the code in a Git repository for secrets and other sensitive information. It can be used to identify hardcoded passwords, access tokens, and API keys that have been accidentally committed to a repository. Attackers can use this information to gain unauthorized access to systems and data. GitLeak is a powerful tool for identifying and mitigating these risks.

## Requirements

1. Access to a Git repository.

1. Docker installed on the system.

## Defense

1. Use secure coding practices to avoid committing sensitive information to Git repositories.

1. Implement access controls and permissions to limit who can access Git repositories.

1. Use Git hooks to scan for sensitive information before it is committed to a repository.

## Objectives

1. Identify and mitigate risks associated with secrets and sensitive information being accidentally committed to a Git repository.

# Instructions

1. This command runs GitLeak against a public repository.

**Code**: [[# Run gitleaks against a public repository
docker ]]

> - `docker run`: Runs a Docker container.
- `--rm`: Removes the container after it has finished running.
- `--name=gitleaks`: Names the container gitleaks.
- `zricethezav/gitleaks`: Specifies the Docker image to use.
- `-v`: Enables verbose output.
- `-r https://github.com/zricethezav/gitleaks.git`: Specifies the repository to scan.

**Command** ([[Run gitleaks against a public repository]]):

```bash
docker run --rm --name=gitleaks zricethezav/gitleaks -v -r https://github.com/zricethezav/gitleaks.git
```

2. This command runs GitLeak against a local repository.

**Code**: [[# Run gitleaks against a local repository already ]]

> - `docker run`: Runs a Docker container.
- `--rm`: Removes the container after it has finished running.
- `--name=gitleaks`: Names the container gitleaks.
- `-v /tmp/:/code/`: Mounts the /tmp/ directory on the host machine to the /code/ directory in the container.
- `zricethezav/gitleaks`: Specifies the Docker image to use.
- `-v`: Enables verbose output.
- `--repo-path=/code/gitleaks`: Specifies the path to the repository within the container.

**Command** ([[Run gitleaks against a local repository]]):

```bash
docker run --rm --name=gitleaks -v /tmp/:/code/  zricethezav/gitleaks -v --repo-path=/code/gitleaks

```

3. This command runs GitLeak against a specific Github Pull request.

**Code**: [[# Run gitleaks against a specific Github Pull requ]]

> - `docker run`: Runs a Docker container.
- `--rm`: Removes the container after it has finished running.
- `--name=gitleaks`: Names the container gitleaks.
- `-e GITHUB_TOKEN={your token}`: Specifies the Github token to use.
- `zricethezav/gitleaks`: Specifies the Docker image to use.
- `--github-pr=https://github.com/owner/repo/pull/9000`: Specifies the Pull request to scan.
- `go get -u github.com/zricethezav/gitleaks`: Alternatively, you can install GitLeak using the `go get` command.

**Command** ([[Run gitleaks against a specific Github Pull request using Docker]]):

```bash
docker run --rm --name=gitleaks -e GITHUB_TOKEN={your token} zricethezav/gitleaks --github-pr=https://github.com/owner/repo/pull/9000
```

**Command** ([[Run gitleaks against a specific Github Pull request using go get]]):

```bash
go get -u github.com/zricethezav/gitleaks
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]

### Sub-Techniques

- [[Domain Controller Authentication|T1556.001 - Domain Controller Authentication]]

## Commands Used

- [[Run gitleaks against a local repository]]
- [[Run gitleaks against a public repository]]
- [[Run gitleaks against a specific Github Pull request using Docker]]
- [[Run gitleaks against a specific Github Pull request using go get]]

## Tags

- [[Git]]
- [[Gitleaks]]
- [[Harvesting secrets]]
- [[Insecure Source Code Management]]
- [[Tools]]
