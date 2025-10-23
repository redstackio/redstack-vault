---
id: 2428aafb-34e6-4be7-9840-05b2f645c151
name: Creating Files with Zero-Width Spaces
type: procedure
verified: true
submitted: true
created_at: '2020-01-23T22:06:49.225853+00:00'
updated_at: '2023-05-25T20:21:20.144028+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
platforms:
- Linux
tags:
- '[[Obfuscation]]'
---

# Creating Files with Zero-Width Spaces

**Status**: ✓ Verified

## Summary

Zero-width spaces are non-printing characters, used to indicate word boundaries to things like text processors. One of the many ways attackers can use these is creating filenames which are visually indistinguishable from those without them, creating confusing situations where multiple files appear 

## Description

# Description

Zero-width spaces are non-printing characters, used to indicate word boundaries to things like text processors. One of the many ways attackers can use these is creating filenames which are visually indistinguishable from those without them, creating confusing situations where multiple files appear to share the same name.

For example in this screenshot, two seemingly identical files exist, with the first one having been created with a zero-width space in between "i" and "n" :



![61b616e2-6976-4f25-bd10-d3edfa253b24.png](_assets/images/Mark/61b616e2-6976-4f25-bd10-d3edfa253b24.png)



# Instructions

In order to create files with zero-width spaces, the Unicode character must be entered. Much like Window's Alt key codes, Linux supports entering Unicode characters directly by first pressing:

(Left) [CTRL] + [SHIFT] + U", followed by the Unicode value, then [ENTER]

As a zero-width space is Unicode 200b, the combination would be:

(Left) [CTRL] + [SHIFT] + "U" + 200b + [ENTER]

For example, create a filename with a zero-width space:







**Code**: [[touch i[CTRL + SHIFT + U]200b[ENTER]ndex.html]]



This technique works for files, folders, and many other Linux object, giving attackers many opportunities to abuse the confusing names, and while they cannot be used in web domains, they can be used in the path value for web addresses.

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]

## Tags

- [[Obfuscation]]


