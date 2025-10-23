---
id: af9d0e0e-38db-4c1e-9cac-82200025e31a
name: Windows - Impacket Psexec Remote Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.795602+00:00'
updated_at: '2023-04-10T20:38:06.576192+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Binary Padding|T1027.001 - Binary Padding]]'
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Impacket]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Download File]]'
- '[[Execute remote command]]'
- '[[Set codec to ibm850]]'
- '[[Upload File]]'
- '[[lput -v -i input.txt -o output.txt]]'
---

# Windows - Impacket Psexec Remote Command Execution

## Summary

Impacket's Psexec tool is a command-line tool that allows for the execution of commands on a remote Windows system, using the credentials of a specified user. This tool can be used offensively to gain remote access to a system and execute commands, such as the ones listed in the commands field. Pse

## Description

# Description

Impacket's Psexec tool is a command-line tool that allows for the execution of commands on a remote Windows system, using the credentials of a specified user. This tool can be used offensively to gain remote access to a system and execute commands, such as the ones listed in the commands field. Psexec uses the SMB protocol to establish a connection to the remote system and execute the command. The tool can also be used defensively for system administration tasks, such as installing software on remote systems. The business value of this tool is that it allows for efficient remote administration of Windows systems.

 

## Requirements

1. Valid credentials for a user account on the remote Windows system

1. Network access to the remote Windows system

 

## Defense

1. Ensure that user accounts have strong passwords and are not shared between users

1. Use network segmentation to limit access to critical systems and services

1. Monitor for suspicious network activity, such as connections to remote systems using Psexec

 

## Objectives

1. Execute commands on a remote Windows system using the credentials of a specified user

1. Gain remote access to a Windows system

 

# Instructions

1. To get the warning message, use the following command:

 



**Code**: [[get]]



> This command will return a warning message in the form of an emoji. The warning message can be used to indicate potential issues or problems with a specific task or action.

2. To add data to a resource, use the PUT method.

 



**Code**: [[put]]



> The PUT method replaces all current representations of the target resource with the request payload. The payload can be in any format supported by the server, such as JSON or XML. The URI of the target resource must be included in the request. If the resource does not exist, the server can create it. If the resource does exist, the server can update it with the new representation.



**Command** ([[Upload File]]):

```bash
put example.txt /var/www/html/
```



3. Use the new command names when executing the respective commands.

 



**Code**: [[lget]]



> The lget command is used for retrieving files from a remote system. Previously, this command was executed using different commands depending on the method of remote execution. However, these command names have now been changed to standardize the naming convention. Users should now use the following commands for remote file retrieval: 
- wmiexec: lget
- psexec: wget
- smbexec: get
- dcomexec: lget



**Command** ([[Download File]]):

```bash
lget https://example.com/file.txt -o output.txt
```



4. LPut is a command used to put a value at a specified index of a list in Redis database. The command takes three arguments: the name of the list, the index at which the value is to be inserted, and the value to be inserted.

 



**Code**: [[lput]]



> The first argument to the LPut command is the name of the list in Redis database. The second argument is the index at which the value is to be inserted. If the index is out of range, the command will return an error. The third argument is the value to be inserted at the specified index. If the list does not exist, the command will create a new list and insert the value at the specified index. If the index is negative, the value will be inserted from the end of the list. If the index is greater than the length of the list, the value will be inserted at the end of the list.



**Command** ([[lput -v -i input.txt -o output.txt]]):

```bash
lput -v -i input.txt -o output.txt
```



5. The -codec ibm850 command is used to specify the encoding format for the text. In this case, it is set to IBM850 encoding.

 



**Code**: [[-codec ibm850]]



> IBM850 encoding is a character encoding used for the Latin alphabet. It is commonly used in Western European countries and supports French characters. However, it may not display these characters correctly on all output devices. If you encounter issues with French characters not being displayed correctly, you can try using a different encoding format.



**Command** ([[Set codec to ibm850]]):

```bash
-codec ibm850
```



6. To execute a command on a remote system using Psexec, run the following command:

psexec.py <target_address> <username> <password> <command>

 



**Code**: [[impacket/examples/psexec.py]]



> This command uses the Psexec script from Impacket to remotely execute a command on a Windows system. Replace <target_address> with the IP address or hostname of the target system, <username> and <password> with valid credentials for the target system, and <command> with the command you wish to execute. Note that the command must be enclosed in quotes if it contains spaces or special characters. Example: psexec.py 192.168.1.100 Administrator Password123 "ipconfig /all"



**Command** ([[Execute remote command]]):

```bash
python3 ./psexec.py domain/user:password@remote-hostname 'cmd.exe /c whoami'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Binary Padding|T1027.001 - Binary Padding]]
- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Download File]]
- [[Execute remote command]]
- [[Set codec to ibm850]]
- [[Upload File]]
- [[lput -v -i input.txt -o output.txt]]

## Tags

- [[Impacket]]
- [[Windows - Using credentials]]


