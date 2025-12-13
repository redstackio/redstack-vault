---
url: null
tags:
  - web-server
  - ruby
type: tool
platforms:
  - Linux
description: Lightweight web framework for Ruby used to create simple web servers.
id: 03725a8d-7a62-40a4-81e1-5c46751e0d0f
created_at: '2025-12-13T09:00:27.273Z'
updated_at: '2025-12-13T09:00:27.273Z'
verified: false
validated: true
submitted: true
---
# Sinatra

**Status**: Unverified

## Overview

Sinatra is a lightweight web framework for Ruby, ideal for creating simple web servers to host malicious files in security testing scenarios like XXE exploitation.

## Description

It allows defining routes for HTTP endpoints quickly, used here to serve robots.txt, sitemap.xml, exfil.dtd, and pingback for data exfiltration.

## Features

- Feature 1: Simple route definition
- Feature 2: Lightweight and fast
- Feature 3: Easy integration with Ruby scripts

## Installation

### Requirements

- Ruby installed

### Install Commands

```bash
gem install sinatra
```

## Basic Usage

```bash
ruby server.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| `get '/'` | Define GET route |
| `set :bind` | Set bind address |

## Examples

### Example 1: Basic Usage

```ruby
require 'sinatra'
get '/robots.txt' { 'Sitemap: /sitemap.xml' }
```

### Example 2: Advanced Usage

```ruby
get '/pingback' { puts URI.unescape(request.query_string) }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Ruby processes binding to ports
- Detection method 2: Log unusual HTTP traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ruby]]

## References

- Official documentation: http://sinatrarb.com
