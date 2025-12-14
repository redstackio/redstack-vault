---
url: 'https://github.com/rgrove/sanitize'
tags:
  - html-sanitizer
  - security
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.471Z'
id: 58ca2145-bdc6-4bcc-9978-7f0521c6e307
validated: true
submitted: true
---
# Sanitize

**Status**: Unverified

## Overview

Sanitize is a Ruby gem for cleaning potentially dangerous HTML, used in GitLab to escape user input but vulnerable when applied only to direct input, not filter-generated attributes in this XSS exploit.

## Description

Attackers exploit Sanitize's selective escaping (" to %22 for user href, but not generated ones) to inject attributes. It whitelists tags/attributes and is common in Rails for XSS prevention, but misconfigurations allow breakout in pipelines like Banzai.

## Features

- Feature 1: Whitelist-based HTML scrubbing
- Feature 2: Quote escaping in attributes via UNSAFE_LIBXML_ESCAPE_CHARS
- Feature 3: Integration with Nokogiri for parsing

## Installation

### Requirements

- Ruby 2.3+
- Nokogiri gem

### Install Commands

```bash
# Gem installation
gem install sanitize
```

## Basic Usage

```ruby
require 'sanitize'
html = Sanitize.clean('<script>alert(1)</script>')
puts html  # Outputs empty or safe
```

### Common Options

| Option | Description |
|--------|-------------|
| `:elements` | Whitelist of allowed tags |
| `:attributes` | Allowed attributes per tag |

## Examples

### Example 1: Basic Cleaning

```ruby
input = '<a href="javascript:alert(1)">link</a>'
clean = Sanitize.clean(input)
puts clean  # Escapes to safe href
```

### Example 2: Advanced Usage

```ruby
config = { :attributes => { 'a' => ['href'] } }
Sanitize.clean('<a href=unsanitized>link</a>', config)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gemfile.lock entries for sanitize ~> 6.0.0
- Application logs for unsanitized attribute injections

## Related Procedures


## Related Tools

- [[tools/Nokogiri]]

## References

- Official documentation: https://github.com/rgrove/sanitize
- GitLab Banzai pipeline usage
