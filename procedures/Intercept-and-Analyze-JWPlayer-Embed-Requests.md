---
id: proc-intercept-jwplayer-requests
tags:
  - recon
  - web
  - jwplayer
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:15:31.637Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Intercept-and-Analyze-JWPlayer-Embed-Requests

## Summary

This procedure involves using browser tools to capture and examine HTTP requests to Udemy's video embed endpoints, revealing how JWPlayer 6 parameters are passed without validation, setting the stage for configuration-based exploits.

## Description

In the context of Udemy's course pages, visiting a video overview triggers requests to /embed/video/ endpoints where query parameters like params[vars][playlist][0][image] are directly injected into JWPlayer's JavaScript setup. This reconnaissance step identifies the vulnerability by showing lack of sanitization, enabling subsequent payload crafting. Expected outcomes include a clear understanding of injectable parameters for XSS or redirect attacks, primarily on web platforms using Firefox or Opera.

## Requirements

1. Access to a modern web browser with developer tools (e.g., Firefox Developer Tools)
2. Public access to a Udemy course page, such as https://www.udemy.com/overview-of-big-data-hadoop/
3. No special credentials or network privileges needed

## Defense

Defensive measures and detection strategies:

- Implement request logging at the web server to monitor /embed/video/ accesses
- Use Web Application Firewalls (WAF) to flag unusual parameter lengths or data: URIs in queries
- Educate users on verifying embed sources before interaction

## Objectives

1. Capture the JWPlayer embed request structure
2. Identify unvalidated parameters for exploitation
3. Confirm direct injection into player configuration

## Instructions

### Step 1: Access Udemy Course Page

**Context**: Load a target course page to trigger the embed request.

Navigate to https://www.udemy.com/overview-of-big-data-hadoop/ in your browser.

> This initiates the video embed load, generating the vulnerable request.

### Step 2: Intercept Network Requests

**Context**: Use developer tools to capture and inspect the request.

Open browser developer tools (F12), go to the Network tab, and filter for /embed/video/. Reload the page and select the request to view details like https://www.udemy.com/embed/video/E0IfdVtaQngT/?params[vars][playlist][0][image]=https://dujk9xa5fr1wz.cloudfront.net/course/750x422/211248_71a0_4.jpg&params[trackVideoPlay]=true.

> Examine the Response tab to see JWPlayer setup code incorporating the parameters unsanitized.

### Step 3: Analyze Parameter Injection

**Context**: Verify how parameters reach the JWPlayer configuration.

In the intercepted request, note params[vars] keys and trace them in the page source or JWPlayer init function.

> Success confirms arbitrary config options like logo settings can be set.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- recon
- web
- jwplayer
