---
id: 50c9b0a5-4bcd-40ea-a09b-e737486ba100
name: Embed a File In an Image Using Steghide
type: procedure
verified: false
submitted: false
created_at: '2019-10-10T00:28:44.147383+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
tags:
- '[[Cryptography]]'
- '[[data encryption]]'
commands:
- '[[Steghide Embed a File in an Image]]'
---

# Embed a File In an Image Using Steghide

## Summary

Embed a file within an image (or audio file) using steganography, effectively hiding the original file within an image/audio which appears innocent. In most cases, the only noticeable differences are file size and occasionally the quality. 

## Description

# Description

Embed a file within an image (or audio file) using steganography, effectively hiding the original file within an image/audio which appears innocent. In most cases, the only noticeable differences are file size and occasionally the quality.



# Instructions

Select a cover file and embedded file. For this example, an image will be used to hide  an SSH public key.





**Command** ([[Steghide Embed a File in an Image]]):

```bash
steghide embed -ef $_EMBEDDED -cf $_COVER
```





Final image using a password of 'secret'.



![50bc6f59-b52a-472a-88bc-58dcccc906ac.jpg](_assets/images/Mark/50bc6f59-b52a-472a-88bc-58dcccc906ac.jpg)



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]

## Commands Used

- [[Steghide Embed a File in an Image]]

## Tags

- [[Cryptography]]
- [[data encryption]]


