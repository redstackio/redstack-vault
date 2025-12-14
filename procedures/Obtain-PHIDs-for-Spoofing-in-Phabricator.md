---
id: proc-uuid-2
tags:
  - phabricator
  - phid-extraction
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-get-phabricator-user-phid]]'
  - '[[commands/curl-get-phabricator-object-phid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:11.077Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain PHIDs for Spoofing in Phabricator

## Summary

Extract PHIDs from user profiles and object references in Phabricator to enable spoofing in feed stories, targeting users or restricted items visible in HTML or API responses.

## Description

PHIDs (Phabricator Hardware IDs) uniquely identify entities like users and projects. Attackers can retrieve a target user's PHID from their profile page HTML (e.g., meta tags or JSON data). For restricted objects, inspect accessible pages like task views where subtasks reference hidden items. This procedure assumes basic view access and focuses on non-privileged reconnaissance. Outcomes include collectible PHIDs for payload manipulation, exploiting the API's lack of access checks.

## Requirements

1. Authenticated browser session to Phabricator
2. Access to target user pages and partial object views
3. Tools for inspecting HTML or making API queries

## Defense

Defensive measures and detection strategies:

- Restrict PHID exposure in HTML/JSON to authorized viewers only
- Log and audit unusual page views on user/object pages
- Use rate limiting on profile and object access endpoints

## Objectives

1. Retrieve authorPHID for user impersonation
2. Obtain objectPHID for restricted item references
3. Validate PHIDs for use in API payloads

## Instructions

### Step 1: Extract User PHID

**Context**: Visit the target user's page and pull PHID from source or API.

**Command** ([[commands/curl-get-phabricator-user-phid]]):
```bash
curl -X GET 'https://phabricator.example.com/api/user.search' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&constraints[usernames]=[\"targetuser\"]'
```

> Parse the response JSON for 'data' array containing 'phid' field. Expected output: {"result":{"data":[{"phid":"PHID-USER-abc123",...}]}}.

### Step 2: Extract Object PHID from References

**Context**: Inspect HTML of a viewable page referencing the restricted object.

**Command** ([[commands/curl-get-phabricator-object-phid]]):
```bash
curl -X GET 'https://phabricator.example.com/T123' \
  -H 'Cookie: session=authenticated' | grep -o 'PHID-[A-Z]*-[a-z0-9]*'
```

> Grep for PHID patterns in HTML output, focusing on subtasks or mentions. Success if restricted PHID appears without direct access denial.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-phabricator-user-phid]]
- [[commands/curl-get-phabricator-object-phid]]

## Tools Used


## Tags

- phabricator
- phid-extraction
- discovery
