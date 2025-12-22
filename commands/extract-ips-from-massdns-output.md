---
id: 67677097-dd4e-4ee2-8135-2b502ffb25f3
type: command
executor: bash
data: >-
  cat $_MASSDNS_OUTPUT | awk '{print $3}' | sort -u | grep -oE
  "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > $_OUTPUT_FILE
output: >-
  root@hacker:~# cat massdns.out | awk '{print $3}' | sort -u | grep -oE
  "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > ips-online.txt

  104.22.26.77

  104.22.27.77

  172.67.10.39
created_at: '2020-06-30T05:03:09.607678+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - parsing
  - ip
verified: true
validated: true
---

# extract-ips-from-massdns-output

## Command

```bash
cat $_MASSDNS_OUTPUT | awk '{print $3}' | sort -u | grep -oE "\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b" > $_OUTPUT_FILE
```

## Description

Extracts unique IPv4 addresses from MassDNS results using regex.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MASSDNS_OUTPUT | Input file | Yes |
| $_OUTPUT_FILE | Output file | Yes |

## Examples

### Basic Usage

```bash
cat massdns.out | awk '{print $3}' | sort -u | grep -oE "\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b" > ips.txt
```

## Expected Output

IPv4 addresses, one per line.

## Related

- [[procedures/Resolve-and-Validate-Subdomains-with-MassDNS]]
