---
id: c543cd82-3434-4376-a354-ef65467f5e6d
name: Windows Simple User Startup Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.815561+00:00'
updated_at: '2023-04-10T20:37:27.159078+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
sub_techniques:
- '[[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]'
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[Simple User]]'
- '[[Startup]]'
- '[[Windows - Persistence]]'
commands:
- '[[Run backdoor.bat on Startup]]'
---

# Windows Simple User Startup Persistence

## Summary

Windows Simple User Startup Persistence is a technique used by attackers to maintain their foothold on the compromised system. By placing a backdoor batch script in the Startup folder, the attacker can ensure that the script will run every time the user logs in, providing them with persistent acces

## Description

# Description

Windows Simple User Startup Persistence is a technique used by attackers to maintain their foothold on the compromised system. By placing a backdoor batch script in the Startup folder, the attacker can ensure that the script will run every time the user logs in, providing them with persistent access to the system. This technique is particularly effective for attackers who have gained access to a system with low privileges, such as a simple user account.

From a technical perspective, this technique involves creating a batch script that contains a command or series of commands that the attacker wants to run. The script is then placed in the Startup folder, which is a location on the file system that contains a list of programs that are automatically started when the user logs in. When the user logs in, the script is executed, and the attacker's commands are run. This provides the attacker with a persistent backdoor into the system.

From a business perspective, this technique can be used by attackers to maintain access to a compromised system, allowing them to steal data, install additional malware, or use the compromised system as a jumping-off point for further attacks.

 

## Requirements

1. Access to the target system

1. Ability to create a backdoor batch script

1. Ability to add the script to the Startup folder

 

## Defense

1. Regularly monitor the Startup folder for any unauthorized scripts or programs

1. Restrict write access to the Startup folder to prevent unauthorized modifications

1. Implement a least privilege model to limit the impact of a compromised simple user account

 

## Objectives

1. Maintain persistent access to a compromised system

1. Execute commands on the compromised system every time the user logs in

 

# Instructions

1. To create a backdoor batch script in the user startup folder, follow the steps below:
1. Open PowerShell.
2. Run the following command: gc C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\backdoor.bat
3. Replace <username> with the username of the target user.
4. Enter the code for the batch script.
5. Save the file.
6. Run the following command: start /b C:\Users\<username>\AppData\Local\Temp\backdoor.exe
7. Replace <username> with the username of the target user.

 



**Code**: [[PS C:\> gc C:\Users\Rasta\AppData\Roaming\Microsof]]



> This command creates a batch script in the user startup folder. The batch script will run every time the user logs in, allowing an attacker to maintain persistent access to the system. The code for the batch script can be customized to execute any desired actions, such as downloading and executing malware or creating a reverse shell. The 'gc' command is used to get the content of the file, and 'start' is used to run the backdoor executable in the background.



**Command** ([[Run backdoor.bat on Startup]]):

```bash
start /b C:\Users\Rasta\AppData\Local\Temp\backdoor.exe
```



2. To add a command to the Windows Startup Folder using SharPersist, follow these steps:
1. Open the command prompt as an administrator.
2. Navigate to the directory where SharPersist is located.
3. Enter the following command: SharPersist -t startupfolder -c "C:\Windows\System32\cmd.exe" -a "/c [Your Command Here]" -f "Some File" -m add
   - Replace [Your Command Here] with the command you want to add to the Startup Folder.
   - Replace "Some File" with a name for the file that will be created in the Startup Folder.
4. Press Enter to execute the command.

 



**Code**: [[SharPersist -t startupfolder -c "C:\Windows\System]]



> -t: Specifies the type of persistence to use. In this case, we are using the startup folder.
-c: Specifies the command to be executed.
-a: Specifies the arguments for the command.
-f: Specifies the name of the file to be created in the startup folder.
-m: Specifies the mode of operation. In this case, we are adding a command to the startup folder.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]
- [[Create or Modify System Process|T1543 - Create or Modify System Process]]

### Sub-Techniques

- [[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]
- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[Run backdoor.bat on Startup]]

## Tags

- [[Simple User]]
- [[Startup]]
- [[Windows - Persistence]]


