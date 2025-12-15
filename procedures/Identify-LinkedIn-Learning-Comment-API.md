---
tags:
  - api
  - recon
  - linkedin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inspect-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.108Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f8631c3e-2c65-4a52-932e-7233b5820a91
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-LinkedIn-Learning-Comment-API

## Summary

This procedure involves inspecting network traffic in the LinkedIn Learning Q&A section to identify the API endpoint and parameters used for deleting comment replies, setting the stage for access control testing.

## Description

In the context of testing the LinkedIn Learning platform, an authenticated user navigates to a course's Q&A section and uses browser developer tools to monitor network requests during comment interactions. This reveals the DELETE endpoint for comments, which relies on a URN parameter for identification. The procedure assumes access to a valid session and focuses on reconnaissance without exploitation. Expected outcomes include endpoint URL, method, and key parameters like the comment URN.

## Requirements

1. Authenticated LinkedIn Learning session
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Access to a course with active Q&A comments

## Defense

Defensive measures and detection strategies:

- Implement API request logging to monitor unusual DELETE operations
- Enforce rate limiting on comment-related endpoints
- Use client-side obfuscation for URNs to hinder inspection

## Objectives

1. Locate the comment deletion API endpoint
2. Document the URN parameter structure
3. Prepare for parameter manipulation testing

## Instructions

### Step 1: Navigate to Q&A Section

**Context**: Access a LinkedIn Learning course with comments to trigger relevant API calls.

**Command** ([[commands/curl-inspect-api]]):
```bash
# No direct command; use browser DevTools to open Network tab and interact with comments
```

> Open the course page, post or view a comment, and filter network logs for DELETE requests to `/comments/` paths. Note the full URL and headers.

### Step 2: Capture and Analyze Request

**Context**: Isolate the deletion request to understand its structure.

**Command** ([[commands/curl-inspect-api]]):
```bash
curl -X GET 'https://www.linkedin.com/learning/course-name/discussions' \
  -H 'Authorization: Bearer {token}'
```

> This simulates fetching discussions; in DevTools, replay or copy the actual DELETE request as curl for analysis. Identify URN in the path or body.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-api]]

## Tools Used


## Tags

- [[api]]
- [[recon]]
- [[linkedin]]
