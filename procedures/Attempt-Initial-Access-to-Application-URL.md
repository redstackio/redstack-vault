---
id: proc-001
tags:
  - initial-access
  - web
  - sso
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
updated_at: '2025-12-14T17:29:57.326Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Initial-Access-to-Application-URL

## Summary

This procedure tests initial access to the target DoD application URL to confirm SSO enforcement via redirect, setting the stage for bypass attempts.

## Description

In a typical attack scenario, the attacker first visits the public-facing application URL to observe authentication behavior. The U.S. Department of Defense application redirects to an SSO provider, indicating that authentication is handled externally via Akamai. This step confirms the need for a bypass and provides baseline behavior for comparison after exploitation. Prerequisites include a web browser and internet access to the target domain.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Public internet access to https://███
3. No special credentials or tools needed

## Defense

Defensive measures and detection strategies:

- Monitor web server logs for access patterns and redirects to SSO
- Implement rate limiting on authentication endpoints
- Use WAF rules to detect anomalous access attempts

## Objectives

1. Confirm SSO redirect behavior
2. Establish baseline for bypass validation
3. Identify the application as a potential target

## Instructions

### Step 1: Navigate to Target URL

**Context**: This step simulates a legitimate user attempt to access the application, triggering the SSO flow.

**Command** (Browser Navigation):

No command-line tool; use a web browser to visit https://███.

> The page should immediately redirect to the SSO authentication URL. If no redirect occurs, the application may not enforce SSO properly.

**Expected Output**: Redirect to https://█████████/pool/sso/authenticate/l/2?m=GET&r=t&u=https%3A%2F%2F████████%2F, prompting for login credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[initial-access]]
- [[web]]
- [[sso]]
