---
id: df05dc11-83a2-4119-b065-4b0c1592f89d
name: Cloudflare-XSS-Bypass-using-SVG-and-Video-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.307711+00:00'
updated_at: '2023-04-10T20:21:48.520105+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - cloudflare
  - waf-bypass
  - svg-injection
  - video-injection
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Cloudflare-XSS-Bypass-using-SVG-and-Video-Injection

## Summary

This procedure demonstrates how to bypass Cloudflare's Web Application Firewall (WAF) XSS protections by injecting malicious payloads embedded in SVG or video elements. The technique exploits gaps in how Cloudflare filters event handlers in non-script contexts, allowing arbitrary JavaScript execution in the victim's browser upon rendering or interaction, such as loading the SVG or hovering over the video.

## Description

Cloudflare's WAF typically blocks common XSS payloads by inspecting for script tags, inline JavaScript, and known event handlers. However, this bypass leverages SVG and video elements, which are less aggressively filtered, to embed onload or onmouseover handlers that trigger JavaScript. For instance, an SVG with an onload event or a video with an onmouseover event can execute code like alert(1) or more malicious actions such as stealing cookies or session tokens. This is effective against reflected or stored XSS vulnerabilities in web applications protected by Cloudflare. The target environment is any web app with user input reflection (e.g., search fields, comments) that renders HTML without proper sanitization. Success results in client-side code execution, enabling data exfiltration, keylogging, or phishing within the victim's session. This technique maps to MITRE ATT&CK [[JavaScript]] for JavaScript execution in a browser context.

## Requirements

1. Access to a vulnerable web application protected by Cloudflare that reflects user input without proper HTML sanitization (e.g., via URL parameters, POST data, or file uploads).
2. Ability to craft and test payloads, potentially using a proxy tool like Burp Suite for interception and modification.
3. Knowledge of the application's input points (e.g., forms, search bars) where SVG or video elements can be injected.
4. A testing environment or victim browser to verify payload execution.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding, sanitizing all user inputs to prevent HTML injection (use libraries like DOMPurify).
- Deploy a robust Content Security Policy (CSP) that blocks inline scripts and restricts executable sources to trusted domains.
- Configure Cloudflare WAF rules to inspect SVG and media elements for suspicious attributes (e.g., onload, onmouseover) and update rules regularly.
- Enable client-side protections like XSS auditors in browsers and monitor for anomalous JavaScript execution via browser developer tools or endpoint detection.
- Regularly audit and patch web applications to address reflection points, and use web vulnerability scanners to identify injection flaws.

## Objectives

1. Bypass Cloudflare's XSS filtering to inject and execute arbitrary JavaScript in the victim's browser.
2. Demonstrate potential for session hijacking, data theft (e.g., cookies, localStorage), or further exploitation like credential harvesting.
3. Validate the vulnerability in a controlled environment to inform remediation.

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a reflected or stored XSS vulnerability in the Cloudflare-protected application where user input is rendered as HTML, such as a search parameter or comment field. Test basic payloads like <script>alert(1)</script> to confirm filtering, then pivot to SVG/video for bypass.

Inspect the application using browser developer tools or a proxy to find unsanitized inputs.

### Step 2: Craft Malicious Payload

**Context**: Create the bypass payload using SVG and video elements with obfuscated event handlers. This embeds JavaScript that executes on load (SVG) or interaction (video hover), evading Cloudflare's signature-based detection.

Reference the payload code: [[codes/SVG-Video-XSS-Bypass-Payload-for-Cloudflare]]

Embed the payload in the injection point, e.g., via a URL like https://vulnerable-site.com/search?q=<svg/onrandom=random onload=confirm(1)><video onnull=null onmouseover=confirm(1)>.

> This step ensures the payload is compact and triggers reliably. The 'onrandom=random' and 'onnull=null' are non-standard attributes that confuse filters while setting up the event.

### Step 3: Inject and Trigger Payload

**Context**: Submit the crafted payload through the identified injection point and observe execution in the victim's browser context.

Use a form submission, URL parameter, or file upload (if applicable) to inject the payload. For video elements, ensure the page allows hover interaction.

If using a proxy, intercept the request, modify the body or parameters with the payload, and forward it.

### Step 4: Verify Execution

**Context**: Confirm the bypass by checking for JavaScript execution, such as a confirm dialog or network requests to an attacker-controlled server.

Load the page with the injected payload in a browser. Look for the alert/confirm box or monitor network traffic for exfiltration attempts.

> Success is indicated by the payload firing without Cloudflare blocking the request. If blocked, iterate on obfuscation (e.g., case variations like OnLoad).

## Expected Output

Upon successful injection and rendering:
- SVG loads and triggers onload, displaying a confirm(1) dialog.
- Video element appears; hovering triggers onmouseover, showing another confirm(1).
- No WAF blocks in Cloudflare logs; JavaScript executes client-side, potentially logging to console or sending data outbound.

Sample browser console output:
```
confirm(1) executed
confirm(1) executed on hover
```
