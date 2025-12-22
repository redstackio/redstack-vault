---
id: proc-uuid-123
tags:
  - xss
  - stored-xss
  - javascript-injection
  - api-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:20.596Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-JavaScript-Link-in-Infogram-Text-Object

## Summary

This procedure exploits a stored XSS vulnerability in Infogram's infographic text objects by intercepting and modifying the API request used to save hyperlinks, replacing a legitimate URL with a javascript: scheme that executes arbitrary code when clicked by viewers of the public infographic.

## Description

Infogram allows users to embed links in text objects within infographics, but the server-side API at https://infogram.com/api/infographics/update/[project_id] fails to validate URL schemes, permitting javascript: payloads to be stored. When the infographic is published and viewed, clicking the link triggers client-side execution, potentially leading to session cookie theft, keylogging, or phishing. This targets web browsers and requires an authenticated Infogram account. Prerequisites include proxy setup for request interception. Expected outcomes: Payload persistence and execution confirmation via alert or console logs.

## Requirements

1. Valid Infogram user account with permissions to create and publish infographics.
2. Browser configured to proxy through a web debugger like Burp Suite.
3. Internet access to infogram.com API endpoints.
4. Basic knowledge of HTTP request manipulation and JSON payloads.

## Defense

Defensive measures and detection strategies:

- Implement server-side URL validation to whitelist only http/https schemes and reject javascript: or data:.
- Apply Content Security Policy (CSP) headers to block inline JavaScript execution on infographic pages.
- Sanitize stored links client-side before rendering, using libraries like DOMPurify.
- Monitor API logs for suspicious URL patterns in update requests and rate-limit link insertions.

## Objectives

1. Inject and store a malicious javascript: URL in an infographic text object.
2. Publish the infographic to enable victim interaction.
3. Achieve JavaScript execution in the viewer's browser for data exfiltration or hijacking.
4. Validate the vulnerability without alerting the target.

## Instructions

### Step 1: Create and Prepare Infographic

**Context**: Set up the attack vector by creating a new project and adding a text element.

Log in to Infogram, create a new infographic, and add a text object. Highlight text and prepare to insert a link (e.g., http://google.com) to observe the API behavior.

### Step 2: Intercept API Request with Web Debugger

**Context**: Capture the link-saving request to enable payload modification.

Configure [[tools/Burp-Suite]] as a proxy, enable interception for infogram.com. Insert the benign link to trigger the POST to /api/infographics/update/[project_id].

### Step 3: Modify and Forward Payload

**Context**: Replace the URL with the XSS payload to bypass validation.

In the intercepted request, edit the JSON body: change the link field to "javascript:alert(document.domain)". Inspect the response for success (200 OK) and forward.

### Step 4: Publish and Test Exploitation

**Context**: Make the payload accessible and verify execution.

Save the infographic, set to public, and access the URL. Click the link to trigger the alert, confirming stored XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[stored-xss]]
- [[web-exploitation]]
