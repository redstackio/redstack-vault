---
id: proc-uuid-1
tags:
  - csrf
  - xss
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/send-csrf-xss-post-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:43.224Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Identify-and-Test-CSRF-and-XSS-in-POST-Endpoint

## Summary

This procedure identifies a POST endpoint vulnerable to CSRF by testing form submissions without tokens and injects XSS payloads into parameters like building, classroom, and course to confirm arbitrary JavaScript execution.

## Description

In a web application handling scheduling or form data, the absence of CSRF protection allows external sites to submit POST requests on behalf of authenticated users. Combined with poor input validation, this enables XSS injection. The procedure uses tools like Burp Suite to craft and send requests with URL-encoded payloads such as %22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E, observing if the payload executes in the browser context, granting access to cookies and local storage for session hijacking.

## Requirements

1. Burp Suite Professional for request interception and modification
2. Valid authenticated session cookie for the target application
3. Knowledge of the target endpoint URL (e.g., /schedule)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Sanitize and encode user inputs in form parameters to prevent XSS
- Monitor for anomalous form submissions from unexpected origins

## Objectives

1. Confirm CSRF vulnerability by successful unauthorized submission
2. Validate XSS by executing a test payload like alert(document.domain)
3. Assess impact on session data access and page manipulation

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Use Burp Suite to capture a normal POST to the endpoint and note the form parameters.

No command needed; configure Burp proxy and browse the form.

### Step 2: Modify and Test with XSS Payload

**Context**: Replace parameter values with encoded XSS and resend to test injection.

**Command** ([[commands/send-csrf-xss-post-request]]):
```bash
curl -X POST https://target.com/schedule \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: session=value" \
  -d "schedule-building=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-classroom=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-course=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E"
```

> This sends the malicious form data; expected output is a 200 OK response without errors, and on page load, the alert executes confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/send-csrf-xss-post-request]]

## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[xss]]
