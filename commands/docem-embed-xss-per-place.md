---
id: c8a8a953-a517-41cb-9f56-8477a322f785
name: docem-embed-xss-per-place
type: command
executor: bash
data: ./docem.py -s $_SAMPLE_FILE -pm xss -pf $_PAYLOAD_FILE -pt per_place
output: null
created_at: '2023-04-06T03:56:43.974220+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xss
  - embed
  - place
verified: true
validated: true
---

# docem-embed-xss-per-place

## Command

```bash
./docem.py -s $_SAMPLE_FILE -pm xss -pf $_PAYLOAD_FILE -pt per_place
```

## Description

Embeds XSS at specific locations within a document.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s $_SAMPLE_FILE | Sample file | Yes |
| -pm xss | XSS mode | Built-in |
| -pf $_PAYLOAD_FILE | Payload file | Yes |
| -pt per_place | Per place targeting | Built-in |

## Examples

### Basic Usage

```bash
./docem.py -s samples/xss_sample_0.odt -pm xss -pf payloads/xss_tiny.txt -pt per_place
```

## Expected Output

Document with targeted XSS insertion.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/Docem]]
