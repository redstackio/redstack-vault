---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - >-
    [[techniques/Exploitation for Defense Evasion|T1211 - Exploitation for
    Defense Evasion]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypassing using DNS Rebinding (TOCTOU)]]'
  - '[[tags/Server-Side Request Forgery]]'
commands:
  - '[[commands/construct-dns-rebinding-domain]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# DNS-Rebinding-for-SSRF-Bypass

## Summary

This procedure demonstrates how to use DNS rebinding in conjunction with a Server-Side Request Forgery (SSRF) vulnerability to bypass network filters and access internal systems. By constructing a domain that initially resolves to an attacker-controlled IP and then rebinds to an internal IP, the vulnerable server can be tricked into making unauthorized requests to restricted resources, potentially leading to data exfiltration or further compromise.

## Description

DNS rebinding attacks exploit the fact that browsers and servers may cache DNS resolutions briefly, allowing a domain to resolve to different IPs over time. In an SSRF context, an attacker crafts a malicious URL using a rebinding domain. When the vulnerable server fetches the URL, it first resolves to the attacker's server (to bypass same-origin checks or filters), then rebinds to an internal IP (e.g., 169.254.169.254 for AWS metadata). This technique is effective against applications that validate external URLs but fail to re-validate after DNS changes. It targets web applications with SSRF vulnerabilities, such as those using user-supplied URLs for image fetching or API calls. Success enables access to internal services like metadata endpoints, databases, or admin panels, facilitating credential theft, lateral movement, or full network compromise.

## Requirements

1. A vulnerable web application with an SSRF flaw allowing server-side HTTP requests to attacker-controlled domains.
2. Control over a DNS rebinding service or the ability to construct rebinding domains (e.g., via 1u.ms).
3. Knowledge of target internal IPs (e.g., 127.0.0.1 for localhost, 169.254.169.254 for cloud metadata).
4. Attacker server to host initial response (e.g., to return benign content or JavaScript).
5. Network access to submit requests to the vulnerable application.

## Defense

- Deploy a Web Application Firewall (WAF) configured to detect SSRF patterns, such as requests to private IPs or rapid DNS changes.
- Isolate internal systems by ensuring they are not reachable from public-facing servers; use network segmentation and firewall rules to block outbound requests to private ranges.
- Implement DNS filtering and sinkholing for known rebinding domains; enforce strict DNS resolution policies with short TTLs and validation.
- Sanitize and validate all user-supplied URLs in server-side requests, blocking private IPs and using allowlists for permitted domains.
- Monitor server logs for anomalous outbound requests to internal resources and enable DNS query logging to detect rebinding attempts.

## Objectives

1. Bypass domain validation filters in SSRF-vulnerable applications to access internal network resources.
2. Retrieve sensitive data from internal endpoints, such as cloud instance metadata or administrative interfaces.
3. Establish a foundation for lateral movement or credential access within the target network.
4. Evade detection by mimicking legitimate external requests initially.

## Instructions

### Step 1: Construct the DNS Rebinding Domain

**Context**: Create a domain name that rotates between your attacker-controlled IP (initial resolution) and the target internal IP (rebound resolution). This uses the 1u.ms service, which generates rebinding domains based on a specific naming convention. The initial IP should be yours to host a benign page, while the rebound IP targets internals like localhost or metadata services.

**Command** ([[commands/construct-dns-rebinding-domain]]):
```bash
echo "make-$_ATTACKER_IP-rebind-$_INTERNAL_IP-rr.1u.ms"
```

> This command outputs the formatted domain string. Replace placeholders with actual IPs (e.g., your public IP for $_ATTACKER_IP and 169.254.169.254 for $_INTERNAL_IP). Visit http://1u.ms/ manually if needed to verify the format, but the constructed string can be used directly. The '-rr' enables round-robin rotation, causing the DNS to alternate resolutions quickly (typically within 30 seconds due to short TTLs).

**Expected Output**: A domain like "make-203.0.113.1-rebind-169.254.169.254-rr.1u.ms", ready for use in SSRF payloads.

### Step 2: Host Initial Response on Attacker Server

**Context**: Set up a simple web server on your IP to respond to the first request from the vulnerable server. This could be a benign image or JSON to pass initial validation, preventing immediate blocking.

**Instructions**: Use a tool like Python's HTTP server or nginx to serve content at the root path. Ensure the response mimics expected content (e.g., a 1x1 pixel image if the SSRF is for image loading).

**Expected Output**: When the vulnerable server requests http://[rebind-domain]/, it receives your hosted content without errors.

### Step 3: Craft and Submit SSRF Payload

**Context**: Inject the rebinding domain into the vulnerable application's SSRF endpoint (e.g., a URL parameter for fetching external resources). The server will first resolve to your IP, pass filters, then re-resolve to the internal IP, allowing access to restricted resources.

**Instructions**: Identify the SSRF input (e.g., ?url= or an API endpoint). Submit a request like http://[rebind-domain]/internal-path. Monitor your server logs for the initial hit, then check for internal access indicators (e.g., metadata response).

**Expected Output**: Initial request to your server succeeds; subsequent rebound request returns internal data, such as AWS IMDS JSON with credentials.

### Step 4: Verify and Exfiltrate Data

**Context**: Confirm the rebound worked by observing if internal data is returned or proxied through your server (if configured to forward). Extract any sensitive information like tokens or configs.

**Instructions**: If the application echoes responses, capture them; otherwise, use the access to pivot (e.g., request internal APIs).

**Expected Output**: Successful access to internal endpoint, e.g., HTTP 200 with metadata like {"UserData": "...", "InstanceId": "..."}.

**Success Indicators**:
- Domain resolves correctly to both IPs (test with dig or nslookup multiple times).
- Vulnerable server makes initial request to attacker IP without blocking.
- Internal data is retrieved post-rebind, indicating bypass success.
