---
id: proc-uuid-3
name: Trigger Stored XSS on Profile Page
tags:
  - xss
  - execution
  - weblate
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.343Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS on Profile Page

## Summary

This procedure triggers the stored XSS payload by visiting the user's profile page, causing arbitrary JavaScript to execute in the browser context of any affected user.

## Description

Once the payload is injected into the project name, Weblate renders it unsanitized on the /accounts/profile/ page, which lists watched projects. Any user visiting this page—regardless of project access—will execute the JavaScript. The payload <svg/onload=alert(document.domain)> demonstrates proof-of-concept by alerting the domain, but could be escalated to steal cookies, keystrokes, or perform further exploits. This impacts the entire application user base in a Django/Weblate setup.

## Requirements

1. Any user account (admin, regular, or public viewer)
2. Injected payload in a watched project
3. Access to /accounts/profile/
4. Browser supporting JavaScript

## Defense

Defensive measures and detection strategies:

- Output-encode all dynamic content on profile pages using libraries like bleach
- Deploy browser-based protections like XSS auditors
- Monitor for unexpected JavaScript execution via client-side logging or anomaly detection

## Objectives

1. Execute the stored payload
2. Confirm arbitrary JS control in victim browser
3. Assess impact on application-wide users

## Instructions

### Step 1: Log In as Target User

**Context**: Use a victim account to simulate execution.

Log in to Weblate with the target user's credentials.

> Ensure the user has the injected project in their watched list (automatic if permissions were set).

### Step 2: Navigate to Profile Page

**Context**: Access the page where the payload renders.

Go to https://<domain>/accounts/profile/.

> The page loads, rendering the project name and triggering the onload event.

### Step 3: Observe Execution

**Context**: Verify the payload activates.

Watch for the alert dialog displaying 'document.domain'.

> If successful, the JS executes; replace alert with more malicious code for real attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- xss
- execution
- weblate
