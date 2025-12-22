---
id: d388b46a-d5b9-4138-bf38-d7a60aec7920
name: SSRF-Enumeration-via-HTTP-URL-Scheme
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.803511+00:00'
updated_at: '2023-04-10T20:24:03.948733+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - '[[tags/HTTP]]'
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF exploitation via URL Scheme]]'
commands:
  - '[[commands/curl-ssrf-test-internal-url]]'
platforms:
  - Web
tools: []
validated: true
---

# SSRF-Enumeration-via-HTTP-URL-Scheme

## Summary

SSRF Enumeration via HTTP URL Scheme is a reconnaissance technique that exploits a vulnerable application's URL parameter to force the server to make requests to internal network resources, such as localhost ports or private IP addresses. This allows attackers to identify hidden services, open ports, and potentially sensitive internal data without direct access to the network.

## Description

Server-Side Request Forgery (SSRF) via HTTP URL schemes occurs when an application fetches resources based on user-supplied URLs without proper validation, enabling attackers to target internal systems like metadata services (e.g., AWS IMDS), database servers, or administrative interfaces. This procedure focuses on enumerating internal hosts and ports by crafting requests to common internal endpoints. It is typically used during reconnaissance to map the target's internal architecture, identify exploitable services, and gather information for further attacks. Success depends on the application's lack of URL whitelisting, IP restrictions, or response filtering. The target environment is usually a web application with a backend that processes URL parameters for fetching external content, such as image loaders or webhooks.

## Requirements

1. Valid access to the vulnerable web application endpoint that accepts a URL parameter (e.g., no authentication required or valid session).
2. Knowledge of the vulnerable parameter name (e.g., 'url' in ssrf.php?url=).
3. Network tools like curl for sending HTTP requests.
4. Optional: A proxy like Burp Suite for intercepting and modifying requests.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and URL whitelisting to allow only external, trusted domains.
- Use network segmentation and firewalls to block server-side requests to internal IPs (e.g., 127.0.0.1, 10.0.0.0/8, 169.254.169.254).
- Monitor application logs and network traffic for anomalous outbound requests from the web server to internal resources.
- Disable unnecessary internal services and use response filtering to avoid leaking internal data in error messages.

## Objectives

1. Identify internal systems and services not exposed to the public internet by probing common ports and IPs.
2. Gather information about the target's internal network structure, such as open ports on localhost or private hosts.
3. Discover potentially vulnerable internal services (e.g., admin panels, databases) for targeting in subsequent attack stages.

## Instructions

### Step 1: Identify the Vulnerable Endpoint and Parameter

**Context**: Confirm the application endpoint that accepts and processes user-supplied URLs. This step verifies SSRF is possible by testing with a harmless external URL.

**Command** ([[commands/curl-ssrf-test-internal-url]]):
```bash
curl "$_VULN_ENDPOINT?url=http://example.com"
```

> This command sends a request to the vulnerable endpoint with an external URL. Replace $_VULN_ENDPOINT with the full path (e.g., http://target.com/ssrf.php). Expected output: The application fetches and returns content from example.com without errors, confirming the parameter is processed server-side.

### Step 2: Enumerate Localhost Ports

**Context**: Test for open ports on the local server (127.0.0.1) by attempting to connect to common services. Different responses (e.g., banners, errors) indicate open ports and service types.

**Command** ([[commands/curl-ssrf-test-internal-url]]):
```bash
curl "$_VULN_ENDPOINT?url=http://127.0.0.1:22"
```

> Run this for ports like 22 (SSH), 80 (HTTP), 443 (HTTPS), 3306 (MySQL), etc. Why: Open ports will return service-specific content or timeouts, while closed ports return connection refused errors. Expected output: For port 22, an SSH banner like "SSH-2.0-OpenSSH_7.6" if open; otherwise, a timeout or error.

If the response varies by port, proceed to map more ports systematically.

### Step 3: Probe Internal Network IPs

**Context**: Extend enumeration to private IP ranges to discover other internal hosts. Start with common ranges like 10.0.0.0/8 or 192.168.0.0/16.

**Command** ([[commands/curl-ssrf-test-internal-url]]):
```bash
curl "$_VULN_ENDPOINT?url=http://10.0.0.1:80"
```

> Iterate over IPs and ports (e.g., using a script or manual tests). Why: This reveals internal web servers or routers. Expected output: HTTP response from an internal service if reachable, such as a 200 OK with server headers; connection errors otherwise.

### Step 4: Verify and Document Findings

**Context**: Analyze responses to confirm internal access and note any sensitive leaks (e.g., metadata endpoints).

No specific command; review outputs from previous steps. If a response includes internal data (e.g., AWS metadata), SSRF is confirmed successful. Decision point: If blocked, try URL encoding (e.g., http://127%2e0%2e0%2e1:22) or alternative schemes like gopher:// for bypassing filters.
