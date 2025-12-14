---
url: 'https://github.com/lostisland/faraday'
tags:
  - http-client
  - ruby
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.642Z'
id: 27bccfef-0f93-44cf-9f50-ae34935f71b1
validated: true
submitted: true
---
# Faraday-Ruby-HTTP-Client

**Status**: Unverified

## Overview

Faraday is a Ruby HTTP client library for making requests, commonly used in security testing for API interactions like uploading malicious packages to endpoints.

## Description

Faraday supports multiple adapters (Net::HTTP, Typhoeus) and middleware for handling authentication, retries, and multipart uploads. In offensive ops, it's used to simulate client uploads exploiting web vulnerabilities without browser dependencies.

## Features

- Feature 1: Adapter-agnostic HTTP requests
- Feature 2: Built-in authentication (Basic, OAuth)
- Feature 3: Multipart file uploads for package exploits

## Installation

### Requirements

- Ruby 2.6+
- Bundler

### Install Commands

```bash
# Installation command
gem install faraday
```

## Basic Usage

```bash
irb -r faraday
conn = Faraday.new(url: 'https://example.com')
response = conn.get('/path')
```

### Common Options

| Option | Description |
|--------|-------------|
| -r, --require | Require library in IRB |
| url: | Base URL for connections |

## Examples

### Example 1: Basic Usage

```ruby
require 'faraday'
conn = Faraday.new
response = conn.get('https://httpbin.org/get')
puts response.body
```

### Example 2: Advanced Usage

```ruby
conn = Faraday.new(url: 'https://target.com') do |f|
  f.basic_auth('user', 'pass')
end
conn.put('/api/upload', {file: File.read('payload')})
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Ruby User-Agent in API calls
- Gem installation traces in package managers

## Related Procedures

- [[procedures/Upload-Malicious-NuGet-Package-to-GitLab-Registry]]

## Related Tools

- [[tools/RubyZip-Archive-Library]]

## References

- Official documentation: https://lostisland.github.io/faraday
- Related resources: RubyGems.org
