---
id: 74000980-d4b4-45da-879d-ed603794af64
name: Bypass-PHP-Filter-Var-for-SSRF-Port-Scanning
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.609336+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network-Service-Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Bypass-filter-var-php-function]]'
  - '[[tags/Bypassing-filters]]'
  - '[[tags/Server-Side-Request-Forgery]]'
  - ssrf
  - php-bypass
  - port-scanning
commands:
  - '[[commands/curl-send-ssrf-payload]]'
platforms:
  - Web
  - PHP
tools:
  - '[[tools/URL-Port-Scanner]]'
validated: true
---

# Bypass-PHP-Filter-Var-for-SSRF-Port-Scanning

## Summary

This procedure outlines how to bypass PHP's filter_var() function to enable Server-Side Request Forgery (SSRF) attacks, allowing port scanning of internal systems via a vulnerable web application. By crafting invalid URL schemes and chaining multiple URLs, attackers can trick the filter into allowing requests to internal hosts and ports, facilitating discovery of open services not accessible from the internet.

## Description

Server-Side Request Forgery (SSRF) exploits occur when a web application fetches resources based on user-supplied input without proper validation. PHP's filter_var() function is commonly used to validate URLs but can be bypassed using malformed schemes like '0://' or by appending legitimate URLs with semicolons to chain requests. This technique enables attackers to use the application as a proxy to scan internal network ports, identifying services like databases or metadata endpoints (e.g., AWS IMDS). The target environment is typically a PHP-based web app with an SSRF vulnerability in features like image loaders or URL fetchers. Success allows internal reconnaissance without direct network access.

## Requirements

1. Access to a vulnerable PHP web application with an SSRF endpoint (e.g., a URL parameter that triggers server-side fetches).
2. Knowledge of the target's internal IP ranges (e.g., 10.0.0.0/8, 169.254.169.254 for AWS metadata).
3. [[tools/URL-Port-Scanner]] or equivalent tool for interpreting responses.
4. Network access to the external web app (no direct internal access needed).

## Defense

- Implement strict URL validation using whitelists for allowed domains/protocols and block private IP ranges (RFC 1918).
- Use network segmentation with firewalls to isolate internal services from web servers.
- Monitor application logs and network traffic for anomalous internal requests, such as port scans or metadata access.
- Enable Web Application Firewall (WAF) rules to detect SSRF patterns like invalid schemes or chained URLs.

## Objectives

1. Bypass PHP filter_var() to allow SSRF payloads targeting internal hosts.
2. Perform port scanning on internal systems to identify open services.
3. Gather intelligence on internal network architecture for further exploitation.

## Instructions

### Step 1: Identify the SSRF Endpoint

**Context**: Locate the vulnerable parameter in the web application that accepts user-controlled URLs for server-side fetching, such as a profile image loader or API endpoint.

Use manual testing or automated scanning to confirm the SSRF vulnerability. For example, test with a basic internal URL like http://127.0.0.1 to see if the app responds with internal content.

> No specific command needed here; use browser or proxy tools like Burp Suite to intercept and test requests.

### Step 2: Craft the Bypass Payload

**Context**: Create a malformed URL that evades filter_var() by using an invalid scheme ('0://') followed by a semicolon-separated chain to a benign external URL. This tricks the PHP filter into validating the chain as legitimate while allowing the invalid part to trigger the SSRF request to internal targets.

Use the following payload snippet [[codes/Invalid-Scheme-URL-for-Filter-Bypass]] as the base, substituting internal targets:

```powershell
0://$_INTERNAL_IP:$_PORT;http://google.com:80/
```

> Replace $_INTERNAL_IP with the target internal address (e.g., 10.0.0.1) and $_PORT with the port to scan (e.g., 80, 443, 3306). The '0://' scheme bypasses protocol checks, and the semicolon chain satisfies URL validation.

### Step 3: Send the SSRF Request and Scan Ports

**Context**: Inject the crafted payload into the vulnerable endpoint to force the server to request the internal resource. Analyze responses for open port indicators (e.g., HTTP 200 vs. timeout).

**Command** ([[commands/curl-send-ssrf-payload]]):
```bash
curl -X POST "http://$_TARGET_APP/ssrf-endpoint" -d "url=0://$_INTERNAL_IP:$_PORT;http://google.com:80/" -v
```

> This sends the bypass payload via POST to the SSRF endpoint. Iterate over ports (e.g., via a loop in a script) to scan. Use [[tools/URL-Port-Scanner]] to automate multi-URL/port testing. Expected output includes server responses revealing if the port is open (e.g., banner grabbing) or closed (error/timeout).

### Step 4: Interpret Results and Verify

**Context**: Review responses for success indicators, such as internal service banners or error messages indicating open ports. Chain findings to target discovered services.

Use tools like grep or the URL Port Scanner to parse outputs for keywords like "Apache", "MySQL", or connection successes.

> If the response includes content from the internal service, the port is open. Log results for further procedures like [[procedures/Exploit-Internal-Service-via-SSRF]].
