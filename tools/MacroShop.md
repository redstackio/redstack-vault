---
id: f9c5aa3b-2008-4958-a710-ca577fdee5aa
type: tool
verified: true
created_at: '2019-08-28T21:17:41.217615+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - macro
  - office
  - vba
  - payload-delivery
  - obfuscation
url: 'https://github.com/parsiya/MacroShop'
validated: true
---

# MacroShop

**Status**: Unverified

## Overview

MacroShop is a collection of Python scripts designed to assist red teams and penetration testers in generating and obfuscating VBA macros for Microsoft Office documents. It's primarily used for crafting malicious macros that enable payload delivery, command execution, or persistence in social engineering campaigns targeting Office users.

## Description

MacroShop provides modular scripts for creating VBA code that can download remote payloads, execute shell commands, or establish reverse connections while incorporating basic obfuscation to bypass macro security warnings and endpoint detection. The tool supports integration with Office applications like Word, Excel, and PowerPoint, making it ideal for spearphishing attachments in initial access scenarios.

## Features

- Feature 1: Macro generation for downloading and executing remote payloads via HTTP/XMLHTTP objects.
- Feature 2: VBA code obfuscation using string encoding, variable renaming, and junk code insertion.
- Feature 3: Templates for common attack patterns like AutoOpen triggers and shell spawning.
- Feature 4: Support for embedding payloads directly or fetching them dynamically.

## Installation

### Requirements

- Python 3.6+
- Git
- No additional dependencies beyond standard library (some scripts may require requests for advanced features).

### Install Commands

```bash
# Clone the repository
git clone https://github.com/parsiya/MacroShop.git
cd MacroShop

# No pip install needed; scripts are standalone Python files
```

## Basic Usage

```bash
python MacroShop.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available scripts |
| --generate | Flag to run macro generation mode |
| --obfuscate | Flag to obfuscate existing VBA code |
| -o, --output | Specify output file for generated code |

## Examples

### Example 1: Basic Usage

Generate a simple download-execute macro:

```bash
python MacroShop.py --download-execute --url http://example.com/payload.exe --output malicious_macro.vba
```

### Example 2: Advanced Usage

Obfuscate an existing macro file:

```bash
python obfuscate.py input.vba --output obfuscated.vba
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File
- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of obfuscated VBA in Office documents (e.g., unusual Chr() functions or encoded strings).
- Detection method 2: Office macro logging enabled; monitor for AutoOpen or Document_Open events triggering network activity.
- Detection method 3: YARA rules for common MacroShop patterns like XMLHTTP downloads in VBA.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Donut]]
- [[tools/Invoke-Obfuscation]]

## References

- Official GitHub: https://github.com/parsiya/MacroShop
- Blog post by author: https://parsiya.io/2019/10/02/macroshop/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1204/002/
