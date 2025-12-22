---
type: command
executor: bash
data: |
  eyewitness --web -f $_URL_FILE
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - web
created_at: '2020-07-24T17:11:37.846539+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
verified: true
validated: true
---

# eyewitness-screenshot-list-of-urls

## Command

```bash
eyewitness --web -f $_URL_FILE
```

## Description

This command uses Eyewitness to capture screenshots of multiple websites listed in a text file, using a headless Selenium browser. It is designed for batch reconnaissance when processing outputs from tools like httpx or Amass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --web | Run in headless web mode using Selenium/Chrome | Yes |
| -f | Path to the input file containing URLs (one per line) | Yes |
| $_URL_FILE | Text file with target URLs (e.g., http.txt) | Yes |

## Examples

### Basic Usage

```bash
eyewitness --web -f http.txt
```

### Advanced Usage

```bash
eyewitness --web -f http.txt --threads 5 --timeout 20
```

## Expected Output

Creates a screenshots/ directory with subfolders for each responsive hostname, each containing a PNG screenshot and JSON metadata. A top-level report.json summarizes all attempts, including successes, failures (e.g., timeouts, 404s), and statistics. Console logs progress per URL, e.g., "Processing https://example.com... Screenshot captured."

## Related

- [[procedures/Capture-Website-Screenshots-with-Eyewitness]]
- [[tools/eyewitness]]
