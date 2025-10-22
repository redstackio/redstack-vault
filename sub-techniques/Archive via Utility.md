---
id: adac0244-c505-4cb5-9b84-798b02dfdc6e
name: Archive via Utility
type: sub-technique
mitre_id: T1560.001
mitre_url: null
created_at: '2023-04-06T00:31:25.411245+00:00'
updated_at: '2023-04-06T00:31:25.411245+00:00'
parent_technique: '[[Archive Collected Data|T1560 - Archive Collected Data]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Archive via Utility

**MITRE ID**: T1560.001

**Parent Technique**: [[Archive Collected Data|T1560 - Archive Collected Data]]

This is a sub-technique of T1560 - Archive Collected Data.

## Summary

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.

Adversaries may abuse various utilities to compress or encrypt

## Description

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.

Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as <code>tar</code> on Linux and macOS or <code>zip</code> on Windows systems. On Windows, <code>diantz</code> or <code> makecab</code> may be used to package collected files into a cabinet (.cab) file. <code>diantz</code> may also be used to download and compress files from remote locations (i.e. [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002)).(Citation: diantz.exe_lolbas) Additionally, <code>xcopy</code> on Windows can copy files and directories with a variety of options.

Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.(Citation: 7zip Homepage)(Citation: WinRAR Homepage)(Citation: WinZip Homepage)

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
