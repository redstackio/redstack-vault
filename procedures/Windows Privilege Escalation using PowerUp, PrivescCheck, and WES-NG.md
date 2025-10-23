---
id: 9e0e771c-4e3d-429a-aa96-fcfc8863c902
name: Windows Privilege Escalation using PowerUp, PrivescCheck, and WES-NG
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.533774+00:00'
updated_at: '2023-04-10T20:37:50.950310+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
sub_techniques:
- '[[Windows Management Instrumentation Event Subscription|T1546.003 - Windows Management
  Instrumentation Event Subscription]]'
tags:
- '[[Tools]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[JAWS Enum]]'
- '[[Obtain systeminfo]]'
- '[[Run PrivescCheck.ps1 script]]'
- '[[Run PrivescCheck.ps1 script and generate report]]'
- '[[Run PrivescCheck.ps1 script with extended checks]]'
- '[[Scan for exploits using Windows Exploit Suggester tool]]'
- '[[Seatbelt group all full]]'
- '[[Seatbelt group remote]]'
- '[[Seatbelt group system output file]]'
- '[[Update WES]]'
- '[[Update Windows Exploit Suggester tool]]'
---

# Windows Privilege Escalation using PowerUp, PrivescCheck, and WES-NG

## Summary

Windows privilege escalation is a critical phase of an attacker's kill chain. It allows attackers to gain elevated privileges on a compromised system and move laterally across the network. PowerUp, PrivescCheck, and WES-NG are powerful tools that can help identify potential privilege escalation vul

## Description

# Description

Windows privilege escalation is a critical phase of an attacker's kill chain. It allows attackers to gain elevated privileges on a compromised system and move laterally across the network. PowerUp, PrivescCheck, and WES-NG are powerful tools that can help identify potential privilege escalation vulnerabilities on Windows systems. PowerUp is a PowerShell script that performs a variety of enumeration and privilege escalation tasks. PrivescCheck is a Python script that performs security checks on Windows systems to identify potential privilege escalation vulnerabilities. WES-NG is a tool that suggests exploits for Windows systems based on the output of system information gathering tools such as systeminfo and the Microsoft Baseline Security Analyzer. These tools can be used together to identify and exploit potential privilege escalation vulnerabilities on Windows systems.

 

## Requirements

1. Access to a Windows system

1. Authentication credentials with sufficient privileges to run the tools

1. PowerShell and Python installed on the system

 

## Defense

1. Regularly update and patch Windows systems to prevent known privilege escalation vulnerabilities

1. Monitor system logs and event subscriptions for suspicious activity related to privilege escalation

1. Implement the principle of least privilege to limit the impact of privilege escalation vulnerabilities

 

## Objectives

1. Identify potential privilege escalation vulnerabilities on Windows systems

1. Exploit identified vulnerabilities to gain elevated privileges on a compromised system

1. Move laterally across the network using the newly obtained elevated privileges

 

# Instructions

1. The PowerUp command is used to perform system enumeration and privilege escalation checks on a Windows machine. It uses PowerSploit's PowerUp module to identify misconfigurations and vulnerabilities that can be exploited by an attacker. The command executes a PowerShell script that downloads and runs the PowerUp module on the target machine.

 



