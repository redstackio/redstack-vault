---
tags:
  - xss
  - reflected-xss
  - testing
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.516Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ab2dfa6e-4733-4b0c-8fec-5b39a5b741a4
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-for-Reflected-XSS-in-Error-Parameter

## Summary

This procedure tests the /cloudinary_cors.html endpoint on urbandictionary.com to confirm that the 'error' parameter is reflected into the HTML response without proper encoding, indicating a classic reflected XSS vulnerability.

## Description

After triggering the error redirect, the page inserts the error value directly into the DOM. By modifying the parameter with HTML-breaking characters and script tags, an attacker can verify if JavaScript can be injected and executed. This is a non-destructive reconnaissance step to assess exploitability before crafting payloads.

## Requirements

1. Access to the triggered error URL from the previous step
2. Browser developer tools for inspection
3. Basic knowledge of URL encoding

## Defense

Defensive measures and detection strategies:

- Apply HTML entity encoding to all user inputs reflected in responses
- Use HTTP-only cookies to mitigate session theft
- Monitor for anomalous query parameters in logs

## Objectives

1. Confirm lack of sanitization in error reflection
2. Identify injection points for JavaScript
3. Validate vulnerability without causing harm

## Instructions

### Step 1: Inspect Default Reflection

**Context**: Load the standard error URL and examine how the parameter is used in the page.

Navigate to http://www.urbandictionary.com/cloudinary_cors.html?error=Invalid+image+file and view page source (Ctrl+U in browser).

**Expected Output**: Error text appears unencoded in HTML, e.g., <div>Invalid image file</div>.

### Step 2: Test Basic Injection

**Context**: Append a payload to break out of the HTML context.

Modify the URL to http://www.urbandictionary.com/cloudinary_cors.html?error=Invalid%20image%20file%22%3E%3Cscript%3Ealert(1)%3C/script%3E and load it.

**Expected Output**: Alert box pops up if XSS is confirmed.

### Step 3: Analyze Page Source

**Context**: Verify injection in DOM.

Use browser dev tools (F12) to inspect elements and confirm script insertion.

**Expected Output**: Payload visible in rendered HTML without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[testing]]
