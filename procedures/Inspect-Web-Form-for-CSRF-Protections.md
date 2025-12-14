---
id: proc-uuid-1
name: Inspect-Web-Form-for-CSRF-Protections
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:03.128Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-Web-Form-for-CSRF-Protections

## Summary

This procedure involves using browser developer tools to inspect a web form's submission request, specifically checking for the absence of CSRF protection mechanisms like tokens or origin checks, as seen in the Legal Robot beta webhook endpoint.

## Description

In web applications, CSRF vulnerabilities arise when endpoints accept cross-origin requests without validation. This procedure targets forms like the one on Legal Robot's beta/nl page, where a POST to /webhooks/beta sends user data (names, email, language) without protections. The attacker analyzes the request to confirm exploitability, enabling subsequent forgery. Expected outcomes include identifying vulnerable fields and confirming session-based authentication without CSRF mitigations. Prerequisites include access to the target site and basic browser knowledge.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Authenticated session to the target application
3. Network access to the web application

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Enforce same-origin policy with CORS headers
- Monitor for anomalous cross-origin POST requests in server logs

## Objectives

1. Confirm absence of CSRF protections on the endpoint
2. Document form fields for exploitation planning
3. Validate that requests rely on session cookies

## Instructions

### Step 1: Access the Target Form

**Context**: Navigate to the vulnerable page to prepare for inspection.

Visit https://www.legalrobot.com/beta/nl/ and ensure you are authenticated. Fill in sample form data: firstName: Test, lastName: User, position: Tester, company: Example, email: test@example.com, language: nl.

### Step 2: Monitor and Submit the Form

**Context**: Use dev tools to capture the submission and analyze protections.

Open browser developer tools (F12), go to the Network tab, and submit the form. Locate the POST request to https://app.legalrobot.com/webhooks/beta.

Inspect headers and payload for CSRF tokens (e.g., _csrf field) or Origin/Referer checks. Note the absence of such measures.

**Expected Output**: Request details showing multipart/form-data with fields but no tokens.

### Step 3: Verify Vulnerability

**Context**: Confirm cross-origin potential by testing request replication.

Copy the request as cURL from dev tools and test from a different origin (e.g., local HTML file) to see if it succeeds without modifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
