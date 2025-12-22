---
id: 83193d0d-4b9c-4278-87a9-95a88b26f905
name: pdgmail
type: tool
verified: true
created_at: '2019-08-28T21:17:27.327944+00:00'
updated_at: '2023-10-01T12:00:00+00:00'
platforms:
  - Linux
tags:
  - forensics
  - memory-analysis
  - gmail
  - digital-forensics
url: 'https://tools.kali.org/information-gathering/pdgmail'
commands:
  - '[[commands/pdgmail-extract-gmail-artifacts]]'
validated: true
---

# pdgmail

**Status**: Unverified

## Overview

pdgmail is a Python-based forensic tool designed to extract Gmail artifacts from a process memory dump, specifically targeting the 'pd' process (likely referring to a Pidgin or similar client process interacting with Gmail). It recovers valuable data such as contacts, email content, last access times, and IP addresses, making it essential for incident response and digital forensics in investigations involving email client memory analysis.

## Description

The tool parses memory dumps to identify and reconstruct Gmail-related structures, including user contacts, partial email messages, session timestamps, and network artifacts like IP addresses used in Gmail communications. It is particularly useful in red team post-exploitation scenarios for analyzing captured memory or in blue team forensics to investigate compromised email clients. pdgmail operates offline on the dump file and does not require live system access, supporting investigations into data exfiltration or persistence via email services.

## Features

- Contact extraction: Recovers Gmail contact lists with names and email addresses.
- Email content recovery: Pulls subjects, bodies, and metadata from memory.
- Timestamp analysis: Extracts last access and session times for Gmail interactions.
- IP address identification: Identifies IPs associated with Gmail logins or data transfers.
- Output to structured files: Saves artifacts in readable text formats for further analysis.

## Installation

### Requirements

- Python 3.x
- Dependencies: Typically includes standard libraries; may require additional modules like `struct` for binary parsing (installed via pip if needed).
- Kali Linux (pre-configured environment recommended).

### Install Commands

```bash
# On Kali Linux (pre-installed in /usr/share/pdgmail/)
# If not present, clone from repository or install via apt
sudo apt update
sudo apt install pdgmail

# Manual installation from source
git clone https://gitlab.com/kalilinux/packages/pdgmail.git
cd pdgmail
sudo make install
```

## Basic Usage

```bash
pdgmail --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -o, --output | Specify output directory for artifacts |
| -v, --verbose | Enable verbose logging during extraction |

## Examples

### Example 1: Basic Usage

```bash
python3 /usr/share/pdgmail/pdgmail.py /path/to/memory_dump.dmp -o ./extracted_artifacts
```

This extracts all Gmail artifacts from the memory dump and saves them to the `./extracted_artifacts` directory.

### Example 2: Advanced Usage

```bash
python3 /usr/share/pdgmail/pdgmail.py /path/to/memory_dump.dmp -o ./artifacts --verbose
```

Runs with verbose output to monitor the extraction process in real-time.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System (for memory dump analysis in Collection)
- [[Process Discovery]] Process Discovery (identifying processes like 'pd' for artifact extraction)

### Tactics

- [[Collection]] Collection (gathering email and contact data from memory)
- [[Impact]] Impact (forensic analysis in incident response)

## Detection

Indicators and methods for detecting this tool's usage:

- File system artifacts: Presence of pdgmail.py or extracted files like contacts.txt in working directories.
- Process monitoring: Python processes executing pdgmail.py with memory dump arguments.
- Log analysis: Command-line logs showing pdgmail invocations in bash history or audit logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/volatility]] (General memory forensics framework)
- [[rekall]] (Advanced memory analysis tool)
- [[strings]] (Basic string extraction from binaries)

## References

- Official Kali Documentation: https://tools.kali.org/information-gathering/pdgmail
- GitLab Repository: https://gitlab.com/kalilinux/packages/pdgmail
- Related Forensic Guides: Memory Forensics for Email Clients
