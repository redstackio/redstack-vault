---
tags:
  - recon
  - web
  - cookies
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
updated_at: '2025-12-14T03:15:04.846Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a2126dd3-e40c-4e80-a46d-8159fab7252c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Cookies During Login Request

## Summary

This procedure involves monitoring HTTP requests to a web login page to identify unusual or potentially injectable cookies, such as 'orange' and 'squeeze' in the Zomato reviews application, serving as the initial reconnaissance step for SQL injection testing.

## Description

In web applications, cookies often carry session or tracking data that may be processed in backend queries without proper sanitization. By observing the login request to https://reviews.zomato.com, attackers can spot oddly named cookies like 'orange' and 'squeeze' that are submitted in POST requests. This step requires intercepting traffic to catalog these values, setting the stage for vulnerability fuzzing. Expected outcomes include identification of cookie names and values, with no exploitation yet, but high potential for follow-on attacks if unsanitized.

## Requirements

1. Access to the target login page (https://reviews.zomato.com)
2. Tool for HTTP interception (e.g., browser dev tools or Burp Suite)
3. Basic understanding of HTTP headers and cookies

## Defense

Defensive measures and detection strategies:

- Implement cookie prefixing (e.g., __Secure-) and HttpOnly flags to limit client-side access
- Log and monitor unusual cookie values or request patterns to login endpoints
- Use web application firewalls (WAFs) to inspect cookie contents for anomalies

## Objectives

1. Catalog all cookies in login requests
2. Identify potentially injectable parameters
3. Establish baseline response behavior (e.g., 302 redirect on failed login)

## Instructions

### Step 1: Access Login Page and Intercept Request

**Context**: Navigate to the login page and capture the outgoing request to examine cookie headers.

Intercept the POST request using a proxy tool. Look for 'Cookie' header containing 'orange' and 'squeeze'.

**Expected Output**: Headers like 'Cookie: orange=value1; squeeze=value2' in request to /login.

### Step 2: Document Baseline Response

**Context**: Submit a normal login attempt to note standard behavior.

Submit valid or invalid credentials and record response: typically HTTP 302 redirect for failed login.

**Expected Output**: Quick response with 302 status and redirect location.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- web
- cookies
