---
type: tool
description: >-
  FAB (Files Already Bagged) is a Ruby tool for extracting metadata like authors
  and emails from files to generate custom wordlists for password cracking and
  reconnaissance.
url: 'https://github.com/digininja/CeWL'
tags:
  - wordlist-generation
  - metadata-extraction
  - reconnaissance
platforms:
  - Linux
  - Windows
  - macOS
verified: true
validated: true
---

# fab

**Status**: Unverified

## Overview

FAB (Files Already Bagged) is a command-line tool written in Ruby that analyzes metadata from various file types (e.g., PDFs, Microsoft Office documents) to extract names, authors, creators, and optionally emails. These extractions form custom wordlists useful for password cracking tools like John the Ripper or Hashcat, particularly in reconnaissance phases of security assessments.

## Description

As a companion to CeWL (which spiders websites for wordlists), FAB focuses on offline files already obtained by the attacker. It parses metadata fields to identify human-readable strings like names, which can reveal organizational structures or personal details for targeted attacks. Common use cases include processing leaked documents or internal files during post-exploitation to build dictionaries for credential attacks.

## Features

- Extracts author, creator, producer, and title metadata
- Filters output by minimum word length to reduce noise
- Supports batch processing of multiple files or directories
- Optional email address extraction for enhanced reconnaissance
- Outputs plain text wordlists compatible with cracking tools

## Installation

### Requirements

- Ruby 1.9 or higher
- Required gems: nokogiri, builder, mime-types (installed via CeWL setup)

### Install Commands

```bash
# On Kali Linux or Ubuntu (CeWL package includes FAB)
sudo apt update && sudo apt install cewl

# From source (recommended for latest version)
git clone https://github.com/digininja/CeWL.git
cd CeWL
# FAB is located in the root or bin/ directory; run with ruby fab.rb

# Verify installation
ruby fab.rb --help
```

For Windows/macOS, use Ruby installer and run from source.

## Basic Usage

```bash
fab --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --min WORDLENGTH | Set minimum word length (default: 3) |
| --output FILE | Specify output file (default: stdout) |
| --email | Include email addresses in extraction |
| --help | Show usage information |

## Examples

### Example 1: Basic Usage

Extract authors from PDF files:

```bash
fab --min 5 --output authors.txt document1.pdf document2.docx
```

### Example 2: Advanced Usage

Process a directory with emails:

```bash
fab --email --min 4 --output reconnaissance_wordlist.txt /path/to/leaked/files/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials]] Credentials In Files (for metadata-based credential guessing)
- [[Gather Victim Host Information]] Gather Victim Host Information (via document metadata)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Ruby processes (ruby.exe or ruby) accessing multiple document files
- Creation of text files with lists of names/emails in temporary directories
- File access patterns to metadata-heavy formats like .pdf, .docx
- Integration with cracking tools like john or hashcat in process trees

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/CeWL]] (Companion web spider for wordlists)
- [[tools/john-the-ripper]] (Password cracker using generated wordlists)

## References

- Official GitHub: https://github.com/digininja/CeWL
- CeWL Documentation: https://digi.ninja/projects/cewl.php
