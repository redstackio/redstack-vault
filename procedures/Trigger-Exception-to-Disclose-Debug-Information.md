---
tags:
  - information-disclosure
  - debug-leak
  - sinatra
  - oauth
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/send-invalid-oauth-redirect-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:13.216Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: aae36525-ad4b-4651-aefb-fe937e8b343d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Trigger-Exception-to-Disclose-Debug-Information

## Summary

This procedure exploits a misconfigured Sintra (Sinatra) framework application by sending an invalid OAuth redirect URI cookie to trigger an unhandled exception, resulting in the disclosure of debug information such as internal configuration, environment variables, and source code snippets. It is primarily used in reconnaissance phases to gather sensitive details about the target's infrastructure without requiring authentication.

## Description

The attack targets OAuth redirector services built on the Sintra framework where the show_exceptions setting is enabled in production, which is a security misconfiguration. By submitting an invalid oauth_redirect_uri cookie value to the /integrations/oauth/create endpoint, an unhandled exception occurs during URI validation or processing. The framework then renders a detailed error page exposing stack traces, loaded environment variables (potentially including secrets like database URLs or API keys), and code snippets from the application. This was observed in a security assessment of Greenhouse.io's OAuth login flow. The procedure assumes public access to the endpoint and uses standard HTTP requests. Expected outcomes include reconnaissance data that could facilitate further attacks, such as identifying weak configurations or internal endpoints.

## Requirements

1. Network access to the target HTTPS endpoint (e.g., oauth-redirector.services.greenhouse.io on port 443)
2. Ability to craft HTTP requests with custom cookies (using tools like curl, Burp Suite, or browser dev tools)
3. Basic understanding of OAuth flows and web request manipulation

## Defense

Defensive measures and detection strategies:

- Disable show_exceptions in production environments for Sintra/Sinatra apps (set to false in config)
- Implement custom error handlers to sanitize exception outputs and log detailed errors server-side only
- Use web application firewalls (WAF) to detect and block requests with malformed OAuth parameters or suspicious cookies
- Monitor server logs for unhandled exceptions and anomalous request patterns to the OAuth endpoints

## Objectives

1. Trigger an unhandled exception to bypass normal error handling
2. Extract sensitive internal information from the debug output for reconnaissance
3. Identify potential vulnerabilities or secrets exposed in the environment variables and code

## Instructions

### Step 1: Craft and Send Invalid OAuth Request

**Context**: Prepare an HTTP GET request to the OAuth creation endpoint with a deliberately invalid oauth_redirect_uri cookie value. The invalid URI (e.g., pointing to a malformed callback path) will fail validation, causing an exception in the Sintra app.

**Command** ([[commands/send-invalid-oauth-redirect-request]]):
```bash
curl -X GET "https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x" -H "Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback" -v
```

> This command sends a GET request with query parameters state=x and code=x (dummy values to simulate OAuth callback) and sets the oauth_redirect_uri cookie to an invalid URL. The -v flag enables verbose output to inspect headers and response. On success, the response body will contain the debug exception page. Analyze the output for exposed data like ENV['DATABASE_URL'] or stack traces revealing file paths.

### Step 2: Analyze Disclosed Information

**Context**: Review the response for sensitive leaks. No additional command is needed; parse the HTML manually or with grep for keywords like 'ENV', 'config', or Ruby stack traces.

**Command** (grep for analysis):
```bash
curl -s -X GET "https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x" -H "Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback" | grep -i "env\|config\|exception"
```

> This pipes the response through grep to highlight potential leaks. Expected output includes lines with environment variables or config details if disclosure occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/send-invalid-oauth-redirect-request]]

## Tools Used


## Tags

- information-disclosure
- debug-leak
- sinatra
- oauth
- reconnaissance
