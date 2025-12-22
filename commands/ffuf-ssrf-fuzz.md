---
data: >-
  ffuf -w fuzz-urls-encoded.txt -u
  "https://app.bountypay.h1ctf.com/statements/?month=04&year=2020" -H "Cookie:
  token=FUZZ" -fw 5
tags:
  - ssrf
  - fuzzing
type: command
output: Discovery of /uploads/ with directory listing including BountyPay.apk
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.976Z'
id: a02e2925-9461-48fc-8153-aa8abc634905
verified: false
validated: true
submitted: true
---
# ffuf-ssrf-fuzz

## Command

```bash
ffuf -w fuzz-urls-encoded.txt -u "https://app.bountypay.h1ctf.com/statements/?month=04&year=2020" -H "Cookie: token=FUZZ" -fw 5
```

## Description

Fuzzes via SSRF by injecting payloads into cookie header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w` | Payload wordlist | Yes |
| `-H` | Custom header | Yes |
| `-fw 5` | Filter by word count | No |

## Examples

### Basic Usage

```bash
ffuf -w payloads.txt -H "Header: FUZZ" -u target
```

## Expected Output

Valid SSRF hits.

## Related

- [[tools/ffuf]]
