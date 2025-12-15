---
url: >-
  https://github.com/charliesome/charlie.bz/blob/master/posts/rails-3.2.10-remote-code-execution.md
tags:
  - payload
  - deserialization
type: tool
platforms:
  - Linux
description: >-
  Custom Ruby script for generating base64 Marshal payloads adapted from Rails
  RCE exploits.
id: 70ab6ff0-0876-458c-88f9-5da893f7a08e
created_at: '2025-12-14T17:23:53.929Z'
updated_at: '2025-12-14T17:23:53.929Z'
verified: false
validated: true
submitted: true
---
# generate.rb-script

**Status**: Unverified

## Overview

A custom Ruby script used to create deserialization payloads by encoding Ruby code into base64 Marshal format, targeted at YAML vulnerabilities in Ruby applications.

## Description

Adapted from a Rails remote code execution blog post, the script takes Ruby code from a file and generates a serializable payload that, when loaded via YAML/Marshal, executes the code. Essential for crafting exploits like the RubyGems deserialization attack.

## Features

- Feature 1: Encodes arbitrary Ruby code into Marshal
- Feature 2: Base64 output for easy embedding in YAML
- Feature 3: Leverages Ruby's serialization for gadget chains

## Installation

### Requirements

- Ruby installed

### Install Commands

```bash
# Download and save as generate.rb from source
curl -o generate.rb https://raw.githubusercontent.com/.../generate.rb
```

## Basic Usage

```bash
ruby generate.rb payload.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Script takes one argument: payload file |

## Examples

### Example 1: Basic Usage

```bash
ruby generate.rb payload.rb
```

### Example 2: Advanced Usage

Modify script for custom gadgets, then run.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of generate.rb or similar scripts in workspaces
- Ruby process args including payload files

## Related Procedures

- [[procedures/Craft-Malicious-Gem-with-Deserialization-Payload]]

## Related Tools

- [[ysoserial]]

## References

- Source: https://github.com/charliesome/charlie.bz/blob/master/posts/rails-3.2.10-remote-code-execution.md
