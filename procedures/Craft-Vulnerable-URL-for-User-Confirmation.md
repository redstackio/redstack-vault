---
tags:
  - path-traversal
  - web-exploit
type: procedure
tools:
  - '[[tools/Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.499Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a6392be5-3d4b-4bc8-b823-b7eb6c011519
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Vulnerable-URL-for-User-Confirmation

## Summary

This procedure crafts a URL exploiting path traversal in the invitation_token parameter of the /users/confirmation endpoint to access arbitrary internal paths like /test.json.

## Description

The vulnerability stems from insufficient validation of the invitation_token, allowing '../' sequences to manipulate file paths. In a web application like HackerOne, visiting a crafted URL triggers an internal request to unintended resources, potentially enabling CSRF on GET endpoints. This is useful in reconnaissance or chaining with other web vulnerabilities for unauthorized access.

## Requirements

1. Access to a browser
2. Target endpoint URL (e.g., https://hackerone.com/users/confirmation)
3. Basic understanding of URL parameters

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all path parameters to prevent traversal sequences
- Implement path normalization and allowlisting for file access
- Monitor server logs for anomalous internal requests to non-standard paths

## Objectives

1. Trigger path traversal to arbitrary internal file
2. Set up for traffic inspection to confirm exploitation
3. Assess potential for CSRF amplification

## Instructions

### Step 1: Construct the Vulnerable URL

**Context**: Build the URL with traversal payload in invitation_token to reach /test.json.

No command required; manually enter in browser address bar:

https://hackerone.com/users/confirmation?confirmation_token=z2-aaa&invitation_token=/../../test

> This payload uses '/../' to escape the intended directory and target /test.json. The page should load normally, but it initiates the internal request.

### Step 2: Access the URL

**Context**: Visit the URL to activate the traversal.

Navigate to the constructed URL in the browser.

> Expected behavior: Page renders without error, but network inspection (in next procedure) will reveal the unauthorized GET.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Developer-Tools]]

## Tags

- [[path-traversal]]
- [[web-exploit]]
