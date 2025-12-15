---
url: 'https://github.com/rubyzip/rubyzip'
tags:
  - zip
  - ruby
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.638Z'
id: 0afa9e71-19c8-47f5-8bca-7266f41b6e8b
validated: true
submitted: true
---
# RubyZip-Archive-Library

**Status**: Unverified

## Overview

RubyZip is a Ruby library for reading and writing ZIP files, used in security contexts to craft malicious archives like .nupkg for vulnerability exploitation.

## Description

It provides APIs for creating, extracting, and manipulating ZIP contents, ideal for embedding payloads in package formats. In offensive security, it's leveraged to build exploit artifacts without external tools.

## Features

- Feature 1: ZIP creation and addition of files
- Feature 2: Compression and encryption support
- Feature 3: In-memory archive handling

## Installation

### Requirements

- Ruby 2.6+

### Install Commands

```bash
# Installation command
gem install rubyzip
```

## Basic Usage

```bash
irb -r zip
Zip::File.open('archive.zip', Zip::File::CREATE) { |z| z.add('file.txt', 'content') }
```

### Common Options

| Option | Description |
|--------|-------------|
| CREATE | Mode for new archives |
| add | Add file to ZIP |

## Examples

### Example 1: Basic Usage

```ruby
require 'zip'
Zip::File.open('test.zip', Zip::File::CREATE) do |zipfile|
  zipfile.get_output_stream('file.txt') { |f| f.write 'Hello' }
end
```

### Example 2: Advanced Usage

```ruby
Zip::File.open('malicious.nupkg', Zip::File::CREATE) do |zip|
  zip.add('dummy.nuspec', File.read('payload.xml'))
end
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- ZIP files with anomalous structures in uploads
- Ruby process creating archives

## Related Procedures

- [[procedures/Create-Malicious-NuGet-Package-with-Path-Traversal-Payload]]

## Related Tools

- [[tools/Faraday-Ruby-HTTP-Client]]

## References

- Official documentation: https://github.com/rubyzip/rubyzip
- Related resources: RubyGems.org
