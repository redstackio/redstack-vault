---
type: procedure
description: >-
  This procedure demonstrates techniques to bypass dot filters in cross-site
  scripting (XSS) attacks using bracket notation, base64 encoding, and decimal
  IP conversion for resource loading.
verified: true
submitted: false
created_at: '2023-04-06T03:56:42Z'
updated_at: '2023-04-10T20:21:41Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.007 -
    JavaScript|T1059.007]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Data Encoding|T1132 - Data Encoding]]'
sub_techniques: []
tags:
  - '[[tags/xss]]'
  - '[[tags/filter-bypass]]'
  - '[[tags/dot-filter]]'
  - '[[tags/base64-encoding]]'
  - '[[tags/javascript-obfuscation]]'
commands:
  - '[[commands/base64-encode-xss-payload]]'
  - '[[commands/curl-access-decimal-ip]]'
platforms:
  - Web
tools: []
validated: true
---

# XSS-Dot-Filter-Bypass-Using-Exotic-Payloads

## Summary

This procedure outlines methods to bypass dot (.) filters commonly implemented in web applications to prevent XSS attacks. By using JavaScript bracket notation to avoid direct property access, base64 encoding to obfuscate payloads, and converting dotted IP addresses to decimal format for resource references, attackers can execute arbitrary JavaScript, such as alerting domain information or stealing cookies, even when filters block standard payloads containing dots.

## Description

Dot filters often block or sanitize inputs containing periods to prevent malicious resource loading or property access in JavaScript objects like document.domain or document.cookie. This procedure targets reflected or stored XSS vulnerabilities where such filters are in place. The techniques allow execution of code to confirm XSS (e.g., via alert(domain)) or exfiltrate data (e.g., cookies). These methods are useful in red team engagements to test web application defenses. The target environment is typically a web browser interacting with a vulnerable input field, search parameter, or URL fragment. Expected outcomes include successful payload execution without triggering filters, leading to code execution or data theft.

## Requirements

1. Access to a vulnerable web application with a reflected or stored XSS entry point (e.g., search box, user input field).
2. A modern web browser with developer console (e.g., Chrome DevTools) for testing payloads.
3. Command-line interface (CLI) on Linux/macOS for base64 encoding and IP conversion utilities.
4. Optional: Proxy tool like Burp Suite for intercepting and modifying requests.
5. Knowledge of the target's domain and any internal IPs for resource loading bypasses.

## Defense

- Implement Content Security Policy (CSP) to restrict script execution and resource loading.
- Use strict input validation and output encoding (e.g., HTML entity encoding) on all user inputs.
- Deploy a Web Application Firewall (WAF) tuned to detect obfuscated XSS patterns like base64 decoding or bracket notation.
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite Scanner.
- Enable browser security features like XSS Auditor (deprecated in some browsers) or strict CSP headers.

## Objectives

1. Execute JavaScript payloads in a filtered environment to confirm XSS vulnerability.
2. Obfuscate payloads using base64 and bracket notation to evade dot-based filters.
3. Bypass restrictions on dotted URLs (e.g., for loading internal resources) by converting IPs to decimal format.
4. Steal sensitive data like cookies or domain information without detection.

## Instructions

### Step 1: Test Basic XSS with Bracket Notation to Alert Domain

**Context**: This step uses bracket notation (e.g., ['alert'] instead of .alert) to avoid filters that block dotted property access, executing an alert with the current domain to confirm control.

**Code** ([[codes/JavaScript-Alert-Document-Domain-Bracket-Notation]]):

```javascript
<script>window['alert'](document['domain'])</script>
```

> Inject this payload into the vulnerable input field (e.g., via URL parameter like ?q=<payload>). The bracket notation evades filters scanning for 'document.domain'. Expected output is a browser alert box displaying the domain (e.g., "example.com"). If successful, proceed; if blocked, move to encoding.

### Step 2: Encode XSS Payload Using Base64 for Obfuscation

**Context**: Encode the desired JavaScript payload (e.g., alert(document.cookie)) in base64 to bypass filters that inspect plaintext dots or keywords. This step prepares the payload for decoding in the browser.

**Command** ([[commands/base64-encode-xss-payload]]):

```bash
echo -n "alert(document.cookie)" | base64
```

> Run this on your CLI to generate the base64 string (output: YWxlcnQoZG9jdW1lbnQuY29va2llKQ==). The -n flag suppresses newlines for clean encoding. Use this string in the next step's decoding payload. Success is confirmed by the encoded output without errors.

### Step 3: Decode and Execute Base64 Payload in Browser

**Context**: Use JavaScript's atob() function to decode the base64 string and eval() to execute it, stealing cookies despite dot filters blocking direct access to document.cookie.

**Code** ([[codes/JavaScript-Eval-Atop-Base64-Decode-Alert-Cookie]]):

```javascript
<script>eval(atob("YWxlcnQoZG9jdW1lbnQuY29va2llKQ=="))<script>
```

> Replace the hardcoded base64 string with your encoded payload from Step 2 if targeting different actions. Inject into the XSS vector. The atob() decodes the string, and eval() runs the JS. Expected output: Alert box showing cookie data (e.g., "sessionid=abc123"). If the payload is filtered, adjust encoding or add more obfuscation.

### Step 4: Bypass Dot Filters in URLs Using Decimal IP Conversion

**Context**: For payloads loading external resources (e.g., <img src="http://internal-ip/image">), convert dotted IPs to decimal to evade URL dot filters. This is useful for exfiltrating data to internal systems in XSS.

**Instructions**: Manually convert the IP (e.g., 192.168.1.1): 192*256^3 + 168*256^2 + 1*256 + 1 = 3232235777. Then test access.

**Command** ([[commands/curl-access-decimal-ip]]):

```bash
curl http://3232235777
```

> Use curl to verify the decimal IP resolves to the target (e.g., router admin page). Expected output: HTTP response from the internal service (e.g., HTML login page). In XSS, embed as <img src="http://3232235777/endpoint"> to load without dots. If curl succeeds without resolution errors, the bypass works; integrate into payload for data exfil.

### Step 5: Verify and Chain Payloads

**Context**: Combine techniques (e.g., base64 + decimal IP) for complex attacks like loading a script from an internal decimal IP.

**Instructions**: Craft a payload like <script>eval(atob("..."))</script> where the decoded JS fetches from http://$_DECIMAL_IP. Test in browser console or via proxy. Expected outcome: Successful execution without filter blocks, potentially chaining to further exploitation like keylogging.
