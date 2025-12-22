---
tags:
  - ntlm
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ntlm-trigger-get-request]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1dc230a8-d792-411a-adda-88247d292909
created_at: '2025-12-14T17:31:19.116Z'
updated_at: '2025-12-14T17:31:19.116Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Trigger-NTLM-Challenge-via-HTTP-Request

## Summary

This procedure exploits misconfigured Windows Authentication on IIS web servers to trigger an NTLM challenge response via a crafted HTTP request, disclosing encoded internal information without requiring user credentials or a login prompt.

## Description

In scenarios where internal web applications use hidden NTLM authentication, attackers can force a challenge by including an 'Authorization: NTLM' header in a GET request to protected endpoints. This bypasses typical login flows due to server misconfiguration, returning a base64-encoded NTLM Type 2 message in the WWW-Authenticate header. The attack targets environments like MTN Group's internal blogs, revealing network details upon decoding.

## Requirements

1. Network access to the target web server (HTTP/HTTPS on port 80/443)
2. Proxy tool like Burp Suite for request crafting and interception
3. Knowledge of protected paths (e.g., /fr/Pages/ on internal sites)

## Defense

Defensive measures and detection strategies:

- Disable unnecessary Windows Authentication or enforce prompt-based auth
- Monitor for anomalous Authorization headers in IIS logs
- Use WAF rules to block NTLM header injections on public-facing paths

## Objectives

1. Initiate NTLM handshake to obtain challenge blob
2. Avoid authentication prompts for stealthy reconnaissance
3. Collect encoded data for further decoding and analysis

## Instructions

### Step 1: Craft and Send Request

**Context**: Use Burp Suite to modify an intercepted request or create a new one targeting a protected endpoint, adding the NTLM header to trigger the challenge.

**Command** ([[commands/ntlm-trigger-get-request]]):
```bash
GET /fr/Pages/ HTTP/1.1
Host: target-internal-server
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Authorization: NTLM
```

> This command sends a GET request with an empty NTLM authorization to invoke the server's challenge. Expected output is a 401 Unauthorized response with WWW-Authenticate: NTLM <base64-encoded-challenge>.

### Step 2: Intercept Response

**Context**: Capture the full response in Burp Suite to access the WWW-Authenticate header for decoding in the next procedure.

**Command** (No direct command; use Burp Repeater):
```bash
# In Burp: Forward request and inspect response headers
```

> Verify the presence of the NTLM challenge in the header. Success if encoded blob is returned without redirecting to login.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information

### Sub-Techniques

- None

## Commands Used

- [[commands/ntlm-trigger-get-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ntlm
- web-auth-bypass
