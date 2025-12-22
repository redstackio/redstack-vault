---
id: 94840ce6-2966-4590-aa19-e08ed98480dd
name: rcracki-mt
type: tool
verified: true
created_at: '2019-08-28T21:17:27.508128+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - hash-cracking
  - rainbow-tables
  - credential-access
url: 'https://github.com/viperman/rcracki-mt'
validated: true
---

# rcracki-mt

**Status**: Unverified

## Overview

rcracki_mt is an enhanced, multi-threaded version of the original rcrack tool, designed for fast cracking of password hashes using precomputed rainbow tables. It supports hybrid and indexed table formats, making it efficient for offline password recovery in security assessments, forensics, and penetration testing scenarios involving credential dumping.

## Description

Originally based on the RainbowCrack project, rcracki_mt extends the core functionality by adding multi-core CPU support, which significantly speeds up the cracking process on modern hardware. It is particularly useful for cracking hashes obtained from tools like Mimikatz or Responder in red team engagements. The tool works by loading rainbow tables (precomputed chain tables) and performing time-memory trade-off attacks to recover plaintext passwords without brute-forcing every possibility.

## Features

- Feature 1: Multi-threaded processing for utilization of all CPU cores, reducing cracking time by up to the number of cores available.
- Feature 2: Support for hybrid tables combining dictionary attacks with rainbow chains for better coverage of complex passwords.
- Feature 3: Indexed table support for faster lookups in large table sets.
- Feature 4: Batch processing of multiple hashes from files.
- Feature 5: Compatible with standard RainbowCrack table formats (.rt, .rtc).

## Installation

### Requirements

- GCC compiler and make utilities.
- 64-bit Linux system recommended for optimal performance.
- Sufficient RAM and storage for loading large rainbow tables (tables can be gigabytes in size).

### Install Commands

```bash
# On Ubuntu/Debian (including Kali)
sudo apt update
sudo apt install build-essential libssl-dev

# Clone and build from source
git clone https://github.com/viperman/rcracki-mt.git
cd rcracki-mt
make
sudo make install

# Alternative: If available in repos (check for your distro)
sudo apt install rcracki-mt
```

For Kali Linux, it may be available via `apt search rcrack` or built from source as shown.

## Basic Usage

```bash
rcracki_mt --help
```

This displays all available options, including table paths and hash formats.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --hash | Specify hash file |
| -d, --dir | Directory of rainbow tables |
| -t, --threads | Set number of threads |
| -l, --list | Process hash list file |
| -v, --verbose | Enable verbose output |

## Examples

### Example 1: Basic Usage

Crack a single MD5 hash using tables in a directory:

```bash
rcracki_mt -h hash.txt -d /path/to/rt_tables/
```

### Example 2: Advanced Usage

Process a batch of NTLM hashes with 8 threads:

```bash
rcracki_mt -l ntlm_hashes.txt -d /opt/rainbow/ntlm/ -t 8 -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for targeted cracking)
- [[Password Cracking]] Password Cracking (direct use for offline cracking)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for high CPU usage on systems with rainbow table directories (e.g., /opt/rainbow/).
- Detection method 2: Process monitoring for rcracki_mt binary or child processes spawning during hash cracking.
- Detection method 3: File system scans for large .rt or .rtc table files, which are unusual in production environments.
- Detection method 4: Audit logs showing compilation or execution of cracking tools post-breach.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rainbowcrack]]
- [[tools/Hashcat]]
- [[tools/john-the-ripper]]

## References

- Official GitHub Repository: https://github.com/viperman/rcracki-mt
- Original RainbowCrack Project: http://project-rainbowcrack.com/
- Usage Guide: Included in source README after installation
