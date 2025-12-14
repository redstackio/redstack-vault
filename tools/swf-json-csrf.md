---
id: t-swf-json-csrf
url: 'https://github.com/sp1d3r/swf_json_csrf'
tags:
  - csrf
  - flash
  - exploit-kit
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.802Z'
validated: true
submitted: true
---
# swf_json_csrf

**Status**: Unverified

## Overview

GitHub repository providing SWF and PHP scripts for JSON CSRF exploits using Flash to bypass Content-Type and CORS.

## Description

Contains pre-built tools for crafting and testing Flash-based CSRF, including SWF generator, PHP proxy, and examples tailored for APIs like Federalist.

## Features

- SWF compilation scripts
- PHP redirect templates
- Testing HTML pages
- Documentation for parameterization

## Installation

### Requirements

- Git, PHP, Flash compiler

### Install Commands

```bash
git clone https://github.com/sp1d3r/swf_json_csrf
cd swf_json_csrf
# Compile SWF if needed
```

## Basic Usage

Host files and embed SWF as per repo README.

### Common Options

| Option | Description |
|--------|-------------|
| --help | Repo usage |

## Examples

### Example 1: Local Test

Host on local server, load index.html with params.

### Example 2: Production Deploy

Upload to attacker server, update endpoints in config.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Repo clones in attacker environments
- SWF files matching repo signatures
- GitHub traffic to exploit repos

## Related Procedures


## Related Tools

- [[tools/Flash-SWF-File]]
- [[tools/PHP-Redirector]]

## References

- https://github.com/sp1d3r/swf_json_csrf
