---
type: procedure
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - bypassing-filters
  - unicode-bypass
  - ssrf
commands:
  - '[[commands/curl-basic-ssrf-payload]]'
  - '[[commands/curl-unicode-ssrf-payload]]'
tools:
  - '[[tools/cURL]]'
platforms:
  - web
verified: true
validated: true
---

# Unicode Bypass of Server-Side Request Forgery Filters

## Summary

This procedure demonstrates how to bypass server-side request forgery (SSRF) filters by replacing ASCII digits in target URLs with Unicode digit equivalents, such as Thai numerals. This evades naive filters that check for numeric patterns without handling Unicode normalization, allowing access to internal resources like localhost or cloud metadata services.

## Description

SSRF vulnerabilities occur when a web application fetches external resources based on user-controlled input without proper validation. Defenses often include blacklisting internal IPs (e.g., 127.0.0.1 or 169.254.169.254 for AWS metadata) by detecting ASCII digits or specific patterns. By using Unicode characters that visually and semantically represent digits (e.g., Thai digits U+0E50–U+0E59), the payload can bypass these checks if the filter does not decode or normalize Unicode. This technique is effective against custom or poorly implemented filters in web applications, leading to unauthorized internal network access, data exfiltration, or further exploitation. It assumes the SSRF endpoint accepts URL parameters and the backend HTTP client resolves the Unicode-encoded URL correctly.

## Requirements

1. Access to a web application with an SSRF vulnerability (e.g., an endpoint that fetches URLs from POST data).
2. [[tools/cURL]] or a similar HTTP client capable of sending POST requests with Unicode characters.
3. Knowledge of the target internal resource (e.g., IP address like 127.0.0.1 for localhost testing or 169.254.169.254 for cloud metadata).
4. A testing environment where Unicode in URLs is preserved (e.g., UTF-8 encoding).

## Defense

- Normalize all URL inputs to NFKC form or ASCII before validation to collapse Unicode equivalents.
- Implement allowlist-based URL validation instead of blocklists, restricting to external domains only.
- Use a web application firewall (WAF) with Unicode decoding capabilities to inspect payloads.
- Log and monitor for non-ASCII characters in URL parameters and internal request attempts.

## Objectives

1. Identify and confirm an SSRF endpoint with digit-based filtering.
2. Craft and submit a Unicode-encoded payload to evade the filter.
3. Successfully retrieve data from an internal resource, demonstrating bypass.

## Instructions

### Step 1: Test Basic SSRF with Standard ASCII Payload

**Context**: Verify the SSRF vulnerability exists and that filters block standard internal IPs containing ASCII digits. This establishes a baseline for the filter's behavior.

**Command** ([[commands/curl-basic-ssrf-payload]]):
```bash
curl -X POST $_SSRF_ENDPOINT -d "url=http://127.0.0.1"
```

> This attempts to fetch from localhost. If the filter is active, expect a block (e.g., 403 Forbidden or "Invalid URL"). If vulnerable without filtering, you may receive an internal response like a 200 OK with localhost content. Adjust the data format (e.g., JSON) based on the endpoint's requirements.

### Step 2: Map and Prepare Unicode Digit Equivalents

**Context**: Replace each ASCII digit in the target IP with a corresponding Unicode digit to create a bypass payload. This step ensures the filter sees non-ASCII characters, evading pattern matches like IP address regex limited to 0-9.

Use the Thai Unicode digit sequence for reference: [[codes/thai-unicode-digit-sequence]] provides ๐(0), ๑(1), ๒(2), ๓(3), ๔(4), ๕(5), ๖(6), ๗(7), ๘(8), ๙(9). For example:
- 127.0.0.1 becomes 127.๐.๐.๑
- 169.254.169.254 becomes ๑๖๙.๒๕๔.๑๖๙.๒๕๔ (full replacement for stricter filters)

Why this works: Many filters use simple string checks or ASCII-only regex (e.g., /\d{1,3}/), which fail on Unicode. Test encoding in your client to ensure preservation.

### Step 3: Submit Unicode-Encoded SSRF Payload

**Context**: Send the modified payload to the SSRF endpoint. Success indicates the bypass worked, as the server resolves the Unicode URL to the internal IP.

**Command** ([[commands/curl-unicode-ssrf-payload]]):
```bash
curl -X POST $_SSRF_ENDPOINT -d 'url=http://127.๐.๐.๑'
```

> Expect a successful internal response (e.g., HTTP 200 with localhost or metadata content) if the bypass succeeds. If still blocked, try full digit replacement or alternative Unicode blocks (e.g., Arabic-Indic digits U+0660–U+0669). Verify by checking server logs or response content for internal data.
