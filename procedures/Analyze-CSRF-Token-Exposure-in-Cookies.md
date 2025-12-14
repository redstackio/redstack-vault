---
tags:
  - csrf
  - token-exposure
  - cookies
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Cloud Instance Metadata API]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 709aefe2-cda6-4f73-8873-51df9c493da5
created_at: '2025-12-14T17:27:22.589Z'
updated_at: '2025-12-14T17:27:22.589Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
---
# Analyze-CSRF-Token-Exposure-in-Cookies

## Summary

This procedure examines captured CSRF tokens stored in cookies to assess exposure risks, such as interception via network attacks or alongside session cookies in the Gratipay application.

## Description

CSRF tokens should be isolated from transport mechanisms like cookies to prevent compromise. In this case, the token is set in a cookie (e.g., csrftoken=zxRdWnGq3I5bMcXDRUWuWWXjxdsO1JtZ), making it vulnerable if cookies are stolen. This analysis highlights best practice violations and potential for forging requests if tokens are obtained. Requires prior interception; outcomes include risk documentation.

## Requirements

1. Captured HTTP request/response data
2. Access to cookie inspection tools
3. Understanding of CSRF best practices

## Defense

Defensive measures and detection strategies:

- Store CSRF tokens in hidden form fields or custom headers, not cookies
- Enforce SameSite=Strict/Lax on cookies to mitigate CSRF
- Log and alert on unusual cookie access patterns

## Objectives

1. Review token storage in cookies
2. Identify compromise vectors (e.g., XSS, MITM)
3. Assess impact on authenticated request forging

## Instructions

### Step 1: Inspect Cookies

**Context**: Examine the Set-Cookie header from the captured response.

In developer tools or proxy, view response headers for csrftoken cookie.

**Expected Output**: Cookie details showing token value and attributes.

### Step 2: Compare with Session Cookies

**Context**: Check if CSRF token is bundled with sensitive session data.

List all cookies in the request; note csrftoken's visibility.

**Expected Output**: Confirmation that token could be compromised with session hijacking.

### Step 3: Document Risks

**Context**: Summarize exposure potential.

Note risks like interception allowing forged POST requests to /statement.json.

**Expected Output**: Report on best practice violation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Cloud Instance Metadata API]] Credentials from Password Stores

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-exposure]]
- [[cookies]]
