---
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/126/670/cf76b4cbe40ddcc8efcba2e9f014423b3b49adb2/mmap_test.py?response-content-disposition=attachment%3B%20filename%3D%22mmap_test.py%22%3B%20filename%2A%3DUTF-8%27%27mmap_test.py&response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQYU4NBFHP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T112617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCICrNKIDV%2FAOmYWv4rK%2BaFSbEcMlZ5G6juWabdWG%2BQKtVAiA3cpX%2FHIMKkQqowFkB8P5Vi34843gsitwXdtmp5Fp68iqxBQg0EAMaDDAxMzYxOTI3NDg0OSIMQyPmlsduMqhCOOofKo4F6r7Teq6GXjAXaqsnad8RldjeZNI0BK3z%2FeYiuwxZpdmByIbZ3fzIa%2FDFNhz%2BZS%2FpHGm4wqwj%2BbmCWCiBcWest%2BffEWEtAxoypW%2FgQeoSr1h5Z3jAZhkNixwCL9EQsZnSnIAn7QpiahR55IWyLReU0SWFwgLfghOYH8qlO2vOC42FmpnCq1PpjJBKYBt1PkYqMfjxTm8rKOuMfhH8BRRUjv0o1LgUQgvcxgN%2FsLqQp47zDOZ8W345G9f1m2ZqbtI0MdwxTWuajX01lneJ0C8ya4gS6uzgdZNemwCZp1zwFWLfGNf%2B8MiExG4bEplW22dk%2F%2B2pIclf1i8BOPFn1BVHFur8xskXbOmRi%2BConO37WwGSo3d1icxWve%2Bdv2ll8%2BaJ2FMkwyVJPWyfE3%2FLKNeLugh1P4t03V7riJYKWrgkZs0J5g8QLuFeBVzE%2ByvcGHrsWmGVlavovGm%2BV1KIPC%2F88cKizfiL7PNU5Hc0Lchr4v9GnpRNeoGFhDZ8XMd%2BRztNAwXJu9wHNL2NYPcmN12uGVYlxdyOH5O7j5EWlw4so8kk3%2FBGWhjBb1WUfSzFa3EDu2ON7jBcG%2BgYbQQhKpdfv%2FeIJWjXnMVRJyWPprn8g5gIG%2Fg%2B0AJqZiBHz%2B9RyNnhlVBYkj7kUdHr0YlwJaVCv63O8z8QCLpMeGb%2ByGnRcLIvIDaAmDZqkkb91zfYsx7pTmaoFWWGXvClk4xbKorgw5hfAWeFJ5VgBZsE5VJ9H3IaQywFuJwHYEdAp5WTkghXV%2BS7R8mYa0dhL1ndta3Nqfu7h23h6x0N6JQ7qSX38RdT7urzMvpAMUVQuf5WwXGImjtCqeogU9KbHGznifmcUhL58m8TtIvU4n6HC7w0MPCf%2BskGOrIB5eF46m6x978x50ONUk9BC9bu4JuyDRgMIFJ56flOFkWzauzbBaKZgpvo%2FiwVIKLDzp7PJsTRIF6hQQFWwBAyzh%2BCN6TR8aHj2Nr3%2FNvb8K3wBwPzdAIv8aTpvSLnxxO8MWM6lw2QTBrmdED50amBgi976xk6pQp1uJnY%2Fpb0QnaBgqMoaoBNbx487f8As5Tv14ZaHs7U67TOdn78Y0LO%2BiBSJzFKCOXRa6AVIXspZBdRDg%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=8984add120c308ae744ab461b2ad2a65ece75ae35342ebd567ee7e02bfc7567a
tags:
  - exploit
  - python
  - mmap
type: tool
platforms:
  - Windows
  - Linux
description: >-
  Python script to demonstrate and exploit the mmap information disclosure
  vulnerability in Python 2.7.12.
id: f9b0c2a7-161f-46d1-bb9b-04ad3a00535f
created_at: '2025-12-14T17:25:13.160Z'
updated_at: '2025-12-14T17:25:13.160Z'
verified: false
validated: true
submitted: true
---
# mmap-test-py

**Status**: Unverified

## Overview

mmap_test.py is a Python script designed to demonstrate and exploit an information disclosure vulnerability in the mmap module of Python 2.7.12. It maps a file, resizes it to break invariants, performs out-of-bounds reads, and leaks data from adjacent memory pages, primarily tested on Windows 7 with Linux compatibility.

## Description

The script automates the vulnerability exploitation by creating an mmap object, shrinking it via resize() to cause pos > size, then using read() or readline() to bypass boundaries and access unauthorized memory. It's used in security audits to showcase memory leaks, potentially revealing sensitive data. No external dependencies beyond Python 2.7.12.

## Features

- Feature 1: File mapping and initial setup with controlled pos/size
- Feature 2: Invariant-breaking resize operation
- Feature 3: Boundary exploitation via read/readline with leak observation

## Installation

### Requirements

- Python 2.7.12
- Local file system access

### Install Commands

```bash
# Download the script from the provided URL
curl -o mmap_test.py "[URL]"
# Or save the content manually if URL expires
```

## Basic Usage

```bash
python mmap_test.py
```

### Common Options

| Option | Description |
|--------|-------------|
| None (script-based) | Runs the full demonstration sequence |

## Examples

### Example 1: Basic Usage

```bash
python mmap_test.py
```

> Executes the full exploit, printing leaked data or segfault details.

### Example 2: Advanced Usage

```bash
# Modify script for custom file/size if needed
python mmap_test.py customfile
```

> Assumes script accepts file arg; outputs memory leak on success.

## Expected Output

Leaked binary data from adjacent pages (e.g., b'\x00\x01...') or segfault message if no readable adjacent memory.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]
- [[Data from Local System]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor Python processes invoking mmap.resize() followed by large reads
- Detection method 2: Log segfaults in Python with mmap module traces

## Related Procedures


## Related Tools

- [[Python]]

## References

- HackerOne Report #174632: https://hackerone.com/reports/174632
