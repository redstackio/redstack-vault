---
id: 0d258a41-c75a-4be9-a98f-b5a9ef1e7245
name: SSRF-Filter-Bypass-Using-IP-Resolution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.538270+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Network Service Discovery|T1046 - Network Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using tricks combination]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - filter-bypass
  - ip-resolution
commands:
  - '[[commands/dig-resolve-hostname]]'
  - '[[commands/curl-send-ssrf-ip-request]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# SSRF-Filter-Bypass-Using-IP-Resolution

## Summary

This procedure outlines how to bypass Server-Side Request Forgery (SSRF) filters that block requests to specific domains by first resolving the target hostname to its IP address locally, then substituting the IP into the SSRF payload. This technique evades domain-based blacklists or whitelists, allowing access to internal services like metadata endpoints (e.g., AWS instance metadata at 169.254.169.254).

## Description

SSRF vulnerabilities enable attackers to force a server to make unintended requests to internal or external resources. Filters often block requests by domain name (e.g., denying 'metadata.service'), but resolving the domain to an IP address locally allows direct IP usage in the payload, bypassing name-based checks. This is useful in cloud environments where internal services use well-known IPs. The approach involves local DNS resolution to obtain the IP, followed by crafting a request to the vulnerable endpoint with the IP embedded. Success grants access to restricted resources, potentially leading to data exfiltration or further compromise. This method assumes the SSRF endpoint accepts URL parameters and lacks IP-based filtering.

## Requirements

1. Valid user session or authentication to the SSRF-vulnerable web application.
2. Knowledge of the target internal resource (e.g., hostname like 'metadata.google.internal' or IP like 169.254.169.254 for AWS).
3. Network access to perform DNS resolution (local or via attacker machine).
4. Tools like dig for DNS queries and curl for sending HTTP requests.

## Defense

- Implement strict URL validation, parsing, and whitelisting on the server side to allow only approved domains and IPs.
- Use network segmentation and firewalls to restrict server outbound connections to internal services.
- Deploy a Web Application Firewall (WAF) with SSRF-specific rules to detect anomalous request patterns, such as IP-based internal accesses.
- Enable server-side DNS resolution pinning or disable direct IP usage in request handlers.

## Objectives

1. Resolve the target hostname to its IP address without triggering server-side filters.
2. Inject the resolved IP into an SSRF payload to access blocked internal resources.
3. Retrieve sensitive data from the target service, such as cloud metadata.

## Instructions

### Step 1: Resolve Target Hostname to IP Address

**Context**: Perform local DNS resolution to obtain the IP address of the target hostname. This avoids server-side DNS checks that might be filtered. Use the [[commands/dig-resolve-hostname]] command for quick resolution; alternatively, use the [[codes/python-resolve-hostname-to-ip]] script for scripted environments.

**Command** ([[commands/dig-resolve-hostname]]):
```bash
dig +short $_HOSTNAME
```

> This command queries DNS for the IP of the specified hostname. Replace $_HOSTNAME with the target (e.g., '169.254.169.254' for AWS metadata, or a domain like 'internal.example.com'). Expected output is the resolved IP address, such as '169.254.169.254'.

If using Python, execute the [[codes/python-resolve-hostname-to-ip]] code and substitute the hostname variable.

### Step 2: Craft and Send SSRF Payload with Resolved IP

**Context**: Use the resolved IP to construct the SSRF payload. This step sends a request to the vulnerable endpoint, embedding the IP in the URL parameter to fetch the internal resource. Verify the response contains data from the target service.

**Command** ([[commands/curl-send-ssrf-ip-request]]):
```bash
curl -X POST "$_ENDPOINT" -d "url=http://$_IP$_PATH" -H "Content-Type: application/x-www-form-urlencoded"
```

> This sends a POST request to the SSRF endpoint with the IP-based URL. Replace $_ENDPOINT with the vulnerable URL (e.g., 'https://target.com/api/fetch'), $_IP with the resolved IP (e.g., '169.254.169.254'), and $_PATH with the target path (e.g., '/latest/meta-data/'). Expected output is the response body from the internal service, such as JSON metadata. If successful, no filter errors occur, and sensitive data is returned.

**Decision Point**: If the response indicates a connection error, the IP might be firewalled—try alternative ports or protocols (e.g., 'http://$_IP:80/$_PATH'). If blocked, chain with URL encoding: use [[commands/curl-send-ssrf-url-encoded]] for obfuscation.
