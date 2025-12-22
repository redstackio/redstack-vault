---
id: tool-nuclei-2024
url: 'https://vulners.com/nuclei/NUCLEI:CVE-2022-35653'
tags:
  - scanning
  - vulnerability
  - yaml
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.412Z'
validated: true
submitted: true
---
# Nuclei

**Status**: Unverified

## Overview

Nuclei is a fast, customizable vulnerability scanner that uses YAML-based templates to detect issues like XSS, SSRF, and CVEs by sending crafted HTTP requests and matching responses.

## Description

Nuclei excels in offensive security for automated recon and vuln detection. It supports HTTP, DNS, and other protocols, with templates for specific CVEs like CVE-2022-35653. In this context, it's used to probe Moodle's LTI module for reflected XSS by posting payloads and checking reflections.

## Features

- Feature 1: YAML template-driven scans for reproducibility
- Feature 2: High-speed parallel requests for large targets
- Feature 3: Custom matchers for response body, headers, and status codes

## Installation

### Requirements

- Go 1.17+ installed
- Git for template repositories

### Install Commands

```bash
# Installation command
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

## Basic Usage

```bash
nuclei --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --target` | Single URL to scan |
| `-t, --templates` | Path to templates directory |
| `-v, --verbose` | Enable verbose logging |

## Examples

### Example 1: Basic Usage

```bash
nuclei -u https://target.com -t cves/
```

### Example 2: Advanced Usage

```bash
nuclei -u https://target.com -t cves/2022/CVE-2022-35653.yaml -v -o results.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Reconnaissance]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing rapid HTTP POST requests with encoded payloads
- Process monitoring for 'nuclei' binary on scanning hosts
- Template YAML files in /root/.config/nuclei-templates/

## Related Procedures

- [[procedures/Scan-for-Moodle-LTI-Reflected-XSS-Using-Nuclei]]

## Related Tools

- [[Burp Suite]]
- [[ZAP]]

## References

- Official documentation: https://nuclei.projectdiscovery.io/
- Related resources: https://github.com/projectdiscovery/nuclei-templates
