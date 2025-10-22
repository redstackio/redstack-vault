---
id: 0866ba11-a7cf-44c1-b738-cc7aebc07fee
name: File System Permissions Weakness
type: technique
mitre_id: T1044
mitre_url: null
created_at: '2019-08-28T21:17:47.494281+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Change Password in a Writable /etc/passwd]]'
- '[[Docker Privilege Escalation Using Docker Group]]'
- '[[Enumerate Linux Privilege Escalation Paths (LinEnum)]]'
- '[[Enumerate Linux Privilege Escalation Paths (linPEAS)]]'
- '[[Enumerate Windows for Missing Patches and Hotfixes (Sherlock)]]'
- '[[Enumerate Windows for Privilege Escalation (JAWS)]]'
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Enumerate Windows for Privilege Escalation (SharpUp)]]'
- '[[Enumerate Windows for Privilege Escalation (winPEAS)]]'
---

# File System Permissions Weakness

**MITRE ID**: T1044

## Description

Processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself, are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a higher permissions level. If the executing process is set to run at a specific time or during a certain event (e.g., system bootup) then this technique can also be used for persistence.ServicesManipulation of Windows service binaries is one variation of this technique. Adversaries may replace a legitimate service executable with their own executable to gain persistence and/or privilege escalation to the account context the service is set to execute under (local/domain account, SYSTEM, LocalService, or NetworkService). Once the service is started, either directly by the user (if appropriate access is available) or through some other means, such as a system restart if the service starts on bootup, the replaced executable will run instead of the original service executable.Executable InstallersAnother variation of this technique can be performed by taking advantage of a weakness that is common in executable, self-extracting installers. During the installation process, it is common for installers to use a subdirectory within the %TEMP% directory to unpack binaries such as DLLs, EXEs, or other payloads. When installers create subdirectories and files they often do not set appropriate permissions to restrict write access, which allows for execution of untrusted code placed in the subdirectories or overwriting of binaries used in the installation process. This behavior is related to and may take advantage of DLL Search Order Hijacking. Some installers may also require elevated privileges that will result in privilege escalation when executing adversary controlled code. This behavior is related to Bypass User Account Control. Several examples of this weakness in existing common installers have been reported to software vendors. [1] [2]

# Detection

Look for changes to binaries and service executables that may normally occur during software updates. If an executable is written, renamed, and/or moved to match an existing service executable, it could be detected and correlated with other suspicious behavior. Hashing of binaries and service executables could be used to detect replacement against historical data.

Look for abnormal process call trees from typical processes and services and for execution of other commands that could relate to Discovery or other adversary techniques.

# Mitigation

Use auditing tools capable of detecting file system permissions abuse opportunities on systems within an enterprise and correct them. Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service binary target path locations. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for service file system permissions weaknesses. [4]

Identify and block potentially malicious software that may be executed through abuse of file, directory, and service permissions by using whitelisting [5] tools, like AppLocker, [6] [7] that are capable of auditing and/or blocking unknown programs. Deny execution from user directories such as file download directories and temp directories where able. [2]

Turn off UAC's privilege elevation for standard users [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]to automatically deny elevation requests, add: "ConsentPromptBehaviorUser"=dword:00000000 [2]. Consider enabling installer detection for all users by adding: "EnableInstallerDetection"=dword:00000001. This will prompt for a password for installation and also log the attempt. To disable installer detection, instead add: "EnableInstallerDetection"=dword:00000000. This may prevent potential elevation of privileges through exploitation during the process of UAC detecting the installer, but will allow the installation process to continue without being logged.

# Footnotes

[1] Kugler, R. (2012, November 20). Mozilla Foundation Security Advisory 2012-98. Retrieved March 10, 2017.

[2] Kanthak, S. (2015, December 8). Executable installers are vulnerable^WEVIL (case 7): 7z*.exe allows remote code execution with escalation of privilege. Retrieved March 10, 2017.

[3] F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.

[4] PowerSploit. (n.d.). Retrieved December 4, 2014.

[5] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[6] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[7] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

## Defense

Use auditing tools capable of detecting file system permissions abuse opportunities on systems within an enterprise and correct them. Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (9)

- [[Change Password in a Writable /etc/passwd]]
- [[Docker Privilege Escalation Using Docker Group]]
- [[Enumerate Linux Privilege Escalation Paths (LinEnum)]]
- [[Enumerate Linux Privilege Escalation Paths (linPEAS)]]
- [[Enumerate Windows for Missing Patches and Hotfixes (Sherlock)]]
- [[Enumerate Windows for Privilege Escalation (JAWS)]]
- [[Enumerate Windows for Privilege Escalation (PowerUp)]]
- [[Enumerate Windows for Privilege Escalation (SharpUp)]]
- [[Enumerate Windows for Privilege Escalation (winPEAS)]]
