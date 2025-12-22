---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
name: eyewitness-run-web-scan
type: command
executor: bash
data: ./EyeWitness.py -f $_FILENAME --web
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

# eyewitness-run-web-scan

## Command

```bash
./EyeWitness.py -f $_FILENAME --web
```

## Description

Runs EyeWitness in web scanning mode on a list of URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f $_FILENAME | Input file with URLs (e.g., urls.txt) | Yes |
| --web | Enable web screenshot mode | Yes |

## Examples

### Basic Usage

```bash
./EyeWitness.py -f urls.txt --web
```

## Expected Output

Web scan initiated...
Captured 5 screenshots.
Report: /reports/web-report.html

## Related

- [[procedures/Subdomain-Enumeration-with-Knockpy-and-EyeWitness]]
