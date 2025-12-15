---
id: tool-wikicloth
url: 'https://github.com/nricciar/wikicloth'
tags:
  - ruby
  - wiki
  - render
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.093Z'
validated: true
submitted: true
---
# WikiCloth

**Status**: Unverified

## Overview

WikiCloth is a Ruby gem for parsing and rendering MediaWiki markup, integrated in GitLab for wiki pages, with a vulnerable Lua extension when rubyluabridge is present.

## Description

It converts wiki syntax to HTML, supporting extensions like Lua for dynamic content. The luawrapper.lua file uses insecure loadstring, bypassable for RCE. In exploits, it's the vector for executing payloads in authenticated wiki edits.

## Features

- Feature 1: MediaWiki syntax parsing
- Feature 2: Extension support (e.g., Lua)
- Feature 3: HTML output generation

## Installation

### Requirements

- RubyGems
- rubyluabridge for Lua

### Install Commands

```bash
gem install wikicloth -v 0.8.1
# For Lua: Install rubyluabridge as above
```

## Basic Usage

```bash
ruby -r wikicloth -e "puts WikiCloth::WikiCloth.new(:wiki=>'<lua>print("test")</lua>').to_html"
```

### Common Options

N/A (library)

## Examples

### Example 1: Basic Usage

Parse simple wiki: WikiCloth.new(:wiki => '==Title== Text').to_html

### Example 2: Advanced Usage

With Lua: Requires rubyluabridge; renders <lua> blocks executing code.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- WikiCloth gem in Ruby apps
- Rendering logs with Lua errors
- <lua> tags in wiki content

## Related Procedures

- [[procedures/Trigger-RCE-by-Visiting-Wiki-Page]]

## Related Tools

- [[tools/rubyluabridge]]

## References

- Official documentation: https://github.com/nricciar/wikicloth
- Related resources: HackerOne report 1401444
