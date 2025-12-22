---
data: 'result =u({message:"''\"<b>"}); result.message'
tags:
  - test
  - escaping
type: command
output: '"&#39;&quot;&lt;b&gt;\"'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.390Z'
id: f7b42b4f-719d-4bf5-9ea3-96fddd6b9807
verified: false
validated: true
submitted: true
---
# test-normal-escaping

## Command

```javascript
result =u({message:"'\"<b>"}); result.message
```

## Description

Tests escaping on a plain object string property.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| message | Test string with specials | Yes |

## Examples

### Basic Usage

```javascript
result =u({message:"'\"<b>"}); result.message
```

## Expected Output

"&#39;&quot;&lt;b&gt;\" (escaped).

## Related

- [[Related Procedure: Identify-Escaping-Function-Bypass]]
