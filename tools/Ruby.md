---
url: null
tags:
  - programming
  - scripting
type: tool
platforms:
  - Linux
description: Programming language used to script attacker servers.
id: d7ca8c18-b0b8-4463-ae92-7e6b03497e51
created_at: '2025-12-13T09:00:27.270Z'
updated_at: '2025-12-13T09:00:27.270Z'
verified: false
validated: true
submitted: true
---
# Ruby

**Status**: Unverified

## Overview

Ruby is a dynamic programming language used for scripting web servers in offensive security, particularly with frameworks like Sinatra for exploit delivery.

## Description

In this context, Ruby scripts the attacker server, binding to 0.0.0.0 and defining routes for XXE payloads.

## Features

- Feature 1: Easy syntax
- Feature 2: Gem package management
- Feature 3: Web framework support

## Installation

### Requirements

- OS package manager

### Install Commands

```bash
apt install ruby
```

## Basic Usage

```bash
ruby -v
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Require library |
| `-e` | Execute code |

## Examples

### Example 1: Basic Usage

```bash
ruby script.rb
```

### Example 2: Advanced Usage

```bash
ruby -rsinatra server.rb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor ruby processes
- Detection method 2: Check for gem installations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Sinatra]]

## References

- Official documentation: https://ruby-lang.org
