---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - csrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-update-security-questions]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:24.309Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-Security-Questions-Update-Request

## Summary

This procedure involves using a proxy tool to capture the HTTP POST request for updating security questions on a web application, revealing the absence of CSRF token validation for exploitation.

## Description

In the context of a DoD web application, an attacker with an account navigates to the security questions update page, submits a form change, and intercepts the request to analyze parameters and confirm no CSRF protection. This step is crucial for crafting subsequent exploits, targeting the endpoint https://www.█████████/member/updatesecurityquestions. Prerequisites include an active account and proxy setup.

## Requirements

1. Valid account on the target web application
2. Burp Suite Professional installed and configured as a proxy
3. Browser traffic routed through the proxy (e.g., 127.0.0.1:8080)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous proxy traffic or unusual request patterns in WAF logs
- Enforce strict referrer policy checks

## Objectives

1. Capture the exact form parameters and headers of the update request
2. Confirm lack of CSRF token in the response
3. Prepare data for PoC generation

## Instructions

### Step 1: Configure Proxy and Access Update Page

**Context**: Set up interception to capture the legitimate request.

**Command** ([[commands/curl-update-security-questions]]):
```bash
curl -X POST https://www.███████/member/updatesecurityquestions \
  -H "Cookie: {YOUR-COOKIE}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: https://www.██████/member/updatesecurityquestions" \
  -d "security_questions1=1&security_question_answer1=temp&security_questions2=2&security_question_answer2=temp&security_questions3=3&security_question_answer3=temp&submit=Save"
```

> This simulates the POST request; in practice, perform it via the browser with Burp intercepting to capture real cookies and session data. Expected output: 200 OK with updated confirmation.

### Step 2: Analyze Intercepted Request in Burp

**Context**: Examine the request for vulnerabilities.

**Instructions**: In Burp's Proxy > Intercept tab, forward the request and note the absence of a CSRF token parameter. Repeater can be used to test variations.

> Expected output: Raw HTTP request showing form data without token validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-update-security-questions]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- recon
- web
