---
id: fc3ab3eb-c7da-481a-bbd8-a8a3b2e26c7e
name: docem-embed-xxe-per-place
type: command
executor: bash
data: ./docem.py -s $_SAMPLE_FILE -pm xxe -pf $_PAYLOAD_FILE -kt -pt per_place
output: null
created_at: '2023-04-06T03:56:43.974155+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xxe
  - embed
  - place
verified: true
validated: true
---

# docem-embed-xxe-per-place

## Command

```bash
./docem.py -s $_SAMPLE_FILE -pm xxe -pf $_PAYLOAD_FILE -kt -pt per_place
```

## Description

Embeds XXE payloads at specific places in a document for upload exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s $_SAMPLE_FILE | Sample file | Yes |
| -pm xxe | XXE mode | Built-in |
| -pf $_PAYLOAD_FILE | XXE payloads file | Yes |
| -kt | Keep template | Built-in |
| -pt per_place | Per place | Built-in |

## Examples

### Basic Usage

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod1.docx -pm xxe -pf payloads/xxe_special_2.txt -kt -pt per_place
```

## Expected Output

Modified file with XXE payload embedded.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/Docem]]
