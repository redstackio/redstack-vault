---
url: 'https://github.com/ruby/rdoc'
tags:
  - documentation
  - xss
  - ruby
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.924Z'
id: 862eac1d-795a-49d2-9987-e9cb9e4356ab
validated: true
submitted: true
---
# rdoc

**Status**: Unverified

## Overview

RDoc is Ruby's standard documentation generator, converting source code comments into HTML, RI, or other formats. It's vulnerable to stored XSS in versions before 4.0.1 due to improper HTML escaping in paragraph handling, allowing script injection in generated docs.

## Description

RDoc scans Ruby files for special comments (e.g., =begin blocks) and formats them into documentation. The tool is invoked via command line and outputs static HTML viewable in browsers, where XSS can execute JS for attacks like session theft. Commonly used in Ruby projects for auto-generating API docs.

## Features

- Feature 1: Parses Ruby comments into structured HTML with headings, paragraphs, and code blocks
- Feature 2: Supports multiple output formats (HTML, RI, JSON)
- Feature 3: Customizable via templates and flags for styling and content inclusion

## Installation

### Requirements

- Ruby 1.8+ installed

### Install Commands

```bash
# Typically bundled with Ruby; install via gem if needed
gem install rdoc
```

## Basic Usage

```bash
rdoc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--all` | Process all files |
| `--output DIR` | Specify output directory |

## Examples

### Example 1: Basic Usage

```bash
rdoc example.rb
```

Generates docs for a single file.

### Example 2: Advanced Usage

```bash
rdoc --all --output ./docs
```

Processes all files to a custom dir.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of 'doc' directories with HTML files containing <script> tags
- Log entries for 'rdoc' executions in build pipelines
- Anomalous JS alerts when viewing generated docs

## Related Procedures

- [[procedures/Exploit-Stored-XSS-in-RDoc]]

## Related Tools


## References

- Official documentation: https://ruby.github.io/rdoc/
- CVE-2013-0256 details: https://hackerone.com/reports/1977168
