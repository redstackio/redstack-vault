---
id: aee0b0b2-8411-4b4e-ad04-563e0cb510df
name: Remote access to Windows Machine (credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T07:48:43.933593+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
platforms:
- Windows
tags:
- '[[Powershell Remote]]'
- '[[WinRS]]'
commands:
- '[[Powershell remoting to machine]]'
- '[[Powershell remoting to machine with user credentials]]'
- '[[winrs remote CMD on target machine]]'
- '[[winrs remote to machine using credentials]]'
---

# Remote access to Windows Machine (credentials)

## Summary

Open a CMD prompt or powershell session on a remote target machine 

## Description

# Description

Open a CMD prompt or powershell session on a remote target machine



## Objective

1. Connect to a remote machine and obtain a CMD or PS prompt



## Instructions

1. Connect to a remote machine using WInRS and open CMD prompt on the target machine



**Command** ([[winrs remote CMD on target machine]]):

```bash
winrs -r:$COMPUTER_NAME cmd
```



(Alternative) Connect to the remote machine using winrs with a specific user credentials





**Command** ([[winrs remote to machine using credentials]]):

```bash
winrs -r:$SYSTEM -u:.\$USERNAME -p:$PASSWORD cmd
```







2. (Alternative) use Powershell remote to connect to a machine



**Command** ([[Powershell remoting to machine]]):

```bash
$SESSION = New-PSSession $COMPUTER_NAME
Enter-PSSession $SESSION
```



(Optional) Specify user credentials for PS Remote





**Command** ([[Powershell remoting to machine with user credentials]]):

```bash
$pass = ConvertTo-SecureString $PASSWORD -AsPlainText -Force;
$cred= New-Object System.Management.Automation.PSCredential ($USERNAME, $password );
New-PSSession -computername $SYSTEM -credential $cred
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Windows Remote Management|T1028 - Windows Remote Management]]

## Commands Used

- [[Powershell remoting to machine]]
- [[Powershell remoting to machine with user credentials]]
- [[winrs remote CMD on target machine]]
- [[winrs remote to machine using credentials]]

## Tags

- [[Powershell Remote]]
- [[WinRS]]


