---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Intercept-HTTP-Requests-to-Reveal-CSRF-Token-in-Cookies
tags:
  - csrf
  - intercept
  - cookies
  - web-security
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:03.666Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Intercept-HTTP-Requests-to-Reveal-CSRF-Token-in-Cookies

## Summary

This procedure involves intercepting HTTP requests to authenticated endpoints in a web application to identify if CSRF tokens are insecurely stored in cookies, violating secure design principles and potentially exposing them to theft via mechanisms like XSS or network attacks.

## Description

In secure web applications, CSRF tokens should be generated per request or session and transmitted via headers or hidden form fields, not stored in cookies, to prevent exposure through cookie-based attacks. This procedure targets edit endpoints (e.g., /~[USER ID]/statement.json) where state-changing POST requests occur. By capturing the request, you can verify if a 'csrf_token' cookie contains the same value as the X-CSRF-Token header, indicating a misconfiguration. If compromised, this allows attackers to forge requests and bypass CSRF protections. The target environment is a web application like Gratipay, requiring authenticated access.

## Requirements

1. Valid user account and session in the target web application
2. Access to a state-changing endpoint (e.g., edit statement feature)
3. Web proxy or browser developer tools for request interception
4. Basic knowledge of HTTP requests and cookies

## Defense

Defensive measures and detection strategies:

- Store CSRF tokens in session storage or headers only, not cookies
- Implement HttpOnly and Secure flags on session cookies, but avoid for CSRF tokens
- Monitor for anomalous request patterns or token reuse via WAF
- Regularly audit web app configurations for secure token handling

## Objectives

1. Discover if CSRF tokens are stored in cookies
2. Assess potential for token exposure and CSRF bypass
3. Recommend secure alternatives like token isolation to account changes

## Instructions

### Step 1: Authenticate and Navigate to Endpoint

**Context**: Establish a session and prepare to trigger a state-changing request to capture the CSRF token.

Log in to the web application and navigate to the feature that involves editing user data, such as updating a statement.

**Expected Output**: Authenticated session with access to the edit form.

### Step 2: Intercept the POST Request

**Context**: Use a proxy tool to capture the outgoing POST request, revealing cookie and header details.

Configure your browser's developer tools (Network tab) or a proxy like Burp Suite to intercept traffic. Submit the edit form to trigger a POST to /~[USER ID]/statement.json. Examine the request:

- Look for the 'csrf_token' cookie in the Cookie header.
- Compare its value to the X-CSRF-Token request header.

Example request structure (inferred from capture):

```http
POST /~[USER ID]/statement.json HTTP/1.1
Host: target.com
Cookie: csrf_token=y44PyqG67bRQljEA5mLK1bez4hgZ8XSD; session_id=abc123
X-CSRF-Token: y44PyqG67bRQljEA5mLK1bez4hgZ8XSD
Content-Type: application/json

{"statement": "updated content"}
```

> If the cookie value matches the header, it confirms insecure storage. This exposure risks token theft if cookies are compromised (e.g., via XSS stealing document.cookie).

**Expected Output**: Matched token values in cookie and header, indicating violation.

### Step 3: Validate Impact

**Context**: Assess the risk by considering secondary attack vectors like XSS.

Review if the application uses the token for CSRF protection. Test if stolen token allows forging a similar POST request using tools like curl (replace with actual values):

```bash
curl -X POST https://target.com/~[USER ID]/statement.json \
  -H "Cookie: csrf_token=STOLEN_TOKEN" \
  -H "X-CSRF-Token: STOLEN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"statement": "forged content"}'
```

> Success would show the request processed without additional validation, bypassing CSRF.

**Expected Output**: Confirmation of potential forgery if token is reused.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- intercept
- cookies
- web-security
