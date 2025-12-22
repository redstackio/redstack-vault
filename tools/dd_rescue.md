---
id: 9a4b0d23-b558-4024-98d8-4d3dfefe666d
type: tool
verified: true
created_at: '2019-08-28T21:17:38.113954Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - data-recovery
  - forensics
  - disk-imaging
url: 'https://www.gnu.org/software/ddrescue/'
validated: true
---

# dd_rescue

**Status**: Unverified

## Overview

GNU ddrescue (often referred to as dd_rescue) is a data recovery tool designed to copy data from failing or damaged block devices or files to a good one. It is similar to the Unix dd command but excels in handling read errors by retrying problematic areas without aborting the entire process, making it invaluable for forensic imaging of compromised or corrupted storage media in security operations.

## Description

dd_rescue copies data bidirectionally between files or block devices, supporting features like seeking to specific positions, non-abortive error handling, and adaptive block sizes. Unlike dd, it does not perform character set conversions and uses a different syntax. It maintains a mapfile to track copied, non-tried, and error areas, allowing interrupted copies to resume. This tool is commonly used in incident response for creating forensic images of disks that may contain malware artifacts, deleted files, or evidence of data exfiltration attempts.

## Features

- Feature 1: Error-tolerant copying with automatic retries and fallback to smaller block sizes on errors.
- Feature 2: Support for mapfiles to resume interrupted operations and avoid recopying successful areas.
- Feature 3: Direct and sparse I/O modes for optimized performance on block devices.
- Feature 4: Bidirectional copying (forward or reverse) and partial copies with skip/size limits.
- Feature 5: No truncation of output files unless explicitly requested.

## Installation

### Requirements

- Linux kernel with block device support.
- Standard build tools (gcc, make) for compilation from source.

### Install Commands

```bash
# On Debian/Ubuntu (Kali Linux included)
sudo apt update
sudo apt install gddrescue

# On Fedora/RHEL
sudo dnf install ddrescue

# From source (if needed)
wget https://ftp.gnu.org/gnu/ddrescue/ddrescue-1.28.tar.lz
make
sudo make install
```

## Basic Usage

```bash
ddrescue --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -V, --version | Display version information |
| -d, --direct | Use direct disk access for faster I/O |
| -r, --retry-passes=N | Number of retry passes for bad sectors (default 0) |
| -b, --block-size=BYTES | Set block size (default 512 bytes) |
| -s, --skip=BYTES | Skip this many bytes at start |
| -n, --max-retries=N | Maximum number of retries per block |

## Examples

### Example 1: Basic Usage

```bash
ddrescue /dev/sda damaged_image.img mapfile.log
```

### Example 2: Advanced Usage

```bash
ddrescue -d -r3 -b 4096 /dev/sda damaged_image.img mapfile.log
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System (forensic imaging of local storage)
- [[Data from Removable Media]] Data from Removable Media (imaging USB or external drives)

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for ddrescue executions during incident response.
- Detection method 2: Log analysis for high I/O activity on block devices.
- Detection method 3: Presence of mapfile.log or similar artifacts in working directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/DD]]
- [[tools/testdisk]]

## References

- Official documentation: https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html
- Related resources: https://linux.die.net/man/1/ddrescue
