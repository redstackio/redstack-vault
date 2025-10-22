---
id: 7e0bacca-d603-47e7-a564-fb87b2413d9c
name: Windows Privilege Escalation - Processes and Tasks Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.391613+00:00'
updated_at: '2023-04-10T20:37:39.679955+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Process Injection|T1055 - Process Injection]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[EoP - Processes Enumeration and Tasks]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Check PowerShell version]]'
- '[[List of Programs to Run Once at Startup]]'
- '[[List of Startup Programs]]'
- '[[List of Startup Programs in All Users Start Menu]]'
- '[[List of Startup Programs in Current User Start Menu]]'
- '[[List of Startup Programs in Registry (HKCU)]]'
- '[[List of Startup Programs in Registry (HKLM)]]'
---

# Windows Privilege Escalation - Processes and Tasks Enumeration

## Summary

This procedure involves enumerating running processes and tasks on a Windows system to identify potential vulnerabilities that can be exploited for privilege escalation. By identifying processes running as SYSTEM, this procedure can help an attacker find a process that can be abused to escalate pri

## Description

# Description

This procedure involves enumerating running processes and tasks on a Windows system to identify potential vulnerabilities that can be exploited for privilege escalation. By identifying processes running as SYSTEM, this procedure can help an attacker find a process that can be abused to escalate privileges. The attacker can then use a variety of techniques, such as process injection, scheduled tasks/jobs, or service execution, to achieve their objectives. This procedure can help an attacker move from a low-privileged account to a higher-privileged account, giving them access to sensitive data and resources.

## Requirements

1. Access to a Windows system

1. User with low-privileges

## Defense

1. Ensure that all users have the least privilege necessary to perform their job functions

1. Monitor system logs for any suspicious activity related to process injection, scheduled tasks/jobs, or service execution

1. Regularly update and patch software to prevent known vulnerabilities from being exploited

## Objectives

1. Identify processes running as SYSTEM

1. Find potential vulnerabilities that can be exploited for privilege escalation

1. Escalate privileges to gain access to sensitive data and resources

# Instructions

1. This command will list all the running processes on the system along with their process id and the user who is running the process.

**Code**: [[tasklist /v
net start
sc query
Get-Service
Get-Pro]]

> The command uses various PowerShell cmdlets to list all the running processes on the system. The 'Get-Process' cmdlet lists all the running processes on the system. The 'Get-WmiObject' cmdlet is used to get the process owner information. The 'where' clause is used to filter out the 'svchost' processes. Finally, the 'Select' cmdlet is used to display the process name, process id, and the process owner information in a table format.

2. This command will list all the processes currently running on the system that are being executed under the 'system' user account.

**Code**: [[tasklist /v /fi "username eq system"]]

> The 'tasklist' command is used to display a list of all the running processes on a system. '/v' switch is used to display the verbose information about the processes. '/fi' switch is used to filter the output of the command based on a specific criteria. In this case, we are filtering the output to show only the processes that are running under the 'system' user account.

3. To check the version of PowerShell installed on your system, run the following command in PowerShell prompt:

**Code**: [[REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\Po]]

> This command queries the registry key for PowerShell version information. The output will show the version number of the installed PowerShell on your system.

**Command** ([[Check PowerShell version]]):

```powershell
REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion
```

4. This command will list all the installed programs on your system. The first part of the command will list the programs installed in the 'C:\Program Files' and 'C:\Program Files (x86)' directories. The second part of the command will list the programs installed in the 'HKEY_LOCAL_MACHINE\SOFTWARE' registry key. The output will include the parent directory, name, and last write time of the programs installed in the directories and only the name of the programs installed in the registry key.

**Code**: [[Get-ChildItem 'C:\Program Files', 'C:\Program File]]

> The 'Get-ChildItem' command is used to retrieve the items in the specified directory or registry key. The 'ft' command is used to format the output in a table view. The 'Parent' parameter is used to display the parent directory of the item. The 'Name' parameter is used to display the name of the item. The 'LastWriteTime' parameter is used to display the date and time the item was last written to.

5. To list all the services running on your system, run the following commands:

**Code**: [[net start
wmic service list brief
tasklist /SVC]]

> This command will list all the services running on your system along with their status and other details. The 'net start' command will list all the services that are currently running, while the 'wmic service list brief' command will list all the services along with their status and other details. The 'tasklist /SVC' command will list all the running processes along with the services that they are associated with.

6. This command will list all scheduled tasks on the system, along with their paths and current state.

**Code**: [[schtasks /query /fo LIST 2>nul | findstr TaskName
]]

> The 'schtasks' command is used to query and manage scheduled tasks on Windows systems. The first part of the command, 'schtasks /query /fo LIST 2>nul | findstr TaskName', will list all task names on the system. The second part of the command, 'schtasks /query /fo LIST /v > schtasks.txt; cat schtask.txt | grep "SYSTEM\|Task To Run" | grep -B 1 SYSTEM', will output all scheduled tasks and their properties to a file called 'schtasks.txt', and then filter the results to only show tasks that are set to run under the SYSTEM account. Finally, the 'Get-ScheduledTask' cmdlet is used to retrieve a list of all scheduled tasks on the system that are not part of the Microsoft namespace, and the 'ft' (format-table) cmdlet is used to display the task name, task path, and current state in a table format.

7. This command will list all the tasks that run at startup on your system.

**Code**: [[wmic startup get caption,command
reg query HKLM\So]]

> This command uses multiple commands to list all the tasks that run at startup on your system. The 'wmic startup get caption,command' command lists all the startup programs using Windows Management Instrumentation (WMI). The 'reg query' commands list the startup programs listed in the Windows Registry. Finally, the 'dir' commands list the startup programs that are located in the 'Start Menu\Programs\Startup' folder for all users and the current user. These commands can help you identify any unwanted programs that are set to run at startup and can be disabled to improve system performance.

**Command** ([[List of Startup Programs]]):

```bash
wmic startup get caption,command
```

**Command** ([[List of Startup Programs in Registry (HKLM)]]):

```bash
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\R
```

**Command** ([[List of Startup Programs in Registry (HKCU)]]):

```bash
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

**Command** ([[List of Programs to Run Once at Startup]]):

```bash
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```

**Command** ([[List of Startup Programs in All Users Start Menu]]):

```bash
dir "C:\\Documents and Settings\\All Users\\Start Menu\\Programs\\Startup"
```

**Command** ([[List of Startup Programs in Current User Start Menu]]):

```bash
dir "C:\\Documents and Settings\\%username%\\Start Menu\\Programs\\Startup"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Process Injection|T1055 - Process Injection]]
- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[Check PowerShell version]]
- [[List of Programs to Run Once at Startup]]
- [[List of Startup Programs]]
- [[List of Startup Programs in All Users Start Menu]]
- [[List of Startup Programs in Current User Start Menu]]
- [[List of Startup Programs in Registry (HKCU)]]
- [[List of Startup Programs in Registry (HKLM)]]

## Tags

- [[EoP - Processes Enumeration and Tasks]]
- [[Windows - Privilege Escalation]]
