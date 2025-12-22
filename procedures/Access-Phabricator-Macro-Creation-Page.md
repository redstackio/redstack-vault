---
id: proc-access-macro-page
tags:
  - ssrf
  - phabricator
  - initial-access
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
updated_at: '2025-12-14T04:39:02.184Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Phabricator-Macro-Creation-Page

## Summary

This procedure involves navigating to the Phabricator macro creation page to access the vulnerable URL input field, enabling subsequent SSRF exploitation.

## Description

In the context of Phabricator, a project management tool, the macro creation feature at `/macro/create/` includes a URL field for fetching external resources like images. Due to lack of validation, this field can be abused for SSRF. This step requires authenticated access and sets up the attack vector for internal requests.

## Requirements

1. Authenticated session in Phabricator
2. Web browser access to the target instance
3. Knowledge of the `/macro/create/` endpoint

## Defense

Defensive measures and detection strategies:

- Implement role-based access control to restrict macro creation
- Monitor access logs for repeated form submissions to `/macro/create/`
- Use web application firewalls (WAF) to block suspicious URL patterns

## Objectives

1. Locate the exploitable URL input field
2. Prepare for SSRF payload injection
3. Validate form accessibility

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Access the macro creation form to identify the target input.

Open a web browser and go to `https://target-phabricator.com/macro/create/`. Ensure you are logged in with a valid account that has permission to create macros.

> Upon successful navigation, the form should display fields including the URL input for resource fetching.

### Step 2: Inspect Form Elements

**Context**: Confirm the presence of the vulnerable URL field.

Examine the HTML form to locate the `<input>` element for the URL, typically labeled for image or resource URLs.

> Expected: Form submission button available; no immediate validation on URL input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[phabricator]]
