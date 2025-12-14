---
data: require 'private_address_check'
tags:
  - testing
  - ruby
type: command
executor: ruby
platforms:
  - Ruby
id: 1e9b4a79-71c5-40bc-84b1-bd4468e56dd0
created_at: '2025-12-14T04:08:54.855Z'
updated_at: '2025-12-14T04:08:54.855Z'
verified: false
validated: true
submitted: true
---
# Require Private Address Check

## Command

```ruby
require 'private_address_check'
```

## Description

This command loads the private_address_check Ruby gem into the current session, enabling use of its IP validation methods for SSRF testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | The gem name is hardcoded | Yes |

## Examples

### Basic Usage

```ruby
require 'private_address_check'
```

### Advanced Usage

In IRB:
```ruby
irb
> require 'private_address_check'
```

## Expected Output

`true` - Indicates the gem was successfully loaded.

## Related

- [[commands/private-address-check-0.0.0.0]]
