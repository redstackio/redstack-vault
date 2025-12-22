---
id: 9f2eceb7-fc26-4571-88c4-ac998cdd2bf3
name: Octal-IP-Format-SSRF-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.395129+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - ssrf
  - bypass-filters
  - octal-ip
commands:
  - '[[commands/awk-convert-octal-ip-to-decimal]]'
platforms:
  - Web
tools: []
validated: true
---

# Octal-IP-Format-SSRF-Bypass

## Summary

This procedure demonstrates how to use octal IP address formatting to bypass IP-based filters in Server-Side Request Forgery (SSRF) attacks, allowing requests to internal or blocked resources like localhost (127.0.0.1) by representing it as 0177.0.0.1. It includes converting octal IPs to decimal for verification and crafting SSRF payloads that evade simple string-based blocking.

## Description

Server-Side Request Forgery (SSRF) vulnerabilities allow attackers to make unauthorized requests from a vulnerable server to arbitrary destinations, often internal services. Many applications implement basic filters to block requests to private IPs (e.g., 127.0.0.1, 10.0.0.0/8) by checking for decimal string matches. Using octal notation (base-8), where each octet ranges from 0 to 377, attackers can represent the same IP differently—e.g., 127 in octal is 0177—bypassing these filters if the backend parses the IP numerically rather than as a string. This technique is effective against misconfigured web applications, proxies, or cloud metadata endpoints. The target environment is typically a web application with an SSRF vuln exposed via user input like URL parameters. Prerequisites include identifying the SSRF endpoint through fuzzing or manual testing. Expected outcomes include successful internal requests, such as accessing localhost services or cloud metadata (e.g., http://169.254.169.254/latest/meta-data/ in AWS).

## Requirements

1. Access to a vulnerable web application endpoint susceptible to SSRF (e.g., via a feature that fetches external URLs).
2. Knowledge of the target internal IP or resource to reach (e.g., localhost or metadata service).
3. Tools for sending HTTP requests, such as curl or Burp Suite.
4. Basic understanding of IP address formats and octal conversion.

## Defense

- Implement proper input validation and sanitization to restrict SSRF by whitelisting allowed domains and blocking all private IP ranges at the parsing level, not just string matching.
- Use libraries that normalize IP formats (e.g., convert octal/decimal/hex to canonical form before validation).
- Configure firewalls and WAFs to block SSRF patterns, including non-standard IP notations.
- Monitor server logs for anomalous internal requests and implement rate limiting on URL fetching features.

## Objectives

1. Bypass IP-based filters to perform SSRF against internal resources.
2. Access protected services like localhost or cloud metadata endpoints.
3. Verify the bypass by converting and testing octal IP payloads.

## Instructions

### Step 1: Convert Octal IP to Decimal for Verification

**Context**: Before crafting SSRF payloads, verify the octal representation of the target IP by converting it to decimal. This ensures the notation will resolve correctly on the server side. Use the awk command to perform the conversion, as many networking stacks interpret leading zeros as octal.

**Command** ([[commands/awk-convert-octal-ip-to-decimal]]):
```bash
echo '0177.0.0.1' | awk -F. '{printf "%d.%d.%d.%d\n",$1,$2,$3,$4}'
```

This command takes an octal IP as input and outputs the decimal equivalent. For example, input '0177.0.0.1' should output '127.0.0.1', confirming the mapping.

### Step 2: Craft and Test SSRF Payload with Octal IP

**Context**: Identify the SSRF-vulnerable parameter (e.g., a 'url' query in an API endpoint). Replace the blocked decimal IP with its octal equivalent in the payload. Test variations like 0177.0.0.1, o177.0.0.1, or 0o177.0.0.1, as parser support varies. Send the request using curl or a proxy tool, targeting a localhost service (e.g., /admin).

**Instructions**: Use curl to send a GET request to the vulnerable endpoint with the octal IP payload. For example:
```bash
curl "http://vulnerable-app.com/fetch?url=http://0177.0.0.1/admin"
```

Expected behavior: The server fetches from localhost/admin and returns the response, bypassing any '127.*' string filter.

### Step 3: Handle Variations and Edge Cases

**Context**: If the basic octal fails, try prefixed variations (o177, 0o177, q177) or pad octets to 3 digits (e.g., 0177.000.000.001). Test against the target resource, such as cloud metadata, and monitor responses for success.

**Instructions**: Iterate payloads in a tool like Burp Intruder:
- http://0177.0.0.1/
- http://o177.0.0.1/
- http://0o177.0.0.1/
- http://q177.0.0.1/

Verify by checking if internal content (e.g., server banners or metadata) appears in the response.
