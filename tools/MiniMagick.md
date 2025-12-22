---
url: ''
tags:
  - ruby
  - wrapper
type: tool
platforms:
  - Linux
  - Web
description: 'Ruby wrapper for ImageMagick, enabling method calls to CLI conversions.'
id: dda2244c-0139-41c3-9777-880f356b77e9
created_at: '2025-12-14T17:28:28.313Z'
updated_at: '2025-12-14T17:28:28.313Z'
verified: false
validated: true
submitted: true
---
# MiniMagick

**Status**: Unverified

## Overview

MiniMagick is a Ruby gem wrapping ImageMagick, simplifying image operations in Rails apps via method_missing for CLI mapping.

## Description

Converts Ruby method calls to ImageMagick commands; vulnerable when user params trigger method_missing with arrays/hashes, injecting args.

## Features

- Feature 1: Dynamic method invocation for transformations
- Feature 2: Handles arrays as multi-args
- Feature 3: Integrates with ActiveStorage

## Installation

### Requirements

- Ruby and bundler

### Install Commands

```bash
# Gem install
gem install mini_magick
```

## Basic Usage

```bash
# In Ruby
image = MiniMagick::Image.new('input.jpg')
image.resize '100x100'
image.write 'output.png'
```

### Common Options

| Option | Description |
|--------|-------------|
| method_missing | Converts unknown methods to CLI |
| resize | Maps to -resize flag |

## Examples

### Example 1: Basic Usage

```ruby
MiniMagick::Image.open('input.jpg') do |img|
  img.resize '100x100'
end
```

### Example 2: Advanced Usage

```ruby
img = MiniMagick::Image.new('input.jpg')
img.write('/tmp/out.jpg')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Log Ruby method calls in ImageProcessing
- Static analysis for unsanitized params

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ImageMagick]]

## References

- GitHub repo
