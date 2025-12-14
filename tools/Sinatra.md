---
url: 'https://sinatrarb.com/'
tags:
  - web-server
  - ruby
  - cors
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T17:27:03.498Z'
id: 7fac3bea-41b8-4908-8f4b-ff2ab508b0e6
validated: true
submitted: true
---
# Sinatra

**Status**: Unverified

## Overview

Sinatra is a lightweight Ruby DSL for creating web applications, ideal for quickly setting up servers to handle HTTP requests, including CORS configurations for capturing cross-origin data like CSRF tokens in security testing.

## Description

Sinatra enables domain-specific language for routing and handling requests with minimal boilerplate. In offensive security, it's used to prototype malicious endpoints that receive exfiltrated data, support CORS for browser-based attacks, and log headers like authentication tokens. It's domain-specific to Ruby ecosystems like Rails exploitation scenarios.

## Features

- Feature 1: Simple routing for GET, POST, OPTIONS with custom headers
- Feature 2: Built-in support for Rack middleware, including CORS handling
- Feature 3: Lightweight and fast startup for temporary attack servers

## Installation

### Requirements

- Ruby 2.0+ installed
- Bundler for gem management

### Install Commands

```bash
# Install Sinatra gem
gem install sinatra
```

## Basic Usage

```bash
ruby app.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p PORT` | Specify port (default 4567) |
| `-e ENVIRONMENT` | Set environment (development/production) |

## Examples

### Example 1: Basic Usage

Create a simple echo server:

```ruby
require 'sinatra'
get '/' do
  'Hello World'
end
```

Run: `ruby app.rb`, visit http://localhost:4567.

### Example 2: Advanced Usage

CORS-enabled POST capturer:

```ruby
require 'sinatra'

options '/*' do
  headers['Access-Control-Allow-Origin'] = '*'
  headers['Access-Control-Allow-Methods'] = 'POST'
  headers['Access-Control-Allow-Headers'] = 'x-csrf-token'
  200
end

post '/' do
  token = request.env['HTTP_X_CSRF_TOKEN']
  token || 'No token'
end
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Web Session Cookie]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Sinatra banner in responses
- Unusual Ruby processes on servers with open ports (e.g., 4567)
- CORS headers from non-standard domains

## Related Procedures


## Related Tools

- [[tools/Express.js]]
- [[tools/Flask]]

## References

- Official documentation: https://sinatrarb.com/documentation.html
- Related resources: RubyGems.org for Sinatra
