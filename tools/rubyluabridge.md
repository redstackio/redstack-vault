---
id: tool-rubyluabridge
url: 'https://github.com/neomantra/rubyluabridge'
tags:
  - ruby
  - lua
  - bridge
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.101Z'
validated: true
submitted: true
---
# rubyluabridge

**Status**: Unverified

## Overview

RubyLuaBridge is a Ruby gem providing a bridge to embed and execute Lua code from Ruby, enabling vulnerable Lua extensions in libraries like WikiCloth for RCE exploitation.

## Description

This C++ extension allows Ruby apps to run Lua scripts, but its sandbox in WikiCloth is flawed. In pentesting, it's installed to activate Lua processing in GitLab wikis, allowing sandbox escapes. Alternatives: Tamar gem.

## Features

- Feature 1: Embed Lua interpreter in Ruby
- Feature 2: Call Lua from Ruby and vice versa
- Feature 3: Shared library integration

## Installation

### Requirements

- Ruby 2.7.x
- Lua 5.1 dev libs
- Boost dev libs

### Install Commands

```bash
git clone https://github.com/neomantra/rubyluabridge
cd rubyluabridge
./build/extconf_ubuntu.sh && make
sudo cp rubyluabridge.so /path/to/ruby/lib/
```

## Basic Usage

```bash
# No direct CLI; loaded as Ruby extension
ruby -e "require 'rubyluabridge'; # Lua code here"
```

### Common Options

N/A (library)

## Examples

### Example 1: Basic Usage

In Ruby: require 'rubyluabridge'; LuaBridge.new.eval('print("Hello Lua")')

### Example 2: Advanced Usage

Build and load in WikiCloth context for wiki rendering.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Lua

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- rubyluabridge.so in Ruby lib paths
- Lua eval calls in app logs
- GitHub clone history

## Related Procedures

- [[procedures/Install-rubyluabridge-for-Lua-Extension]]

## Related Tools

- [[tools/WikiCloth]]

## References

- Official documentation: Repo README
- Related resources: Lua users wiki on sandboxes
