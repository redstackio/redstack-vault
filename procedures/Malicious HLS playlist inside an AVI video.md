---
id: e37cfb90-5248-4599-ba99-2d3f02051f90
name: Malicious HLS playlist inside an AVI video
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.790201+00:00'
updated_at: '2023-04-06T03:56:40.808734+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
sub_techniques:
- '[[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]'
tags:
- '[[Exploits]]'
- '[[FFmpeg HLS vulnerability]]'
commands:
- '[[Access file contents on server]]'
- '[[Convert file to AVI format]]'
- '[[Execute ffmpeg command on server side]]'
- '[[Play video]]'
- '[[Upload AVI file to video processing website]]'
---

# Malicious HLS playlist inside an AVI video

## Summary

This procedure exploits a vulnerability in FFmpeg that allows an attacker to embed a malicious HLS playlist inside an AVI video file. When the video is played, the embedded playlist triggers the vulnerability and allows the attacker to execute arbitrary code on the victim's machine. This can lead t

## Description

# Description

This procedure exploits a vulnerability in FFmpeg that allows an attacker to embed a malicious HLS playlist inside an AVI video file. When the video is played, the embedded playlist triggers the vulnerability and allows the attacker to execute arbitrary code on the victim's machine. This can lead to complete compromise of the system and theft of sensitive information.

To execute this attack, the attacker needs to create a specially crafted AVI video file with the embedded playlist. The victim needs to download and play the video file on their machine, which can be achieved through social engineering or other means.

This procedure can be used by attackers to gain access to sensitive information, steal credentials, or deploy malware on the victim's machine.

 

## Requirements

1. Victim needs to download and play the specially crafted AVI video file

 

## Defense

1. Ensure all software is up-to-date to prevent known vulnerabilities

1. Use anti-virus software to detect and prevent the download and execution of malicious files

1. Educate users on the dangers of downloading and playing files from untrusted sources

 

## Objectives

1. Execute arbitrary code on the victim's machine

1. Gain access to sensitive information

1. Steal credentials

1. Deploy malware on the victim's machine

 

# Instructions

1. To execute this command, you need to follow the steps provided in the `data` field. First, run the command `./gen_xbin_avi.py file://<filename> file_read.avi` to generate a new AVI file. Next, upload the generated `file_read.avi` to a website that processes video files. The videoservice will execute the command `ffmpeg -i file_read.avi output.mp4` on the server side. Finally, click the "Play" button in the videoservice to access the contents of `<filename>` from the server.

 

This command exploits a vulnerability in FFmpeg software, which allows an attacker to embed a malicious HLS playlist inside an AVI video file. When the video file is processed by a videoservice, the malicious playlist is executed on the server side, which can lead to arbitrary file read. The steps provided in the `data` field are a proof-of-concept of how this vulnerability can be exploited.



**Command** ([[Convert file to AVI format]]):

```bash
./gen_xbin_avi.py file://<filename> file_read.avi
```





**Command** ([[Upload AVI file to video processing website]]):

```bash
file_read.avi
```





**Command** ([[Execute ffmpeg command on server side]]):

```bash
ffmpeg -i file_read.avi output.mp4
```





**Command** ([[Play video]]):

```bash
output.mp4
```





**Command** ([[Access file contents on server]]):

```bash
<filename>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Hide Artifacts|T1564 - Hide Artifacts]]

### Sub-Techniques

- [[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]

## Commands Used

- [[Access file contents on server]]
- [[Convert file to AVI format]]
- [[Execute ffmpeg command on server side]]
- [[Play video]]
- [[Upload AVI file to video processing website]]

## Tags

- [[Exploits]]
- [[FFmpeg HLS vulnerability]]


