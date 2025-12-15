---
id: tool-uuid-3
url: 'https://www.ghostscript.com/'
tags:
  - postscript-interpreter
  - rce
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.777Z'
validated: true
submitted: true
---
# Ghostscript

**Status**: Unverified

## Overview

Ghostscript is a PostScript and PDF interpreter used by image libraries like ImageMagick for processing EPS files, vulnerable to RCE (e.g., CVE-2017-8291) when interpreting untrusted input from file uploads.

## Description

Integrated into server-side processing pipelines, it executes PostScript code, including embedded shell commands in vulnerable versions. Attackers exploit this by uploading files with '%!' headers containing payloads, leading to arbitrary command execution on the server.

## Features

- Feature 1: Interprets PostScript Level 1-3 and PDF
- Feature 2: Supports piping output to system commands (exploitable in old versions)
- Feature 3: SAFER mode to restrict file access and execution (enable for defense)

## Installation

### Requirements

- Unix-like OS
- Font libraries

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install ghostscript

# From source (use patched version)
wget https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10000/ghostscript-10.00.0.tar.gz
# ./configure && make install
```

## Basic Usage

```bash
gs input.ps
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Help |
| `-dSAFER` | Enable safe mode to block dangerous ops |

## Examples

### Example 1: Basic Usage

```bash
gs rce.ps  # Executes embedded commands if vulnerable
```

### Example 2: Advanced Usage

```bash
gs -sDEVICE=null -dNOPAUSE -dBATCH rce.ps  # Silent execution
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- gs process with untrusted input files
- Syslog entries for PostScript errors or executions
- Network anomalies post-image upload (e.g., pings to external hosts)

## Related Procedures

- [[procedures/Upload-Malicious-PostScript-as-Profile-Image]]

## Related Tools

- [[tools/ImageMagick]]
- [[tools/GraphicsMagick]]

## References

- Official documentation: https://www.ghostscript.com/doc/current/Use.htm
- CVE-2017-8291: https://nvd.nist.gov/vuln/detail/CVE-2017-8291
