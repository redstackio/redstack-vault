---
url: 'https://github.com/BuffaloWill/oxml_xxe'
tags:
  - xxe
  - payload
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: XXE payload generator for documents
id: e3ea2918-51c3-44ef-92f9-bda11afc9e8f
created_at: '2025-12-13T09:00:33.647Z'
updated_at: '2025-12-13T09:00:33.647Z'
verified: false
validated: true
submitted: true
---
# oxml_xxe

**Status**: Unverified

## Overview

Tool to generate XXE payloads for office documents, adaptable for images.

## Description

Creates files with embedded XXE for testing.

## Features

- Payload forging
- Custom DTD

## Installation

### Requirements

- Python

### Install Commands

```bash
git clone https://github.com/BuffaloWill/oxml_xxe
```

## Basic Usage

```bash
python oxml_xxe.py
```

## Examples

### Example 1: Basic Usage

```bash
python oxml_xxe.py -d payload
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- File analysis

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/EXIFTool]]

## References

- GitHub repo
