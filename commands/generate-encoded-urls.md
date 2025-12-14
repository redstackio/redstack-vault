---
data: >-
  cat ./SecLists/Discovery/Web-Content/common.txt | while read line; do
  ./soft-urls.sh "https://software.bountypay.h1ctf.com/${line}?"; done >
  fuzz-urls-encoded.txt
tags:
  - payload-generation
type: command
output: File with base64-encoded cookie values for fuzzing
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.991Z'
id: d1cc1524-d0d4-4e3e-b32b-ecd4ace08cf4
verified: false
validated: true
submitted: true
---
# generate-encoded-urls

## Command

```bash
cat ./SecLists/Discovery/Web-Content/common.txt | while read line; do ./soft-urls.sh "https://software.bountypay.h1ctf.com/${line}?"; done > fuzz-urls-encoded.txt
```

## Description

Generates base64-encoded payloads for SSRF fuzzing using a custom script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Wordlist | Input paths | Yes |

## Examples

### Basic Usage

```bash
cat wordlist | while read; do script "$url"; done > output.txt
```

## Expected Output

Encoded file for ffuf.

## Related

- Custom soft-urls.sh
