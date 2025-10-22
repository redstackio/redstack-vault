---
id: f1fd8252-2bf4-4232-98dc-523afd1b0012
name: Hidden Files and Directories
type: sub-technique
mitre_id: T1564.001
mitre_url: null
created_at: '2023-04-06T00:31:27.139354+00:00'
updated_at: '2023-04-06T00:31:27.139354+00:00'
parent_technique: '[[Hide Artifacts|T1564 - Hide Artifacts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Linux - Backdoor MOTD Persistence]]'
- '[[Linux - Startup Service Backdoor with Reverse Shell]]'
- '[[Linux - Text Hiding and Payload Creation]]'
- '[[Malicious HLS playlist inside an AVI video]]'
- '[[Windows - Mimikatz Hidden Persistence]]'
- '[[Windows - Simple User File Hidden Persistence]]'
---

# Hidden Files and Directories

**MITRE ID**: T1564.001

**Parent Technique**: [[Hide Artifacts|T1564 - Hide Artifacts]]

This is a sub-technique of T1564 - Hide Artifacts.

## Summary

Adversaries may set files and directories to be hidden to evade detection mechanisms. To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or 

## Description

Adversaries may set files and directories to be hidden to evade detection mechanisms. To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or when using normal commands on the command line. Users must explicitly ask to show the hidden files either via a series of Graphical User Interface (GUI) prompts or with command line switches (<code>dir /a</code> for Windows and <code>ls –a</code> for Linux and macOS).

On Linux and Mac, users can mark specific files as hidden simply by putting a “.” as the first character in the file or folder name  (Citation: Sofacy Komplex Trojan) (Citation: Antiquated Mac Malware). Files and folders that start with a period, ‘.’, are by default hidden from being viewed in the Finder application and standard command-line utilities like “ls”. Users must specifically change settings to have these files viewable.

Files on macOS can also be marked with the UF_HIDDEN flag which prevents them from being seen in Finder.app, but still allows them to be seen in Terminal.app (Citation: WireLurker). On Windows, users can mark specific files as hidden by using the attrib.exe binary. Many applications create these hidden files and folders to store information so that it doesn’t clutter up the user’s workspace. For example, SSH utilities create a .ssh folder that’s hidden and contains the user’s known hosts and keys.

Adversaries can use this to their advantage to hide files and folders anywhere on the system and evading a typical user or system analysis that does not incorporate investigation of hidden files.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 6 procedures using this sub-technique:

- [[Linux - Backdoor MOTD Persistence]]
- [[Linux - Startup Service Backdoor with Reverse Shell]]
- [[Linux - Text Hiding and Payload Creation]]
- [[Malicious HLS playlist inside an AVI video]]
- [[Windows - Mimikatz Hidden Persistence]]
- [[Windows - Simple User File Hidden Persistence]]
