---
id: 3b48bcdc-70f3-4982-a7f5-470093917275
name: CRLF-Injection-Phishing-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.324112+00:00'
updated_at: '2023-04-06T03:55:55.335297+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques:
  - >-
    [[sub-techniques/Spearphishing Attachment|T1566.001 - Spearphishing
    Attachment]]
  - '[[sub-techniques/Spearphishing Link|T1566.002 - Spearphishing Link]]'
tags:
  - crlf-injection
  - phishing
  - http-header-injection
commands:
  - '[[commands/curl-crlf-url-injection]]'
platforms:
  - Web
tools: []
validated: true
---

# CRLF-Injection-Phishing-Attack

## Summary

This procedure demonstrates a CRLF injection attack combined with phishing techniques to inject malicious HTTP headers and body content into a vulnerable web application. By encoding CRLF sequences (%0D%0A) in user inputs like URL parameters or form fields, an attacker can hijack HTTP responses, insert arbitrary headers, or append malicious HTML, enabling credential theft or session hijacking in a phishing scenario.

## Description

CRLF injection exploits web applications that fail to sanitize user inputs in HTTP headers or responses, allowing attackers to inject carriage return (%0D) and line feed (%0A) characters. In a phishing context, this can be used to craft malicious links or attachments that, when interacted with by victims, trigger the injection on a vulnerable server. For example, an attacker might send a spearphishing email with a link to a legitimate site but append encoded CRLF payloads to manipulate the server's response, injecting fake login forms or redirecting to malicious sites. This technique targets applications using outdated header parsing or insufficient input validation, common in legacy web apps. Success leads to response smuggling, where the victim's browser receives attacker-controlled content, facilitating data exfiltration like credentials or cookies.

## Requirements

1. Access to a vulnerable web application that echoes user input into HTTP headers without sanitization (e.g., via language parameter or custom headers).
2. Knowledge of the target's URL structure and input points (e.g., query parameters like ?lang=).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite, to test and deliver the payload.
4. Victim interaction in phishing scenarios, such as clicking a crafted link.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject or strip CRLF characters (%0D%0A) from all user inputs.
- Use secure HTTP header parsing libraries that handle edge cases, and enforce HTTP response splitting protections in web frameworks.
- Deploy web application firewalls (WAFs) with rules to detect anomalous header injections or unusual response lengths.
- Educate users on phishing recognition and enable browser protections against injected content, such as content security policies (CSP).

## Objectives

1. Inject CRLF sequences into HTTP requests to manipulate server responses.
2. Deliver phishing payloads via email or links that trigger the injection upon victim interaction.
3. Steal sensitive information, such as login credentials or session cookies, by injecting malicious HTML or redirects.
4. Achieve response hijacking to display fake content to the victim.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a parameter or field in the web application where user input is reflected into HTTP headers or responses without proper sanitization, such as a language selector (?lang=) or custom header input.

Inspect the application using developer tools or a proxy to confirm input reflection.

### Step 2: Craft and Test CRLF Injection Payload

**Context**: Encode a CRLF sequence to inject a fake HTTP response, terminating the original response and appending malicious content. This step uses a URL-based injection to hijack the response body.

**Command** ([[commands/curl-crlf-url-injection]]):
```bash
curl "http://www.example.net/index.php?lang=en%0D%0AContent-Length%3A%200%0A%20%0AHTTP/1.1%20200%20OK%0AContent-Type%3A%20text/html%0ALast-Modified%3A%20Mon%2C%2027%20Oct%202060%2014%3A50%3A18%20GMT%0AContent-Length%3A%2034%0A%20%0A%3Chtml%3EYou%20have%20been%20Phished%3C/html%3E"
```

> This command sends a GET request with the CRLF-encoded payload in the 'lang' parameter. The %0D%0A sequence splits the header, sets a zero Content-Length to end the legitimate response, and injects a new 200 OK response with malicious HTML. Expected output includes the injected "You have been Phished" message in the browser or response body, confirming successful hijacking.

Reference the payload code for details: [[codes/CRLF-Injected-URL-for-Response-Hijacking]]

### Step 3: Inject Malicious Content via Header Modification

**Context**: Use CRLF to modify existing headers and append a full malicious response, simulating a phishing page that captures credentials. This is useful for injecting Set-Cookie or redirect headers in phishing links.

Prepare the raw HTTP request with CRLF in the body or headers, then send it to the vulnerable endpoint.

Reference the payload code for details: [[codes/CRLF-Header-Injection-for-Response-Modification]]

Test by sending the request and verifying the response includes the injected HTML, such as a fake login form that posts data to an attacker-controlled server.

### Step 4: Deliver via Phishing

**Context**: Integrate the tested payload into a phishing campaign, such as embedding the malicious URL in an email link disguised as a legitimate site.

Send the spearphishing email or attachment. Monitor for victim clicks, which trigger the injection on the vulnerable server, delivering the malicious content to steal data.

Verify success by checking attacker logs for exfiltrated credentials.
