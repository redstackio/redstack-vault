---
id: 495ecec7-0b5a-41ba-9936-44e6db15c15b
name: run-linenum-stealth-keyword-report-thorough
type: command
executor: bash
data: ./LinEnum.sh -s -k $_KEYWORD -r $_REPORT_NAME -e /tmp/ -t
output: null
created_at: '2023-04-06T03:56:18.414246+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - reporting
verified: true
validated: true
---

# run-linenum-stealth-keyword-report-thorough

## Command

```bash
./LinEnum.sh -s -k $_KEYWORD -r $_REPORT_NAME -e /tmp/ -t
```

## Description

Runs LinEnum in stealth mode with keyword search, report generation, and thorough tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Stealth mode | Yes |
| -k $_KEYWORD | Keyword to search | Yes |
| -r $_REPORT_NAME | Report name | Yes |
| -e /tmp/ | Output directory | Yes |
| -t | Thorough tests | Yes |

## Examples

### Basic Usage

```bash
./LinEnum.sh -s -k sudo -r linenum_report -e /tmp/ -t
```

## Expected Output

Report generated in /tmp/linenum_report.html with highlighted keyword matches.

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/LinEnum]]
