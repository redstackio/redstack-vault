---
id: tool-ruby
url: 'https://www.ruby-lang.org/'
tags:
  - programming
  - server
  - web
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.583Z'
configuration: Version 2.5.5
validated: true
submitted: true
---
# Ruby

**Status**: Verified

## Overview

Ruby is a dynamic programming language used for web development, including running servers like WEBrick. In security testing, it's used to set up vulnerable environments for reproducing issues like ReDoS in standard libraries.

## Description

Ruby includes WEBrick as a standard HTTP server module. Version 2.5.5 is vulnerable to the described ReDoS. It's scripted for custom server configs in exploit reproduction.

## Features

- Feature 1: Dynamic scripting for HTTP servers
- Feature 2: Built-in auth modules like DigestAuth
- Feature 3: Easy local testing without external deps

## Installation

### Requirements

- Compatible OS

### Install Commands

```bash
# Using rbenv or rvm for version management
rbenv install 2.5.5
rbenv global 2.5.5

# Or system package
sudo apt install ruby2.5
```

## Basic Usage

```bash
ruby --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e` | Execute code snippet |
| `-r` | Require library |

## Examples

### Example 1: Basic Usage

```bash
ruby -e 'puts "Hello Ruby"'
```

### Example 2: Advanced Usage

```bash
ruby server.rb  # Run WEBrick script
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for ruby/webrick processes
- Network binds on non-standard ports like 8000
- Script analysis for auth configs

## Related Procedures

- [[procedures/Configure-Vulnerable-WEBrick-Server-with-Digest-Auth]]

## Related Tools

- [[tools/WEBrick]]

## References

- Official documentation: https://www.ruby-lang.org/en/documentation/
