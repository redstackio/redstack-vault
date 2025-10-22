---
id: 169be0b7-8777-49bf-9294-3b168befc5bc
name: smbclient
type: tool
verified: false
created_at: '2019-08-28T21:17:32.203892+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[smbclient -U '''' -N -L $_TARGET_IP]]'
- '[[smbclient List SMB Shares]]'
platforms:
- Linux
- Windows
tags:
- '[[File System]]'
- '[[Network]]'
---

# smbclient

## Overview

Smbclient is used to connect to SMB/CIFS shares, providing an interface with which users can query and interact with SMB/CIFS services. Common uses include share enumeration, file/directory enumeration, file upload and download, and more. Not only can smbclient authenticate with a username and pass

## Description

# Description

Smbclient is used to connect to SMB/CIFS shares, providing an interface with which users can query and interact with SMB/CIFS services. Common uses include share enumeration, file/directory enumeration, file upload and download, and more. Not only can smbclient authenticate with a username and password, it also supports authentication using a Windows NT hash, allowing users to authenticate with uncracked password hashes assuming the target system supports it.

# Example

# Installation

## Install on Debian/Ubuntu

## Platforms

- Linux
- Windows

## Services

- netbios-ss
- smb

## Commands (2)

- [[smbclient -U '' -N -L $_TARGET_IP]]
- [[smbclient List SMB Shares]]

## Tags

- [[File System]]
- [[Network]]
