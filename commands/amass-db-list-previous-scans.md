---
type: command
executor: bash
data: amass db -dir $_OUTPUT_DIRECTORY -list
output: >-
  root@kali ~# amass db -dir owasp.org/ -list

  1) 06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT: owasp.org, 2.ip6.arpa,
  178.in-addr.arpa, 159.in-addr.arpa


  2) 06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT: owasp.org,
  178.in-addr.arpa, 2.ip6.arpa, 159.in-addr.arpa


  3) 06/29 13:22:13 2020 EDT -> 06/29 13:24:55 2020 EDT: 159.in-addr.arpa,
  2.ip6.arpa, 178.in-addr.arpa, owasp.org
tags:
  - reconnaissance
  - dns
  - amass
platforms:
  - Linux
verified: true
validated: true
---

# amass-db-list-previous-scans

## Command

```bash
amass db -dir $_OUTPUT_DIRECTORY -list
```

## Description

This command lists all previous Amass enumeration scans stored in the database directory, displaying details like timestamps, durations, and associated domains or zones. Use it to review historical reconnaissance sessions before querying specific results.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OUTPUT_DIRECTORY | Path to the directory containing Amass .db files (e.g., /path/to/output/) | Yes |
| -list | Flag to list all scans in the database | Yes (built-in) |

## Examples

### Basic Usage

```bash
amass db -dir /home/user/owasp-output/ -list
```

### Advanced Usage

If combining with other db options, ensure the directory path is absolute to avoid errors.

```bash
amass db -dir ./recon-output/ -list
```

## Expected Output

A numbered list of scans, each showing start time, end time, and involved domains. For example:

```
root@kali ~# amass db -dir owasp.org/ -list
1) 06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT: owasp.org, 2.ip6.arpa, 178.in-addr.arpa, 159.in-addr.arpa

2) 06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT: owasp.org, 178.in-addr.arpa, 2.ip6.arpa, 159.in-addr.arpa

3) 06/29 13:22:13 2020 EDT -> 06/29 13:24:55 2020 EDT: 159.in-addr.arpa, 2.ip6.arpa, 178.in-addr.arpa, owasp.org
```

Success is indicated by the presence of scan entries; an empty output means no prior scans in the directory.

## Related

- [[procedures/Query-Amass-Database-for-Previous-Scans-and-Assets]]
- [[commands/amass-db-display-assets-from-scan]]
