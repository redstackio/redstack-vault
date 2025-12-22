---
id: 252e8038-a8f5-4b11-ac46-b8c1558aead7
name: Kramdown
type: tool
verified: false
created_at: '2025-12-11T06:10:13.204Z'
updated_at: '2025-12-11T06:10:13.204Z'
platforms:
  - Web
  - Linux
tags:
  - markdown
  - parser
url: 'https://kramdown.gettalong.org/options.html'
description: >-
  Markdown parser allowing inline options for syntax highlighting, exploited for
  class instantiation.
validated: true
submitted: true
---

# Kramdown

**Status**: Unverified

## Overview

Kramdown is a Markdown parser used in GitLab for rendering wiki pages, vulnerable to unsafe inline options leading to RCE.

## Description

Supports options like syntax_highlighter_opts for custom formatters, which can instantiate arbitrary Ruby classes.

## Features

- Feature 1: Markdown to HTML conversion
- Feature 2: Inline option configuration
- Feature 3: Syntax highlighting integration

## Installation

### Requirements

- Ruby environment

### Install Commands

```bash
gem install kramdown
```

## Basic Usage

```bash
kramdown file.md
```

### Common Options

| Option | Description |
|--------|-------------|
| --help | Show help |

## Examples

### Example 1: Basic Usage

```bash
kramdown input.md > output.html
```

### Example 2: Advanced Usage

With custom options for exploitation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unusual Kramdown options in wikis
- Rendering errors in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Rouge]]

## References

- https://kramdown.gettalong.org/options.html
