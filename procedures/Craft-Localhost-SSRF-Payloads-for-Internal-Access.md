---
id: cfb9a7aa-fd7d-45d4-9e7b-8ef4d0cd54b7
name: Craft-Localhost-SSRF-Payloads-for-Internal-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.210346+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - payloads-with-localhost
  - server-side-request-forgery
commands:
  - '[[commands/generate-localhost-urls-for-ssrf]]'
  - '[[commands/generate-loopback-urls-for-ssrf]]'
  - '[[commands/send-ssrf-payload-via-curl]]'
platforms:
  - Web
tools: []
validated: true
---

# Craft-Localhost-SSRF-Payloads-for-Internal-Access

## Summary

This procedure outlines how to craft and test Server-Side Request Forgery (SSRF) payloads targeting localhost resources, such as internal services running on the server's loopback interface. By injecting URLs like http://localhost:80 into a vulnerable application's input fields, an attacker can trick the server into making requests to its own internal resources, bypassing external access controls to enumerate or interact with local services like web servers, databases, or metadata endpoints.

## Description

Server-Side Request Forgery (SSRF) vulnerabilities allow attackers to manipulate a server into making unintended requests on their behalf. When focused on localhost, these payloads exploit the fact that the server can access its own internal network (e.g., 127.0.0.1 or localhost), which is typically firewalled from external access. Common targets include port 80 (HTTP), 443 (HTTPS), 22 (SSH), or cloud metadata services like http://169.254.169.254 (for AWS/GCP). This technique is particularly effective against cloud-hosted applications where internal metadata can reveal credentials or configuration details. The procedure assumes a vulnerable endpoint that accepts URL parameters (e.g., ?url= or ?image=) without proper validation. Success enables data exfiltration, port scanning, or further exploitation of internal systems.

## Requirements

1. Access to a public-facing web application vulnerable to SSRF (e.g., an endpoint that fetches resources from user-supplied URLs).
2. Knowledge of common internal ports and services (e.g., web server on 80, admin panel on 8080).
3. Tools like curl for testing payloads or a proxy like Burp Suite for interception and modification.
4. Network position allowing HTTP requests to the target application (no authentication required for initial testing).

## Defense

- Implement strict input validation and whitelisting to reject localhost, loopback (127.0.0.0/8), and private IP ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).
- Use a web application firewall (WAF) to block requests containing suspicious URLs like localhost or 127.0.0.1.
- Monitor server logs and network traffic for outbound connections to internal resources from the application server.
- Disable unnecessary internal services and use network segmentation to limit lateral movement.

## Objectives

1. Craft payloads to access internal localhost resources via SSRF.
2. Test payloads to confirm vulnerability and retrieve internal data.
3. Exfiltrate sensitive information such as service banners, metadata, or files from internal endpoints.

## Instructions

### Step 1: Generate Localhost URL Payloads

**Context**: Start by generating a list of common localhost URLs targeting typical internal ports. This helps identify potential services like HTTP or SSH that may be accessible only from the server itself. Use this list to build SSRF payloads.

**Command** ([[commands/generate-localhost-urls-for-ssrf]]):
```bash
echo -e "http://localhost:80\nhttp://localhost:443\nhttp://localhost:22"
```

> This command outputs a list of URLs using the 'localhost' hostname. Each URL points to a standard port: 80 for HTTP, 443 for HTTPS, and 22 for SSH. Customize ports based on reconnaissance of the target environment.

### Step 2: Generate Loopback and All-Interfaces URL Variants

**Context**: Expand the payload list to include IP-based variants like 127.0.0.1 (loopback) and 0.0.0.0 (all interfaces). These are useful because some applications resolve or filter 'localhost' differently than IP addresses, increasing the chance of bypassing basic checks.

**Command** ([[commands/generate-loopback-urls-for-ssrf]]):
```bash
echo -e "http://127.0.0.1:80\nhttp://127.0.0.1:443\nhttp://127.0.0.1:22\nhttp://0.0.0.0:80\nhttp://0.0.0.0:443\nhttp://0.0.0.0:22"
```

> This outputs URLs using loopback (127.0.0.1) and wildcard (0.0.0.0) addresses. 127.0.0.1 routes traffic back to the local machine, while 0.0.0.0 may target services bound to all interfaces. Pipe the output to a file (e.g., | tee payloads.txt) for reuse.

### Step 3: Test SSRF Payload by Sending to Vulnerable Endpoint

**Context**: Use the generated payloads to test the vulnerability. Inject one URL at a time into the application's SSRF-prone parameter (e.g., ?url= or ?redirect=). Monitor the response for internal service data, such as HTTP headers or error messages revealing service versions.

**Command** ([[commands/send-ssrf-payload-via-curl]]):
```bash
curl -v "http://$_TARGET_APP/ssrf-endpoint?url=$_PAYLOAD_URL" 2>&1 | grep -i "server|location|content"
```

> Replace $_TARGET_APP with the vulnerable application's URL (e.g., http://example.com) and $_PAYLOAD_URL with a generated payload (e.g., http://localhost:80). The -v flag enables verbose output to see request/response details. Grep filters for indicators like server banners. If successful, the response may include internal content; if blocked, look for error messages hinting at internal access attempts. Test multiple payloads iteratively, and if the app uses POST, adjust to -X POST -d "url=$_PAYLOAD_URL".

### Step 4: Analyze Response and Iterate

**Context**: Review the output from the test command for signs of success, such as internal HTML, JSON data, or connection errors indicating local service interaction. If no response, try URL encoding the payload (e.g., %68%74%74%70%3A%2F%2F%6C%6F%63%61%6C%68%6F%73%74%3A%38%30) to bypass filters.

No specific command needed here, but reuse [[commands/send-ssrf-payload-via-curl]] with variations. Success is confirmed if internal data is reflected; otherwise, enumerate more ports or combine with other techniques like DNS rebinding.
