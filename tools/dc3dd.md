---
id: 10b78e38-2000-4c25-b2e3-98e604b02ee9
name: dc3dd
type: tool
verified: true
created_at: '2019-08-28T21:17:38.372687+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - forensics
  - imaging
  - hashing
  - data-acquisition
url: 'https://github.com/libyal/dc3dd'
validated: true
---

# dc3dd

**Status**: Unverified

## Overview

dc3dd is an enhanced version of the GNU dd command tailored for computer forensics and data acquisition. It supports on-the-fly hashing, error logging, pattern wiping, progress reporting, and output splitting, making it essential for creating verifiable disk images, sanitizing media, and handling large-scale data transfers in security investigations.

## Description

dc3dd extends the core functionality of dd by adding forensic-specific features. It is commonly used in offensive security for exfiltrating data with integrity checks, wiping traces during post-exploitation, or acquiring evidence in red team operations. Key enhancements include simultaneous computation of multiple hash algorithms (MD5, SHA-1, SHA-256, SHA-512), grouping and logging of read/write errors, customizable pattern-based wiping, real-time progress indicators, and automatic splitting of output files to manage large datasets.

## Features

- **On-the-Fly Hashing**: Compute MD5, SHA-1, SHA-256, or SHA-512 hashes during read/write operations for data integrity verification.
- **Error Handling**: Write read/write errors to a separate log file and group similar errors to reduce noise in analysis.
- **Pattern Wiping**: Overwrite data with repeating patterns (e.g., zeros, ones, or custom bytes) for secure sanitization.
- **Progress Reporting**: Display transfer progress, speed, and ETA in real-time.
- **Output Splitting**: Automatically split large output files into manageable segments based on size.

## Installation

### Requirements

- Linux/Unix-based system (e.g., Kali Linux, Ubuntu)
- Build tools (gcc, make) for compilation from source

### Install Commands

```bash
# On Kali Linux (pre-installed in many forensic distros)
sudo apt update && sudo apt install dc3dd

# On Ubuntu from source
git clone https://github.com/libyal/dc3dd.git
cd dc3dd
./configure && make && sudo make install

# On macOS via Homebrew (if available) or compile from source
brew install dc3dd  # If tap exists, otherwise build manually
```

## Basic Usage

```bash
dc3dd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| --version | Display version information |
| if=FILE | Input file or device |
| of=FILE | Output file or device |
| hash=ALGO | Compute hash (md5, sha1, sha256, sha512) |
| log=FILE | Error log file |
| split=SIZE | Split output into blocks of SIZE (e.g., 1G) |
| pat=PATTERN | Use PATTERN for wiping |
| progress=on | Enable progress reporting |

## Examples

### Example 1: Basic Usage

Create a simple disk image:

```bash
dc3dd if=/dev/sdb of=usb_image.img
```

### Example 2: Advanced Usage

Image with hashing and error logging:

```bash
dc3dd if=/dev/sda1 of=partition.img hash=md5 sha256 log=acquisition_errors.log progress=on
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System (for forensic imaging in post-exploitation)
- [[Data Destruction]] Data Destruction (for pattern wiping to cover tracks)

### Tactics

- [[Discovery]] Discovery (data acquisition)
- [[Exfiltration]] Exfiltration (verifiable data transfer)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for dc3dd executions with high I/O activity
- Log entries for unusual disk reads/writes or hash computations
- File system changes: creation of .img files or error logs with dc3dd signatures
- Network transfers of large split files if used for exfiltration

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/DD]] (Base tool without forensic enhancements)
- [[ftk-imager]] (GUI-based forensic imaging alternative)

## References

- Official GitHub: https://github.com/libyal/dc3dd
- Documentation: https://github.com/libyal/dc3dd/blob/main/documentation/README.md
