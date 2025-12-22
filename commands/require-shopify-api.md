---
id: cmd-uuid-1
data: require 'shopify_api'
tags:
  - setup
  - shopify
type: command
output: 'true'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.762Z'
verified: false
validated: true
submitted: true
---
# require-shopify-api

## Command

```ruby
require 'shopify_api'
```

## Description

Loads the Shopify API Ruby gem into the current Ruby environment, making classes like ShopifyAPI::Session available for use in interactive shells or scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Standard require syntax for gems | Yes |

## Examples

### Basic Usage

```ruby
require 'shopify_api'
```

### Advanced Usage

In a script: include at top for SDK access.

## Expected Output

true (indicating successful load)

## Related

- [[commands/setup-session-with-port]]
