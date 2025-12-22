---
id: 09185716-0859-446e-86fb-9cbcc5657a80
name: amass-intel-ip-cidr-enumeration
type: command
executor: bash
data: amass intel -ip -cidr $_CIDR_RANGE -o $_OUTPUT_FILE
output: |-
  r.cloudfront.net 13.224.13.184
  domain2.example.com 13.224.10.50
created_at: '2020-06-29T16:32:10.894203+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - osint
verified: true
validated: true
---

# amass-intel-ip-cidr-enumeration

## Command

```bash
amass intel -ip -cidr $_CIDR_RANGE -o $_OUTPUT_FILE
```

## Description

This command uses Amass's intel module to enumerate domain names associated with IP addresses in a specified CIDR range through passive OSINT sources. It is ideal for initial reconnaissance to map network blocks to organizational assets without active scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ip | Enable IP address gathering mode | Yes |
| -cidr $_CIDR_RANGE | Specify the CIDR IP range to enumerate (e.g., 13.224.8.0/21) | Yes |
| -o $_OUTPUT_FILE | Output file for results (e.g., domains.txt); defaults to stdout if omitted | No |

## Examples

### Basic Usage

```bash
amass intel -ip -cidr 13.224.8.0/21
```

Enumerates domains for the CIDR and prints to console.

### Advanced Usage

```bash
amass intel -ip -cidr 13.224.8.0/21 -o results.txt -timeout 30
```

Includes timeout for longer queries and saves to file.

## Expected Output

Description of what output to expect when the command runs successfully.

Sample output shows domain-IP pairs from public sources:

```
r.cloudfront.net 13.224.13.184
another.domain.com 13.224.12.100
```

If no domains are found, output may be empty. Errors indicate invalid CIDR or tool issues.

## Related

- [[procedures/Enumerate-Domains-from-CIDR-IP-Range-Using-Amass]]
- [[tools/amass]]
