---
url: 'https://github.com/asciinema/asciinema'
tags:
  - recording
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.852Z'
id: 56d9f3c0-872a-4c5a-900a-cfd75b332eff
validated: true
submitted: true
---
# asciinema

**Status**: Unverified

## Overview

Tool for recording and sharing terminal sessions, used to capture proof-of-concept exploit demonstrations.

## Description

asciinema records terminal output as JSON for playback. Useful for documenting attack chains in reports.

## Features

- Feature 1: Session recording
- Feature 2: Upload to asciinema.org
- Feature 3: Playback in terminals/browsers

## Installation

### Requirements

- Python or binary

### Install Commands

```bash
# Via pip
pip install asciinema
# Or curl install script
curl -sS https://asciinema.org/install.sh | sh
```

## Basic Usage

```bash
asciinema --help
```

### Common Options

| Option | Description |
|--------|-------------|
| rec | Record session |
| play | Play recording |
| upload | Share online |

## Examples

### Example 1: Basic Usage

```bash
asciinema rec demo.cast
# Run commands, then Ctrl+D to stop
```

### Example 2: Advanced Usage

```bash
asciinema rec --upload demo.cast
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (for demo purposes)

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- asciinema processes during sessions
- .cast files in filesystem

## Related Procedures

- None specific

## Related Tools

- [[tools/script]]

## References

- GitHub: https://github.com/asciinema/asciinema
