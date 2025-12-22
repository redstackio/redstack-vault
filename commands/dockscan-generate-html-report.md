---
id: 16ba5c52-efc0-4def-bb92-fd04cd452cbd
name: dockscan-generate-html-report
type: command
executor: bash
data: 'dockscan -r html -o myreport -v tcp://example.com:5422'
output: null
created_at: '2023-04-06T03:56:16.860223+00:00'
updated_at: '2023-04-10T20:33:48.514623+00:00'
platforms:
  - Linux
tags:
  - docker
  - reporting
verified: true
validated: true
---

# dockscan-generate-html-report

## Command

```bash
dockscan -r html -o myreport -v tcp://example.com:5422
```

## Description

This command scans the Docker environment and generates an HTML report, pulling vulnerability data from a remote database for comprehensive analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r html | Output format as HTML | Yes |
| -o myreport | Output filename for the report | Yes |
| -v tcp://example.com:5422 | Vulnerability database endpoint | Yes |

## Examples

### Basic Usage

```bash
dockscan -r html -o myreport -v tcp://example.com:5422
```

### Advanced Usage

Combine with socket: dockscan unix:///var/run/docker.sock -r html -o report.html -v tcp://db:port

## Expected Output

Generates 'myreport.html' with sections on vulnerabilities, affected containers, and remediation steps. Sample: "High Risk: 3 CVEs found in image X."

## Related

- [[procedures/Docker-Security-Assessment]]
- [[commands/dockscan-basic-scan]]
