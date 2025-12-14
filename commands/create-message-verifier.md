---
data: 'verifier = ActiveSupport::MessageVerifier.new(secret)'
tags:
  - payload
  - verifier
  - ruby
type: command
output: MessageVerifier object with Marshal serializer
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.268Z'
id: b6556698-288c-419b-aaa0-b0e66ea72d62
verified: false
validated: true
submitted: true
---
# create-message-verifier

## Command

```ruby
verifier = ActiveSupport::MessageVerifier.new(secret)
```

## Description

Instantiate a MessageVerifier with the generated secret to encode the malicious payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| secret | Secret key | Yes |

## Examples

### Basic Usage

```ruby
verifier = ActiveSupport::MessageVerifier.new(secret)
```

## Expected Output

MessageVerifier object with Marshal serializer

## Related

- [[commands/generate-activestorage-secret]]
