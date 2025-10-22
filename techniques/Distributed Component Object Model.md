---
id: 00351b73-bbb1-4dac-b2fa-ceb77a84897b
name: Distributed Component Object Model
type: technique
mitre_id: T1175
mitre_url: null
created_at: '2019-08-28T21:17:33.088520+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Execute .NET Remote Execution with Beacon Post-Exploitation Job]]'
- '[[Local DTD Injection in Citrix XenMobile Server]]'
---

# Distributed Component Object Model

**MITRE ID**: T1175

## Description

Windows Distributed Component Object Model (DCOM) is transparent middleware that extends the functionality of Component Object Model (COM) [1] beyond a local computer using remote procedure call (RPC) technology. COM is a component of the Windows application programming interface (API) that enables interaction between software objects. Through COM, a client object can call methods of server objects, which are typically Dynamic Link Libraries (DLL) or executables (EXE).Permissions to interact with local and remote server COM objects are specified by access control lists (ACL) in the Registry. [2] [3] [4] By default, only Administrators may remotely activate and launch COM objects through DCOM.Adversaries may use DCOM for lateral movement. Through DCOM, adversaries operating in the context of an appropriately privileged user can remotely obtain arbitrary and even direct shellcode execution through Office applications [5] as well as other Windows objects that contain insecure methods. [6] [7] DCOM can also execute macros in existing documents [8] and may also invoke Dynamic Data Exchange (DDE) execution directly through a COM created instance of a Microsoft Office application [9], bypassing the need for a malicious document.DCOM may also expose functionalities that can be leveraged during other areas of the adversary chain of activity such as Privilege Escalation and Persistence. [10]

# Detection

Monitor for COM objects loading DLLs and other modules not typically associated with the application. [5]

Monitor for spawning of processes associated with COM objects, especially those invoked by a user different than the one currently logged on.

Monitor for influx of Distributed Computing Environment/Remote Procedure Call (DCE/RPC) traffic.

# Mitigation

Modify Registry settings (directly or using Dcomcnfg.exe) in HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID{AppID_GUID} associated with the process-wide security of individual COM applications. [3]

Modify Registry settings (directly or using Dcomcnfg.exe) in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole associated with system-wide security defaults for all COM applications that do no set their own process-wide security. [4] [2]

Consider disabling DCOM through Dcomcnfg.exe. [15]

Enable Windows firewall, which prevents DCOM instantiation by default.

Ensure all COM alerts and Protected View are enabled. [16]

# Footnotes

[1] Microsoft. (n.d.). Component Object Model (COM). Retrieved November 22, 2017.

[2] Microsoft. (n.d.). DCOM Security Enhancements in Windows XP Service Pack 2 and Windows Server 2003 Service Pack 1. Retrieved November 22, 2017.

[3] Microsoft. (n.d.). Setting Process-Wide Security Through the Registry. Retrieved November 21, 2017.

[4] Microsoft. (n.d.). Registry Values for System-Wide Security. Retrieved November 21, 2017.

[5] Nelson, M. (2017, November 16). Lateral Movement using Outlook's CreateObject Method and DotNetToJScript. Retrieved November 21, 2017.

[6] Nelson, M. (2017, January 5). Lateral Movement using the MMC20 Application COM Object. Retrieved November 21, 2017.

[7] Nelson, M. (2017, January 23). Lateral Movement via DCOM: Round 2. Retrieved November 21, 2017.

[8] Nelson, M. (2017, September 11). Lateral Movement using Excel.Application and DCOM. Retrieved November 21, 2017.

[9] Tsukerman, P. (2017, November 8). Leveraging Excel DDE for lateral movement via DCOM. Retrieved November 21, 2017.

[10] Forshaw, J. (2018, April 18). Windows Exploitation Tricks: Exploiting Arbitrary File Writes for Local Elevation of Privilege. Retrieved May 3, 2018.

[11] Mudge, R. (2017, January 24). Scripting Matt Nelson’s MMC20.Application Lateral Movement Technique. Retrieved November 21, 2017.

[12] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[13] Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.

[14] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[15] Microsoft. (n.d.). Enable or Disable DCOM. Retrieved November 22, 2017.

[16] Microsoft. (n.d.). What is Protected View?. Retrieved November 22, 2017.

## Defense

Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{AppID_GUID}</code> associated with the process-wide security of individual COM applications. (Citation: Microsoft Process Wide Com Keys)

Modify 

## Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (2)

- [[Execute .NET Remote Execution with Beacon Post-Exploitation Job]]
- [[Local DTD Injection in Citrix XenMobile Server]]
