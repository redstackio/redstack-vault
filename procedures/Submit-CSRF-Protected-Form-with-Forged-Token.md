---
id: proc-submit-forged-form
tags:
  - csrf
  - form-submission
  - django
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T17:27:57.509Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Pass the Hash]]'
---
# Submit-CSRF-Protected-Form-with-Forged-Token

## Summary

This procedure submits a POST form to a CSRF-protected Django endpoint using the injected forged csrftoken, enabling unauthorized state changes like following a user.

## Description

With the forged token in cookies, the form parameter csrfmiddlewaretoken='x' matches, passing validation. Targets actions like /web/friendships/{id}/follow/. Requires prior injection.

## Requirements

1. Forged csrftoken in browser cookies
2. Target endpoint URL
3. Browser dev tools for form inspection

## Defense

Defensive measures and detection strategies:

- Use double-submit cookie with randomization
- Validate token binding to session
- Rate-limit state-changing endpoints

## Objectives

1. Submit POST with forged token
2. Bypass CSRF
3. Achieve unauthorized action

## Instructions

### Step 1: Prepare Form

**Context**: Identify and modify the CSRF-protected form.

Use dev tools to set csrfmiddlewaretoken='x' in the form.

> Expected: Form ready for submission.

### Step 2: Submit to Endpoint

**Context**: POST to target like /web/friendships/1312928755/follow/.

Submit via browser or curl equivalent.

> Expected: 200 OK, action completed without CSRF error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Pass the Hash]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[csrf]]
- [[form-submission]]
- [[django]]
