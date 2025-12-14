---
tags:
  - idor
  - information-disclosure
  - rest-api
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-retrieve-sensei-message]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:32:29.190Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 46fad535-f668-4f93-bd5f-89c908b753f0
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Data from Information Repositories]]'
---
# Access-Private-Sensei-Messages-via-REST-API

## Summary

This procedure exploits the lack of authentication on the Sensei LMS REST API endpoint to retrieve private messages by brute-forcing numeric IDs, leading to information disclosure.

## Description

The vulnerability allows unauthenticated GET requests to /wp-json/wp/v2/sensei-messages/<ID>, where IDs are sequential and predictable. In an attack scenario, an attacker enumerates IDs to access private student-teacher communications. Target: WordPress with Sensei LMS <= 4.4.3. Expected outcomes: Exposure of sensitive message content, including questions and responses.

## Requirements

1. Public access to the WordPress REST API
2. Knowledge of approximate ID ranges (e.g., from recent submissions)
3. curl or similar tool for HTTP requests

## Defense

Defensive measures and detection strategies:

- Add authentication checks to REST API endpoints for private post types
- Implement ID obfuscation or non-sequential identifiers
- Monitor API logs for enumeration patterns (e.g., sequential requests)
- Update to Sensei LMS > 4.4.3 if patch available

## Objectives

1. Bypass permissions to access private messages
2. Enumerate and disclose unauthorized data
3. Demonstrate impact of IDOR in LMS environments

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Confirm the vulnerable API path.

The endpoint is https://target.com/wp-json/wp/v2/sensei-messages/.

### Step 2: Enumerate and Retrieve Message

**Context**: Brute-force IDs starting from low numbers or known values to find private messages.

Execute [[commands/curl-retrieve-sensei-message]] to test specific IDs:

```bash
curl -X GET "https://target.com/wp-json/wp/v2/sensei-messages/123"
```

> This sends an unauthenticated request. If successful, JSON with message details (title, content, author) is returned. Repeat for sequential IDs to discover more.

**Expected Output**: JSON object like {"id":123,"title":"Private Question","content":"Student query here","status":"private"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Account Discovery]] Account Discovery
- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-retrieve-sensei-message]]

## Tools Used

- None

## Tags

- [[idor]]
- [[information-disclosure]]
- [[rest-api]]
- [[wordpress]]
