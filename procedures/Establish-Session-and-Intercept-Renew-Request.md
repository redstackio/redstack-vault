---
tags:
  - session-hijack
  - web-proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:18.053Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2a8f579d-3177-4f22-8140-cdbff869d27b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Establish-Session-and-Intercept-Renew-Request

## Summary

This procedure establishes a valid session on Algolia.com and intercepts the HTTP request for renewing support access using a web proxy, setting the stage for capturing sensitive API responses.

## Description

In the context of exploiting an information disclosure vulnerability, an attacker with initial session access (via valid credentials or stolen cookies) logs into the target account, navigates to the support page, and uses a tool like Burp Suite to intercept the 'Renew' action. This allows manipulation and inspection of the API traffic without alerting the application. Prerequisites include a configured proxy and browser traffic routing. Expected outcomes include a captured request ready for replay, enabling secret extraction in subsequent steps.

## Requirements

1. Valid Algolia account credentials or session cookies
2. Burp Suite installed and running with Proxy listener on port 8080
3. Browser configured to route traffic through the proxy (e.g., FoxyProxy extension)

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to block proxy interception
- Monitor for anomalous proxy traffic patterns or unusual User-Agent strings from tools like Burp
- Enforce short session timeouts and require re-authentication for sensitive pages

## Objectives

1. Obtain and maintain a valid session for the target account
2. Intercept the support access renewal request without disrupting the flow
3. Prepare for response analysis to identify leaked data

## Instructions

### Step 1: Login to Algolia

**Context**: Authenticate to create an active session, ensuring all subsequent requests carry valid cookies.

No specific command; use browser to visit https://www.algolia.com, enter credentials, and submit the login form. Verify dashboard access.

> Successful login results in a redirect and session establishment. Check Burp Proxy history for the login request and response cookies.

### Step 2: Navigate to Support Page

**Context**: Reach the endpoint hosting the vulnerable renew action.

No specific command; from the dashboard, select account settings and click to load https://www.algolia.com/account/support. Confirm the page loads with the Renew button.

> Page load confirms session validity. Look for GET request in Burp history targeting the support URL.

### Step 3: Trigger and Intercept Renew

**Context**: Initiate the API call and capture it for inspection.

No specific command; click the 'Renew' button. In Burp Suite Proxy, set to intercept and capture the outgoing POST request (likely to an endpoint like /api/support/renew).

> Intercepted request shows headers with session cookies and body with renew parameters. Do not drop; forward to proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-hijack
- web-proxy
