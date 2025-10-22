---
id: b4399afe-6172-4e82-9706-a94dbce3416f
name: SCF and URL File Attack Against Writable Share via Windows Library Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.460601+00:00'
updated_at: '2023-04-10T20:26:19.207769+00:00'
tags:
- '[[Active Directory Attacks]]'
- '[[SCF and URL file attack against writeable share]]'
- '[[Windows Library Files]]'
---

# SCF and URL File Attack Against Writable Share via Windows Library Files

## Summary

This attack involves using Windows Library Files (.library-ms files) to execute malicious code on a target system. Attackers can create a specially crafted library file that contains a reference to a malicious .scf or .url file hosted on a remote server. When the library file is opened, the .scf or

## Description

# Description

This attack involves using Windows Library Files (.library-ms files) to execute malicious code on a target system. Attackers can create a specially crafted library file that contains a reference to a malicious .scf or .url file hosted on a remote server. When the library file is opened, the .scf or .url file is automatically executed, which can lead to the execution of arbitrary code on the target system. This technique can be used to gain elevated privileges on a compromised system, and can be particularly effective when combined with other attack techniques.

From a technical perspective, this attack relies on the fact that Windows Library Files are designed to allow users to quickly and easily access frequently used files and folders. When a user opens a library file, Windows Explorer automatically loads the file paths contained within the library, and displays them in a convenient interface. By including a reference to a malicious .scf or .url file in a specially crafted library file, attackers can trick Windows Explorer into executing the malicious file when the library is opened.

From a business perspective, this attack can be used to gain access to sensitive data or systems, and can be particularly effective when combined with social engineering techniques. By convincing a user to open a malicious library file, an attacker can execute arbitrary code on the target system, potentially leading to the compromise of sensitive data or systems.

## Requirements

1. Access to a writable share on the target system

1. A malicious .scf or .url file hosted on a remote server

1. Ability to create a specially crafted Windows Library File

## Defense

1. Implement least privilege policies to restrict access to sensitive systems and data

1. Monitor for and block suspicious network traffic, particularly traffic involving .scf and .url files

1. Disable the WebClient service to prevent the automatic execution of remote .scf and .url files

## Objectives

1. Gain elevated privileges on a compromised system

1. Execute arbitrary code on a target system

1. Access sensitive data or systems

# Instructions

1. This command provides the details of a library description including the name, version, icon reference, template info, and search connector description list.

**Code**: [[<?xml version="1.0" encoding="UTF-8"?>
<libraryDes]]

> The 'name' field provides the name of the library. The 'version' field provides the version number of the library. The 'isLibraryPinned' field indicates whether the library is pinned or not. The 'iconReference' field provides the icon reference of the library. The 'folderType' field provides the folder type of the library. The 'searchConnectorDescriptionList' field provides a list of search connectors. The 'isDefaultSaveLocation' field indicates whether the search connector is the default save location or not. The 'isSupported' field indicates whether the search connector is supported or not. The 'simpleLocation' field provides the URL of the search connector.

## Tags

- [[Active Directory Attacks]]
- [[SCF and URL file attack against writeable share]]
- [[Windows Library Files]]
