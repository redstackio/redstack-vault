---
url: 'https://digi.ninja/projects/fdb.php'
tags:
  - reconnaissance
  - parsing
  - macos
type: tool
platforms:
  - Web
  - macOS
description: >-
  Online tool for parsing macOS .DS_Store files to extract folder metadata, file
  paths, and directory structures.
id: 6e4e776b-b9c1-41c1-a6c6-f6b574e4105a
created_at: '2025-12-14T17:25:13.036Z'
updated_at: '2025-12-14T17:25:13.036Z'
verified: false
validated: true
submitted: true
---
# DS_Store Parser

**Status**: Unverified

## Overview

The DS_Store Parser is a web-based tool designed to analyze and extract information from macOS .DS_Store files, commonly used in security testing to uncover hidden directory structures and file paths exposed on misconfigured web servers.

## Description

.DS_Store files store metadata about folders, including file positions, icons, and paths. This tool parses the binary format to output human-readable directory trees, aiding in reconnaissance for information disclosure vulnerabilities. It's particularly useful for pentesting web apps where macOS artifacts are inadvertently left public.

## Features

- Feature 1: Upload and parse .DS_Store files to generate directory listings
- Feature 2: Visualize folder hierarchies and file attributes
- Feature 3: Export parsed data for further analysis

## Installation

### Requirements

- Web browser with file upload support
- No local installation needed (online tool)

### Install Commands

N/A (web-based)

## Basic Usage

Visit https://digi.ninja/projects/fdb.php and upload the .DS_Store file.

### Common Options

| Option | Description |
|--------|-------------|
| Upload | Select and submit .DS_Store file for parsing |
| View Output | Display tree structure post-parsing |

## Examples

### Example 1: Basic Usage

1. Download .DS_Store from target (e.g., curl https://target.com/.DS_Store -o file.ds)
2. Upload to https://digi.ninja/projects/fdb.php
3. View generated directory tree

### Example 2: Advanced Usage

Parse multiple files sequentially to map chained directories (e.g., root then /Packages).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing uploads to digi.ninja
- Parsing of .DS_Store files in web access logs

## Related Procedures


## Related Tools

- [[Python DSStore Library]]
- [[Hex Editors for Manual Parsing]]

## References

- Official page: https://digi.ninja/projects/fdb.php
- macOS .DS_Store format docs
