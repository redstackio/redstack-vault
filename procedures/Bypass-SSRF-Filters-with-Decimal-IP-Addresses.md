---
id: e52f47ab-2574-4e8d-a7ae-115f818ebd5d
name: Bypass-SSRF-Filters-with-Decimal-IP-Addresses
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.371859+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using a decimal IP location]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - bypass
commands:
  - '[[commands/python-convert-ip-to-decimal]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-SSRF-Filters-with-Decimal-IP-Addresses

## Summary

This procedure demonstrates how to bypass Server-Side Request Forgery (SSRF) filters that block standard dotted-notation IP addresses by converting target IPs to their decimal (integer) equivalents and using them in SSRF payloads. This technique evades simple regex-based filters that only check for formats like '127.0.0.1' while allowing numeric representations, enabling access to internal resources like metadata endpoints.

## Description

SSRF vulnerabilities allow attackers to force a server to make unauthorized requests to internal or external resources. Many applications implement basic filters to block requests to private IP ranges (e.g., 127.0.0.0/8, 192.168.0.0/16), but these often fail against alternative IP encodings like decimal notation. In decimal IP bypass, an IPv4 address is treated as a 32-bit integer (e.g., 127.0.0.1 becomes 2130706433), which can be embedded directly in URLs without dots. This procedure covers converting IPs to decimal and integrating them into SSRF payloads, typically tested against web applications with user-controlled URL parameters. It assumes a vulnerable endpoint like '/fetch?url=' and targets common internal services such as AWS instance metadata (169.254.169.254). Success grants access to restricted networks, potentially leading to further exploitation like data exfiltration or lateral movement.

## Requirements

1. Access to a web application with an SSRF vulnerability (e.g., a parameter that fetches external URLs).
2. Knowledge of the target internal IP address (e.g., localhost 127.0.0.1 or metadata service 169.254.169.254).
3. Python 3 installed on the attacker's machine for IP conversion.
4. Tools like curl or Burp Suite for sending test requests.
5. Network position allowing interaction with the vulnerable application (e.g., authenticated user or public endpoint).

## Defense

- Implement strict URL whitelisting and blacklist all private IP ranges using comprehensive regex that covers decimal, octal, hex, and other encodings.
- Use a Web Application Firewall (WAF) like ModSecurity with SSRF-specific rules to detect anomalous request patterns.
- Disable unnecessary internal service access from the application server and monitor outbound traffic for requests to metadata endpoints or private IPs.
- Validate and sanitize all user-supplied URLs, rejecting any that resolve to private networks via server-side DNS resolution.

## Objectives

1. Convert a target IP address to its decimal equivalent to evade SSRF filters.
2. Construct and send an SSRF payload using the decimal IP to access restricted internal resources.
3. Verify successful bypass by retrieving sensitive data, such as instance metadata.

## Instructions

### Step 1: Convert Target IP to Decimal Notation

**Context**: Begin by identifying the internal IP you want to target (e.g., 127.0.0.1 for localhost or 169.254.169.254 for AWS metadata). Use a Python one-liner to compute its decimal equivalent, which treats the IP as a 32-bit integer. This step ensures the payload avoids dotted notation filters.

**Command** ([[commands/python-convert-ip-to-decimal]]):
```bash
python3 -c "print(sum(int(octet) << (8*(3-i)) for i,octet in enumerate('$_TARGET_IP'.split('.'))))"
```

> This command outputs the decimal integer for the provided IP. For example, inputting '127.0.0.1' yields 2130706433. If the IP is invalid, it will raise a ValueError—verify the format before running. Common conversions include: 127.0.0.1 → 2130706433, 192.168.0.1 → 3232235521, 192.168.1.1 → 3232235777, 169.254.169.254 → 2852039166.

### Step 2: Construct SSRF Payload with Decimal IP

**Context**: Integrate the decimal IP into a URL for the vulnerable SSRF endpoint. Append the decimal value directly after the protocol (e.g., http://DECIMAL_IP/path). This bypasses filters expecting dotted IPs. Test against a parameter like ?url= or a fetch function.

**Command** ([[commands/python-convert-ip-to-decimal]]):
```bash
python3 -c "print(sum(int(octet) << (8*(3-i)) for i,octet in enumerate('$_TARGET_IP'.split('.'))))"
```

> Run the conversion command first to get the decimal (e.g., 2130706433 for localhost). Then, in your SSRF test (e.g., via curl): curl "http://vulnerable-app.com/fetch?url=http://2130706433/metadata". Replace with your endpoint and path. If using Burp Suite, intercept and modify the request body or query params accordingly.

### Step 3: Send Request and Verify Bypass

**Context**: Submit the payload to the vulnerable application and observe the response. Success indicates the server made the internal request on your behalf. Monitor for errors like 'invalid URL' (filter hit) vs. internal content (bypass success). If CAPTCHA or other challenges appear, solve them manually.

> Use tools like curl to send: curl -X POST "http://vulnerable-app.com/api/fetch" -d "url=http://$_DECIMAL_IP/$_PATH". Expected response includes internal data (e.g., XML from metadata). If blocked, try variations like http://0.0.0.0 (decimal 0) or combine with other bypasses (e.g., @ or #).

## Expected Output

- Step 1: A single integer output, e.g., '2130706433' for 127.0.0.1.
- Step 2: Valid SSRF URL like 'http://2130706433/latest/meta-data/'.
- Step 3: Server response containing internal resource data, such as AWS metadata JSON/XML, confirming the bypass.
