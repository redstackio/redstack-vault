---
id: 4546a697-6309-4f2b-a63a-56e5096a8907
type: command
executor: bash
data: >-
  cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $2}' | sort -u >
  $_OUTPUT_FILE
output: >
  104.22.26.77,104.22.27.77,172.67.10.39

  104.22.26.77,172.67.10.39,104.22.27.77

  104.22.27.77,104.22.26.77,172.67.10.39

  104.22.27.77,172.67.10.39,104.22.26.77

  172.67.10.39,104.22.26.77,104.22.27.77

  172.67.10.39,104.22.27.77,104.22.26.77

  172.67.10.39,2606:4700:10::6816:1a4d,104.22.26.77,104.22.27.77,2606:4700:10::ac43:a27,2606:4700:10::6816:1b4d

  2606:4700:10::ac43:a27,172.67.10.39,104.22.27.77,104.22.26.77,2606:4700:10::6816:1b4d,2606:4700:10::6816:1a4d
created_at: '2020-06-30T04:31:50.451916+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - parsing
  - ip-extraction
verified: true
validated: true
---

# extract-ips-from-amass-output

## Command

```bash
cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $2}' | sort -u > $_OUTPUT_FILE
```

## Description

Extracts unique IPs from Amass results.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RESULTS_FILE | Input file | Yes |
| $_OUTPUT_FILE | Output file | Yes |

## Examples

### Basic Usage

```bash
cat amass.txt | cut -d']' -f2 | awk '{print $2}' | sort -u > ips.txt
```

## Expected Output

Unique IPs, comma-separated or per line.

## Related

- [[procedures/Enumerate-Subdomains-with-Amass]]
