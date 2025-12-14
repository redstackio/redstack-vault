---
id: tool-uuid-2
url: 'https://github.com/rails/rails-html-sanitizer'
tags:
  - sanitizer
  - xss-prevention
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.814Z'
validated: true
submitted: true
---
# rails-html-sanitizer

**Status**: Unverified

## Overview

A Ruby gem for HTML sanitization in Rails, providing SafeListSanitizer to whitelist tags and attributes, vulnerable to XSS when allowing 'select' and 'style' prior to version 1.4.3.

## Description

It scrubs dangerous content using Nokogiri but fails on nested scripts due to parser differences, enabling bypasses in permissive configurations.

## Features

- Feature 1: Tag/attribute whitelisting
- Feature 2: Integration with Rails ActionView
- Feature 3: Custom sanitizer classes

## Installation

### Requirements

- Rails 5+ or standalone Ruby
- Nokogiri gem

### Install Commands

```bash
gem install rails-html-sanitizer
```

## Basic Usage

```ruby
require 'rails/html/sanitizer'
sanitizer = Rails::Html::SafeListSanitizer.new
puts sanitizer.sanitize('<p>safe</p>')
```

### Common Options

| Option | Description |
|--------|-------------|
| `tags:` | Array of allowed tags |
| `attributes:` | Allowed attributes |

## Examples

### Example 1: Basic Usage

```ruby
tags = %w(p strong)
puts Rails::Html::SafeListSanitizer.new.sanitize(input, tags: tags)
```

### Example 2: Advanced Usage

```ruby
# Vulnerable config
tags = %w(select style)
puts Rails::Html::SafeListSanitizer.new.sanitize(malicious, tags: tags)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence in Gemfile.lock
- Logs showing SafeListSanitizer calls
- Version checks for <1.4.3

## Related Procedures


## Related Tools

- [[tools/Nokogiri]]

## References

- GitHub: https://github.com/rails/rails-html-sanitizer
- HackerOne report: https://hackerone.com/reports/1530898
