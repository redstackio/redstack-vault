---
id: 54803b0d-eba9-4d68-acd8-dbca1658e952
name: Identifying-Secure-and-HTTPOnly-Flags-On-Cookies
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:01:40.478939+00:00'
updated_at: '2023-05-26T01:22:18.169280+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Cookie Flags]]'
  - '[[tags/HTTPOnly Flag]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Secure Flag]]'
  - '[[tags/Session Management]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Browser-Cookie-Editor-Extension]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Identifying-Secure-and-HTTPOnly-Flags-On-Cookies

## Summary

This procedure uses a browser extension to inspect cookies set by a web application, specifically checking for the presence of Secure and HTTPOnly flags. These flags are critical for protecting session cookies from interception over insecure channels or access via client-side scripts, helping identify potential session management vulnerabilities during web security assessments.

## Description

The Secure flag ensures that cookies are only transmitted over HTTPS connections, preventing exposure on unencrypted HTTP traffic. The HTTPOnly flag prevents client-side JavaScript from accessing the cookie, mitigating risks like XSS-based session hijacking. This procedure is typically used in penetration testing or vulnerability assessments to evaluate session management security in web applications, aligning with OWASP Top 10 categories such as A05:2021 Security Misconfiguration and A07:2021 Identification and Authentication Failures. By identifying missing flags, testers can recommend hardening measures to prevent unauthorized access to sensitive session data.

## Requirements

1. A web browser such as Google Chrome or Mozilla Firefox with extension support.
2. Access to the target web application, including valid login credentials if authentication is required.
3. Installation of a cookie editor browser extension, such as Cookie-Editor.
4. Network access to the target application over HTTP/HTTPS.

## Defense

To mitigate risks from missing cookie flags:
- Always set the Secure flag on sensitive cookies in production environments using HTTPS.
- Implement HTTPOnly for session cookies to block JavaScript access.
- Use tools like browser developer consoles or server-side logging to regularly audit cookie attributes.
- Enforce HTTPS-only traffic via HSTS (HTTP Strict Transport Security) headers.

## Objectives

1. Verify the Secure flag on cookies to ensure transmission only over secure channels.
2. Confirm the HTTPOnly flag to protect against client-side script access.
3. Identify any misconfigured cookies that could lead to session exposure or hijacking.
4. Document findings for remediation in web application security reports.

## Instructions

### Step 1: Install and Configure the Browser Extension

**Context**: Begin by installing a cookie editor extension to enable easy inspection of cookie attributes without relying on developer tools alone. This step ensures you have the necessary tool ready for analysis.

Install the extension from your browser's web store (e.g., Chrome Web Store). Once installed, pin it to the toolbar for quick access. No command is required as this is a GUI-based setup.

> This extension provides a user-friendly interface to view, edit, and analyze all cookies for the current domain, including flags like Secure and HTTPOnly.

### Step 2: Access and Authenticate to the Target Application

**Context**: Log in to the web application to trigger the setting of session cookies, which are the primary focus for flag inspection. This simulates a legitimate user session to observe real cookie behavior.

Navigate to the login page of the target application using your browser. Enter valid credentials and submit the login form. Ensure you are on a page where session cookies are actively used, such as the dashboard.

> Successful login will set cookies visible in the extension. If the application uses multi-factor authentication, complete all steps to establish a full session.

### Step 3: Inspect Cookies Using the Extension

**Context**: Use the extension to list and examine cookies, focusing on Secure and HTTPOnly attributes. This reveals misconfigurations that could expose sessions to man-in-the-middle attacks or XSS exploits.

Click the extension icon in your browser toolbar while on the authenticated page. The extension will display a list of all cookies for the current domain. Select and expand each relevant cookie (e.g., session ID cookies like JSESSIONID or PHPSESSID) to view its attributes.

Look for:
- **Secure**: Should be present (true) for sensitive cookies.
- **HTTPOnly**: Should be present (true) for session cookies.

If flags are missing, note the cookie name, domain, path, and expiration for reporting.

> Example view: A cookie without Secure might show "Secure: false", indicating vulnerability to HTTP interception. Export the cookie list if needed for documentation.

### Step 4: Verify and Document Findings

**Context**: Validate the inspection by cross-checking with browser developer tools and document any issues. This ensures accuracy and provides evidence for security reports.

Open the browser's Developer Tools (F12 or right-click > Inspect), navigate to the Application/Storage tab > Cookies, and compare attributes with the extension's view. Take screenshots or export data to record missing flags.

> Cross-verification confirms the extension's accuracy. If discrepancies arise, rely on Developer Tools as the authoritative source.
