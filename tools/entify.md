---
id: 9eb6dd53-3777-4d39-ab46-54e77b1d4afe
type: tool
verified: true
created_at: '2019-08-28T21:17:28.164736+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - entity-extraction
  - reconnaissance
url: 'https://github.com/i3visio/osrframework'
validated: true
---

# entify

**Status**: Unverified

## Overview

Entify is a Python script within the OSRFramework suite designed for extracting entities from text data. It uses regular expressions to identify and pull out items like email addresses, phone numbers, URLs, and other structured information. Commonly used in OSINT operations for processing scraped content, logs, or documents to uncover hidden contact details and links.

## Description

OSRFramework provides a collection of tools for Open Source Intelligence gathering, and entify.py specifically focuses on entity recognition and extraction. It supports various input formats, including files and stdin, and can filter by entity type. This makes it valuable for reconnaissance phases where analysts need to quickly parse large volumes of unstructured text for actionable intelligence. Entify integrates well with other OSRFramework tools for username checks, DNS lookups, and more, enabling comprehensive OSINT workflows.

## Features

- Feature 1: Extracts multiple entity types (emails, phones, URLs, IP addresses) using predefined regex patterns.
- Feature 2: Supports batch processing of files or real-time stdin input for pipeline integration.
- Feature 3: Customizable output formats and entity filtering to focus on specific data types.
- Feature 4: Lightweight and scriptable, suitable for automation in security testing environments.

## Installation

### Requirements

- Python 3.6+
- pip package manager

### Install Commands

```bash
# Install OSRFramework (includes entify.py)
pip install osrframework

# Or clone from GitHub for latest version
git clone https://github.com/i3visio/osrframework.git
cd osrframework
pip install -r requirements.txt
```

For Kali Linux, it may be available via apt:

```bash
apt update && apt install osrframework
```

## Basic Usage

```bash
python entify.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Input file path |
| -o, --output | Output file path |
| -s, --stdin | Process from standard input |
| -t, --type | Specify entity types (e.g., email,phone,url) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Extract entities from a text file:

```bash
python entify.py -i sample.txt -o extracted_entities.txt
```

### Example 2: Advanced Usage

Process stdin and filter for emails only:

```bash
cat webpage_content.html | python entify.py -s -t email
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Search Open Websites-Domains]] Search Open Technical Databases

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Python processes invoking entify.py or OSRFramework modules in reconnaissance tools.
- Detection method 2: Log file accesses and stdin piping in OSINT workflows; unusual regex pattern matching in logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/osrframework]]
- [[tools/Maltego]]

## References

- Official GitHub: https://github.com/i3visio/osrframework
- OSRFramework Documentation: https://github.com/i3visio/osrframework/wiki
