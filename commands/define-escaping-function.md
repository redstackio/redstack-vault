---
data: >-
  function u(payload){for(var idx in payload){if(payload.hasOwnProperty(idx)){
  payload[idx]= Ve.escapeHtml(payload[idx]);}} return payload;}
tags:
  - escaping
  - function
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.394Z'
id: ab9cf52c-46e4-464a-a24d-e952ede19146
verified: false
validated: true
submitted: true
---
# define-escaping-function

## Command

```javascript
function u(payload){for(var idx in payload){if(payload.hasOwnProperty(idx)){ payload[idx]= Ve.escapeHtml(payload[idx]);}} return payload;}
```

## Description

Defines the vulnerable escaping function that skips non-hasOwnProperty props.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | Object to escape | Yes |

## Examples

### Basic Usage

```javascript
function u(payload){for(var idx in payload){if(payload.hasOwnProperty(idx)){ payload[idx]= Ve.escapeHtml(payload[idx]);}} return payload;}
```

## Expected Output

Escaped object (partial).

## Related

- [[Related Procedure: Identify-Escaping-Function-Bypass]]
