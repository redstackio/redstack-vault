---
id: 9658e9f6-7e90-4d6e-aa5b-0715413f1c4f
type: tool
verified: true
created_at: '2019-08-28T21:17:24.800530Z'
updated_at: '2023-05-29T16:48:53.029709Z'
platforms:
  - Linux
tags:
  - forensics
  - data-extraction
  - investigation
url: 'https://github.com/simsong/bulk_extractor'
commands:
  - '[[commands/bulk_extractor-basic-file-extraction]]'
  - '[[commands/bulk_extractor-directory-scan]]'
  - '[[commands/bulk_extractor-specific-scanner-disk-image]]'
validated: true
---

# bulk_extractor

**Status**: Unverified

## Overview

bulk_extractor is a forensic tool designed to extract structured information such as email addresses, credit card numbers, URLs, and other features from digital evidence files, disk images, or directories. It is commonly used in security investigations, including malware analysis, intrusion detection, identity theft probes, and cybercrime examinations. In offensive security contexts, it aids red teams in post-exploitation data collection by rapidly identifying valuable artifacts without relying on file system parsing.

## Description

bulk_extractor processes input data in pages using multiple scanners, handling compressed, fragmented, or corrupted files (e.g., ZIP, PDF, GZIP, JPEGs, RAR archives). It excels at carving files from unallocated space, building wordlists for password cracking, and generating histograms of common features like domains or search terms. The tool is multi-threaded for performance on multi-core systems and outputs results in easily parsable feature files. It includes a GUI viewer (Bulk Extractor Viewer) for browsing results and Python scripts for further analysis. Unlike traditional tools, it ignores file system structures to avoid parsing errors on damaged media.

## Features

- Feature 1: Extracts features from compressed and fragmented data, including emails, URLs, and credit cards missed by other tools.
- Feature 2: Builds comprehensive wordlists and histograms for password cracking and pattern analysis.
- Feature 3: Multi-threaded processing for faster scans on large datasets.
- Feature 4: Supports carving of files like JPEGs and Office documents from raw data.
- Feature 5: Includes GUI for result visualization and Python utilities for post-processing.

## Installation

### Requirements

- Linux system with GCC, libewf, and libexpat development libraries.
- Approximately 100MB disk space for binaries and dependencies.

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install bulk-extractor

# From source (GitHub)
git clone https://github.com/simsong/bulk_extractor.git
cd bulk_extractor
./bootstrap
./configure
make
sudo make install
```

## Basic Usage

```bash
bulk_extractor --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -V, --version | Display version information |
| -o | Specify output directory for feature files |
| -e | Run specific scanner (e.g., -e email) |
| -R | Recursively process directories |
| -j | Number of threads for multi-core processing |

## Examples

### Example 1: Basic Usage

Scan a single file for all features:

```bash
bulk_extractor -o output_dir input_file.pdf
```

### Example 2: Advanced Usage

Scan a disk image with specific scanners and threading:

```bash
bulk_extractor -e email -e url -j 4 -o output_dir disk.img
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System
- [[Local Data Staging]] Data from Local System: Local Data Staging

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for bulk_extractor binary execution via process monitoring (e.g., Sysmon Event ID 1) or audit logs showing file access patterns on evidence directories.
- Detection method 2: Look for output directories with feature files like *.txt histograms or wordlists in temporary locations.
- Detection method 3: Network logs if used in conjunction with exfiltration tools, though bulk_extractor itself is offline.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/volatility]]
- [[tools/autopsy]]

## References

- Official GitHub: https://github.com/simsong/bulk_extractor
- Documentation: https://github.com/simsong/bulk_extractor/blob/master/doc/bulk_extractor_user_guide.md
- Related resources: NIST Computer Forensics Tool Testing Program
