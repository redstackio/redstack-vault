---
tags:
  - gitlab
  - api
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Cloud (GitLab.com)
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 38345d0e-cefe-45b1-a554-4ee691bfa856
created_at: '2025-12-11T03:47:56.781Z'
updated_at: '2025-12-11T03:47:56.781Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
---
# Query Import API Endpoint

## Summary

This procedure queries the GitLab import API to retrieve status, which includes leaked data from the vulnerability.

## Description

After import, the API endpoint exposes up to 250 bytes of arbitrary files in its response, including sensitive credentials.

## Requirements

1. Imported project ID
2. Access to GitLab API

## Defense

Defensive measures and detection strategies:

- Monitor API access logs for import queries
- Restrict API endpoints

## Objectives

1. Retrieve leaked data
2. Exploit SSRF if applicable

## Instructions

### Step 1: Send GET Request

**Context**: Access the import API.

Execute [[commands/curl-api-query]] to query:

```bash
curl https://gitlab.com/api/v4/projects/PROJECT_ID/import
```

> Replace PROJECT_ID with the actual ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-api-query]]

## Tools Used



## Tags

- #gitlab
- [[commands/curl-api-query]]
