---
id: 204776d5-293a-4009-8740-bbd076099788
name: Windows Local Service Permissions Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.450155+00:00'
updated_at: '2023-04-10T20:37:36.965006+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
- '[[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]'
tags:
- '[[EoP - Incorrect permissions in services]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Check Permissions]]'
- '[[Compile malicious dll]]'
- '[[Content of windows_dll.c]]'
- '[[Displaying ACLs for a file or directory]]'
- '[[Find missing DLL using Find-PathDLLHijack PowerUp.ps1 and Process Monitor]]'
- '[[Granting a user permission to a file or directory]]'
- '[[Revoking a user''s permission to a file or directory]]'
---

# Windows Local Service Permissions Escalation

## Summary

Windows Local Service Permissions Escalation is a technique used by attackers to elevate their privileges on a Windows machine by exploiting incorrect permissions in services. By exploiting the permissions of a local service, an attacker can gain elevated privileges and execute malicious code. This

## Description

# Description

Windows Local Service Permissions Escalation is a technique used by attackers to elevate their privileges on a Windows machine by exploiting incorrect permissions in services. By exploiting the permissions of a local service, an attacker can gain elevated privileges and execute malicious code. This is typically done by hijacking a DLL that is loaded by a vulnerable service. This technique is commonly used in post-exploitation scenarios where an attacker has already gained access to a machine and is looking to escalate their privileges to gain access to additional resources.

To execute this technique, an attacker must first identify vulnerable services and then exploit the incorrect permissions to gain elevated privileges. This can be done using a variety of tools and techniques including DLL hijacking, weak permission paths, and modifying service permissions using tools like ICAcls.

The business value of this technique is that it allows attackers to gain access to sensitive data and resources that are otherwise protected. By elevating their privileges, attackers can bypass security controls and gain access to critical systems and data.

 

## Requirements

1. Access to a vulnerable Windows machine

1. Authentication credentials with sufficient privileges

1. Tools and techniques for exploiting incorrect permissions in services

 

## Defense

1. Regularly review and update service permissions to ensure that they are configured correctly

1. Use tools like ICAcls to manage service permissions and ensure that they are set correctly

1. Monitor for suspicious activity and behavior on Windows machines, including changes to service permissions

 

## Objectives

1. Gain elevated privileges on a Windows machine

1. Execute malicious code with elevated privileges

1. Access sensitive data and resources

 

# Instructions

1. To perform the DLL Hijacking attack, follow the instructions below:
1. Find a missing DLL using the 'Find-PathDLLHijack PowerUp.ps1' command.
2. Use Process Monitor to check for 'Name Not Found'.
3. Compile a malicious DLL using the given commands for x64 or x86.
4. In the content of windows_dll.c, insert the code you want to execute on the target system.
5. Place the compiled DLL in a location where it will be loaded by the target application.
6. Wait for the target application to execute the malicious code.

 



**Code**: [[# find missing DLL 
- Find-PathDLLHijack PowerUp.p]]



> This command is used to perform a DLL Hijacking attack. It involves finding a missing DLL in a target system and replacing it with a malicious DLL. When the target application loads the malicious DLL, the code inside it is executed, allowing the attacker to perform various actions on the target system. The instructions provided above explain the steps to be followed to successfully perform this attack.



**Command** ([[Find missing DLL using Find-PathDLLHijack PowerUp.ps1 and Process Monitor]]):

```bash
# find missing DLL 
- Find-PathDLLHijack PowerUp.ps1
- Process Monitor : check for "Name Not Found"
```





**Command** ([[Compile malicious dll]]):

```bash
# compile a malicious dll
- For x64 compile with: "x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll"
- For x86 compile with: "i686-w64-mingw32-gcc windows_dll.c -shared -o output.dll"
```





**Command** ([[Content of windows_dll.c]]):

```bash
#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Windows\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```



2. This command will identify the directories with weak permissions for the PATH directories. The command will create a temporary file 'permissions.txt' and write the output of the command to it. Then it will execute another command to list the permissions of the directories. It will also create a temporary file 'Servicenames.txt' and write the output of the command to it. It will then execute a few commands to extract the service names and their binary path names and write the output to a file called 'path.txt'.

 



