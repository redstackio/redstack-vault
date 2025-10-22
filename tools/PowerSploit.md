---
id: f2063482-207f-4a17-aa4f-c4b6f723177b
name: PowerSploit
type: tool
verified: false
created_at: '2019-08-28T21:17:33.769050+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[hacking]]'
- '[[persistence]]'
- '[[powershell]]'
---

# PowerSploit

## Overview

A collection of Microsoft PowerShell modules that can be used to aid penetration testers during all phases of an assessment. ​PowerSploit is made up  of the following modules and scripts: 

## Description

# Description

A collection of Microsoft PowerShell modules that can be used to aid penetration testers during all phases of an assessment. ​PowerSploit is made up  of the following modules and scripts:

## Execution

- Invoke-DllInjection - Injects a Dll into the process ID of your choosing.

- Invoke-ReflectivePEInjection - Reflectively loads a Windows PE file (DLL/EXE) in to the powershell process, or reflectively injects a DLL in to a remote process.

- Invoke-Shellcode - Injects shellcode into the process ID of your choosing or within PowerShell locally.

- Invoke-WmiCommand - Executes a PowerShell ScriptBlock on a target computer and returns its formatted output using WMI as a C2 channel.

## ScriptModification

- Out-EncodedCommand - Compresses, Base-64 encodes, and generates command-line output for a PowerShell payload script.

- Out-CompressedDll - Compresses, Base-64 encodes, and outputs generated code to load a managed dll in memory.

- Out-EncryptedScript - Encrypts text files/scripts.

- Remove-Comments - Strips comments and extra whitespace from a script.

## Persistence

- New-UserPersistenceOption - Configure user-level persistence options for the Add-Persistence function.

- New-ElevatedPersistenceOption - Configure elevated persistence options for the Add-Persistence function.

- Add-Persistence - Add persistence capabilities to a script.

- Install-SSP - Installs a security support provider (SSP) dll.

- Get-SecurityPackages - Enumerates all loaded security packages (SSPs).

## AntivirusBypass

- Find-AVSignature - Locates single Byte AV signatures utilizing the same method as DSplit from "class101".

## Exfiltration

- Invoke-TokenManipulation - Lists available logon tokens. Creates processes with other users logon tokens, and impersonates logon tokens in the current thread.

- Invoke-CredentialInjection - Create logons with clear-text credentials without triggering a suspicious Event ID 4648 (Explicit Credential Logon).

- Invoke-NinjaCopy - Copies a file from an NTFS partitioned volume by reading the raw volume and parsing the NTFS structures.

- Invoke-Mimikatz - Reflectively loads Mimikatz 2.0 in memory using PowerShell. Can be used to dump credentials without writing anything to disk. Can be used for any functionality provided with Mimikatz.

- Get-Keystrokes - Logs keys pressed, time and the active window.

- Get-GPPPassword - Retrieves the plaintext password and other information for accounts pushed through Group Policy Preferences.

- Get-GPPAutologon - Retrieves autologon username and password from registry.xml if pushed through Group Policy Preferences.

- Get-TimedScreenshot - A function that takes screenshots at a regular interval and saves them to a folder.

- New-VolumeShadowCopy - Creates a new volume shadow copy.

- Get-VolumeShadowCopy - Lists the device paths of all local volume shadow copies.

- Mount-VolumeShadowCopy - Munts a volume shadow copy.

- Remove-VolumeShadowCopy - Deletes a volume shadow copy.

- Get-VaultCredential - Displays Windows vault credential objects including cleartext web credentials.

- Out-Minidump - Generates a full-memory minidump of a process.

- Get-MicrophoneAudio - Records audio from system microphone and saves to disk

## Mayhem

- Set-MasterBootRecord - Proof of concept code that overwrites the master boot record with the message of your choice.

- Set-CriticalProcess - Causes your machine to blue screen upon exiting PowerShell.

## Privesc

- PowerUp - Clearing house of common privilege escalation checks, along with some weaponization vectors.

## Recon

- Invoke-Portscan - Does a simple port scan using regular sockets, based (pretty) loosely on nmap.

- Get-HttpStatus - Returns the HTTP Status Codes and full URL for specified paths when provided with a dictionary file.

- Invoke-ReverseDnsLookup - Scans an IP address range for DNS PTR records.

- PowerView - PowerView is series of functions that performs network and Windows domain enumeration and exploitation.

# Installation

## Clone from GitHub (Windows)

PowerSploit with all modules can be loaded on a Windows system by cloning the git repository and copying it to the PowerShell modules directory

1. Clone the dev branch from GitHub

2. Copy the entire PowerSploit folder to the system's PowerShell modules directory (often C:\windows\system32\WindowsPowerShell\v1.0\Modules)

3. PowerSploit can now be imported as any other module with "Invoke-Module Powersploit"

## Platforms

- Windows

## Tags

- [[Active Directory]]
- [[hacking]]
- [[persistence]]
- [[powershell]]
