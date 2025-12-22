---
id: proc-acronis-identify-param-001
tags:
  - xss
  - reconnaissance
  - web-testing
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.678Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Vulnerable-URL-Parameter

## Summary

This procedure involves examining a target web application's URL parameters to identify those that reflect user input without proper sanitization, setting the stage for XSS exploitation. In the Acronis case, it targets the 'SFDCCampaignID' parameter on the Cyber Protect trial page.

## Description

In a reflected XSS attack, user-supplied data in URL parameters is echoed back into the HTML response without encoding, allowing script injection. This procedure focuses on reconnaissance of the Acronis trial page (https://www.acronis.com/products/cyber-protect/trial/) to confirm reflection in 'SFDCCampaignID'. Prerequisites include browser developer tools for inspecting responses. Expected outcomes: Identification of injectable points leading to potential data leakage or page manipulation.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public access to the target URL
3. Basic knowledge of URL encoding and HTML inspection

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution
- Sanitize and encode all user inputs in query parameters using HTML entity encoding
- Monitor for anomalous JavaScript in server logs or WAF rules

## Objectives

1. Confirm parameter reflection without sanitization
2. Assess potential for JavaScript injection
3. Map vulnerable endpoints for further testing

## Instructions

### Step 1: Access and Inspect Target URL

**Context**: Load the trial page and examine its query parameters to identify candidates for injection.

Navigate to https://www.acronis.com/products/cyber-protect/trial/ and open developer tools (F12). Append a test value to 'SFDCCampaignID', e.g., ?SFDCCampaignID=test123, then reload and search the page source for 'test123'.

> If the value appears unencoded in HTML attributes or text nodes, it's vulnerable to XSS.

### Step 2: Test for Reflection

**Context**: Verify if inputs are directly reflected, indicating lack of output encoding.

Modify the URL to include special characters, e.g., ?SFDCCampaignID=<script>alert(1)</script>, and check if it breaks HTML or appears as-is in the response.

> Expected: Raw input visible in source, confirming reflection without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Reconnaissance]]
