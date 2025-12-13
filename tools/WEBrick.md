---
url: null
tags:
  - ruby
  - webrick
  - http-server
type: tool
platforms:
  - Web
description: >-
  Ruby library for creating HTTP servers, vulnerable to request smuggling in
  older versions.
id: a3705d7c-aa5f-4783-bd26-cce327c73199
created_at: '2025-12-13T09:01:22.190Z'
updated_at: '2025-12-13T09:01:22.190Z'
verified: false
validated: true
submitted: true
---
# WEBrick

**Status**: Unverified

## Overview

WEBrick is a Ruby library for building HTTP servers, often used in development and testing, but vulnerable to HTTP Request Smuggling due to loose header parsing.

## Description

Allows quick setup of HTTP servers with custom endpoints. Vulnerability in /lib/webrick/httprequest.rb permits malformed Transfer-Encoding headers.

## Features

- Simple server creation
- Endpoint mounting
- HTTP request handling

## Installation

### Requirements

- Ruby installed

### Install Commands

Included in Ruby standard library; require 'webrick'

## Basic Usage

```ruby
require 'webrick'
server = WEBrick::HTTPServer.new(:Port => 8080)
server.start
```

### Common Options

| Option | Description |
|--------|-------------|
| `:Port` | Listening port |
| `mount_proc` | Endpoint handler |

## Examples

### Example 1: Basic Usage

```ruby
server.mount_proc '/' do |req, res|
  res.body = 'hello'
end
```

### Example 2: Advanced Usage

Mount multiple procs for different paths.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unusual HTTP headers
- Server logs for parsing errors

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/HAProxy]]

## References

- Ruby WEBrick documentation
