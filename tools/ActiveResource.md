---
url: 'https://github.com/rails/activeresource'
tags:
  - ruby-gem
  - rest-client
type: tool
verified: false
platforms:
  - Web
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.590Z'
id: 9c7f337e-e16c-40a6-8f78-7b2d0e039298
validated: true
submitted: true
---
# ActiveResource

**Status**: Unverified

## Overview

ActiveResource is a Ruby gem for simplified RESTful web service consumption in Rails apps, but its lack of ID encoding enables parameter injection in vulnerable setups like HackerOne's Payments backend.

## Description

It maps Ruby objects to remote REST resources, handling HTTP requests automatically. In this context, it's used to fetch Payment objects but decodes URLs without validation, allowing attacks via GraphQL global IDs.

## Features

- Feature 1: Automatic HTTP request construction for CRUD
- Feature 2: Integration with Rails models
- Feature 3: Support for custom headers and formats (e.g., .json)

## Installation

### Requirements

- Ruby 2.5+
- Rails 5+

### Install Commands

```bash
# Add to Gemfile
# gem 'activeresource'

bundle install
```

## Basic Usage

```bash
# In Rails console or script
Payment.find(1)  # Triggers GET /payments/1
```

### Common Options

| Option | Description |
|--------|-------------|
| site | Base URL for requests |
| format | Response format (json/xml) |

## Examples

### Example 1: Basic Usage

```ruby
class Payment < ActiveResource::Base
  self.site = "https://payments.example.com"
end
Payment.find(1)
```

### Example 2: Advanced Usage

```ruby
Payment.find('?param=value')  # Vulnerable injection
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Rails logs for unencoded paths in ActiveResource calls
- Scan for gem versions <7.0 without patches

## Related Procedures


## Related Tools

- [[tools/Rails]]
- [[tools/GraphQL-Ruby]]

## References

- Official documentation: https://api.rubyonrails.org/classes/ActiveResource/Base.html
- Related resources: HackerOne Report #800231
