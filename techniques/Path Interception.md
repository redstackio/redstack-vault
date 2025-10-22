---
id: 02929826-ab91-48be-bc16-3054f81aa880
name: Path Interception
type: technique
mitre_id: T1034
mitre_url: null
created_at: '2019-08-28T21:17:45.915448+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Query Windows for Unquoted Service Paths]]'
---

# Path Interception

**MITRE ID**: T1034

## Description

Path interception occurs when an executable is placed in a specific path so that it is executed by an application instead of the intended target. One example of this was the use of a copy of cmd in the current working directory of a vulnerable application that loads a CMD or BAT file with the CreateProcess function. [1]There are multiple distinct weaknesses or misconfigurations that adversaries may take advantage of when performing path interception: unquoted paths, path environment variable misconfigurations, and search order hijacking. The first vulnerability deals with full program paths, while the second and third occur when program paths are not specified. These techniques can be used for persistence if executables are called on a regular basis, as well as privilege escalation if intercepted executables are started by a higher privileged process.Unquoted PathsService paths (stored in Windows Registry keys) [2] and shortcut paths are vulnerable to path interception if the path has one or more spaces and is not surrounded by quotation marks (e.g., C:\unsafe path with space\program.exe vs. "C:\safe path with space\program.exe"). [3] An adversary can place an executable in a higher level directory of the path, and Windows will resolve that executable instead of the intended executable. For example, if the path in a shortcut is C:\program files\myapp.exe, an adversary may create a program at C:\program.exe that will be run instead of the intended program. [4] [5]PATH Environment Variable MisconfigurationThe PATH environment variable contains a list of directories. Certain methods of executing a program (namely using cmd.exe or the command-line) rely solely on the PATH environment variable to determine the locations that are searched for a program when the path for the program is not given. If any directories are listed in the PATH environment variable before the Windows directory, %SystemRoot%\system32 (e.g., C:\Windows\system32), a program may be placed in the preceding directory that is named the same as a Windows program (such as cmd, PowerShell, or Python), which will be executed when that command is executed from a script or command-line.For example, if C:\example path precedes C:\Windows\system32 is in the PATH environment variable, a program that is named net.exe and placed in C:\example path will be called instead of the Windows system "net" when "net" is executed from the command-line.Search Order HijackingSearch order hijacking occurs when an adversary abuses the order in which Windows searches for programs that are not given a path. The search order differs depending on the method that is used to execute the program. [6] [7] [8] However, it is common for Windows to search in the directory of the initiating program before searching through the Windows system directory. An adversary who finds a program vulnerable to search order hijacking (i.e., a program that does not specify the path to an executable) may take advantage of this vulnerability by creating a program named after the improperly specified program and placing it within the initiating program's directory.For example, "example.exe" runs "cmd.exe" with the command-line argument net user. An adversary may place a program called "net.exe" within the same directory as example.exe, "net.exe" will be run instead of the Windows system utility net. In addition, if an adversary places a program called "net.com" in the same directory as "net.exe", then cmd.exe /C net user will execute "net.com" instead of "net.exe" due to the order of executable extensions defined under PATHEXT. [9]Search order hijacking is also a common practice for hijacking DLL loads and is covered in DLL Search Order Hijacking.

# Detection

Monitor file creation for files named after partial directories and in locations that may be searched for common processes through the environment variable, or otherwise should not be user writable. Monitor the executing process for process executable paths that are named for partial directories. Monitor file creation for programs that are named after Windows system programs or programs commonly executed without a path (such as "findstr," "net," and "python"). If this activity occurs outside of known administration activity, upgrades, installations, or patches, then it may be suspicious. 

Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

# Mitigation

Eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them [6]. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate [13]. Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries.

Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations [14]. 

Require that all executables be placed in write-protected directories. Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory C: and system directories, such as C:\Windows\, to reduce places where malicious files could be placed for execution.

Identify and block potentially malicious software that may be executed through the path interception by using whitelisting [15] tools, like AppLocker [16] [17] or Software Restriction Policies, [18] that are capable of auditing and/or blocking unknown executables.

# Footnotes

[1] Nagaraju, S. (2014, April 8). MS14-019 – Fixing a binary hijacking via .cmd or .bat file. Retrieved July 25, 2016.

[2] Microsoft. (n.d.). CurrentControlSet\Services Subkey Entries. Retrieved November 30, 2014.

[3] Baggett, M. (2012, November 8). Help eliminate unquoted path vulnerabilities. Retrieved December 4, 2014.

[4] HackHappy. (2018, April 23). Windows Privilege Escalation – Unquoted Services. Retrieved August 10, 2018.

[5] McFarland, R. (2018, January 26). Windows Privilege Escalation Guide. Retrieved August 10, 2018.

[6] Microsoft. (n.d.). CreateProcess function. Retrieved December 5, 2014.

[7] Hill, T. (n.d.). Windows NT Command Shell. Retrieved December 5, 2014.

[8] Microsoft. (n.d.). WinExec function. Retrieved December 5, 2014.

[9] Microsoft. (n.d.). Environment Property. Retrieved July 27, 2016.

[10] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[11] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[12] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[13] Microsoft. (n.d.). Dynamic-Link Library Security. Retrieved July 25, 2016.

[14] Kanthak, S. (2016, July 20). Vulnerability and Exploit Detector. Retrieved February 3, 2017.

[15] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[16] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[17] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[18] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

## Defense

Eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them (Citation: Microsoft CreateProcess).

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (2)

- [[Enumerate Windows for Privilege Escalation (PowerUp)]]
- [[Query Windows for Unquoted Service Paths]]
