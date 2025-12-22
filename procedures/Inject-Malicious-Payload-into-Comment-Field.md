---
tags:
  - xss
  - injection
  - payload
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:41.612Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 49e22898-ac66-4dee-80c1-3662f2e6b44e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Comment-Field

## Summary

This procedure involves injecting a malicious JavaScript payload into a comment field on apps.owncloud.com, exploiting insufficient input sanitization to store XSS code that executes when viewed on a profile page.

## Description

In the context of the stored XSS vulnerability on apps.owncloud.com, attackers post comments containing unsanitized HTML and JavaScript. The payload `'><img src=x onerror=confirm(2)>` breaks out of HTML context and uses an invalid image source to trigger JavaScript via the onerror event. This is stored server-side and displayed raw on profile pages, affecting any viewer, including unauthenticated users. Prerequisites include a registered account for posting comments; outcomes enable client-side attacks like cookie theft.

## Requirements

1. Registered user account on apps.owncloud.com
2. Web browser with developer tools for inspection
3. Internet access to the target site

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization using libraries like DOMPurify for all user inputs
- Apply output encoding (e.g., HTML entity encoding) when rendering comments
- Use Content Security Policy (CSP) to restrict inline scripts and eval
- Monitor for anomalous JavaScript execution in browser logs or WAF alerts

## Objectives

1. Store malicious JavaScript payload on the server via comment submission
2. Ensure payload evades basic client-side validation
3. Prepare for execution on profile page views

## Instructions

### Step 1: Locate Comment Field

**Context**: Identify a section where comments can be posted, such as app reviews or discussions on apps.owncloud.com.

Navigate to https://apps.owncloud.com and find a comment input area. Inspect the form using browser developer tools to confirm no client-side sanitization blocks the payload.

### Step 2: Craft and Submit Payload

**Context**: Enter the malicious payload to inject executable JavaScript.

In the comment textarea, input the following payload:

```
'><img src=x onerror=confirm(2)>
```

Click submit to post the comment. Verify submission success without errors.

> This payload closes any enclosing HTML tag with `'>`, then inserts an `<img>` element with an invalid `src` attribute, triggering the `onerror` event to execute `confirm(2)`, which displays a dialog box.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
