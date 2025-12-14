---
id: proc-gitlab-login-tokens
tags:
  - authentication
  - token-extraction
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:25:47.637Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
---
# Login-to-GitLab-and-Extract-Tokens

## Summary

This procedure authenticates a user to a GitLab instance and extracts necessary authentication tokens (session cookies and CSRF tokens) from GraphQL API responses to enable subsequent authenticated requests for exploiting vulnerabilities.

## Description

In the context of GitLab IDOR exploitation, logging in establishes a valid session that can be abused to access unauthorized resources. Tokens are captured via interception during normal API interactions, allowing replay in custom GraphQL queries. This step requires only a standard user account and works across GitLab.com and self-managed instances. Prerequisites include browser access and basic knowledge of HTTP headers.

## Requirements

1. Valid GitLab username and password
2. Access to GitLab web interface (https://gitlab.com or instance URL)
3. Browser with developer tools (e.g., Chrome DevTools) or HTTP proxy (e.g., Burp Suite)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) to limit account compromise
- Monitor for unusual GraphQL query patterns or high-volume ID enumerations in API logs
- Use session timeouts and IP-based rate limiting on API endpoints

## Objectives

1. Establish authenticated session to GitLab
2. Extract reusable tokens for API abuse
3. Enable unauthorized data access without re-authentication

## Instructions

### Step 1: Authenticate to GitLab

**Context**: Log in via the web interface to create a session.

Navigate to https://gitlab.com/users/sign_in and enter credentials.

> Successful login redirects to the dashboard; inspect network tab for session establishment.

### Step 2: Trigger GraphQL Request and Intercept

**Context**: Perform an action (e.g., view a project) to generate a GraphQL API call, then capture headers.

Use browser dev tools: Open Network tab, filter for /api/graphql, and copy Cookie (_gitlab_session) and X-Csrf-Token from response headers.

> Tokens are now available for use in cURL or scripts; test by replaying a simple authenticated request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- token-extraction
- gitlab
