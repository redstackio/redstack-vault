---
data: cookies = request.cookie_jar
tags:
  - rails
  - cookie
type: command
executor: ruby
platforms:
  - Linux
id: 59b8049e-5b4f-4e3d-b3c2-a6c3dc7e838c
created_at: '2025-12-11T03:47:59.289Z'
updated_at: '2025-12-11T03:47:59.289Z'
verified: false
validated: true
submitted: true
---
# rails-cookie-jar

## Command

```ruby
cookies = request.cookie_jar
```

## Description

Retrieves the cookie jar from the request object for signing and serializing payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```ruby
cookies = request.cookie_jar
```

## Expected Output

Cookie jar object.

## Related

- [[commands/rails-set-serializer]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
