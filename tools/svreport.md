---
id: d8b9d0ea-c630-4caf-a7b2-500c3cf0ed8a
type: tool
verified: true
description: >-
  svreport is a reporting tool within the SIPVicious suite, used to generate
  formatted reports from SIP audit scans, supporting HTML, CSV, and XML outputs
  for analyzing VoIP security assessments.
url: 'https://github.com/EnableSecurity/sipvicious'
created_at: '2019-08-28T21:17:38.824828+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - voip
  - sip
  - reconnaissance
  - reporting
commands:
  - '[[commands/svreport-generate-html-report]]'
  - '[[commands/svreport-generate-csv-report]]'
validated: true
---

# svreport

**Status**: Unverified

## Overview

svreport is part of the SIPVicious suite, a set of open-source tools for auditing SIP-based VoIP systems. Specifically, svreport processes output from other SIPVicious tools (like svmap, svwar, or svcrack) to generate human-readable reports in various formats. It is commonly used in penetration testing to summarize scan results, such as discovered SIP devices, active extensions, or brute-force attempts, making it easier to review findings without parsing raw logs.

## Description

The SIPVicious suite audits VoIP infrastructure by scanning for SIP devices, identifying extensions, cracking passwords, and generating reports. svreport focuses on the reporting aspect: it takes session files or scan outputs as input and exports them to formats like HTML for web viewing, CSV for data analysis, or XML for integration with other tools. This is essential for red team operations targeting PBX systems, as it helps document reconnaissance and enumeration phases efficiently.

## Features

- Feature 1: Supports multiple output formats (HTML, CSV, XML) for flexible reporting.
- Feature 2: Parses SIPVicious session data to summarize key findings like active extensions and response codes.
- Feature 3: Handles large scan outputs, filtering and organizing data for quick review.

## Installation

### Requirements

- Python 3.6+
- Git (for cloning the repository)

### Install Commands

```bash
# Clone the EnableSecurity fork (recommended, as original is outdated)
git clone https://github.com/EnableSecurity/sipvicious.git
cd sipvicious

# Install via setup.py
python setup.py install

# Alternatively, via pip (may require dependencies)
pip install sipvicious
```

On Kali Linux, it may be available via apt: `sudo apt install sipvicious`

## Basic Usage

```bash
svreport --help
```

This displays available options, including input file specification and output formats.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -o, --output | Specify output file path |
| -f, --format | Output format (html, csv, xml) |
| -i, --input | Input file path (default: stdin) |

## Examples

### Example 1: Basic Usage

Generate an HTML report from a svwar scan output:

```bash
svreport svwar_results.txt -o report.html
```

### Example 2: Advanced Usage

Export to CSV for spreadsheet analysis:

```bash
svreport extensions_scan.txt -o data.csv -f csv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Used to process and report on SIP service scans.
- [[Network Service Scanning]] Network Service Scanning: Summarizes VoIP enumeration results.

### Tactics

- [[Reconnaissance]] Reconnaissance: Aids in documenting discovery of VoIP infrastructure.

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of SIPVicious Python modules in process lists or logs (e.g., `ps aux | grep svreport`).
- Detection method 2: Generated report files (e.g., .html or .csv with SIP extension data) on audited systems or attacker machines.
- Detection method 3: Network logs showing SIP OPTIONS/INVITE probes followed by report generation activity.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/svmap]]
- [[tools/svwar]]
- [[tools/svcrack]]

## References

- Official GitHub: https://github.com/EnableSecurity/sipvicious
- Original SIPVicious: https://github.com/sipvicious/sipvicious (archived)
- VoIP Security Auditing Guide: https://www.owasp.org/index.php/OWASP_VoIP_Project
