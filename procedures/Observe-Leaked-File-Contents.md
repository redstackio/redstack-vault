---
id: proc-uuid-2
tags:
  - file-leak
  - data-collection
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:32:48.444Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Observe-Leaked-File-Contents

## Summary

This procedure involves parsing the JSON response from the GitLab Search API after injection to observe and extract leaked file contents from the server's filesystem, confirming the arbitrary read and identifying sensitive information.

## Description

Following the injection, the API returns a JSON array of search results containing escaped or base64-encoded data from files in /var/opt/gitlab/gitaly, such as VERSION files and config.toml snippets. This step focuses on analysis to validate the exploit and pinpoint credentials like tokens, without requiring additional requests.

## Requirements

1. Successful output from prior injection step
2. JSON parsing tool like jq (optional for automation)
3. Knowledge of expected file formats (e.g., TOML config)

## Defense

Defensive measures and detection strategies:

- Implement response filtering to exclude non-repo file data in API outputs
- Log and alert on search results containing filesystem paths outside repos
- Use content security policies or API gateways to inspect and redact sensitive leaks

## Objectives

1. Validate arbitrary file read by inspecting response data
2. Identify and extract sensitive configurations
3. Prepare for credential validation in subsequent steps

## Instructions

### Step 1: Parse API Response

**Context**: Examine the JSON for 'data' fields containing file contents, looking for indicators of server files.

No specific command; manually review or use:
```bash
echo '[{"basename":null,"data":"VERSION\\u00001\\u0000Gitaly, version 1.53.2\\n","filename":null,"id":null,"ref":"--no-index","startline":0,"project_id":4}]' | jq '.[].data'
```

> Output shows escaped contents from VERSION file, confirming leak from /var/opt/gitlab/gitaly.

### Step 2: Identify Sensitive Data

**Context**: Search for keywords like 'token', 'dsn', or config sections in the leaked snippets.

Review for patterns:
```bash
# Hypothetical grep on saved response
grep -i 'token\|dsn' response.json
```

> Expected to reveal partial config.toml with API keys if present.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- file-leak
- data-exfiltration
