---
id: 640e44d1-3380-460b-9a01-049bd1f9d831
name: SSRF-via-Injected-HTML-File-as-Image-or-Text
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.131525+00:00'
updated_at: '2023-04-10T20:23:57.524023+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Network Share Discovery|T1135 - Network Share Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF from XSS]]'
  - '[[tags/Using an iframe]]'
commands:
  - '[[commands/curl-inject-html-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# SSRF-via-Injected-HTML-File-as-Image-or-Text

## Summary

This procedure exploits a web application vulnerability that permits the injection of malicious HTML content disguised as an image or text file. The injected HTML uses tags like <img> with an onerror handler to dynamically insert an <iframe> pointing to a target endpoint. When processed, this can force server-side requests to internal or remote resources, enabling SSRF for sensitive data disclosure or further exploitation such as accessing metadata services or internal networks.

## Description

The attack targets applications that fail to properly sanitize user-supplied content in fields intended for images or text, allowing HTML injection. The malicious payload triggers on load failure (via onerror) to embed an iframe sourcing a controlled URL, such as an internal server or cloud metadata endpoint (e.g., http://169.254.169.254/latest/meta-data/ for AWS). If the application renders or processes the HTML server-side (e.g., during preview or proxying resources), it makes unauthorized requests on behalf of the attacker, bypassing firewalls and exposing internal systems. This technique combines HTML injection (often via XSS-like flaws) with SSRF to proxy requests through the vulnerable app. Potential outcomes include data exfiltration, network discovery, or chaining to RCE. From a defender's view, it highlights risks in unsanitized file uploads or content rendering. Business impacts include data breaches leading to compliance violations and reputational damage.

## Requirements

1. Access to a vulnerable web application endpoint that accepts user input for image or text content without proper HTML sanitization (e.g., file upload or rich text editor).
2. Knowledge of target internal endpoints or services (e.g., localhost ports, cloud metadata URLs like http://169.254.169.254/).
3. Ability to observe or capture responses, such as via a controlled server for request verification or application output reflecting fetched data.
4. Basic web proxy tool (optional, for interception) and a listening server to confirm SSRF requests.

## Defense

- Implement strict input validation and output encoding, using libraries like DOMPurify to strip dangerous HTML tags and attributes.
- Enforce Content Security Policy (CSP) headers to block inline scripts, iframes, and unsafe resource loads.
- Avoid server-side fetching or proxying of user-controlled URLs; validate and restrict URLs to whitelisted domains.
- Monitor application logs and network traffic for anomalous outbound requests to internal IPs, localhost, or metadata services.

## Objectives

1. Inject malicious HTML to force the server to request unauthorized internal or remote resources.
2. Disclose sensitive data, such as cloud instance metadata, internal files, or network shares.
3. Bypass network controls by proxying requests through the compromised application.

## Instructions

### Step 1: Identify the Vulnerable Injection Point

**Context**: Locate the application feature allowing HTML injection, such as a file upload for profile images or a text field for content that gets rendered without escaping. Test by submitting simple HTML like <script>alert(1)</script> to confirm execution.

Manual exploration or use a proxy to inspect requests. Why: Ensures the point accepts and processes HTML server-side or client-side in a way that triggers fetches.

**Expected Output**: Alert pops or HTML renders, confirming injection success.

### Step 2: Craft the Malicious Payload

**Context**: Prepare the HTML snippet that will trigger the SSRF. Use the provided code snippet, but modify the iframe src to target the desired endpoint (e.g., replace file:///etc/passwd with http://169.254.169.254/latest/meta-data/ for AWS SSRF). This ensures the request goes to a remote/internal resource. Why: The onerror ensures execution even if the initial img src is invalid, embedding the iframe dynamically.

**Code** ([[codes/HTML-Img-OnError-DocumentWrite-Iframe]]):

Modify src in the iframe as needed.

**Expected Output**: Valid HTML snippet ready for injection, with no syntax errors.

### Step 3: Inject the Payload Using HTTP Request

**Context**: Submit the crafted HTML as the content for the image or text field. This could be via a POST request to an upload endpoint. Why: Delivers the payload to the server for processing, where it can trigger the SSRF during rendering or resource fetching.

**Command** ([[commands/curl-inject-html-payload]]):
```bash
curl -X POST -F "file=@payload.html" http://target.com/upload-endpoint
```

> Replace payload.html with a file containing the modified HTML. Expected: 200 OK response or success message indicating upload/processing.

**Expected Output**: Server accepts the input and may render or store it, potentially making the SSRF request immediately or on next load.

### Step 4: Trigger and Verify the SSRF

**Context**: Load the page or resource where the injected content is displayed to activate the payload. Monitor for the forged request. Why: Confirms the server (or proxying behavior) fetches the targeted URL, indicating successful SSRF.

Access the affected page (e.g., via browser or curl) and check your controlled endpoint or application response for leaked data.

**Expected Output**: Request arrives at the target URL from the server's IP (not yours), possibly with sensitive data in the response body or headers.

**Success Indicators**:
- Outbound request logged on your controlled server.
- Application reflects internal data (e.g., metadata JSON) in output or error messages.
