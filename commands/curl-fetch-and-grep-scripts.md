---
id: cmd-uuid-9012
data: 'curl -s https://target-site.com | grep -i ''<script src="https?://[^/]*\.'''
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:13.889Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-and-grep-scripts

## Command

```bash
curl -s https://target-site.com | grep -i '<script src="https?://[^/]*\.'
```

## Description

This command fetches the HTML source of a target website using curl and uses grep to identify script tags with external sources, helping to detect potential XSS vectors from third-party JavaScript inclusions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode to suppress progress meter | Yes |
| `https://target-site.com` | URL of the target page | Yes |
| `grep -i '<script src="https?://[^/]*\.'` | Regex pattern to match external script src attributes (case-insensitive) | Yes |

## Examples

### Basic Usage

```bash
curl -s https://stellar.org | grep -i '<script src="https?://[^/]*\.'
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" https://target.com/page | grep -E '<script[^>]*src=["\']https?://[^/]*\.' > external-scripts.txt
```

## Expected Output

Lines showing external script tags, such as:

<script src="https://analytics.example.com/js/tracker.js"></script>

This indicates third-party scripts that could bypass same-origin policy.

## Related

- [[Related Procedure: Identify-and-Exploit-External-JavaScript-XSS]]
