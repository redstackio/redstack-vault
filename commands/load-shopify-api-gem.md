---
id: cmd-load-shopify-001
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
updated_at: '2025-12-14T17:32:28.657Z'
verified: false
validated: true
submitted: true
---
---

# load-shopify-api-gem

## Command

```ruby
require 'shopify_api'
```

## Description

Loads the Shopify API Ruby gem into the current Ruby session, enabling use of ShopifyAPI classes like Session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; standard require | Yes |

## Examples

### Basic Usage

```ruby
require 'shopify_api'
```

### Advanced Usage

Typically used at the start of a pry or irb session.

## Expected Output

true (indicating successful load)

## Related

- [[commands/setup-session-benign-port]]
- [[procedures/Test-Session-Setup-with-Port-Parameter]]

---
