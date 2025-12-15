---
id: tool-maltego-927413
url: 'https://www.maltego.com'
tags:
  - osint
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.576Z'
validated: true
submitted: true
---
# Maltego

**Status**: Unverified

## Overview

Maltego is an OSINT tool for link analysis and recon, used to compare Zomato subdomain results.

## Description

Visualizes relationships for threat intel and recon.

## Features

- Feature 1: Entity transforms
- Feature 2: Graph visualization
- Feature 3: Data integration

## Installation

### Requirements

- Java

### Install Commands

```bash
# Download installer from site
```

## Basic Usage

```bash
# GUI application
```

### Common Options

| Option | Description |
|--------|-------------|
| Transforms | Run queries |
| Export | Save graphs |

## Examples

### Example 1: Basic Usage

Create graph, add domain, run To Subdomain transform.

### Example 2: Advanced Usage

Integrate with API for deep OSINT.

## MITRE ATT&CK Mapping

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

- Tool signatures in network

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: Aquatone]]

## References

- Maltego docs
