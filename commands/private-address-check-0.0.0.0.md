---
data: PrivateAddressCheck.private_address?("0.0.0.0")
tags:
  - ssrf
  - bypass
  - testing
type: command
executor: ruby
platforms:
  - Ruby
id: 7be0eac1-7023-46bb-aa37-2b0f82f9a7fc
created_at: '2025-12-14T04:08:48.868Z'
updated_at: '2025-12-14T04:08:48.868Z'
verified: false
validated: true
submitted: true
---
# Private Address Check 0.0.0.0

## Command

```ruby
PrivateAddressCheck.private_address?("0.0.0.0")
```

## Description

This command queries the private_address_check gem to determine if the IP '0.0.0.0' is classified as a private address, demonstrating the bypass flaw when it returns false.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ip | The IP address string to validate, e.g., "0.0.0.0" | Yes |

## Examples

### Basic Usage

```ruby
PrivateAddressCheck.private_address?("0.0.0.0")
```

### Advanced Usage

In a script or IRB after requiring the gem:
```ruby
PrivateAddressCheck.private_address?("0.0.0.0")
# Returns false due to gem flaw
```

## Expected Output

`false` - Confirms '0.0.0.0' is not treated as private, allowing SSRF bypass.

## Related

- [[commands/require-private-address-check]]
