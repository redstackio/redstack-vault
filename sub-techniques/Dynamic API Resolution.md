---
id: 25c20aa6-c236-4987-b6a0-f559be4a59f0
name: Dynamic API Resolution
type: sub-technique
mitre_id: T1027.007
mitre_url: null
created_at: '2023-04-06T00:31:27.124148+00:00'
updated_at: '2023-04-06T00:31:27.124148+00:00'
parent_technique: '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Dynamic API Resolution

**MITRE ID**: T1027.007

**Parent Technique**: [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

This is a sub-technique of T1027 - Obfuscated Files or Information.

## Summary

Adversaries may obfuscate then dynamically resolve API functions called by their malware in order to conceal malicious functionalities and impair defensive analysis. Malware commonly uses various [Native API](https://attack.mitre.org/techniques/T1106) functions provided by the OS to perform various 

## Description

Adversaries may obfuscate then dynamically resolve API functions called by their malware in order to conceal malicious functionalities and impair defensive analysis. Malware commonly uses various [Native API](https://attack.mitre.org/techniques/T1106) functions provided by the OS to perform various tasks such as those involving processes, files, and other system artifacts.

API functions called by malware may leave static artifacts such as strings in payload files. Defensive analysts may also uncover which functions a binary file may execute via an import address table (IAT) or other structures that help dynamically link calling code to the shared modules that provide functions.(Citation: Huntress API Hash)(Citation: IRED API Hashing)

To avoid static or other defensive analysis, adversaries may use dynamic API resolution to conceal malware characteristics and functionalities. Similar to [Software Packing](https://attack.mitre.org/techniques/T1027/002), dynamic API resolution may change file signatures and obfuscate malicious API function calls until they are resolved and invoked during runtime.

Various methods may be used to obfuscate malware calls to API functions. For example, hashes of function names are commonly stored in malware in lieu of literal strings. Malware can use these hashes (or other identifiers) to manually reproduce the linking and loading process using functions such as `GetProcAddress()` and `LoadLibrary()`. These hashes/identifiers can also be further obfuscated using encryption or other string manipulation tricks (requiring various forms of [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) during execution).(Citation: BlackHat API Packers)(Citation: Drakonia HInvoke)(Citation: Huntress API Hash)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
