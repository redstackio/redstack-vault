---
data: 'verifier.generate(dump_target, purpose: :blob_key)'
tags:
  - payload
  - encode
  - ruby
type: command
output: Encoded string like "eyJfcmFpbHMiOnsibWVzc2FnZSI6..."
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.209Z'
id: e3e1cef8-084e-4d86-a3ca-b95c1d706485
verified: false
validated: true
submitted: true
---
# generate-encoded-payload

## Command

```ruby
verifier.generate(dump_target, purpose: :blob_key)
```

## Description

Generate the signed and encoded payload using the verifier for Active Storage URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| purpose | :blob_key | Yes |
| dump_target | Payload object | Yes |

## Examples

### Basic Usage

```ruby
verifier.generate(dump_target, purpose: :blob_key)
```

## Expected Output

Encoded string like "eyJfcmFpbHMiOnsibWVzc2FnZSI6..."

## Related

- [[commands/create-deprecation-proxy]]
