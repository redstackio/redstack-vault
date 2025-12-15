---
tags:
  - csrf
  - burp-suite
  - poc-generation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Submit-User-Registration-POST]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.135Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 91ad7893-5ff6-4ebc-9362-1e4f98842120
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Generate-CSRF-PoC-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept a legitimate user registration POST request from an ASP.NET form and generate a malicious HTML proof-of-concept (PoC) that can forge the request, enabling CSRF attacks to create unauthorized accounts.

## Description

Burp Suite acts as a proxy to capture the HTTP POST to the registration endpoint, including ASP.NET-specific parameters like __VIEWSTATE and __EVENTVALIDATION. The CSRF PoC generator creates an HTML file with a hidden form that auto-submits the exact request when loaded in a browser. This targets sites without anti-CSRF measures, leading to unauthorized actions. Prerequisites include proxy configuration in the browser and basic knowledge of HTTP requests.

## Requirements

1. Burp Suite installed and running as a proxy (default port 8080)
2. Browser configured to route traffic through Burp (e.g., manual proxy settings)
3. Target registration form prepared with sample data

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens validated on server-side
- Log and alert on proxy-intercepted or anomalous POST requests
- Use certificate pinning to detect proxy usage

## Objectives

1. Capture the full POST request structure for replication
2. Generate a functional CSRF PoC HTML file
3. Verify the PoC replicates the original request parameters

## Instructions

### Step 1: Intercept the Form Submission

**Context**: Submit the prepared form while Burp is intercepting to capture the POST request.

Execute the form submission, which triggers [[commands/Submit-User-Registration-POST]]:

```http
POST /███████ HTTP/1.1
Host: ████████
Content-Type: application/x-www-form-urlencoded

[form data including __VIEWSTATE, user details, etc.]
```

> In Burp, the request will be paused; forward it after inspection. Expected output: Captured request with all headers and body parameters like ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxFirstName=df.

### Step 2: Generate CSRF PoC

**Context**: Use Burp's built-in tool to create the HTML PoC from the intercepted request.

In Burp Repeater or Proxy, right-click the request and select "Engagement tools > Generate CSRF PoC". Save the output HTML.

> The PoC will include <form> with hidden inputs matching the POST data, and JavaScript to auto-submit. Expected output: HTML file ready for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/Submit-User-Registration-POST]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]