**Code**: [[$ for /f "tokens=2 delims='='" %a in ('wmic servic]]



> This command is useful for identifying the directories with weak permissions in the PATH directories. These directories can be exploited by attackers to execute malicious code on the system. By identifying these directories, system administrators can take necessary actions to secure the system.

3. This exploit allows an attacker to elevate their privileges on a Windows system by exploiting weak service permissions. The attacker can manipulate the service permissions to gain SYSTEM level access and perform various malicious activities.

 



**Code**: [[exploit/windows/local/service_permissions]]



> The exploit targets a specific service on the Windows system and abuses the weak permissions set on the service. The attacker needs to have a user account on the system with limited privileges to execute this exploit. The user account must have the ability to modify the service permissions. Once the exploit is successful, the attacker gains SYSTEM level access and can perform any activity on the compromised system.

4. To check file permissions using cacls, use the following syntax:

cacls <file_path>

 



**Code**: [[cacls]]



> The cacls command is used to display or modify access control lists (ACLs) for files and directories. When used without any arguments, it displays the ACLs for the current directory. By specifying a file path as an argument, you can view the ACLs for a specific file or directory. The output of the command will show the permissions for the file or directory, including which users or groups have access to it and what level of access they have.



**Command** ([[Displaying ACLs for a file or directory]]):

```bash
cacls C:\example\file.txt
```





**Command** ([[Granting a user permission to a file or directory]]):

```bash
cacls C:\example\file.txt /E /G username:F
```





**Command** ([[Revoking a user's permission to a file or directory]]):

```bash
cacls C:\example\file.txt /E /R username
```



5. icacls [path] [/grant[:r] User:Permission] [/deny User:Permission] [/remove[:g|:d]] User [Permission] [/t] [/c] [/l] [/q] [/setintegritylevel [(CI)(OI)]Level] [/save FileName [/t]] [/restore FileName] [/findsid Sid] [/findsidfrom Sid [/restore]] [/verify] [/reset] [/help] [<FileList>]

 



**Code**: [[icacls]]



> The Icacls command is used to display, modify, backup, or restore discretionary access control lists (DACLs) on specified files and directories in Windows. The command can be used to grant or deny permissions to files and directories, remove permissions from users or groups, and set or modify the integrity level of files and directories. The command can also be used to save and restore permissions to a file, find a security identifier (SID) for a user or group, and verify the integrity of security descriptors.



**Command** ([[Check Permissions]]):

```bash
icacls C:\Program Files\
```



6. To view the permissions granted to the Users group, run the following command in Command Prompt or PowerShell: 

icacls <file_path>

 



**Code**: [[BUILTIN\Users:(F)]]



> This command displays the permissions granted to the built-in Users group for a specified file or folder. The output will show the Users group followed by the permissions granted to it, such as (F) for full control, (R) for read-only, and so on.

7. Use the 'icacls' command to view or modify permissions on Windows files and folders

 



**Code**: [[BUILTIN\Users:(M)]]



> This command displays the permissions assigned to the BUILTIN\Users group for the specified file or folder. The '(M)' indicates that the group has 'Modify' permissions, which allows them to create, modify, and delete files and folders within that location.

8. To modify access for BUILTIN\Users, use the following command:

icacls <file_path> /grant BUILTIN\Users:(permissions)

Replace <file_path> with the path to the file or directory you want to modify access for, and replace (permissions) with the specific permissions you want to grant to BUILTIN\Users. For example, to grant full control, use (F), to grant read and execute, use (RX), etc.

 



**Code**: [[BUILTIN\Users:(W)]]



> This command is used to modify the access permissions for a file or directory for the BUILTIN\Users group. By default, the BUILTIN\Users group has read and execute permissions, but using this command, you can grant or revoke additional permissions as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Modify Existing Service|T1031 - Modify Existing Service]]
- [[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]

## Commands Used

- [[Check Permissions]]
- [[Compile malicious dll]]
- [[Content of windows_dll.c]]
- [[Displaying ACLs for a file or directory]]
- [[Find missing DLL using Find-PathDLLHijack PowerUp.ps1 and Process Monitor]]
- [[Granting a user permission to a file or directory]]
- [[Revoking a user's permission to a file or directory]]

## Tags

- [[EoP - Incorrect permissions in services]]
- [[Windows - Privilege Escalation]]


