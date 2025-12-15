---
tags:
  - broken-auth
  - api-capture
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/capture-semrush-project-creation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.273Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 312a2f5a-e441-4540-a4a9-9ecec7654fd1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Test-Users-and-Capture-Initial-Request

## Summary

This procedure sets up test user accounts on Semrush and captures a legitimate project creation API request during an active session, extracting the API key and request format for subsequent replay attacks.

## Description

In the context of exploiting broken authentication in Semrush's API, this initial procedure involves creating two test users, logging in to one, and capturing the HTTP POST request used to create a project. The request relies on an API key in the query parameter without tying it to session cookies, setting the stage for replay. This targets the /projects/api/projects/ endpoint on www.semrush.com, using PHP and Java-based session handling inferred from cookies.

## Requirements

1. Access to email accounts for registering Semrush users (e.g., Gmail)
2. Browser with developer tools for request capture (e.g., Firefox)
3. Network access to semrush.com
4. Basic knowledge of HTTP requests and JSON payloads

## Defense

Defensive measures and detection strategies:

- Implement API key rotation and expiration policies
- Enforce session validation alongside API keys (e.g., CSRF tokens)
- Monitor for anomalous project creation rates per API key
- Log and alert on requests without matching session IDs

## Objectives

1. Obtain valid API keys and request templates for replay
2. Verify legitimate project creation workflow
3. Prepare for demonstration of authentication bypass

## Instructions

### Step 1: Create Test Users

**Context**: Register two free accounts on semrush.com to simulate victim and attacker scenarios.

**Command** ([[commands/create-semrush-users]]):
No direct command; manually register via UI at https://www.semrush.com using emails like cleganearya1@gmail.com and saidutt.mekala@gmail.com.

> Expected: Confirmation emails and account access.

### Step 2: Capture Project Creation Request

**Context**: Log in as saidutt.mekala@gmail.com, navigate to projects, create a test project (e.g., domain: BB1236.com), and capture the network request in browser dev tools.

**Command** ([[commands/capture-semrush-project-creation]]):
```bash
# Replicate captured request via curl for documentation
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" \
  -H "Host: www.semrush.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" \
  -H "Content-Type: application/json" \
  -H "Cookie: cfduid=...; PHPSESSID=...; ..." \
  -d '{"domain":"BB1236.com","name":"BB12367.com","url":"BB123678.com","acl":{"write":true}}'
```

> This command sends the initial project creation. Expected output: HTTP 200 with JSON response including project ID and user email.

### Step 3: Cleanup Test Project

**Context**: Delete the created project via UI to avoid clutter.

> No command needed; use Semrush dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/capture-semrush-project-creation]]

## Tools Used

- [[tools/Python]]

## Tags

- broken-auth
- api-capture
