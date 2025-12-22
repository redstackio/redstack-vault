---
id: 084daad2-801a-4ba4-8a5f-d44fcac9d317
name: docem-embed-xss-per-file
type: command
executor: bash
data: >-
  ./docem.py -s $_SAMPLE_DIR -pm xss -pf $_PAYLOAD_FILE -pt per_file -kt -sx
  docx
output: null
created_at: '2023-04-06T03:56:43.974322+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xss
  - embed
  - file
verified: true
validated: true
---

# docem-embed-xss-per-file

## Command

```bash
./docem.py -s $_SAMPLE_DIR -pm xss -pf $_PAYLOAD_FILE -pt per_file -kt -sx docx
```

## Description

Embeds XSS payloads into all files in a directory using Docem.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s $_SAMPLE_DIR | Sample directory | Yes |
| -pm xss | XSS mode | Built-in |
| -pf $_PAYLOAD_FILE | Payload file | Yes |
| -pt per_file | Per file targeting | Built-in |
| -kt | Keep template | Built-in |
| -sx docx | DOCX extension | Built-in |

## Examples

### Basic Usage

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt -pt per_file -kt -sx docx
```

## Expected Output

Batch of modified files with XSS.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/Docem]]
