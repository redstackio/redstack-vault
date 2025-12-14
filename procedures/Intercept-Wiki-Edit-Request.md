---
tags:
  - intercept
  - http-proxy
  - gitlab
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.724Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 80fa6794-1659-4b2f-ad18-0ac85487c152
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-Wiki-Edit-Request

## Summary

This procedure uses a web proxy to capture the HTTP POST request during Wiki page editing in GitLab, enabling inspection and modification of the 'content' parameter for vulnerability exploitation.

## Description

In the attack scenario, editing a Project Wiki page sends a POST to the /wikis endpoint with Markdown content. Intercepting this allows replacement of the content with a malicious payload. This targets GitLab 10.0's parser, where filters can be bypassed, leading to stored XSS upon save and view.

## Requirements

1. Running GitLab instance with Wiki access
2. Burp Suite configured as proxy (browser traffic routed through it)
3. Authenticated session in GitLab

## Defense

Defensive measures and detection strategies:

- Proxy traffic inspection at network edges to detect interception tools
- Rate-limit Wiki edit requests to prevent tampering attempts
- Log all POST requests to /wikis for anomaly detection in content length or encoding

## Objectives

1. Capture the save request for the Wiki content
2. Identify the modifiable 'content' parameter
3. Position for payload injection without alerting the application

## Instructions

### Step 1: Configure Proxy

**Context**: Route browser traffic through Burp Suite to intercept GitLab requests.

Launch Burp Suite, set it as the system's web proxy (e.g., 127.0.0.1:8080), and configure the browser to use this proxy. Ensure HTTPS interception is enabled if needed.

### Step 2: Trigger Edit and Intercept

**Context**: Perform a Wiki edit to generate the target request.

In GitLab, go to Project Wiki, edit the homepage or create a new page, enter generic text like 'Test content', and click 'Save Changes'. In Burp's Proxy > Intercept tab, the POST request to /projects/:id/wikis should appear paused.

**Expected Output**: Intercepted request showing form-data with 'content' parameter containing the test text.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[http-proxy]]
- [[gitlab]]
