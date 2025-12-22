---
id: 1ce2b1f8-171d-4c69-991a-a2334a7a3825
name: Inject-XSS-via-SVG-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.062189+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - svg-injection
  - cross-site-scripting
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Inject-XSS-via-SVG-Files

## Summary

This procedure demonstrates how to inject malicious JavaScript code into Scalable Vector Graphics (SVG) files to execute cross-site scripting (XSS) attacks when the file is rendered by a victim's browser. It targets web applications that allow user-uploaded SVG files without proper sanitization, enabling theft of session cookies, tokens, or other sensitive data.

## Description

SVG files, being XML-based, can embed executable JavaScript through attributes like 'onload' or CDATA sections within elements such as <desc>, <foreignObject>, or <title>. When a vulnerable web application serves or displays these files without stripping script tags or encoding special characters, the embedded JavaScript executes in the context of the hosting page. This technique is effective against sites using SVG for icons, charts, or images, as browsers parse and render SVG natively. The attack requires an upload point for SVG files and a way to lure victims into viewing the malicious file, such as via email or a shared link. Successful execution can lead to session hijacking, keylogging, or further exploitation like phishing redirects.

## Requirements

1. Access to a web application with an SVG file upload feature that lacks proper content sanitization (e.g., no script tag filtering or attribute escaping).
2. Knowledge of the target's domain or session context to craft payloads that interact with the page (e.g., document.domain for same-origin checks).
3. A method to deliver the malicious SVG to victims, such as social engineering or an existing account on the platform.
4. Optional: A proxy tool like [[tools/Burp-Suite]] to intercept and modify upload requests for testing.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding for uploaded files, disallowing or sanitizing SVG attributes like 'onload' and CDATA sections.
- Use Content Security Policy (CSP) headers to block inline scripts and restrict script sources (e.g., 'script-src 'self'').
- Scan uploads with antivirus or specialized tools to detect embedded JavaScript in non-script files.
- Serve user-uploaded SVGs with a 'Content-Type: image/svg+xml' but add 'X-Content-Type-Options: nosniff' to prevent MIME-type confusion.
- Monitor for anomalous JavaScript execution in image contexts via browser logs or web application firewalls (WAFs).

## Objectives

1. Craft and inject a malicious SVG file containing executable JavaScript.
2. Upload the SVG to a vulnerable application and ensure it is rendered by the victim's browser.
3. Execute the payload to steal sensitive information like cookies or perform actions on the victim's behalf.

## Instructions

### Step 1: Craft Malicious SVG Payload

**Context**: Create an SVG file embedding JavaScript that will execute upon loading, such as alerting the domain or exfiltrating data. Use variations to bypass basic filters.

Embed the payload using [[codes/SVG-XSS-Injection-Payloads]]:

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>

<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>
<svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>
<svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>
```

> Save this as a .svg file (e.g., malicious.svg). Test locally by opening in a browser to verify execution without errors. The 'onload' variant triggers on render, while CDATA methods hide scripts in descriptive elements.

### Step 2: Upload SVG to Vulnerable Application

**Context**: Locate an upload endpoint (e.g., profile image or document upload) and submit the crafted SVG. Ensure the application stores and serves the file without modification.

Use browser developer tools or a proxy to submit the file:

1. Navigate to the upload form.
2. Select the malicious.svg file.
3. Submit and note the response URL where the file is hosted.

> If the upload succeeds, the server should return a success message or the file's display path. Verify by accessing the uploaded file directly in the browser.

### Step 3: Lure Victim and Verify Execution

**Context**: Trick the victim into viewing the uploaded SVG, such as by sending a link disguised as a legitimate image or document.

1. Share the URL to the uploaded SVG (e.g., via email or chat).
2. Observe if the payload executes (e.g., alert pops or data is sent to your server).
3. For data exfiltration, modify the payload to send document.cookie to an attacker-controlled endpoint.

> Success is indicated by the JavaScript running in the victim's session context, confirmed by received data or observed actions like redirects.
