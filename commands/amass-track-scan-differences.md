---
id: 8fc6e5a0-bc2d-4a64-8dff-2d05f181e603
name: amass-track-scan-differences
type: command
executor: bash
data: amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2
output: "root@kali ~# amass track -dir owasp.org/ -d owasp.org -last 2\n--------------------------------------------------------------------------------\nBetween\t06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT\nand\t06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT\n--------------------------------------------------------------------------------\nNo differences discovered"
created_at: '2020-06-29T18:05:44.398305+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - dns
  - reconnaissance
  - amass
verified: true
validated: true
---

# amass-track-scan-differences

## Command

```bash
amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2
```

## Description

This command uses Amass to track and diff DNS scan results between previous enumerations stored in a directory. It compares the specified number of latest scans (default last 2) for a given domain and outputs any differences, such as newly discovered subdomains. Use this during follow-up assessments to identify changes in the target's DNS infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-dir $_OUTPUT_DIRECTORY` | Path to the directory containing Amass database files from prior scans | Yes |
| `-d $_TARGET_DOMAIN` | The target domain to compare scans for (e.g., example.com) | Yes |
| `-last 2` | Number of most recent scans to compare (2 for the last two) | No (default is last 2) |

## Examples

### Basic Usage

```bash
amass track -dir /path/to/scans -d example.com -last 2
```

Compares the two most recent scans for example.com and shows differences.

### Advanced Usage

```bash
amass track -dir /path/to/scans -d example.com -last 3 > differences.txt
```

Compares the last three scans and redirects output to a file for analysis.

## Expected Output

Description of what output to expect when the command runs successfully.

If no differences:
```
root@kali ~# amass track -dir owasp.org/ -d owasp.org -last 2
--------------------------------------------------------------------------------
Between	06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT
and	06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT
--------------------------------------------------------------------------------
No differences discovered
```

If differences exist, it would list added/removed domains with timestamps.

## Related

- [[procedures/Track-Differences-in-DNS-Scans-Using-Amass]]
- [[tools/amass]]
