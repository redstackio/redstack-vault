---
tags:
  - access-bypass
  - redirect-manipulation
  - web-vulnerability
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b312775a-9318-46b0-8eed-5c523705551b
created_at: '2025-12-14T17:30:07.404Z'
updated_at: '2025-12-14T17:30:07.404Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-HTTP-Redirects-with-Burp-Suite

## Summary

This procedure exploits improper access controls in web applications that include target content in 302 redirect responses without authentication checks, allowing attackers to bypass redirects by modifying the HTTP status code to 200 OK using Burp Suite, leading to unauthorized access to protected resources.

## Description

The attack targets web applications like speakerkit.state.gov where login attempts trigger 302 redirects to protected pages (e.g., admin areas), but the server erroneously includes the full target content in the response body. By intercepting the response with Burp Suite and changing the status to 200 OK, the client ignores the redirect and directly accesses the content. This enables viewing sensitive data such as admin passwords and performing actions like file uploads. Prerequisites include a valid user login to trigger the flow and Burp Suite configured as a proxy.

## Requirements

1. Burp Suite installed and running with proxy listener on localhost:8080
2. Browser configured to use Burp proxy (e.g., via FoxyProxy extension)
3. Valid credentials for initial login to the target application
4. Network access to the target web application (HTTPS)

## Defense

Defensive measures and detection strategies:

- Implement proper redirect handling: Do not include target content in 302 response bodies; use 3xx without body or enforce auth on target
- Server-side access controls: Validate authentication on all endpoints, regardless of redirect
- WAF rules to detect status code tampering in proxied requests
- Log and monitor anomalous 200 responses to protected paths

## Objectives

1. Bypass authentication to access admin pages
2. Exfiltrate sensitive user and admin data including passwords
3. Execute administrative functions such as file uploads and category management

## Instructions

### Step 1: Configure Burp Suite and Login

**Context**: Set up interception and trigger the vulnerable redirect flow.

Configure your browser to proxy through Burp Suite. Navigate to https://speakerkit.state.gov/ and log in with valid credentials. This redirects to the 'spklogin' page, generating a 302 response.

Intercept the response in Burp's Proxy tab.

**Expected Output**: 302 Found response with target page content in the body.

### Step 2: Modify the Response Status Code

**Context**: Use Burp's find-and-replace to alter the status, bypassing the redirect.

In Burp Suite, go to Proxy > Options > Match and Replace. Add a rule: Match 'HTTP/1.1 302 Found' and replace with 'HTTP/1.1 200 OK'. Enable the rule and forward the response.

Alternatively, use the Repeater tab: Paste the intercepted request, send it, then edit the response status manually to 200 OK and forward.

**Expected Output**: Browser loads the target page (e.g., admin dashboard) directly.

### Step 3: Exploit Accessed Functionality

**Context**: Leverage the bypass to interact with unauthorized features.

Navigate to admin endpoints (e.g., by modifying URLs or following links). View user lists to see passwords. Attempt actions like uploading a test file or adding a category.

**Expected Output**: Successful data viewing and action execution without further auth prompts.

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

- access-bypass
- redirect-manipulation
- authentication-bypass
