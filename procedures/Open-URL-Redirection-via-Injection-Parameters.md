---
id: c3f9f29a-3820-47b8-9a31-c99592751951
name: Open-URL-Redirection-via-Injection-Parameters
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.853488+00:00'
updated_at: '2023-04-10T20:23:05.573402+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/Common injection parameters]]'
  - '[[tags/Open URL Redirection]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
tools: []
validated: true
---

# Open-URL-Redirection-via-Injection-Parameters

## Summary

This procedure demonstrates how to identify and exploit open URL redirection vulnerabilities in web applications by injecting malicious URLs into common redirect parameters. It allows attackers to redirect users to phishing sites or malicious domains, facilitating initial access through drive-by compromises or credential harvesting.

## Description

Open URL redirection vulnerabilities occur when a web application does not properly validate or sanitize user-supplied URLs in redirect parameters, allowing attackers to manipulate the destination. This is commonly found in login pages, error handlers, or OAuth flows where parameters like 'redirect' or 'next' control navigation. In an attack scenario, an attacker crafts a link with a malicious payload (e.g., http://evil.com) and tricks a user into clicking it on a vulnerable site. Upon interaction, the legitimate site redirects to the attacker's controlled domain, enabling phishing, malware distribution, or session hijacking. This procedure targets web applications and requires no elevated privileges, making it suitable for reconnaissance and initial access phases. Expected outcomes include successful redirection to a controlled domain, confirmed via HTTP response codes (e.g., 302) and Location headers.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. Knowledge of common redirect parameters or ability to enumerate them.
3. Tools for sending HTTP requests, such as curl or a browser with developer tools.
4. A controlled malicious domain or URL for testing redirection (e.g., a phishing page hosted on attacker infrastructure).

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation: Whitelist allowed domains and use absolute path redirects where possible.
- Use HTTP response headers like Content-Security-Policy (CSP) with frame-ancestors to restrict navigation.
- Log and monitor redirect parameters for anomalous domains (e.g., external IPs or blacklisted hosts).
- Employ web application firewalls (WAFs) to block suspicious redirect patterns.

## Objectives

1. Identify vulnerable redirect parameters in the target application.
2. Inject a malicious URL to confirm redirection to an attacker-controlled site.
3. Demonstrate potential for phishing or drive-by compromise by observing successful redirects.

## Instructions

### Step 1: Identify Vulnerable Redirect Parameters

**Context**: Begin by reviewing the target application's forms, URLs, or API endpoints for common redirect parameters. Use the list of parameters from [[codes/Common-Open-Redirect-Injection-Parameters]] to guide enumeration. This step ensures you target the right injection points, such as login or reset pages.

Inspect the application manually or with developer tools to spot parameters like ?redirect= or ?next=.

### Step 2: Test Redirection with a Benign Payload

**Context**: Craft a test request using a harmless URL (e.g., http://example.com) to verify if the parameter allows open redirects without triggering alerts. This confirms vulnerability before using malicious payloads.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -L -v "http://target.com/login?redirect=http://example.com" -o /dev/null
```

> This command follows redirects (-L) and verbose output (-v) to show the Location header. Expected output includes a 302 status and Location: http://example.com, indicating the redirect works. If the response stays on the target domain or returns 403/400, the parameter may be sanitized.

### Step 3: Inject Malicious Payload and Verify Exploitation

**Context**: Replace the benign URL with a malicious one (e.g., http://evil.com/phish) to simulate an attack. Observe if the redirect occurs, confirming the vulnerability can be exploited for phishing or malware delivery. Use a proxy like Burp Suite for interception if needed.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -L -v "http://target.com/login?redirect=http://evil.com/phish" -o /dev/null
```

> Run this on various parameters from the list (e.g., ?next=, ?url=). Success is indicated by redirection to the malicious URL. If blocked, try URL encoding the payload (e.g., %68%74%74%70://evil.com) to bypass basic filters.

### Step 4: Validate Impact in Browser

**Context**: Test the crafted link in a browser to ensure it redirects legitimate users. This simulates social engineering, where the link is shared via email or social media.

Navigate to the full URL (e.g., http://target.com/login?redirect=http://evil.com/phish) and confirm the browser follows to the malicious site without warnings.
