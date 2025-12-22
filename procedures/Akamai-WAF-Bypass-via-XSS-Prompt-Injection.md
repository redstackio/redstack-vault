---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/User Execution|T1204 - User Execution]]'
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - akamai-waf-bypass
  - xss
  - prompt-injection
  - client-side-execution
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Akamai-WAF-Bypass-via-XSS-Prompt-Injection

## Summary

This procedure exploits a cross-site scripting (XSS) vulnerability to bypass Akamai Web Application Firewall (WAF) protections by injecting obfuscated JavaScript code that prompts the user for input, enabling client-side execution of malicious payloads without triggering server-side filters.

## Description

Akamai WAF is designed to inspect and block malicious traffic to web applications, but it may fail to detect client-side generated payloads. This technique leverages an XSS vulnerability on a target webpage to inject an obfuscated HTML element using the <details> tag with a malformed ontoggle event handler. When triggered, it executes a JavaScript prompt() function, allowing the attacker to capture user input or execute further client-side code. This bypasses WAF rules that focus on server-bound requests, as the execution occurs entirely in the victim's browser. The method is particularly effective against reflected or stored XSS scenarios where direct script tags are filtered. Upon success, it can lead to session hijacking, data exfiltration, or further compromise via user interaction.

## Requirements

1. Identification of a vulnerable webpage susceptible to XSS injection (e.g., via unsanitized user input fields like search boxes or comments).
2. Ability to inject HTML/JavaScript payloads into the webpage (e.g., through a reflected input or stored content).
3. Victim interaction to trigger the payload (e.g., opening the page or expanding the details element).
4. Basic knowledge of browser developer tools for testing and refinement.

## Defense

- Implement comprehensive input validation, output encoding, and Content Security Policy (CSP) to prevent XSS injections.
- Use Web Application Firewalls with client-side execution monitoring and anomaly detection for unusual prompt dialogs.
- Employ browser security features like XSS auditors and educate users on avoiding suspicious prompts.
- Regularly scan for vulnerabilities using tools like OWASP ZAP or Burp Suite and apply secure development practices.

## Objectives

1. Inject obfuscated XSS payload to evade Akamai WAF detection.
2. Trigger client-side JavaScript execution via user prompt to capture input or execute commands.
3. Achieve unauthorized access to sensitive data or further compromise the victim's session.

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a point on the target webpage where user input is reflected without proper sanitization, such as a search parameter or form field. Test basic XSS payloads like <script>alert(1)</script> to confirm vulnerability, but expect WAF blocking.

Use browser developer tools to inspect the page and identify injectable attributes or elements.

### Step 2: Craft and Inject Obfuscated Payload

**Context**: Use an obfuscated HTML snippet to bypass WAF filters that block common XSS patterns. The payload exploits the <details> tag's ontoggle event to execute JavaScript indirectly.

**Code** ([[codes/Obfuscated-HTML-Details-Tag-for-Prompt-XSS]]):

```html
<dETAILS%0aopen%0aonToGgle%0a=%0aa=prompt,a() x>
```

Inject this payload into the vulnerable input field (e.g., via URL parameter like ?search=<payload>). The %0a represents line breaks for obfuscation, evading signature-based detection.

### Step 3: Trigger and Verify Execution

**Context**: Once injected, the page must be loaded by the victim. The <details> element opens automatically due to the 'open' attribute, firing the ontoggle event to execute prompt('message'), which displays a dialog and captures user input.

Observe the victim's browser for the prompt dialog. If successful, the prompt executes without server-side alerting the WAF.

**Expected Output**: A browser prompt dialog appears, allowing input capture (e.g., returned value can be used for further JS actions like sending data to an attacker-controlled server).

### Step 4: Escalate if Needed

**Context**: Use the prompted input to chain further attacks, such as sending it to an external endpoint via XMLHttpRequest or modifying DOM elements for persistence.

Modify the prompt callback to exfiltrate data, e.g., extend the JS to include fetch() calls post-prompt.
