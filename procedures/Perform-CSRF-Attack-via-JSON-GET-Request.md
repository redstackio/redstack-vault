---
id: a280e457-aea4-4acd-b8c6-58d670277724
name: Perform-CSRF-Attack-via-JSON-GET-Request
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:56.211481+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Cross-Site Request Forgery]]'
  - '[[tags/JSON GET - Simple Request]]'
  - '[[tags/Payloads]]'
commands:
  - '[[commands/serve-malicious-html-page]]'
platforms:
  - Web
tools: []
validated: true
---

# Perform-CSRF-Attack-via-JSON-GET-Request

## Summary

This procedure demonstrates how to execute a Cross-Site Request Forgery (CSRF) attack using a JSON GET request to exploit an authenticated victim's session. By crafting a malicious web page that triggers an unauthorized GET request to a vulnerable JSON API endpoint, the attacker can steal sensitive data such as user profile information without the victim's knowledge, provided the victim is logged into the target site and visits the attacker's page.

## Description

CSRF attacks exploit the trust a web application has in a user's browser by forcing the browser to send authenticated requests to a target site without user consent. In this variant, the attack targets JSON API endpoints that use GET requests for data retrieval, which are particularly vulnerable if they rely solely on session cookies for authentication without additional CSRF protections like tokens or SameSite attributes. The malicious page uses JavaScript (via XMLHttpRequest) to make the request, capturing the response containing sensitive JSON data (e.g., user details). This technique is effective against legacy or misconfigured web applications and can lead to data theft or unauthorized actions. The attack assumes the victim is already authenticated, making it a post-initial-access escalation. Target environments include any web application with JSON APIs lacking CSRF mitigations, such as older e-commerce sites or internal dashboards.

## Requirements

1. The victim must be authenticated (logged in) to the target website via their browser session.
2. The target JSON API endpoint must accept GET requests authenticated only by session cookies (no CSRF tokens required).
3. Access to a web server to host the malicious HTML page (e.g., attacker-controlled domain).
4. Knowledge of the vulnerable API endpoint URL (e.g., /api/currentuser).

## Defense

Defensive measures and detection strategies:

- Implement SameSite=Strict or SameSite=Lax cookies to prevent cross-site requests from including authentication cookies.
- Use anti-CSRF tokens in all state-changing or data-retrieving requests, validated server-side.
- Enforce Content Security Policy (CSP) to restrict script execution and XMLHttpRequest origins.
- Monitor for anomalous requests from unexpected referers or user-agents.
- Rate limit API endpoints to detect and block rapid or suspicious access patterns.

## Objectives

1. Steal sensitive user data (e.g., profile information, tokens) from the JSON API response.
2. Perform unauthorized data retrieval on behalf of the victim using their session.
3. Use the exfiltrated data for further attacks, such as account takeover or phishing escalation.

## Instructions

### Step 1: Identify the Vulnerable JSON API Endpoint

**Context**: Determine the target endpoint that returns sensitive JSON data via GET when authenticated. This can be found through reconnaissance, such as browsing the application or reviewing API documentation. Ensure the endpoint does not require CSRF tokens.

**Why**: Confirming the endpoint allows crafting the precise request URL for the malicious script.

No specific command needed here; use browser developer tools or [[commands/curl-basic-get]] (if testing manually) to verify the endpoint returns data when authenticated.

**Expected Output**: JSON response with sensitive data, e.g., {"user_id": 123, "email": "victim@example.com"}.

### Step 2: Craft the Malicious HTML Page

**Context**: Create an HTML file embedding the JavaScript payload that will trigger the CSRF request. Reference the code snippet [[codes/CSRF-JSON-GET-Request-Payload]] for the exact script.

**Why**: The script uses XMLHttpRequest to send the GET request from the victim's browser, leveraging their session cookies.

Save the following as malicious.html (using the preserved code from [[codes/CSRF-JSON-GET-Request-Payload]]):

```html
<script>
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.example.com/api/currentuser");
xhr.send();
</script>
```

Replace "http://www.example.com/api/currentuser" with the actual target URL.

**Expected Output**: The file is ready for hosting; no immediate output.

### Step 3: Host the Malicious Page

**Context**: Serve the HTML file from an attacker-controlled server to lure the victim into visiting it while logged into the target site.

**Why**: The victim must load the page in their browser for the script to execute in the context of their session.

**Command** ([[commands/serve-malicious-html-page]]):

```bash
python3 -m http.server 8000
```

Navigate to http://attacker-ip:8000/malicious.html in the victim's browser (e.g., via phishing link).

> This starts a simple HTTP server in the directory containing malicious.html. The script executes automatically upon page load, sending the request to the target API.

**Expected Output**: Server logs show a GET request for /malicious.html from the victim's IP.

### Step 4: Capture and Verify the Exfiltrated Data

**Context**: Monitor the response from the API request. In this basic implementation, the response is sent to the attacker's console or can be modified to exfiltrate via a secondary request (e.g., to attacker's server).

**Why**: Confirm the attack succeeded by obtaining the victim's sensitive JSON data.

Enhance the script if needed to log or send the response (e.g., xhr.onreadystatechange to capture xhr.responseText and beacon it back).

**Expected Output**: JSON data from the API, such as user details, visible in browser console or exfiltrated to attacker's server.

**Success Indicators**:
- Victim visits the page while authenticated.
- API request succeeds (200 OK) with sensitive JSON in response.
- No CSRF token errors or blocks from the server.
