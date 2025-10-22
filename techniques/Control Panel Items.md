---
id: 1a264385-8291-4b31-a747-cd041f184846
name: Control Panel Items
type: technique
mitre_id: T1196
mitre_url: null
created_at: '2019-08-28T21:17:20.958351+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[CSRF Payload to Set Role to Admin via JSON POST]]'
- '[[CSRF Payload to Set Role to Admin via JSON POST]]'
- '[[Subdomain CSRF Attack]]'
- '[[Subdomain CSRF Attack]]'
---

# Control Panel Items

**MITRE ID**: T1196

## Description

Windows Control Panel items are utilities that allow users to view and adjust computer settings. Control Panel items are registered executable (.exe) or Control Panel (.cpl) files, the latter are actually renamed dynamic-link library (.dll) files that export a CPlApplet function. [1] [2] Control Panel items can be executed directly from the command line, programmatically via an application programming interface (API) call, or by simply double-clicking the file. [1] [2] [3]For ease of use, Control Panel items typically include graphical menus available to users after being registered and loaded into the Control Panel. [1]Adversaries can use Control Panel items as execution payloads to execute arbitrary commands. Malicious Control Panel items can be delivered via Spearphishing Attachment campaigns [2] [3] or executed as part of multi-stage malware. [4] Control Panel items, specifically CPL files, may also bypass application and/or file extension whitelisting.

# Detection

Monitor and analyze activity related to items associated with CPL files, such as the Windows Control Panel process binary (control.exe) and the Control_RunDLL and ControlRunDLLAsUser API functions in shell32.dll. When executed from the command line or clicked, control.exe will execute the CPL file (ex: control.exe file.cpl) before Rundll32 is used to call the CPL's API functions (ex: rundll32.exe shell32.dll,Control_RunDLL file.cpl). CPL files can be executed directly via the CPL API function with just the latter Rundll32 command, which may bypass detections and/or execution filters for control.exe. [2]

Inventory Control Panel items to locate unregistered and potentially malicious files present on systems:

Executable format registered Control Panel items will have a globally unique identifier (GUID) and registration Registry entries in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel\NameSpace and HKEY_CLASSES_ROOT\CLSID{GUID}. These entries may contain information about the Control Panel item such as its display name, path to the local file, and the command executed when opened in the Control Panel. [1]CPL format registered Control Panel items stored in the System32 directory are automatically shown in the Control Panel. Other Control Panel items will have registration entries in the Cpls and Extended Properties Registry keys of HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Control Panel. These entries may include information such as a GUID, path to the local file, and a canonical name used to launch the file programmatically ( WinExec("c:\windows\system32\control.exe {Canonical_Name}", SW_NORMAL);) or from a command line (control.exe /name {Canonical_Name}). [1]Some Control Panel items are extensible via Shell extensions registered in HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Controls Folder{name}\Shellex\PropertySheetHandlers where {name} is the predefined name of the system item. [1]

Analyze new Control Panel items as well as those present on disk for malicious content. Both executable and CPL formats are compliant Portable Executable (PE) images and can be examined using traditional tools and methods, pending anti-reverse-engineering techniques. [2]

# Mitigation

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating specific Windows API calls and/or execution of particular file extensions will likely have unintended side effects, such as preventing legitimate software (i.e., drivers and configuration tools) from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior.

Restrict storage and execution of Control Panel items to protected directories, such as C:\Windows, rather than user directories.

Index known safe Control Panel items and block potentially malicious software using whitelisting [5] tools like AppLocker [6] [7] that are capable of auditing and/or blocking unknown executable files.

Consider fully enabling User Account Control (UAC) to impede system-wide changes from illegitimate administrators. [8]

# Footnotes

[1] M. (n.d.). Implementing Control Panel Items. Retrieved January 18, 2018.

[2] Mercês, F. (2014, January 27). CPL Malware - Malicious Control Panel Items. Retrieved January 18, 2018.

[3] Bernardino, J. (2013, December 17). Control Panel Files Used As Malicious Attachments. Retrieved January 18, 2018.

[4] Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.

[5] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[6] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[7] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[8] Microsoft. (n.d.). User Account Control. Retrieved January 18, 2018.

## Defense

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating specific Windows API calls and/or execution of particular file extensions will li

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (4)

- [[CSRF Payload to Set Role to Admin via JSON POST]]
- [[CSRF Payload to Set Role to Admin via JSON POST]]
- [[Subdomain CSRF Attack]]
- [[Subdomain CSRF Attack]]
