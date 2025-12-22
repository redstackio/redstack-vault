---
id: 8a2a0dae-8bb1-4eca-8fb8-206c556e686c
name: docem-embed-xss-per-document
type: command
executor: bash
data: >-
  ./docem.py -s $_SAMPLE_DIR -pm xss -pf $_PAYLOAD_FILE -pt per_document -kt -sx
  docx
output: null
created_at: '2023-04-06T03:56:43.974119+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xss
  - embed
  - document
verified: true
validated: true
---

# docem-embed-xss-per-document

## Command

```bash
./docem.py -s $_SAMPLE_DIR -pm xss -pf $_PAYLOAD_FILE -pt per_document -kt -sx docx
```

## Description

Embeds XSS payloads into a single document using Docem, for related injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s $_SAMPLE_DIR | Sample document or directory | Yes |
| -pm xss | Payload mode: XSS | Built-in |
| -pf $_PAYLOAD_FILE | Payloads file path | Yes |
| -pt per_document | Target: per document | Built-in |
| -kt | Keep template | Built-in |
| -sx docx | Supported extension: DOCX | Built-in |

## Examples

### Basic Usage

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt -pt per_document -kt -sx docx
```

## Expected Output

Modified DOCX with embedded XSS payload.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/Docem]]
