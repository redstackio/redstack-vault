---
id: 268ab2dd-8962-41f3-9375-b4cc7f39dd2c
name: Perform-SSRF-Using-IPv6-IPv4-Address-Embedding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.421022+00:00'
updated_at: '2023-04-10T20:24:15.495587+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using IPv6/IPv4 Address Embedding]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - ipv6-bypass
  - filter-bypass
commands:
  - '[[commands/curl-send-ipv6-embedded-ssrf-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Perform-SSRF-Using-IPv6-IPv4-Address-Embedding

## Summary

This procedure demonstrates how to bypass URL filters in Server-Side Request Forgery (SSRF) vulnerabilities by embedding an IPv4 address within an IPv6 address. By constructing an IPv6 URL that embeds the target IPv4 address in the last 32 bits (using the ::ffff: prefix), attackers can trick applications that block direct IPv4 access but allow IPv6, enabling unauthorized requests to internal resources like localhost or metadata services.

## Description

Server-Side Request Forgery (SSRF) allows attackers to make the target application send requests to arbitrary locations, often internal systems. Many filters block common internal IPs (e.g., 127.0.0.1, 169.254.169.254 for AWS metadata) but may not validate IPv6 addresses properly. This technique embeds the IPv4 address into an IPv6 format, such as http://[0:0:0:0:0:ffff:127.0.0.1], which resolves to the same IPv4 endpoint. It is particularly effective against web applications with SSRF in features like image fetching, webhooks, or URL imports. The target environment is typically a public-facing web app on cloud infrastructure (e.g., AWS, Azure) where internal pivoting is the goal. Success allows access to sensitive internal data, such as instance metadata, leading to further compromise.

## Requirements

1. Access to a public-facing web application with a confirmed SSRF vulnerability (e.g., a parameter that fetches external URLs).
2. Knowledge of the target internal IPv4 address (e.g., 127.0.0.1 for localhost, 169.254.169.254 for AWS metadata).
3. Tools like curl or a proxy (e.g., Burp Suite) to craft and send HTTP requests.
4. Network access to the vulnerable application from the attacker's position.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation that parses and blocks both IPv4 and IPv6 addresses, including embedded formats (use libraries like Python's ipaddress module).
- Deploy a Web Application Firewall (WAF) with SSRF-specific rules to detect anomalous internal requests or IPv6 embeddings.
- Restrict server outbound connections to only whitelisted domains/IPs using network ACLs or proxies.
- Enable logging of all outbound requests from the application server to monitor for unexpected internal fetches.

## Objectives

1. Bypass IPv4-specific filters in SSRF-vulnerable endpoints to reach internal resources.
2. Retrieve data from blocked internal services, such as localhost or cloud metadata endpoints.
3. Escalate access by chaining with other vulnerabilities, like reading sensitive files or querying internal APIs.

## Instructions

### Step 1: Identify the SSRF-Vulnerable Parameter

**Context**: Locate the input field or API endpoint that accepts and fetches URLs from user input, such as a 'url' parameter in a POST request. Test basic SSRF by submitting http://example.com to confirm the app fetches and responds with content.

Use reconnaissance tools or manual testing to find this. No specific command here, but verify with a simple external URL test.

**Expected Output**: The application returns content from the external site, confirming SSRF is possible.

### Step 2: Craft the IPv6-Embedded URL for the Target

**Context**: Convert the target IPv4 address into an IPv6-embedded format. For localhost (127.0.0.1), use [0:0:0:0:0:ffff:127.0.0.1]. For other IPs, replace accordingly (e.g., for 10.0.0.1: [0:0:0:0:0:ffff:10.0.0.1]). Append the desired path, like /etc/passwd for file access or /latest/meta-data/ for AWS.

This step prepares the payload to evade IPv4 blocks while targeting internals.

**Expected Output**: A valid URL string that resolves to the internal IPv4 address when parsed by the server.

### Step 3: Send the SSRF Request with Embedded Payload

**Context**: Submit the crafted URL via the vulnerable parameter to trigger the internal request. This step executes the bypass and fetches the target resource.

**Command** ([[commands/curl-send-ipv6-embedded-ssrf-payload]]):
```bash
curl -X POST http://vulnerable-app.com/ssrf-endpoint -d "url=http://[0:0:0:0:0:ffff:127.0.0.1]/target-path"
```

> This command sends a POST request to the SSRF endpoint with the embedded URL. Replace 'vulnerable-app.com/ssrf-endpoint' with the actual URL, and '/target-path' with the desired internal path (e.g., /latest/meta-data/iam/security-credentials/ for AWS). If the bypass works, the response will contain data from the internal resource.

**Expected Output**: HTTP response body containing the fetched internal content, such as localhost page output or metadata JSON, instead of an error or blocked message.

### Step 4: Verify and Iterate

**Context**: Check the response for success indicators. If blocked, try variations like longer IPv6 notations (e.g., [::ffff:127.0.0.1]) or combine with URL encoding. If successful, chain to extract more data.

No command needed, but re-run Step 3 with adjustments.

**Expected Output**: Confirmation of internal access, e.g., reading a file or metadata.

**Success Indicators**:
- Response includes internal resource data without filter errors.
- No IPv4 block messages; IPv6 parsing succeeds on the server.
