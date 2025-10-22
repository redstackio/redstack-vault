---
id: 6c1bd9a3-0ad6-4187-b7b6-2120c3d5de52
name: Steganography
type: sub-technique
mitre_id: T1027.003
mitre_url: null
created_at: '2023-04-06T00:31:26.875386+00:00'
updated_at: '2023-04-06T00:31:26.875386+00:00'
parent_technique: '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[VBA Obfuscation in Git Repositories]]'
---

# Steganography

**MITRE ID**: T1027.003

**Parent Technique**: [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

This is a sub-technique of T1027 - Obfuscated Files or Information.

## Summary

Adversaries may use steganography techniques in order to prevent the detection of hidden information. Steganographic techniques can be used to hide data in digital media such as images, audio tracks, video clips, or text files.

[Duqu](https://attack.mitre.org/software/S0038) was an early example of

## Description

Adversaries may use steganography techniques in order to prevent the detection of hidden information. Steganographic techniques can be used to hide data in digital media such as images, audio tracks, video clips, or text files.

[Duqu](https://attack.mitre.org/software/S0038) was an early example of malware that used steganography. It encrypted the gathered information from a victim's system and hid it within an image before exfiltrating the image to a C2 server.(Citation: Wikipedia Duqu) 

By the end of 2017, a threat group used <code>Invoke-PSImage</code> to hide [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands in an image file (.png) and execute the code on a victim's system. In this particular case the [PowerShell](https://attack.mitre.org/techniques/T1059/001) code downloaded another obfuscated script to gather intelligence from the victim's machine and communicate it back to the adversary.(Citation: McAfee Malicious Doc Targets Pyeongchang Olympics)  

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[VBA Obfuscation in Git Repositories]]
