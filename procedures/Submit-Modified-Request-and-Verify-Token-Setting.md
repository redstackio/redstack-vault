---
id: 0f4b45e3-40fd-47fb-9002-cd9b6d3a78e0
name: Submit-Modified-Request-and-Verify-Token-Setting
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.388Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - web
  - verification
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Submit-Modified-Request-and-Verify-Token-Setting

## Summary

This procedure submits the modified request with arbitrary CSRF tokens and verifies that the token persists in browser cookies, confirming the vulnerability.

## Description

Following token modification, this step ensures the server sets the arbitrary CSRF token in the response cookies and that it is accepted in subsequent requests. In the Veris Django application, this highlights the informative risk of weakened CSRF protection, as attackers could forge requests to unauthenticated endpoints without proper token validation.

## Requirements

1. Successful prior modification and submission
2. Access to browser developer tools for cookie inspection
3. Proxy tool for any follow-up request interception

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens against server-generated values with timing-safe comparisons
- Audit cookie settings to ensure CSRF tokens are not arbitrarily settable
- Implement WAF rules to detect mismatched or suspicious token patterns

## Objectives

1. Confirm request success post-modification
2. Verify arbitrary token storage in cookies
3. Test persistence in follow-up interactions

## Instructions

### Step 1: Update Token in Subsequent Request

**Context**: Ensure the arbitrary token is used in the next interaction to test persistence.

If needed, intercept a follow-up request (e.g., login) and set the csrftoken cookie to the arbitrary value used previously.

> This simulates continued use of the bypassed token.

### Step 2: Inspect Browser Cookies

**Context**: Check if the server has set the arbitrary token in the browser's cookie storage.

Use browser DevTools (Application > Cookies) or proxy history to view the csrftoken cookie.

> The cookie should show the arbitrary value (e.g., 'arbitrarytoken1234567890') without expiration or rejection.

### Step 3: Validate Acceptance

**Context**: Confirm no errors in token handling for ongoing sessions.

Perform another action on the site and observe no CSRF-related errors.

> Success indicated by normal site functionality with the custom token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[verification]]
