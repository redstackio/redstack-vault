---
tags:
  - data-exfiltration
  - collection
  - sensitive-information
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-inbox]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:33:34.555Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a43063e1-b234-4fe2-91d1-381b2aa68f13
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Data from Information Repositories]]'
---
# Access-Sensitive-Information-via-Inboxes

## Summary

This procedure covers navigating an authenticated session to extract sensitive data from platform inboxes and report views, including vulnerability details and program metadata.

## Description

With a hijacked session on HackerOne, attackers can access inboxes like HAS (up to 25 reports), Triage (up to 100), and full Report Views via UI or GraphQL. This exposes titles, descriptions, comments, and customer program info, loaded without additional auth checks. The procedure assumes an active session and focuses on data collection before potential revocation.

## Requirements

1. Active authenticated session via leaked cookie
2. Knowledge of platform endpoints (e.g., /inbox/has)
3. Tool for capturing responses (browser or cURL with output redirection)

## Defense

Defensive measures and detection strategies:

- Role-based access controls on inboxes
- Audit logs for unusual data access patterns
- Rate limiting on GraphQL queries
- Encrypt sensitive report data at rest

## Objectives

1. Load and view reports from multiple inboxes
2. Extract vulnerability details and metadata
3. Document exposure across programs

## Instructions

### Step 1: Access HAS Inbox

**Context**: Load the first inbox to retrieve initial report metadata.

**Command** ([[commands/curl-access-inbox]]):
```bash
curl -H "Cookie: __session=leaked_cookie_value_here" https://hackerone.com/inbox/has > has_reports.json
```

> Response includes up to 25 reports with titles and metadata. Expected output: JSON array of report objects.

### Step 2: Query Triage and Report Views

**Context**: Expand to other inboxes and full details.

**Command** ([[commands/curl-access-inbox]]):
```bash
curl -H "Cookie: __session=leaked_cookie_value_here" -X POST https://hackerone.com/graphql -d '{"query":"{ triageInbox(first:100) { reports { title description } } }"}'
```

> Uses GraphQL for bulk data. Expected output: Detailed vulnerability info and comments.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System
- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/curl-access-inbox]]

## Tools Used


## Tags

- [[data-exfiltration]]
- [[Collection]]
