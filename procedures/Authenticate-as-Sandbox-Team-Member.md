---
id: proc-auth-sandbox-member
tags:
  - authentication
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.476Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate as Sandbox Team Member

## Summary

This procedure establishes authenticated access to HackerOne's GraphQL API by registering or joining a sandbox program, enabling queries that require team membership.

## Description

In the context of enumerating private programs, authentication as a sandbox team member is crucial because the GraphQL endpoint checks for membership in at least one sandbox team to allow access to certain fields like remaining_reports. This step involves creating a HackerOne account and joining a public sandbox program, which grants the necessary permissions without alerting defenses.

## Requirements

1. Valid email address for HackerOne registration
2. Internet access to hackerone.com
3. No prior bans or restrictions on the platform

## Defense

Defensive measures and detection strategies:

- Monitor for unusual account registrations or sandbox joins
- Implement rate limiting on API authentication endpoints
- Log all authentication attempts and review for anomalies

## Objectives

1. Obtain a valid authentication token
2. Verify access to GraphQL API
3. Prepare for subsequent queries

## Instructions

### Step 1: Register HackerOne Account

**Context**: Create an account if not already present to gain initial access.

Visit https://hackerone.com/signup and complete registration with email verification.

> Expected output: Confirmation email and login success.

### Step 2: Join Sandbox Program

**Context**: Join any public sandbox team to acquire membership status.

Navigate to a sandbox program page (e.g., search for 'sandbox' in directory) and request to join as a reporter.

> Expected output: Acceptance into the team, visible in user profile.

### Step 3: Obtain API Token

**Context**: Retrieve or generate an authentication token for API calls.

After login, use browser dev tools or API documentation to capture the Bearer token from session headers.

> Expected output: Token string for use in Authorization header.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- initial-access
