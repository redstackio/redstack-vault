---
id: 37be8a3c-735c-42ce-ba40-c0d868f90073
name: cutycapt
type: tool
verified: true
created_at: '2019-08-28T21:17:33.257250+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-capture
  - screenshot
  - utility
url: 'http://cutycapt.sourceforge.net/'
validated: true
---

# cutycapt

**Status**: Unverified

## Overview

CutyCapt is a cross-platform command-line utility that uses QtWebKit to render and capture web pages into various formats such as PNG, PDF, JPEG, and more. In security testing, it's commonly used for automated screenshotting of web applications during reconnaissance, documentation of vulnerabilities, or verifying page states without manual browser interaction.

## Description

CutyCapt leverages WebKit's rendering engine to produce high-fidelity captures of web content, supporting JavaScript execution and CSS rendering. It's lightweight and scriptable, making it suitable for integration into penetration testing workflows, such as batch-capturing pages for visual diffing or archiving evidence.

## Features

- Feature 1: Supports multiple output formats including PNG, PDF, JPEG, TIFF, GIF, BMP, SVG, and PS.
- Feature 2: Configurable viewport size, delays for dynamic content, and JavaScript inclusion.
- Feature 3: Cross-platform compatibility with minimal dependencies on Qt libraries.

## Installation

### Requirements

- Qt4 or Qt5 libraries (including QtWebKit).
- Build tools like cmake and a C++ compiler for source compilation.

### Install Commands

```bash
# On Ubuntu/Debian (Kali Linux included)
sudo apt update
sudo apt install cutycapt

# On macOS with Homebrew
brew install cutycapt

# On Windows: Download pre-built binary from SourceForge or compile using Qt Creator
# Source: http://cutycapt.sourceforge.net/
```

For source installation:

```bash
# Clone and build (requires Qt development packages)
git clone https://github.com/acrisci/CutyCapt.git
cd CutyCapt
qmake-qt4
make
sudo make install
```

## Basic Usage

```bash
cutycapt --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --url | Specify the URL to capture |
| --out | Output file path |
| --delay | Wait time in seconds before capture |
| --min-width | Minimum viewport width in pixels |
| --format | Output format (default: PNG) |

## Examples

### Example 1: Basic Usage

```bash
cutycapt --url=https://example.com --out=screenshot.png
```

### Example 2: Advanced Usage

```bash
cutycapt --url=https://example.com --delay=5 --min-width=1200 --out=page.pdf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (for web page reconnaissance)
- [[Search Victim-Owned Websites]] Search Open Technical Databases (web content capture for analysis)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for 'cutycapt' executable.
- Detection method 2: Network traffic showing automated HTTP requests from QtWebKit user-agent.
- Detection method 3: File system artifacts like generated PNG/PDF files in temp directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/webkit2png]]
- [[tools/phantomjs]]

## References

- Official website: http://cutycapt.sourceforge.net/
- GitHub repository: https://github.com/acrisci/CutyCapt
- QtWebKit documentation for advanced rendering options.
