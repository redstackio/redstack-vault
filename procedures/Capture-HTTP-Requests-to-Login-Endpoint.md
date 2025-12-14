---
tags:
  - http-capture
  - network-analysis
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
updated_at: '2025-12-14T17:27:15.758Z'
sub_techniques: []
id: 26ddb82b-717b-4b7f-b400-f67fcd542acc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-HTTP-Requests-to-Login-Endpoint

## Summary

This procedure captures and analyzes HTTP requests to a web login endpoint using browser tools, revealing request headers and form data to support CSRF vulnerability assessment.

## Description

Capturing network traffic helps understand how login forms interact with the server, confirming reliance on session cookies without CSRF validation. Targeted at web platforms like IRCCloud, this manual process uses browser DevTools. Prerequisites: Browser access. Outcomes: Detailed request logs for PoC crafting, highlighting no-cache and referer headers.

## Requirements

1. Web browser with Network tab in DevTools
2. Target URL accessible (e.g., https://www.irccloud.com/)
3. No proxy setup required for basic capture

## Defense

Defensive measures and detection strategies:

- Enforce strict referer policies
- Log and alert on requests from untrusted origins
- Use Content Security Policy (CSP) to restrict frames and scripts

## Objectives

1. Record initial GET request to the login page
2. Note headers indicating potential CSRF weaknesses
3. Validate form submission path for exploitation

## Instructions

### Step 1: Prepare Network Monitoring

**Context**: Enable request logging before accessing the page.

Open DevTools (F12), go to the Network tab, and clear any existing logs. Ensure "Preserve log" is checked.

### Step 2: Load the Target Page

**Context**: Trigger the request to capture initial traffic.

Enter https://www.irccloud.com/ in the address bar and press Enter. Filter for the root domain request.

### Step 3: Analyze Captured Request

**Context**: Review details to confirm structure.

Click on the GET request to /. Examine headers: Pragma: no-cache, Cache-Control: no-cache, Referer: http://www.irccloud.com/, Host: www.irccloud.com, User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36, Accept: */*.

**Expected Output**: Request details showing no CSRF-related headers or tokens in response.

> Headers indicate standard browser behavior without additional security layers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[http-capture]]
- [[network-analysis]]
