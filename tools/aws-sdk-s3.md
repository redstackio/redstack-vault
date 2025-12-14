---
id: tool-uuid-1
url: 'https://github.com/aws/aws-sdk-ruby/tree/master/gems/aws-sdk-s3'
tags:
  - aws
  - s3
  - sdk
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.027Z'
validated: true
submitted: true
---
# aws-sdk-s3

**Status**: Unverified

## Overview

Ruby gem for AWS S3 interactions, used in Rails ActiveStorage; vulnerable due to content-length blacklisting in presigned URLs.

## Description

Provides APIs for S3 operations like presigned_url generation. In this context, presigner.rb blacklists headers, enabling bypasses.

## Features

- Feature 1: Presigned URL creation for direct uploads
- Feature 2: Header signing with blacklists
- Feature 3: Integration with Rails ActiveStorage

## Installation

### Requirements

- Ruby 2.5+
- Bundler

### Install Commands

```bash
gem install aws-sdk-s3
# Or in Gemfile: gem 'aws-sdk-s3'
bundle install
```

## Basic Usage

```ruby
require 'aws-sdk-s3'
s3 = Aws::S3::Resource.new
obj = s3.bucket('mybucket').object('key')
url = obj.presigned_url(:put, expires_in: 3600)
```

### Common Options

| Option | Description |
|--------|-------------|
| `whitelist_headers` | Array to include blacklisted headers like content-length |
| `expires_in` | URL expiration time |

## Examples

### Example 1: Basic Usage

```ruby
url = obj.presigned_url(:put, content_type: 'text/plain')
puts url
```

### Example 2: Advanced Usage

```ruby
url = obj.presigned_url(:put, whitelist_headers: ['content-length'], content_length: 10000)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor gem dependencies in Rails apps
- Log presigned URL generations without whitelists

## Related Procedures


## Related Tools

- [[ActiveStorage]]

## References

- Official documentation: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/s3-examples.html
