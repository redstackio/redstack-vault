---
tags:
  - xss
  - reflected-xss
  - html-injection
  - csp-bypass
  - tumblr
  - firefox
type: attack_chain
tools:
  - '[[tools/Firefox-69]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-JSON-Payload-for-Tumblr-XSS]]'
  - '[[procedures/Authenticate-to-Tumblr-Account]]'
  - '[[procedures/Access-Tumblr-Abuse-Page-with-Payload]]'
  - '[[procedures/Observe-XSS-Execution-in-Firefox]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.198Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in Tumblr's
  abuse reporting page by injecting malicious JSON into the base64-encoded
  'prefill' parameter, leading to JavaScript execution in older Firefox versions
  and HTML injection across browsers.
skill_level: intermediate
impact_level: high
id: c2a2e5a4-d3b9-4aea-a02d-5c17715fa977
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---

# Tumblr Reflected XSS via Base64-Encoded JSON Prefill Parameter

Multi-stage attack chain demonstrating a complete attack workflow exploiting unsanitized user input in Tumblr's abuse reporting form.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Payload] --> B[Authenticate]
    B --> C[Access Abuse Page]
    C --> D[Execute and Observe]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox-69]]

### Target Environment

- Web platform
- Access to Tumblr.com
- No specific ports or services beyond standard HTTPS

### Initial Access Requirements

- Valid Tumblr account credentials
- Network access to https://www.tumblr.com
- Firefox version 69 or below for full JS execution (HTML injection works in any browser)

## Detailed Attack Procedures

### Step 1: Prepare Malicious Payload
procedure: [[procedures/Craft-Malicious-JSON-Payload-for-Tumblr-XSS]]

**Objective**: Create a JSON payload with an XSS vector in the 'tumblelog' field and encode it to base64 for the 'prefill' parameter.

**Instructions**: Construct the JSON object as follows and encode it using [[commands/base64-encode-json]]:

```bash
echo '{"post":null,"urlreporting":"https://fuzzme.tumblr.com/","tumblelog":"<object data=\"javascript:alert(document.cookie)\">","context":"blog"}' | base64
```

**Expected Output**: Base64-encoded string, e.g., eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxvYmplY3QgZGF0YT1cXGphdmFzY3JpcHQ6YWxlcnQoZG9jdW1lbnQuY29va2llKVwiPiIsImNvbnRleHQiOiJibG9nIn0=

**Success Indicators**:
- Valid base64 string generated without encoding errors
- JSON decodes correctly with XSS payload in 'tumblelog'

### Step 2: Authenticate to Tumblr
procedure: [[procedures/Authenticate-to-Tumblr-Account]]

**Objective**: Log in to a Tumblr account to access authenticated features, though the vulnerability is accessible without login in some cases.

**Instructions**: Navigate to the login page and enter credentials manually.

**Expected Output**: Successful login redirect to dashboard.

**Success Indicators**:
- Session cookies established
- Access to /abuse/start page confirmed

### Step 3: Access Vulnerable URL with Payload
procedure: [[procedures/Access-Tumblr-Abuse-Page-with-Payload]]

**Objective**: Inject the base64-encoded payload into the 'prefill' parameter to trigger reflection.

**Instructions**: Append the base64 string to the URL in the browser address bar.

**Expected Output**: Abuse form loads with reflected 'tumblelog' value in HTML.

**Success Indicators**:
- Payload reflected in page source without sanitization
- No errors in URL loading

### Step 4: Observe XSS Execution
procedure: [[procedures/Observe-XSS-Execution-in-Firefox]]

**Objective**: Trigger JavaScript execution in vulnerable browsers or observe HTML injection.

**Instructions**: Load the page in Firefox 69; the <object> tag should execute the javascript: URL. In modern browsers, inspect for HTML rendering like fake inputs.

**Expected Output**: Alert box with document.cookie in Firefox <70; rendered HTML elements in any browser.

**Success Indicators**:
- JS alert fires in older Firefox
- HTML injection visible in dev tools across browsers

## Attack Chain Summary

### Key Achievements

1. Successful payload crafting and encoding
2. Reflection of unsanitized input in abuse form
3. JS execution via CSP bypass in Firefox <70
4. Cross-browser HTML injection for phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
