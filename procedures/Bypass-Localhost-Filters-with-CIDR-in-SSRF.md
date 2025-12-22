---
type: procedure
description: >-
  Bypasses localhost restrictions in SSRF attacks by using CIDR notation and
  loopback IP variations to access internal resources.
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.349404+00:00'
updated_at: '2023-04-10T20:24:03.616156+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - bypassing-filters
  - bypass-localhost-cidr
  - ssrf
commands:
  - '[[commands/powershell-get-netipaddress-loopback]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Localhost-Filters-with-CIDR-in-SSRF

## Summary

This procedure demonstrates how to bypass filters blocking direct access to localhost (127.0.0.1 or ::1) in a Server-Side Request Forgery (SSRF) attack by leveraging CIDR notation and alternative representations of loopback IP addresses. By crafting requests that fall within the 127.0.0.0/8 range but avoid exact matches to blocked addresses, attackers can trick the server into making internal requests to sensitive resources like metadata services or databases.

## Description

In SSRF vulnerabilities, applications often implement filters to prevent requests to localhost to avoid internal pivoting. However, these filters may only block explicit mentions of 127.0.0.1 or 127.0.0.0/8 without considering variations like 127.127.127.127 or decimal equivalents. This procedure starts by enumerating loopback interfaces to understand available IPs, then uses crafted URLs in SSRF payloads to bypass restrictions. It targets web applications vulnerable to SSRF, such as those using user-supplied URLs for fetching resources. Successful execution allows access to internal endpoints, enabling data exfiltration or further network pivoting. This maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under Initial Access.

## Requirements

1. Valid SSRF vulnerability in the target application allowing user-controlled URL fetching.
2. Network access to the target web application.
3. PowerShell environment (Windows) to enumerate loopback IPs, or equivalent tools on other platforms.
4. Knowledge of the target's internal architecture to target specific localhost ports/services (e.g., port 80 for web servers, 169.254.169.254 for AWS metadata).

## Defense

- Implement strict URL validation and whitelisting to block private IP ranges (RFC 1918, loopback) using libraries like OWASP Java Encoder or URL parsing in backend code.
- Use network segmentation and firewalls to restrict internal requests from application servers.
- Enable logging of all outbound requests from the application server and monitor for anomalies like loopback traffic.
- Deploy Web Application Firewalls (WAFs) with SSRF-specific rules to detect and block crafted IP variations.

## Objectives

1. Enumerate loopback IP addresses to identify bypass candidates.
2. Craft SSRF payloads using CIDR-range IPs to evade localhost filters.
3. Access internal resources via the bypassed requests for reconnaissance or exfiltration.
4. Pivot to additional internal systems if successful.

## Instructions

### Step 1: Enumerate Loopback IP Addresses

**Context**: Begin by querying the system's network interfaces to retrieve loopback addresses. This helps identify the standard 127.0.0.1 (IPv4) and ::1 (IPv6), as well as confirming the 127.0.0.0/8 range reservation. Understanding these allows crafting variations that stay within the CIDR block but avoid direct blocks.

**Command** ([[commands/powershell-get-netipaddress-loopback]]):
```powershell
Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -like "127.*" }
```

> This command filters for IPv4 addresses starting with 127., displaying IP, prefix length, and interface details. It confirms the loopback range without routing to external networks. If no output appears, verify PowerShell execution policy allows the command.

**Expected Output**:
```
IPAddress         : 127.0.0.1
InterfaceAlias    : Loopback Pseudo-Interface 1
InterfaceIndex    : 1
AddressFamily     : IPv4
PrefixLength      : 8
PrefixOrigin      : WellKnown
SuffixOrigin      : WellKnown
```

### Step 2: Craft Bypass URLs Using Loopback Variations

**Context**: Using the enumerated loopback range, construct URL variations that represent localhost but may evade string-based or partial IP filters. Common bypasses include padding within the /8 subnet (e.g., 127.127.127.127), zero-padded (127.0.0.0), or alternative notations. Test these in the SSRF endpoint by submitting them as user-supplied URLs.

**Code** ([[codes/ssrf-localhost-bypass-urls]]):
```powershell
http://127.127.127.127
http://127.0.1.3
http://127.0.0.0
```

> These URLs target localhost equivalents. Submit them via the vulnerable SSRF parameter (e.g., in a GET/POST request). For example, if the app fetches images from a user-provided URL, use one of these to request http://127.127.127.127:80/internal-endpoint. Monitor responses for internal content leakage.

**Expected Output**: Successful bypass returns internal resource data (e.g., HTTP 200 with database query results or metadata XML/JSON). Failed attempts return 403/denied or external errors.

### Step 3: Test and Validate SSRF Payload

**Context**: Inject the crafted URLs into the SSRF-vulnerable endpoint and observe responses. If the filter is bypassed, the server will fetch from localhost, potentially exposing sensitive data. Iterate on variations if initial attempts fail, and target specific internal ports (e.g., append :8080 for admin panels).

**Instructions**: Use a proxy like Burp Suite to intercept and modify requests. Submit the URL (e.g., http://127.0.0.0:80/admin) and check the server's response for signs of internal access, such as error messages revealing backend paths or leaked data.

**Expected Output**: Response body containing internal content, like "Welcome to Internal Dashboard" or AWS instance metadata.

**Success Indicators**:
- Server processes the request and returns non-external content.
- No filter-triggered errors (e.g., "Localhost access denied").
- Ability to append ports or paths to reach specific services.
