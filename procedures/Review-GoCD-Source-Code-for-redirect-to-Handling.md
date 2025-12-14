---
tags:
  - code-review
  - gocd
  - xss
type: procedure
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
updated_at: '2025-12-13T23:52:49.927Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ae1f332b-688b-437a-b0ff-e01c3de40ca6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Review-GoCD-Source-Code-for-redirect-to-Handling

## Summary

This procedure involves analyzing the GoCD source code, specifically the new.loading.page.html file, to identify improper handling of the 'redirect_to' query parameter in the redirectToLanding function, revealing a reflected XSS vulnerability.

## Description

In a security assessment of GoCD, review the JavaScript code in the loading page to detect the lack of validation for javascript: URIs. The function parses the URL search parameters, decodes the redirect_to value, and assigns it directly to window.location, allowing arbitrary code execution. This is targeted at web applications using Jetty and HTML/JS, with outcomes including vulnerability confirmation for reporting or exploitation planning. Prerequisites include access to the GitHub repository.

## Requirements

1. Internet access to GitHub
2. Basic knowledge of JavaScript and URL parsing
3. Web browser for code inspection

## Defense

Defensive measures and detection strategies:

- Implement input validation to block javascript: schemes in URL parameters
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript execution in loading pages

## Objectives

1. Confirm the presence of unvalidated parameter assignment
2. Document the vulnerable code snippet for reporting
3. Assess potential impact on user sessions

## Instructions

### Step 1: Access the Source Code

**Context**: Locate the relevant file in the GoCD repository to begin analysis.

Navigate to https://github.com/gocd/gocd/blob/0199f22311c83c88ee249a3a71907ce6f58ebd9f/jetty/src/main/resources/loading_pages/new.loading.page.html.

**Expected Output**: View of the HTML file containing embedded JavaScript.

### Step 2: Inspect the redirectToLanding Function

**Context**: Examine lines 397-404 for parameter handling logic.

Search for the redirectToLanding function and verify it uses window.location.search to extract 'redirect_to', decodes it with decodeURIComponent, and assigns to window.location without scheme checks.

**Expected Output**: Identification of the vulnerable code: `var locationData = window.location.search.match(/redirect_to=([^&]*)/); window.location = decodeURIComponent(locationData[1]);`.

### Step 3: Validate Vulnerability

**Context**: Confirm the absence of sanitization.

Check for any regex or blacklist filtering javascript: URIs; note the direct assignment enables XSS.

**Expected Output**: Documentation of the root cause as inadequate validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- gocd
- xss
