---
id: 6ae50f95-ebee-4e8e-8b61-cad7c32f90c1
name: Server-Side-Request-Forgery-via-Bypassing-Filters-with-HTTPS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.241475+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using HTTPS]]'
  - '[[tags/Server-Side Request Forgery]]'
commands:
  - '[[commands/curl-ssrf-https-localhost]]'
platforms:
  - Web
tools: []
validated: true
---

# Server-Side-Request-Forgery-via-Bypassing-Filters-with-HTTPS

## Summary

This procedure demonstrates how to exploit a Server-Side Request Forgery (SSRF) vulnerability by bypassing URL filters using HTTPS to access internal resources like localhost. It involves crafting requests to a vulnerable web application that processes user-supplied URLs, allowing attackers to force the server to connect to restricted endpoints such as 127.0.0.1 or localhost over HTTPS, potentially leading to data exfiltration or internal network pivoting.

## Description

Server-Side Request Forgery (SSRF) occurs when a web application fetches resources from URLs provided by users without proper validation. Filters often block HTTP requests to internal IPs like 127.0.0.1 to prevent access to localhost services, but many implementations fail to block HTTPS equivalents. This procedure targets such misconfigurations, using HTTPS URLs to bypass blacklists that only check for HTTP schemes or plain IP addresses. In a typical scenario, the vulnerable application might have an endpoint like /api/fetch?url= that retrieves content from the supplied URL. By inputting https://127.0.0.1/admin or similar, the attacker can access internal metadata services (e.g., AWS instance metadata) or other localhost ports. This is particularly effective in cloud environments where internal services expose sensitive data. Prerequisites include identifying a vulnerable input point via reconnaissance, such as upload forms or image loaders. Success enables lateral movement or command-and-control by proxying through the victim server.

## Requirements

1. Network access to a vulnerable web application with an SSRF-prone endpoint (e.g., URL parameter in GET/POST requests).
2. Knowledge of the target's internal services (e.g., ports 80/443 on localhost).
3. Tools like curl or Burp Suite for crafting and sending requests.
4. Optional: Proxy setup to intercept and modify responses.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation: Whitelist allowed domains and block private IPs (RFC 1918) and localhost for both HTTP and HTTPS schemes.
- Use a Web Application Firewall (WAF) to detect and block anomalous internal requests, such as those targeting 127.0.0.1 or 0.0.0.0.
- Disable unnecessary internal services and monitor server logs for unexpected outbound connections from the application server.
- Employ network segmentation to isolate the web server from internal resources.

## Objectives

1. Bypass URL filters to force the server to make requests to internal resources via HTTPS.
2. Access localhost or internal network endpoints to retrieve sensitive data.
3. Establish a proxy-like connection for further lateral movement or evasion.

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Locate an input field or parameter in the web application that accepts URLs and makes server-side requests (e.g., via features like webhooks, image imports, or API fetches). Test basic SSRF by supplying external URLs to confirm the server fetches them.

Use reconnaissance tools to map the application, then manually test parameters like ?url= or POST body fields.

### Step 2: Craft HTTPS Payload for Localhost Access

**Context**: Construct a payload using HTTPS to bypass filters that only block HTTP to internal addresses. Common bypasses include https://127.0.0.1/, https://localhost/, or variations like https://[::1]/ for IPv6 localhost.

**Command** ([[commands/curl-ssrf-https-localhost]]):
```bash
curl -X GET "http://target.com/vulnerable-endpoint?url=https://127.0.0.1:8080/internal" -v
```

> This command sends a request to the vulnerable endpoint with an HTTPS URL targeting localhost port 8080 (adjust port as needed for the internal service). The -v flag enables verbose output to observe the server's response. If successful, the response may include content from the internal service or an error indicating access was made.

### Step 3: Verify and Escalate

**Context**: Analyze the response for signs of successful internal access, such as leaked metadata or error messages revealing server internals. If partial success, iterate with variations (e.g., https://localhost/admin) or chain with other bypasses like decimal IP encoding (e.g., https://2130706433/ for 127.0.0.1).

Check server logs or use a proxy like Burp Suite to confirm the backend request. If data is exfiltrated, proceed to parse it for credentials or further pivots.

**Expected Output**: The vulnerable application's response includes content from the internal resource (e.g., HTML from localhost) or indirect indicators like changed response times/lengths.
