---
id: fab78900-de58-44c7-a95a-253f240b9ae3
name: Cobalt Strike File Management
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.450374+00:00'
updated_at: '2023-04-10T20:36:25.642419+00:00'
tags:
- '[[Cobalt Strike]]'
- '[[Files]]'
commands:
- '[[Cancel download]]'
- '[[Change working directory]]'
- '[[Copy file]]'
- '[[Delete file or folder]]'
- '[[Download file]]'
- '[[List directory contents]]'
- '[[List downloads]]'
- '[[Upload file]]'
---

# Cobalt Strike File Management

## Summary

Cobalt Strike's file management commands allow an attacker to manipulate files on a compromised system. This can include uploading, downloading, and deleting files. These commands can be used to move laterally through a network, exfiltrate data, or execute payloads.

From a technical perspective, t

## Description

# Description

Cobalt Strike's file management commands allow an attacker to manipulate files on a compromised system. This can include uploading, downloading, and deleting files. These commands can be used to move laterally through a network, exfiltrate data, or execute payloads.

From a technical perspective, these commands are executed through a Command and Control (C2) server, which communicates with the Cobalt Strike implant on the compromised system. The implant then executes the desired file management command. 

From a business perspective, these commands can be used to steal sensitive data, disrupt business operations, or install malware on a network.

## Requirements

1. Access to a compromised system with a Cobalt Strike implant installed

1. Authenticated access to the system

## Defense

1. Monitor for suspicious file activity on systems

1. Implement access controls to prevent unauthorized access to systems

1. Use endpoint detection and response tools to detect and respond to Cobalt Strike activity

## Objectives

1. Manipulate files on a compromised system

1. Move laterally through a network

1. Exfiltrate data

1. Execute payloads

# Instructions

1. These commands are used for file management on the target system. The 'ls' command is used to list the files in the specified directory. The 'cd' command is used to change the current working directory. The 'rm' command is used to delete a file or folder. The 'cp' command is used to copy a file. The 'download' command is used to download a file from the target system. The 'downloads' command is used to list the downloads in progress. The 'cancel' command is used to cancel a download in progress. The 'upload' command is used to upload a file from the attacker's system to the target system.

**Code**: [[# List the file on the specified directory
beacon ]]

> The 'ls' command takes an optional path argument which specifies the directory to list the files in. The 'cd' command takes a directory argument which specifies the directory to change the current working directory to. The 'rm' command takes a file or folder argument which specifies the file or folder to delete. The 'cp' command takes a source file argument and a destination file argument which specifies the source and destination paths respectively. The 'download' command takes a file path argument which specifies the file to download from the target system. The 'cancel' command takes a file argument which specifies the file download to cancel. The 'upload' command takes a file path argument which specifies the file to upload to the target system.

**Command** ([[List directory contents]]):

```bash
beacon > ls <C:\Path>
```

**Command** ([[Change working directory]]):

```bash
beacon > cd [directory]
```

**Command** ([[Delete file or folder]]):

```bash
beacon > rm [file\folder]
```

**Command** ([[Copy file]]):

```bash
beacon > cp [src] [dest]
```

**Command** ([[Download file]]):

```bash
beacon > download [C:\filePath]
```

**Command** ([[List downloads]]):

```bash
beacon > downloads
```

**Command** ([[Cancel download]]):

```bash
beacon > cancel [*file*]
```

**Command** ([[Upload file]]):

```bash
beacon > upload [/path/to/file]
```

## Commands Used

- [[Cancel download]]
- [[Change working directory]]
- [[Copy file]]
- [[Delete file or folder]]
- [[Download file]]
- [[List directory contents]]
- [[List downloads]]
- [[Upload file]]

## Tags

- [[Cobalt Strike]]
- [[Files]]
