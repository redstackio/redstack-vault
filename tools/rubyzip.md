---
url: ''
tags:
  - zip
  - ruby
type: tool
platforms:
  - Linux
description: >-
  Ruby library for creating and handling zip files, used to create .nupkg
  packages.
id: 0edbec33-08a1-42c9-9c48-e0e50ed0588b
created_at: '2025-12-11T03:47:39.711Z'
updated_at: '2025-12-11T03:47:39.711Z'
verified: false
validated: true
submitted: true
---
# rubyzip

**Status**: Unverified

## Overview

rubyzip is a gem for reading and writing zip files in Ruby, essential for crafting NuGet packages in exploits.

## Description

Used in scripts to zip .nuspec files into .nupkg for uploading to vulnerable registries.

## Features

- Zip file creation
- Extraction and manipulation
- Stream support

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install rubyzip
```

## Basic Usage

```ruby
require 'zip'
Zip::File.open('file.zip') { |zip| }
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Library-based |

## Examples

### Example 1: Basic Usage

```ruby
Zip::File.open('dummy.nupkg', Zip::File::CREATE) { |zip| zip.add('dummy.nuspec', 'dummy.nuspec') }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Scan for zip operations in scripts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #zip

## References

- https://github.com/rubyzip/rubyzip
