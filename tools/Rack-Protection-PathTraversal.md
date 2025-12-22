---
url: 'https://github.com/rack/rack-protection'
tags:
  - middleware
  - protection
  - rails
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.345Z'
id: d42821e9-47fa-41e1-bf81-b21826b2661b
validated: true
submitted: true
---
# Rack-Protection-PathTraversal

**Status**: Unverified

## Overview

Rack::Protection::PathTraversal is a middleware for Ruby web apps (including Rails) that prevents path traversal attacks by blocking requests with suspicious path patterns like '/../'. It is not enabled by default and can be bypassed with encoded backslashes.

## Description

This tool provides protection against directory traversal by inspecting request paths for traversal sequences. In offensive security, it's analyzed for bypasses, such as using '%5c../' which evades detection but gets processed by downstream resolvers like ActionView. Commonly used in Rails apps via the rack-protection gem.

## Features

- Feature 1: Blocks paths starting with '/' followed by traversal
- Feature 2: Integrates into Rack middleware stack
- Feature 3: Configurable via Rails initializers

## Installation

### Requirements

- Ruby and Bundler
- Rack-compatible app (e.g., Rails)

### Install Commands

```bash
# Add to Gemfile
# gem 'rack-protection'

bundle install
```

## Basic Usage

```bash
# In config/application.rb or middleware
config.middleware.use Rack::Protection::PathTraversal
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | No CLI; configured in code |

## Examples

### Example 1: Basic Usage

```ruby
# Enable in Rails
Rails.application.config.middleware.use Rack::Protection::PathTraversal
```

### Example 2: Advanced Usage

```ruby
# Custom config if extended
use Rack::Protection::PathTraversal, suspicious_path: /\/\.\./
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery (defensive)

### Tactics

- [[Collection]] Collection (mitigation)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence in Gemfile.lock or middleware stack
- Logs showing blocked traversal requests

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[rack]]
- [[rails-security]]

## References

- Official documentation: https://github.com/rack/rack-protection
- Related resources: Rails security guide
