---
tags:
  - authentication
  - reddit
  - token
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:48.078Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6fe5b305-bb1d-4259-bdb9-0f7e551c2e34
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Reddit-Authentication-Token

## Summary

This procedure authenticates a user to Reddit's platform to obtain a bearer token, enabling subsequent API requests without moderator privileges.

## Description

In the context of exploiting the IDOR vulnerability, any valid Reddit account can be used to generate an authorization token. The token allows access to the GraphQL endpoint where the lack of subreddit-specific checks enables unauthorized mod log retrieval. This step requires standard login via Reddit's web interface or OAuth flow, targeting public endpoints.

## Requirements

1. Valid Reddit username and password
2. Web browser or API client for authentication
3. Network access to reddit.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual login patterns from non-moderator accounts
- Implement token rate limiting and anomaly detection on API usage

## Objectives

1. Acquire a functional bearer token
2. Establish authenticated session for GraphQL queries
3. Enable exploitation without additional privileges

## Instructions

### Step 1: Login to Reddit

**Context**: Use Reddit's login endpoint or web form to authenticate and capture the token.

**Command** (Browser or curl equivalent):
```bash
# Use browser dev tools to login at https://www.reddit.com/login
# Extract bearer token from localStorage or cookies (e.g., via Reddit's OAuth)
# Alternatively, use curl for OAuth flow:
curl -X POST https://www.reddit.com/api/v1/access_token \
  -u 'username:password' \
  -d 'grant_type=password&device_id=DO_NOT_TRACK_THIS_DEVICE'
```

> This command performs OAuth password grant to retrieve the token. Expected output: JSON with 'access_token' field.

### Step 2: Verify Token

**Context**: Test the token with a simple API call to ensure validity.

**Command** ([[reddit-token-verify]]):
```bash
curl -H "Authorization: Bearer your_token" https://oauth.reddit.com/api/v1/me
```

> Returns user profile if token is valid; errors otherwise.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- token-acquisition

