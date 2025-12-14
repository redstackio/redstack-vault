---
url: 'https://github.com/janko/image_processing'
tags:
  - ruby
  - gem
type: tool
platforms:
  - Linux
  - Web
description: 'Ruby gem for image transformations, passing operations to MiniMagick.'
id: 98bf7405-df24-4759-b5b3-83551eea2cdc
created_at: '2025-12-14T17:28:28.310Z'
updated_at: '2025-12-14T17:28:28.310Z'
verified: false
validated: true
submitted: true
---
# ImageProcessing

**Status**: Unverified

## Overview

ImageProcessing gem applies transformations in Rails ActiveStorage, using send() to invoke methods on backends like MiniMagick.

## Description

Chainable transformations; vulnerable send(name, arg) allows arbitrary method calls like eval when name is user-controlled.

## Features

- Feature 1: Supports variant() integrations
- Feature 2: send() for dynamic invocations
- Feature 3: Handles hashes/arrays for ops

## Installation

### Requirements

- Ruby on Rails

### Install Commands

```bash
# Add to Gemfile
gem 'image_processing', '~> 1.12'
bundle install
```

## Basic Usage

```ruby
# In Rails
image.variant(resize: '100x100').processed
```

### Common Options

| Option | Description |
|--------|-------------|
| apply | Applies transformations |
| send | Invokes methods dynamically |

## Examples

### Example 1: Basic Usage

```ruby
require 'image_processing/mini_magick'
ImageProcessing::MiniMagick.source('input.jpg').resize(100).call
```

### Example 2: Advanced Usage

```ruby
processor = ImageProcessing::MiniMagick.source('input')
processor.send(:write, '/tmp/out.jpg')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Trace send() calls in stack traces
- Validate transformation names

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/MiniMagick]]

## References

- GitHub documentation
