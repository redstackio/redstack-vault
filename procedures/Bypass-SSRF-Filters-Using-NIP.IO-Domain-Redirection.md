---
id: 96157cad-182b-49bb-8bfa-45cabb942cd6
name: Bypass-SSRF-Filters-Using-NIP.IO-Domain-Redirection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.330097+00:00'
updated_at: '2023-04-10T20:24:12.051464+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass localhost with a domain redirection]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - domain-redirection
commands:
  - '[[commands/curl-request-to-nip-io-for-ssrf-bypass]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-SSRF-Filters-Using-NIP.IO-Domain-Redirection

## Summary

This procedure demonstrates how to bypass Server-Side Request Forgery (SSRF) filters that block direct IP addresses by using NIP.IO, a dynamic DNS service, to create domain names that resolve to localhost (127.0.0.1) or an attacker's IP address. This allows attackers to redirect server requests to internal resources or external attacker-controlled servers, enabling data exfiltration, internal reconnaissance, or further exploitation.

## Description

Server-Side Request Forgery (SSRF) vulnerabilities occur when a web application fetches resources based on user-supplied input without proper validation, potentially allowing access to internal networks or metadata services. Many SSRF protections filter direct IP addresses (e.g., blocking 127.0.0.1 or 169.254.169.254 for AWS metadata), but they often overlook domain names. NIP.IO addresses this by providing wildcard DNS resolution where a domain like '127.0.0.1.nip.io' resolves to 127.0.0.1, and 'anything.192.168.1.100.nip.io' resolves to 192.168.1.100. This technique is particularly useful in cloud environments (e.g., AWS, Azure) to access instance metadata or pivot internally. The procedure assumes a vulnerable endpoint that accepts URL parameters for resource fetching, such as an image loader or API callback.

## Requirements

1. A vulnerable web application with an SSRF endpoint that processes user-supplied URLs but filters IPs.
2. Attacker's IP address (for external redirection) or target for localhost (e.g., 127.0.0.1 for internal access).
3. Access to a tool like curl for testing requests; no special privileges needed on the attacker side.
4. Knowledge of the vulnerable parameter (e.g., ?url= or ?redirect=).

## Defense

- Implement strict URL whitelisting to allow only trusted domains and block all others.
- Use network-level controls like WAF rules to inspect and block requests to private IP ranges, even via DNS resolution.
- Disable or restrict access to internal metadata endpoints (e.g., via IAM policies in cloud environments).
- Monitor server logs for unusual DNS resolutions or outbound requests to dynamic DNS services like nip.io.

## Objectives

1. Construct a domain name using NIP.IO that resolves to a blocked IP (e.g., localhost or attacker IP).
2. Inject the domain into the SSRF-vulnerable parameter to bypass filters.
3. Verify successful redirection by receiving a response from the target resource (e.g., internal file or metadata).

## Instructions

### Step 1: Construct NIP.IO Domain for Target IP

**Context**: Identify the IP you want to access (e.g., 127.0.0.1 for localhost metadata or your attacker's IP for exfiltration). Append it to .nip.io to create a resolvable domain. This step ensures the domain bypasses IP filters while resolving correctly on the server.

No command needed here; manually build the domain string, e.g., '127.0.0.1.nip.io' for localhost or 'myserver.192.168.1.100.nip.io' for a custom hostname on your IP.

> Verify resolution locally using nslookup or dig: the domain should resolve to the intended IP.

### Step 2: Test SSRF Bypass with Curl Request

**Context**: Send a request to the vulnerable endpoint, injecting the NIP.IO domain as the URL parameter. This tricks the server into making a request to the resolved IP, bypassing filters. Use Burp Suite or similar for interception if needed to modify responses.

**Command** ([[commands/curl-request-to-nip-io-for-ssrf-bypass]]):
```bash
curl "http://vulnerable-app.com/api/fetch?url=http://127.0.0.1.nip.io/internal-endpoint"
```

> This command sends a GET request to the SSRF endpoint, replacing 'vulnerable-app.com/api/fetch' with the actual path and 'internal-endpoint' with the target resource (e.g., /metadata for AWS). If successful, the server will fetch from 127.0.0.1 and return the content. Watch for HTTP 200 responses containing internal data.

### Step 3: Verify and Exfiltrate Data

**Context**: Analyze the response for success indicators like internal data leakage. If targeting an attacker IP, set up a listener (e.g., nc -lvnp 80) to capture the exfiltrated request.

No specific command; inspect the curl output or listener logs for sensitive information (e.g., AWS credentials from metadata).

> If the response includes expected internal content (e.g., XML metadata), the bypass succeeded. Iterate with different subdomains for pivoting.
