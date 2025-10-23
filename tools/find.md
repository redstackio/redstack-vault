---
id: 1eaf0072-48c3-4b71-a42b-9336cc054641
name: find
type: tool
verified: false
created_at: '2019-08-28T21:17:29.215711+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[find $DIRECTORY -perm -4000 -ls 2>/dev/null]]'
- '[[find Search for Files with SUID Rights]]'
platforms:
- Linux
tags:
- '[[Enumeration]]'
- '[[File System]]'
---

# find

## Overview

Find is a standard Linux/Unix utility used for recursively searching a file system for files and folders, based on user-specified criteria. Find includes many options for restricting search results, including by name, type, permissions, owner, group, timestamps (MAC), and more. It is extremely usef

## Description

# Description

Find is a standard Linux/Unix utility used for recursively searching a file system for files and folders, based on user-specified criteria. Find includes many options for restricting search results, including by name, type, permissions, owner, group, timestamps (MAC), and more. It is extremely useful when enumerating a file system for vulnerabilities, as it can quickly identify files with SUID permissions, weak or incorrect permissions, and other attributes which make files and folders stand out. 
 
 Note: Using find to search files and folders which the user lacks permissions to list will generate permission errors, and cause clutter in search results. For this reason, stderr is often piped into /dev/null.



# Example



{{EMBEDDED_COMMAND_90e9e6c8-c80e-480d-a9f4-1ad2d14e7772}}



# Installation

## Install on Debian/Ubuntu









## Platforms

- Linux

## Commands (2)

- [[find $DIRECTORY -perm -4000 -ls 2>/dev/null]]
- [[find Search for Files with SUID Rights]]

## Tags

- [[Enumeration]]
- [[File System]]


