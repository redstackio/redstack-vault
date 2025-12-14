---
id: proc-002
tags:
  - xss
  - stored-xss
  - payload-injection
  - proxy-intercept
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
updated_at: '2025-12-13T23:52:24.096Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-and-Inject-XSS-Payload-in-Home-Page-URL

## Summary

This procedure details intercepting the application save request in the Ping Identity console using a proxy tool and injecting a stored XSS payload into the Home Page URL field, leading to script execution when victims view or edit the application.

## Description

Stored XSS vulnerabilities occur when user input, like URLs, is stored without sanitization and rendered unsafely in views. In PingOne's Connections module, the Home Page URL is echoed back in the Application List edit view without proper encoding, allowing JavaScript injection. The attacker uses a proxy to modify the request body. Upon save, the payload persists; when an admin or user clicks the edit icon, the script executes in their context, potentially stealing sessions or data. This targets JavaScript-capable browsers in web environments.

## Requirements

1. Active proxy session (e.g., Burp Suite) intercepting browser traffic to the console.
2. Existing application from prior setup with access to edit Home Page URL field.
3. Knowledge of XSS payloads that bypass any basic filters (e.g., SVG-based onload).

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs on storage and output (e.g., use HTML entity encoding for URLs).
- Implement Content Security Policy (CSP) to restrict inline scripts and SVG execution.
- Log and alert on proxy-detected request modifications or anomalous URL patterns in application saves.

## Objectives

1. Capture the save request for the Home Page URL parameter.
2. Inject a functional XSS payload without breaking the request.
3. Store the payload to trigger on victim interaction.
4. Achieve JavaScript execution for data access or actions as the victim.

## Instructions

### Step 1: Enter and Intercept URL

**Context**: Add a placeholder URL to trigger the savable request for interception.

No specific command; in the app edit view, enter "https://example.com" in Home Page URL and click Save. Proxy should intercept the request (likely POST to /applications endpoint).

> Expected output: Request paused in proxy with URL parameter visible in body (e.g., JSON or form data: {"homePageUrl": "https://example.com"}).

### Step 2: Modify with XSS Payload

**Context**: Replace the URL to include executable script, ensuring it renders in the victim's view.

No specific command; in the proxy editor, change the parameter to "https://0-a.nl/ <svg/onload=alert(document.domain)>" (note space before SVG to evade simple filters). Forward the request.

> Expected output: Server accepts and saves; no error response (200 OK).

### Step 3: Verify Trigger

**Context**: Test execution by simulating victim view/edit in another session or browser.

No specific command; log out/in or use incognito; go to Application List, click edit pencil on the app.

> Expected output: Alert box pops up showing document.domain (e.g., console-staging.pingone.com), confirming XSS.

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

- [[xss]]
- [[payload-injection]]
