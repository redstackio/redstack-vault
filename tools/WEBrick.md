---
id: tool-webrick
url: 'https://github.com/ruby/webrick'
tags:
  - http-server
  - ruby-library
type: tool
verified: false
platforms:
  - Ruby
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.580Z'
configuration: 'Port 8000, Realm ''DigestAuth example realm'', UserDB via DigestAuth'
validated: true
submitted: true
---
# WEBrick

**Status**: Verified

## Overview

WEBrick is Ruby's standard library HTTP server, configurable for protocols including Digest authentication. It's used in security testing to host vulnerable endpoints for ReDoS exploitation demos.

## Description

WEBrick 1.4.2 (with Ruby 2.5.5) has a ReDoS flaw in HTTPAuth::DigestAuth. It's lightweight for local testing, mounting procs with auth handlers.

## Features

- Feature 1: Built-in DigestAuth support
- Feature 2: Simple scripting for endpoints
- Feature 3: Trap signals for graceful shutdown

## Installation

### Requirements

- Ruby installation

### Install Commands

```bash
# Included in Ruby stdlib; require in script
require 'webrick'
```

## Basic Usage

```bash
# Via Ruby script
ruby -r webrick -e 'WEBrick::HTTPServer.new(:Port=>8000).start'
```

### Common Options

| Option | Description |
|--------|-------------|
| `:Port` | Server port |
| `:Realm` | Auth realm |

## Examples

### Example 1: Basic Usage

```bash
# Simple server script
require 'webrick'; s=WEBrick::HTTPServer.new(:Port=>8000); s.start
```

### Example 2: Advanced Usage

```bash
# With DigestAuth
require 'webrick/httpauth/digestauth'; # config as in procedure
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Server banner: 'WEBrick/1.4.2'
- Port binds and process name 'ruby'
- Auth-related CPU spikes

## Related Procedures

- [[procedures/Configure-Vulnerable-WEBrick-Server-with-Digest-Auth]]

## Related Tools

- [[tools/Ruby]]

## References

- GitHub: https://github.com/ruby/webrick
