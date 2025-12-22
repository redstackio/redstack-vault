---
id: 23abc7ae-d9a6-4aae-ac3c-dfcd33600b54
type: tool
verified: true
created_at: '2019-08-28T21:17:22.550949+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - password-cracking
  - credential-access
  - analysis
url: 'https://github.com/bwall/PACT (related PACK toolkit)'
validated: true
---

# policygen

**Status**: Unverified

## Overview

policygen is a component of the Password Analysis and Cracking Toolkit (PACK), originally developed for the Defcon 2010 "Crack Me If You Can" competition. It aids in preparing for advanced password attacks by analyzing common password creation patterns and generating optimized attack masks for tools like oclHashcat or Hashcat. This tool focuses on statistical analysis to enable smarter, non-brute-force cracking strategies, improving efficiency against complex password policies.

## Description

policygen processes datasets of known passwords (e.g., from breaches) to identify patterns such as length distributions, character substitutions (e.g., 'a' to '@'), common bases (e.g., dictionary words + appendages), and structural rules. It builds a statistical database that can then be queried to produce custom mask files, which define rules for hybrid attacks combining wordlists, masks, and rules. While policygen itself does not perform cracking, it significantly enhances the speed and success rate of cracking tools by prioritizing likely password structures. It's particularly useful in red team engagements for targeting enterprise password policies or in forensic analysis of leaked credentials.

## Features

- **Pattern Analysis**: Identifies statistical trends in password composition, length, and transformations.
- **Mask Generation**: Creates Hashcat-compatible mask files based on analyzed data for targeted attacks.
- **Database Management**: Builds and updates SQLite-based statistical databases from input files.
- **Customization**: Supports parameters for focusing on specific pattern types (e.g., PINs, passphrases).
- **Integration**: Outputs formats compatible with popular crackers like Hashcat, John the Ripper.

## Installation

### Requirements

- Python 2.7 or 3.x
- SQLite3 (built-in with Python)
- Optional: NumPy for advanced statistics (if using extended PACK features)
- Access to PACK repository or standalone policygen script

### Install Commands

```bash
# Clone the PACK repository (policygen is included)
git clone https://github.com/bwall/PACT.git
cd PACT

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Or run directly if standalone
python policygen.py --help
```

For Ubuntu/Kali:

```bash
sudo apt update
sudo apt install python3 python3-pip git
# Then clone and install as above
```

## Basic Usage

```bash
policygen --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --version | Display policygen version |
| -a | Activate analysis mode for building database |
| -g | Generate masks from database |
| -i | Specify input file |
| -o | Specify output file |

## Examples

### Example 1: Basic Usage (Analyze Patterns)

```bash
policygen -a -i passwords.txt -db stats.db
```

This analyzes the input file and updates the statistical database.

### Example 2: Advanced Usage (Generate Masks)

```bash
policygen -g -db stats.db -o masks.txt -t hybrid
```

This generates hybrid masks from the database for use in Hashcat.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of PACK-related files or databases (e.g., .db files with password stats) in temporary directories.
- Python processes executing policygen.py or analyzing large password dumps.
- Network downloads of PACK from GitHub or Defcon archives.
- Unusual file I/O patterns involving breach datasets and mask outputs.
- Integration with cracking tools like Hashcat showing custom masks derived from statistical analysis.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hashcat]]
- [[tools/john-the-ripper]]
- [[PACK]]

## References

- Original PACK development: Defcon 2010 "Crack Me If You Can" competition
- GitHub repository: https://github.com/bwall/PACT (modern fork of PACK)
- Related paper: Analysis of password patterns in cracking competitions

*Last updated: 2023-10-01*
