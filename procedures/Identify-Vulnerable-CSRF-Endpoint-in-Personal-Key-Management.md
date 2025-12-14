---
id: proc-uuid-1
tags:
  - csrf
  - recon
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.907Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable CSRF Endpoint in Personal Key Management

## Summary

This procedure involves manual testing to identify endpoints in account management features that lack CSRF protection, specifically targeting state-changing actions accessible via simple GET requests without token validation.

## Description

In the context of secure.login.gov, examine the personal key management functions to find unprotected endpoints. The attack scenario relies on discovering that session cookies alone suffice for actions like key resets, allowing cross-origin forgery. Prerequisites include access to a browser with dev tools and basic knowledge of HTTP requests. Expected outcomes: Confirmation of vulnerability enabling unauthorized actions.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Logged-in session on the target site for testing
3. Knowledge of the site's account management flows

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce strict origin/referer header checks
- Use SameSite=Strict cookies to prevent cross-site requests

## Objectives

1. Locate endpoints vulnerable to CSRF
2. Verify lack of protection mechanisms
3. Document request details for exploitation

## Instructions

### Step 1: Examine Account Management Functions

**Context**: Manually navigate to the personal key management section and monitor network traffic to identify relevant endpoints.

Open browser dev tools (Network tab), log in to secure.login.gov, and access the /manage/personal_key page. Trigger actions like resend or reset and inspect the requests.

**Expected Output**: Identification of GET request to https://secure.login.gov/manage/personal_key?resend=true without CSRF headers.

### Step 2: Test for CSRF Protection

**Context**: Attempt to replicate the request from a different origin to confirm vulnerability.

Use browser console or a tool like curl to send a GET request from another domain. Check if the action completes without additional validation.

**Expected Output**: Successful key reset action without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vuln]]
