---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
name: eyewitness-run-with-filename-and-timeout
type: command
executor: bash
data: ./EyeWitness.py -f $_FILENAME -t $_TIMEOUT --open
output: null
created_at: '2023-04-06T03:56:25Z'
updated_at: '2023-04-10T20:25:35Z'
platforms:
  - Linux
  - macOS
tags:
  - recon
  - screenshot
  - web
verified: true
validated: true
---

# eyewitness-run-with-filename-and-timeout

## Command

```bash
./EyeWitness.py -f $_FILENAME -t $_TIMEOUT --open
```

## Description

Runs EyeWitness on a file of URLs with a custom timeout and auto-opens the report.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f $_FILENAME | Input file with URLs/IPs (e.g., urls.txt) | Yes |
| -t $_TIMEOUT | Timeout per page in seconds (e.g., 10) | No |
| --open | Auto-open report in browser | No |

## Examples

### Basic Usage

```bash
./EyeWitness.py -f urls.txt -t 10 --open
```

## Expected Output

Starting EyeWitness scan...
Screenshotting http://sub.example.com...
Report generated: /reports/2023-04-10_12-00-00.html
Opening in browser...

## Related

- [[procedures/Subdomain-Enumeration-with-Knockpy-and-EyeWitness]]
