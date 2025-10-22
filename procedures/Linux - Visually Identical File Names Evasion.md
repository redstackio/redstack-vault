---
id: 21a22695-69e8-4e8d-86cd-4ed7e975bb9f
name: Linux - Visually Identical File Names Evasion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.635873+00:00'
updated_at: '2023-04-10T20:34:11.607001+00:00'
tags:
- '[[File Names]]'
- '[[Linux - Evasion]]'
commands:
- '[[Create decoy and imposter files]]'
---

# Linux - Visually Identical File Names Evasion

## Summary

The Linux - Visually Identical File Names Evasion technique involves creating files with visually identical names as legitimate files to evade detection. In this technique, an attacker creates a file with a name that looks identical to a legitimate file, but with a different file extension or a sli

## Description

# Description

The Linux - Visually Identical File Names Evasion technique involves creating files with visually identical names as legitimate files to evade detection. In this technique, an attacker creates a file with a name that looks identical to a legitimate file, but with a different file extension or a slight variation in spelling. The attacker can then use this file to execute malicious code or hide their presence on the system.

From a technical perspective, this technique relies on the fact that many users and system administrators rely on visual inspection of file names to identify files. By creating files with visually identical names, an attacker can trick users and administrators into thinking that the file is legitimate.

The business value of this technique is that it allows attackers to evade detection and execute malicious code on a system without being detected.

## Requirements

1. Access to a Linux system

1. Ability to create files

## Defense

1. Implement file name validation checks to detect visually identical file names

1. Use file integrity monitoring tools to detect changes to files

1. Limit user privileges to prevent unauthorized file creation

## Objectives

1. Evade detection on a Linux system

1. Execute malicious code on a Linux system

# Instructions

1. To create two files with visually identical names, you can use the touch command in bash and insert an Unicode zero-width space into the name of one of the files using the $'filename\u200D.extension' syntax.

**Code**: [[# A decoy file with no special characters
touch 'i]]

> The touch command is used to create new empty files in bash. By default, it creates files with the given name in the current directory. To create a second file with a visually identical name, we can use the $'filename\u200D.extension' syntax to insert an Unicode zero-width space into the name of one of the files. This makes the two filenames visually identical, but their underlying Unicode representations are different. This can be useful for testing purposes or for creating files with names that are difficult to distinguish at a glance.

**Command** ([[Create decoy and imposter files]]):

```bash
touch 'index.php'

touch $'index\u200D.php'
```

## Commands Used

- [[Create decoy and imposter files]]

## Tags

- [[File Names]]
- [[Linux - Evasion]]
