---
id: aa699e0f-e54a-4348-8ace-fa86bfa138bd
name: Space after Filename
type: sub-technique
mitre_id: T1036.006
mitre_url: null
created_at: '2023-04-06T00:31:27.096437+00:00'
updated_at: '2023-04-06T00:31:27.096437+00:00'
parent_technique: '[[Masquerading|T1036 - Masquerading]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Space after Filename

**MITRE ID**: T1036.006

**Parent Technique**: [[Masquerading|T1036 - Masquerading]]

This is a sub-technique of T1036 - Masquerading.

## Summary

Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system.

For example, if there is a Ma

## Description

Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system.

For example, if there is a Mach-O executable file called <code>evil.bin</code>, when it is double clicked by a user, it will launch Terminal.app and execute. If this file is renamed to <code>evil.txt</code>, then when double clicked by a user, it will launch with the default text editing application (not executing the binary). However, if the file is renamed to <code>evil.txt </code> (note the space at the end), then when double clicked by a user, the true file type is determined by the OS and handled appropriately and the binary will be executed (Citation: Mac Backdoors are back).

Adversaries can use this feature to trick users into double clicking benign-looking files of any format and ultimately executing something malicious.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
