---
data: 'let f =new File(["data"],"controlledvalue"); f.name; f.hasOwnProperty("name");'
tags:
  - file
  - object
type: command
output: '"controlledvalue"; false'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.383Z'
id: d2b29906-24f2-49eb-ad90-8c054acdfc1a
verified: false
validated: true
submitted: true
---
# create-file-object

## Command

```javascript
let f =new File(["data"],"controlledvalue"); f.name; f.hasOwnProperty("name");
```

## Description

Creates a File object and checks its 'name' property enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ["data"] | File contents array | Yes |
| "controlledvalue" | File name | Yes |

## Examples

### Basic Usage

```javascript
let f =new File(["data"],"controlledvalue"); f.name; f.hasOwnProperty("name");
```

## Expected Output

"controlledvalue"; false

## Related

- [[Related Procedure: Identify-Escaping-Function-Bypass]]
