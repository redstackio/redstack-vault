---
id: fcbde5b5-bba8-4894-955b-a9c0c067418a
name: VBA Shell Execute Comment
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.500717+00:00'
updated_at: '2023-04-10T20:36:48.917786+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[User Execution|T1204 - User Execution]]'
sub_techniques:
- '[[Malicious File|T1204.002 - Malicious File]]'
tags:
- '[[DOCM - VBA Shell Execute Comment]]'
- '[[Office - Attacks]]'
---

# VBA Shell Execute Comment

## Summary

The VBA Shell Execute Comment procedure is a technique that leverages malicious macros in Office documents to execute shell commands from comment metadata. This procedure can be used to execute arbitrary code on a victim's machine, allowing an attacker to gain access to sensitive information or to 

## Description

# Description

The VBA Shell Execute Comment procedure is a technique that leverages malicious macros in Office documents to execute shell commands from comment metadata. This procedure can be used to execute arbitrary code on a victim's machine, allowing an attacker to gain access to sensitive information or to establish a foothold for further attacks. The technique is commonly used in phishing attacks and can be difficult to detect as it does not require any user interaction.

 

## Requirements

1. Access to a victim's machine

1. Office document with malicious macro

1. VBA scripting knowledge

 

## Defense

1. Disable macros in Office documents

1. Implement network segmentation and access controls to limit lateral movement

1. Use endpoint protection software to detect and block malicious activity

 

## Objectives

1. Execute arbitrary code on a victim's machine

1. Gain access to sensitive information

1. Establish a foothold for further attacks

 

# Instructions

1. This script allows you to execute a shell command by setting the command payload inside the 'Comment' metadata of the document. To use this script, open the VBA editor in Microsoft Word and paste the code. Save the file as a macro-enabled document and add your shell command to the 'Comment' metadata of the document.

 



**Code**: [[Sub beautifulcomment()
    Dim p As DocumentProper]]



> The 'beautifulcomment' subroutine reads the 'Comment' metadata of the document and executes the shell command if it exists. The 'AutoExec' and 'AutoOpen' subroutines ensure that the 'beautifulcomment' subroutine is executed when the document is opened or when the macro is run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[User Execution|T1204 - User Execution]]

### Sub-Techniques

- [[Malicious File|T1204.002 - Malicious File]]

## Tags

- [[DOCM - VBA Shell Execute Comment]]
- [[Office - Attacks]]


