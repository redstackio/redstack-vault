---
tags:
  - csrf
  - bypass
  - web-vulnerability
  - forgery
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
updated_at: '2025-12-14T17:27:15.418Z'
sub_techniques: []
id: a4e0cae2-6371-404f-a4ca-12b392e958d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass CSRF Protection to Create Unauthorized Udemy Course

## Summary

This procedure demonstrates forging a course creation request to Udemy's endpoint by omitting the CSRF token, exploiting the server's failure to enforce validation, resulting in unauthorized course creation on the victim's behalf.

## Description

Udemy's course creation process sends a CSRF token but does not validate it server-side, allowing attackers to craft malicious requests that mimic legitimate actions. This is typically executed by hosting a forged form on an attacker site and luring an authenticated victim to interact with it (e.g., via a link). The attack requires the victim's session cookie and targets the web platform, with outcomes including creation of unwanted courses, though the impact is low and informative.

## Requirements

1. Victim's authenticated session cookie (obtained via prior social engineering)
2. Knowledge of the course creation endpoint URL and required parameters
3. Ability to host a malicious HTML page or use request forging tools

## Defense

Defensive measures and detection strategies:

- Strictly validate CSRF tokens on all POST endpoints
- Implement same-site cookie attributes (Lax/Strict) to mitigate cross-site requests
- Log and alert on rapid or anomalous course creations

## Objectives

1. Submit a forged request without CSRF token to create a course
2. Confirm successful bypass and unauthorized action
3. Highlight the need for proper token enforcement

## Instructions

### Step 1: Prepare Forged Request

**Context**: Identify the endpoint and parameters from prior inspection.

The endpoint is typically /api/courses/create/ or similar. Required parameters include title, description, and category. Omit the CSRF token field.

**Expected Output**: Malicious HTML form or cURL command ready for execution.

### Step 2: Craft Malicious Form or Request

**Context**: Create a simple HTML page with an auto-submitting form to trick the victim.

Example HTML:

```html
<form action="https://www.udemy.com/api/courses/create/" method="POST" id="csrf-form">
  <input type="hidden" name="title" value="Forged Course">
  <input type="hidden" name="description" value="Unauthorized content">
</form>
<script>document.getElementById('csrf-form').submit();</script>
```

Host this on an attacker server and send the link to the victim.

**Expected Output**: Form submits using victim's cookies, bypassing token check.

### Step 3: Verify Course Creation

**Context**: Check the victim's Udemy account for the new course.

After submission, log in to the victim's account or monitor responses to confirm creation.

**Expected Output**: New course appears in the dashboard with the forged details.

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
- [[bypass]]
- [[udemy]]

