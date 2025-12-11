---
tags:
  - github
  - token-validation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a200ab1f-a3d7-4a5d-b1ff-13f8500bef2d
created_at: '2025-12-11T03:48:06.068Z'
updated_at: '2025-12-11T03:48:06.068Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Validate GitHub Token Authentication

## Summary

This procedure tests a discovered GitHub PAT by authenticating to the GitHub API to retrieve user and organization details, confirming its validity and scope.

## Description

Using curl to send authenticated requests to GitHub endpoints verifies if the token provides access to user info and organizations, essential for assessing potential impact like repository access.

## Requirements

1. Valid GH_TOKEN from prior extraction
2. Internet access to api.github.com
3. curl installed

## Defense

Defensive measures and detection strategies:

- Monitor API logs for unusual authentication attempts
- Use short-lived tokens and regular rotation

## Objectives

1. Confirm token authenticity
2. Identify associated user and orgs
3. Assess access level

## Instructions

### Step 1: Retrieve User Info

**Context**: Authenticate and get user details.

Execute [[commands/curl-github-user]]:

```bash
curl -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

> Returns JSON with user login and details.

### Step 2: Check Organizations

**Context**: List user's organizations.

Send GET to https://api.github.com/user/orgs with same headers.

> Returns array including Shopify org.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/curl-github-user]]

## Tools Used

- #curl

## Tags

- github
- token-validation
