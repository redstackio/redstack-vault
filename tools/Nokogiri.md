---
id: tool-uuid-1
url: 'https://nokogiri.org/'
tags:
  - parser
  - xml
  - html
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.817Z'
validated: true
submitted: true
---
# Nokogiri

**Status**: Unverified

## Overview

Nokogiri is an XML/HTML parsing library for Ruby, used by Rails for sanitization. Implementation differences between JRuby (nekohtml) and CRuby cause the XSS vulnerability in this context.

## Description

Nokogiri provides robust parsing but the JRuby variant uses Java's nekohtml, leading to quirks in handling self-closing tags and nesting, allowing script preservation in sanitizers.

## Features

- Feature 1: Fast XML/HTML parsing with XPath/CSS selectors
- Feature 2: Sanitization support via Rails integration
- Feature 3: Cross-implementation (native Ruby vs. Java)

## Installation

### Requirements

- Ruby 2.5+ or JRuby
- libxml2 and libxslt (for CRuby)

### Install Commands

```bash
gem install nokogiri
```

## Basic Usage

```ruby
require 'nokogiri'
doc = Nokogiri::HTML('<html><body></body></html>')
puts doc
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | No strict parsing |
| `--use-dlibs` | Use system libs (CRuby) |

## Examples

### Example 1: Basic Usage

```ruby
html = '<select><style>script</style></select>'
doc = Nokogiri::HTML(html)
puts doc.to_html
```

### Example 2: Advanced Usage

```ruby
doc = Nokogiri::HTML(input, nil, 'UTF-8')
doc.css('script').remove  # Manual scrubbing
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gemfile entries for nokogiri
- Parsing errors in JRuby logs indicating nekohtml
- Anomalous HTML outputs in app responses

## Related Procedures


## Related Tools

- [[tools/rails-html-sanitizer]]

## References

- Official documentation: https://nokogiri.org/tutorials
- Vulnerability report: https://hackerone.com/reports/1530898
