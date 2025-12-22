---
id: 8c6a455a-e342-4dc2-abc2-c79de163bfa0
name: SSRF-Image-Upload-Bypass-Using-Type-URL
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.692217+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/bypass-filters]]'
  - '[[tags/type-url-bypass]]'
  - '[[tags/ssrf]]'
commands:
  - '[[commands/change-file-input-type-to-url]]'
  - '[[commands/set-url-input-value-and-trigger-change]]'
platforms:
  - Web
tools: []
validated: true
---

# SSRF-Image-Upload-Bypass-Using-Type-URL

## Summary

This procedure demonstrates how to bypass client-side filters on an image upload feature by modifying the HTML input type from 'file' to 'url' using JavaScript, enabling the upload of images from arbitrary URLs. This triggers a Server-Side Request Forgery (SSRF) attack, allowing the server to fetch resources from internal or restricted endpoints on behalf of the attacker.

## Description

In web applications with image upload functionality, client-side restrictions often limit uploads to local files via <input type="file"> elements. By injecting JavaScript (e.g., via browser console or XSS) to change the input type to 'url', attackers can input a remote URL instead. When submitted, the server processes this as a URL-based upload, making an HTTP request to the specified location. This can be abused for SSRF to access internal services like metadata endpoints (e.g., http://169.254.169.254 in AWS), perform port scanning, or exfiltrate data. The technique relies on the server trusting URL inputs without sufficient validation, common in legacy or misconfigured upload handlers. It targets web applications vulnerable to client-side manipulation and server-side request handling flaws, typically in environments like e-commerce sites or content management systems with user-generated content features.

## Requirements

1. Access to the web application's image upload interface (authenticated or public).
2. Ability to execute JavaScript in the browser context (e.g., via developer console, XSS payload, or extension).
3. Knowledge of target internal endpoints for SSRF exploitation (e.g., localhost services or cloud metadata URLs).
4. A controlled server or URL hosting the malicious image/resource to trigger the request.

## Defense

- Implement server-side validation to restrict allowed URL schemes, domains, and protocols (e.g., only https://trusted-cdn.com/*).
- Use network segmentation and firewalls to block outbound requests from application servers to internal IPs or metadata services.
- Disable or sandbox client-side JavaScript execution where possible, and employ Content Security Policy (CSP) to prevent DOM manipulation.
- Monitor application logs and network traffic for anomalous outbound requests from the web server.

## Objectives

1. Bypass client-side file upload restrictions to enable URL-based image sourcing.
2. Trigger SSRF to make unauthorized requests to internal or restricted resources.
3. Access sensitive data or perform reconnaissance on internal infrastructure.

## Instructions

### Step 1: Modify Input Type to URL

**Context**: Locate the file input element for image upload and change its type attribute to 'url' using JavaScript. This alters the client-side behavior to accept text URLs instead of file selections, bypassing the file picker restriction.

**Command** ([[commands/change-file-input-type-to-url]]):
```javascript
document.querySelector('input[type=file]').type = 'url';
```

> This command targets the first <input type="file"> element and sets its type to 'url', transforming it into a text input for URLs. Expected output: The input field changes visually to a text box; no console errors if the selector matches.

### Step 2: Set Malicious URL and Trigger Upload

**Context**: Enter a crafted URL pointing to an internal or restricted resource (e.g., an image hosted on localhost or cloud metadata) into the now-modified input field, then simulate the upload event to submit the form. This causes the server to fetch the URL, executing the SSRF.

**Command** ([[commands/set-url-input-value-and-trigger-change]]):
```javascript
document.querySelector('input[type=url]').value = 'http://169.254.169.254/latest/meta-data/'; // Replace with target internal URL
document.querySelector('input[type=url]').dispatchEvent(new Event('change'));
```

> This sets the value of the URL input to the desired endpoint and dispatches a 'change' event to mimic user interaction, triggering form validation and submission. Expected output: The form submits, and the server responds with the fetched resource (e.g., metadata JSON) or an error indicating SSRF success/failure; check network tab for the outbound request.
