---
url: ''
tags:
  - parsing
  - html
type: tool
platforms:
  - Linux
  - Web
description: >-
  Ruby library for parsing and manipulating HTML/XML, used in GitLab's Kroki
  filter for diagram rendering
id: 0144b773-f28e-4075-bc82-07786b9fa8f8
created_at: '2025-12-11T03:47:56.422Z'
updated_at: '2025-12-11T03:47:56.422Z'
verified: false
validated: true
submitted: true
---
# Nokogiri

**Status**: Unverified

## Overview

Nokogiri is a Ruby gem for parsing and searching HTML and XML documents, commonly used in web applications for content manipulation.

## Description

In the context of GitLab, Nokogiri is utilized in the Kroki filter to process Markdown and generate diagram img tags, but lacks proper validation leading to XSS vulnerabilities.

## Features

- HTML/XML parsing: Efficient document traversal
- CSS/XPath querying: Easy element selection
- Document manipulation: Adding/editing nodes

## Installation

### Requirements

- Ruby environment

### Install Commands

```bash
gem install nokogiri
```

## Basic Usage

```bash
require 'nokogiri'
nokogiri --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

```ruby
doc = Nokogiri::HTML('<html><body>Hello</body></html>')
```

### Example 2: Advanced Usage

```ruby
doc.at_css('body').content = 'Modified'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unexpected HTML manipulations in logs
- Scan for vulnerable Nokogiri versions in dependencies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #axios
- [[tools/jQuery]]

## References

- Official Nokogiri documentation: https://nokogiri.org/
