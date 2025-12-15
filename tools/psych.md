---
url: 'https://github.com/ruby/psych'
tags:
  - yaml
  - parser
  - deserialization
type: tool
platforms:
  - Ruby
description: >-
  Ruby YAML parser used by RDoc, vulnerable to unsafe deserialization in
  versions before 4.0.0
id: 36c6760e-ed96-452e-9eb7-0af50b13e5ba
created_at: '2025-12-14T17:23:42.397Z'
updated_at: '2025-12-14T17:23:42.397Z'
verified: false
validated: true
submitted: true
---
# psych

**Status**: Unverified

## Overview

Psych is the default YAML parser for Ruby (via Syck), enabling safe and unsafe loading, but defaults to unsafe in older versions, facilitating deserialization attacks.

## Description

Integrated into RDoc for `.rdoc_options` parsing, Psych's `YAML.load_file` without restrictions allows arbitrary object injection. Critical for Ruby ecosystem vulnerabilities.

## Features

- Feature 1: Full YAML 1.1 support
- Feature 2: Ruby object deserialization
- Feature 3: Safe load modes (post-4.0)

## Installation

### Requirements

- Ruby standard library (bundled)

### Install Commands

```bash
# Update via RubyGems
gem update psych
```

## Basic Usage

```bash
ruby -rpsych -e "puts Psych::VERSION"
```

### Common Options

| Option | Description |
|--------|-------------|
| `safe_load` | Enable safe deserialization |

## Examples

### Example 1: Basic Usage

```bash
ruby -ryaml -e "p YAML.load_file('file.yaml')"
```

### Example 2: Advanced Usage

```bash
ruby -ryaml -e "p Psych.safe_load_file('file.yaml')"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Trace Ruby calls to YAML.load without safe flags
- Alert on object injection attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rdoc]]

## References

- Official documentation: https://github.com/ruby/psych
- Vulnerability details: Psych <4.0 unsafe defaults
