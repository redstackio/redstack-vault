---
tags:
  - xss
  - payload-injection
  - javascript
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
updated_at: '2025-12-13T23:56:03.896Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5fe40b5f-cefd-4f1e-b1a5-8255214ce07f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload in Error Description

## Summary

This procedure crafts and injects a JavaScript payload into the unsanitized error_description parameter to execute arbitrary code in the victim's browser.

## Description

Exploiting the identified vulnerability in /authentication/fb_callback, the payload breaks out of the HTML attribute context using a closing quote and injects an <img> tag with an onerror handler. This executes JavaScript when the image fails to load. The attack relies on URL encoding to bypass any basic filters and assumes no CSP restrictions. Expected outcome is immediate JS execution upon page load.

## Requirements

1. Confirmed vulnerable endpoint from prior reconnaissance
2. URL encoder (e.g., browser console or online tool)
3. Victim's browser context (e.g., via phishing link)

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all reflected parameters server-side
- Validate input length and content for error_description
- Log and alert on suspicious payloads in query strings

## Objectives

1. Break out of HTML context to inject executable script
2. Trigger JavaScript execution via event handler
3. Confirm control over victim's DOM

## Instructions

### Step 1: Craft Basic Payload

**Context**: Design a payload to close the attribute and inject a test script.

Use payload: "><img src=x onerror=prompt(document.domain)>. This closes the error_description="..." attribute and adds an invalid image that triggers onerror.

**Expected Output**: Upon execution, a prompt shows the domain.

### Step 2: Encode and Inject

**Context**: URL-encode the payload and append to the endpoint.

Encode to: %22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.domain%29%3E. Full URL: https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.domain%29%3E. Load in browser.

**Expected Output**: JS executes, prompting the domain.

**Success Indicators**:
- No encoding errors in URL
- Prompt appears without console errors

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
- [[JavaScript]]
