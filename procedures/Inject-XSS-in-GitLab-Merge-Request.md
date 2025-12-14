---
tags:
  - xss
  - stored-xss
  - injection
  - gitlab
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:09.121Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 058bd2fc-5356-429f-b814-98ef68c65ec5
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Inject-XSS-in-GitLab-Merge-Request

## Summary

This procedure exploits a Stored XSS vulnerability in GitLab by intercepting the merge request creation HTTP request and injecting a malicious JavaScript payload into the 'merge_request[source_branch]' parameter, resulting in arbitrary code execution when the merge request page is viewed by other users.

## Description

The attack targets the lack of sanitization in the source_branch parameter during merge request rendering. After setting up the project and branch, the procedure navigates to create a merge request, intercepts the POST request using a web proxy, modifies the parameter with a payload like '<img/src=x onerror=alert(1)>', and forwards it. This stores the XSS, executing JavaScript in viewers' browsers for potential session hijacking or data exfiltration. Prerequisites include the project/branch from the setup procedure and proxy configuration. Outcomes include payload persistence and execution confirmation via alert on page view.

## Requirements

1. Existing GitLab project and branch (from setup procedure)
2. Web proxy tool like [[tools/Burp-Suite]] configured to intercept traffic
3. Authenticated session with merge request permissions
4. Knowledge of HTTP request manipulation

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping for all user-controlled parameters in merge requests
- Deploy Content Security Policy (CSP) to restrict inline script execution
- Log and monitor proxy-intercepted requests or unusual parameter values in WAF logs
- Regularly audit merge request pages for anomalous content

## Objectives

1. Intercept and tamper with the merge request submission to inject XSS
2. Store the payload for persistent execution on page views
3. Achieve client-side JavaScript execution leading to data compromise

## Instructions

### Step 1: Navigate to Merge Requests and Initiate Creation

**Context**: Set up the merge request workflow to trigger the interceptable request.

No specific command; use GitLab UI:

- Go to project merge requests page
- Click 'Create merge request'
- Fill basic details if prompted
- Click 'Submit merge request'

> This generates the POST request; ensure proxy is active to capture it.

### Step 2: Intercept and Modify the Request

**Context**: Capture the request and inject the payload into the vulnerable parameter.

Using [[tools/Burp-Suite]]:

- Configure browser proxy to route through Burp
- Intercept the POST to the merge request endpoint
- Locate 'merge_request[source_branch]' in the body
- Replace its value with '<img/src=x onerror=alert(1)>'

> Modified request shows the payload; verify no syntax errors in the body.

### Step 3: Forward and Verify Exploitation

**Context**: Submit the tampered request and confirm XSS execution.

Using [[tools/Burp-Suite]]:

- Click 'Forward' to send the request to GitLab
- Navigate to the created merge request page
- Observe the alert(1) popup on load

> Merge request is created; viewing the page executes the JS, confirming Stored XSS success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[injection]]
- [[web-exploitation]]
