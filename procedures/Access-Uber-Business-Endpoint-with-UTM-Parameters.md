---
id: proc-uber-access-utm-001
tags:
  - recon
  - web
  - utm
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:19.836Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access Uber Business Endpoint with UTM Parameters

## Summary

This procedure involves navigating to the Uber getrush.uber.com/business endpoint using standard UTM tracking parameters to observe how they are handled and rendered in the page's client-side JavaScript, setting the stage for identifying injection points.

## Description

In a reflected XSS attack scenario, the initial step is to access the target web application with benign parameters to understand the reflection mechanism. Here, the endpoint inserts UTM values (e.g., utm_campaign) directly into a JavaScript object without escaping, making it vulnerable to string breakout attacks. This is typically done in a browser to inspect the page source and confirm the insertion pattern, such as `window.utm = {campaign: 'value', medium: 'top', source: 'website'};`. No authentication is required, and the target is a public-facing web page.

## Requirements

1. Web browser (e.g., Firefox or Chrome) with developer tools enabled
2. Internet access to reach https://getrush.uber.com/business
3. Basic knowledge of URL construction and page inspection

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline script execution
- Log and monitor unusual UTM parameter values for anomalies
- Use web application firewall (WAF) rules to detect script tag injections in query parameters

## Objectives

1. Confirm accessibility of the business endpoint
2. Identify reflection of UTM parameters in JavaScript
3. Gather baseline for payload crafting

## Instructions

### Step 1: Construct and Load Base URL

**Context**: Build the URL with standard UTM parameters to mimic legitimate tracking traffic and load it in the browser.

No specific command; manually enter or bookmark the URL: https://getrush.uber.com/business?utm_campaign=somevalue&utm_medium=top&utm_source=website

> Load the page and open developer tools (F12) to inspect the HTML source, locating the <script> tag containing the window.utm object. Verify the parameters are inserted as string literals.

### Step 2: Inspect Rendered JavaScript

**Context**: Examine how parameters are embedded to confirm lack of escaping.

Use browser dev tools to search for 'utm_campaign' in the source.

> Expected: Unescaped string insertion like campaign: 'somevalue'. This indicates potential for XSS if quotes can be closed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[recon]]
- [[web]]
