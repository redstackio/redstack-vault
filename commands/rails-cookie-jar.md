---
data: cookies = request.cookie_jar
tags:
  - rails
  - cookie
type: command
executor: ruby
platforms:
  - Linux
id: 2ad28355-7266-4ce8-8344-fe9ba30c9b9b
created_at: '2025-12-11T06:10:40.422Z'
updated_at: '2025-12-11T06:10:40.422Z'
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

Retrieves the cookie jar from the request object for manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|


## Examples

### Basic Usage

```ruby
cookies = request.cookie_jar
```

## Expected Output

A cookie jar object.

## Related

- [[commands/rails-set-serializer]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