**Code**: [[powershell -Version 2 -nop -exec bypass IEX (New-O]]



> The PowerUp command takes no arguments as it is designed to be run as is. The command downloads the PowerUp.ps1 script from the PowerShellEmpire/PowerTools repository on GitHub and uses the Invoke-AllChecks function to perform a series of checks on the system. These checks include identifying vulnerable services and registry keys, checking for weak file permissions, and searching for misconfigured scheduled tasks. The output of the command provides detailed information on any vulnerabilities or misconfigurations found on the system.

2. To use this tool, download the script from the provided link and run it in PowerShell. The script will scan the system for missing software patches that could lead to local privilege escalation vulnerabilities.

 



**Code**: [[powershell.exe -ExecutionPolicy Bypass -NoLogo -No]]



> The 'Sherlock' script is designed to quickly identify missing software patches on a system that could be exploited to escalate privileges locally. The script scans the system for known vulnerabilities and missing patches and provides detailed information about the vulnerabilities found. This tool is useful for system administrators and security professionals who need to quickly identify and remediate vulnerabilities on Windows systems.

3. To update Windows Exploit Suggester, run the command './windows-exploit-suggester.py --update'. To use the database, run the command './windows-exploit-suggester.py --database [database_file.xlsx] --systeminfo [system_info_file.txt]'.

 



**Code**: [[./windows-exploit-suggester.py --update
./windows-]]



> This command allows you to update the Windows Exploit Suggester tool and use the database to suggest potential exploits for a given system. The '--update' flag updates the tool to the latest version. The '--database' flag specifies the database file to use, and the '--systeminfo' flag specifies the system information file to use. The database file should be in .xlsx format and the system information file should be in .txt format. The tool then suggests potential exploits based on the system information provided.



**Command** ([[Update Windows Exploit Suggester tool]]):

```bash
./windows-exploit-suggester.py --update
```





**Command** ([[Scan for exploits using Windows Exploit Suggester tool]]):

```bash
./windows-exploit-suggester.py --database 2014-06-06-mssb.xlsx --systeminfo win7sp1-systeminfo.txt
```



4. To perform Seatbelt security checks, run the following commands:
1. To perform all security checks, run `Seatbelt.exe -group=all -full`
2. To perform system security checks and save the output to a file, run `Seatbelt.exe -group=system -outputfile="C:\Temp\system.txt"`
3. To perform remote security checks on a specific computer with specified credentials, run `Seatbelt.exe -group=remote -computername=COMPUTERNAME -username=USERNAME -password="PASSWORD"`

 



**Code**: [[Seatbelt.exe -group=all -full
Seatbelt.exe -group=]]



> The Seatbelt tool is a C# project that performs a number of security oriented host-survey "safety checks" relevant from both offensive and defensive security perspectives. The `Seatbelt.exe` command can be used to perform various security checks on a local or remote machine. The `-group` argument specifies the type of security checks to perform, and the `-full` argument specifies to perform all available checks. The `-outputfile` argument can be used to save the output of the security checks to a file. The `-computername`, `-username`, and `-password` arguments can be used to perform remote security checks on a specific computer with specified credentials.



**Command** ([[Seatbelt group all full]]):

```bash
Seatbelt.exe -group=all -full
```





**Command** ([[Seatbelt group system output file]]):

```bash
Seatbelt.exe -group=system -outputfile="C:\Temp\system.txt"
```





**Command** ([[Seatbelt group remote]]):

```bash
Seatbelt.exe -group=remote -computername=dc.theshire.local -computername=192.168.230.209 -username=THESHIRE\sam -password="yum \"po-ta-toes\""
```



5. This command executes the JAWS Enumeration Script which is used to gather information about a Windows system. The command will generate a text file named JAWS-Enum.txt containing the results of the enumeration.

 



**Code**: [[powershell.exe -ExecutionPolicy Bypass -File .\jaw]]



> -ExecutionPolicy Bypass: This parameter allows the script to run without any restrictions on the execution policy.
-File: This parameter specifies the file to be executed.
-OutputFilename: This parameter specifies the name of the output file.
JAWS-Enum.txt: This is the name of the output file that will contain the results of the enumeration.



**Command** ([[JAWS Enum]]):

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt
```



6. To use this tool, first obtain systeminfo by running the command 'systeminfo' and saving the output to a file named 'systeminfo.txt'. Then, run the following commands:
- python3 wes.py --update-wes
- python3 wes.py --update
- python3 wes.py systeminfo.txt
These commands will update the tool and feed it with the obtained systeminfo to suggest possible exploits.

 



**Code**: [[# First obtain systeminfo
systeminfo
systeminfo > ]]



> The Windows Exploit Suggester - Next Generation (WES-NG) is a tool used to suggest possible exploits for a given system based on the output of the 'systeminfo' command. The tool requires Python 3 and can be updated by running the command 'python3 wes.py --update-wes'. After updating, the tool can be run with the obtained systeminfo by running the command 'python3 wes.py systeminfo.txt'. The tool will then suggest possible exploits based on the system information provided.



**Command** ([[Obtain systeminfo]]):

```bash
systeminfo
systeminfo > systeminfo.txt
```





**Command** ([[Update WES]]):

```bash
python3 wes.py --update-wes
python3 wes.py --update
python3 wes.py systeminfo.txt
```



7. To use the PrivescCheck command, run PowerShell with the -ep bypass flag and execute the PrivescCheck.ps1 script. The following are examples of how to use the command:
1. Invoke-PrivescCheck: This command will perform a basic privilege escalation check.
2. Invoke-PrivescCheck -Extended: This command will perform an extended privilege escalation check.
3. Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML: This command will perform an extended privilege escalation check and generate a report in TXT, CSV, and HTML formats.

 



**Code**: [[C:\Temp\>powershell -ep bypass -c ". .\PrivescChec]]



> The PrivescCheck command is used to perform a privilege escalation check on a Windows system. The command requires PowerShell to be run with the -ep bypass flag and the PrivescCheck.ps1 script to be executed. The command has three options:
1. Invoke-PrivescCheck: This command will perform a basic privilege escalation check.
2. Invoke-PrivescCheck -Extended: This command will perform an extended privilege escalation check.
3. Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML: This command will perform an extended privilege escalation check and generate a report in TXT, CSV, and HTML formats. The report will be named PrivescCheck_COMPUTERNAME, where COMPUTERNAME is the name of the computer where the command was executed.



**Command** ([[Run PrivescCheck.ps1 script]]):

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```





**Command** ([[Run PrivescCheck.ps1 script with extended checks]]):

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
```





**Command** ([[Run PrivescCheck.ps1 script and generate report]]):

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

### Sub-Techniques

- [[Windows Management Instrumentation Event Subscription|T1546.003 - Windows Management Instrumentation Event Subscription]]

## Commands Used

- [[JAWS Enum]]
- [[Obtain systeminfo]]
- [[Run PrivescCheck.ps1 script]]
- [[Run PrivescCheck.ps1 script and generate report]]
- [[Run PrivescCheck.ps1 script with extended checks]]
- [[Scan for exploits using Windows Exploit Suggester tool]]
- [[Seatbelt group all full]]
- [[Seatbelt group remote]]
- [[Seatbelt group system output file]]
- [[Update WES]]
- [[Update Windows Exploit Suggester tool]]

## Tags

- [[Tools]]
- [[Windows - Privilege Escalation]]


