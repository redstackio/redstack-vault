---
id: 2abc01a8-b735-4c5a-ac6e-6e1a4d599207
name: Office Application Startup
type: technique
mitre_id: T1137
mitre_url: null
created_at: '2019-08-28T21:17:41.182299+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[DCOM Office Remote Code Execution]]'
- '[[DOCM Download and Execute via PowerShell]]'
- '[[Metasploit Scripting with Meterpreter Reverse HTTPS Payload]]'
- '[[Office Macro-Based Malware]]'
- '[[XLM Excel 4.0 - SharpShooter Payload Creation]]'
---

# Office Application Startup

**MITRE ID**: T1137

## Description

Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started.Office Template MacrosMicrosoft Office contains templates that are part of common Office applications and are used to customize styles. The base templates within the application are used each time an application starts. [1]Office Visual Basic for Applications (VBA) macros [2] can inserted into the base templated and used to execute code when the respective Office application starts in order to obtain persistence. Examples for both Word and Excel have been discovered and published. By default, Word has a Normal.dotm template created that can be modified to include a malicious macro. Excel does not have a template file created by default, but one can be added that will automatically be loaded. [3] [4]Word Normal.dotm location:C:\Users(username)\AppData\Roaming\Microsoft\Templates\Normal.dotmExcel Personal.xlsb location:C:\Users(username)\AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSBAn adversary may need to enable macros to execute unrestricted depending on the system or enterprise security policy on use of macros.Office TestA Registry location was found that when a DLL reference was placed within it the corresponding DLL pointed to by the binary path would be executed every time an Office application is started [5]HKEY_CURRENT_USER\Software\Microsoft\Office test\Special\PerfAdd-insOffice add-ins can be used to add functionality to Office programs. [6]Add-ins can also be used to obtain persistence because they can be set to execute code when an Office application starts. There are different types of add-ins that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook add-ins. [7][8]Outlook Rules, Forms, and Home PageA variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.[9] Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words from a specific sender. Malicious Outlook rules can be created that can trigger code execution when an adversary sends a specifically crafted email to that user.[10]Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook Forms can be created that will execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.[11]Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an internal or external URL to be loaded and presented whenever a folder is opened. A malicious HTML page can be crafted that will execute code when loaded by Outlook Home Page.[12]To abuse these features, an adversary requires prior access to the user’s Outlook mailbox, either via an Exchange/OWA server or via the client application. Once malicious rules, forms, or Home Pages have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious Home Pages will execute when the right Outlook folder is loaded/reloaded while malicious rules and forms will execute when an adversary sends a specifically crafted email to the user.[10][11][12]

# Detection

Many Office-related persistence mechanisms require changes to the Registry and for binaries, files, or scripts to be written to disk or existing files modified to include malicious scripts. Collect events related to Registry key creation and modification for keys that could be used for Office-based persistence.[17][18] Modification to base templated, like Normal.dotm, should also be investigated since the base templates should likely not contain VBA macros. Changes to the Office macro security settings should also be investigated.

Monitor and validate the Office trusted locations on the file system and audit the Registry entries relevant for enabling add-ins. [7]

Non-standard process execution trees may also indicate suspicious or malicious behavior. Collect process execution information including process IDs (PID) and parent process IDs (PPID) and look for abnormal chains of activity resulting from Office processes. If winword.exe is the parent process for suspicious processes and activity relating to other adversarial techniques, then it could indicate that the application was used maliciously.

For the Outlook rules and forms methods, Microsoft has released a PowerShell script to safely gather mail forwarding rules and custom forms in your mail environment as well as steps to interpret the output.[19] SensePost, whose tool Ruler can be used to carry out malicious rules, forms, and Home Page attacks, has released a tool to detect Ruler usage.[20]

# Mitigation

Follow Office macro security best practices suitable for your environment. Disable Office VBA macros from executing. Even setting to disable with notification could enable unsuspecting users to execute potentially malicious macros. [16]

For the Office Test method, create the Registry key used to execute it and set the permissions to "Read Control" to prevent easy access to the key without administrator permissions or requiring Privilege Escalation. [13]

Disable Office add-ins. If they are required, follow best practices for securing them by requiring them to be signed and disabling user notification for allowing add-ins. For some add-ins types (WLL, VBA) additional mitigation is likely required as disabling add-ins in the Office Trust Center does not disable WLL nor does it prevent VBA code from executing. [7]

For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine.[11] Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems.[12]

# Footnotes

[1] Microsoft. (n.d.). Change the Normal template (Normal.dotm). Retrieved July 3, 2017.

[2] Austin, J. (2017, June 6). Getting Started with VBA in Office. Retrieved July 3, 2017.

[3] Nelson, M. (2014, January 23). Maintaining Access with normal.dotm. Retrieved July 3, 2017.

[4] Hexacorn. (2017, April 17). Beyond good ol’ Run key, Part 62. Retrieved July 3, 2017.

[5] Hexacorn. (2014, April 16). Beyond good ol’ Run key, Part 10. Retrieved July 3, 2017.

[6] Microsoft. (n.d.). Add or remove add-ins. Retrieved July 3, 2017.

[7] Knowles, W. (2017, April 21). Add-In Opportunities for Office Persistence. Retrieved July 3, 2017.

[8] Caban, D. and Hirani, M. (2018, October 3). You’ve Got Mail! Enterprise Email Compromise. Retrieved April 22, 2019.

[9] SensePost. (2016, August 18). Ruler: A tool to abuse Exchange services. Retrieved February 4, 2019.

[10] Landers, N. (2015, December 4). Malicious Outlook Rules. Retrieved February 4, 2019.

[11] Stalmans, E. (2017, April 28). Outlook Forms and Shells. Retrieved February 4, 2019.

[12] Stalmans, E. (2017, October 11). Outlook Home Page – Another Ruler Vector. Retrieved February 4, 2019.

[13] Falcone, R. (2016, July 20). Technical Walkthrough: Office Test Persistence Method Used In Recent Sofacy Attacks. Retrieved July 3, 2017.

[14] Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.

[15] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[16] Microsoft Malware Protection Center. (2016, March 22). New feature in Office 2016 can block macros and help prevent infection. Retrieved July 3, 2017.

[17] Parisi, T., et al. (2017, July). Using Outlook Forms for Lateral Movement and Persistence. Retrieved February 5, 2019.

[18] Soutcast. (2018, September 14). Outlook Today Homepage Persistence. Retrieved February 5, 2019.

[19] Fox, C., Vangel, D. (2018, April 22). Detect and Remediate Outlook Rules and Custom Forms Injections Attacks in Office 365. Retrieved February 4, 2019.

[20] SensePost. (2017, September 21). NotRuler - The opposite of Ruler, provides blue teams with the ability to detect Ruler usage against Exchange. Retrieved February 4, 2019.

## Defense

Follow Office macro security best practices suitable for your environment. Disable Office VBA macros from executing. Even setting to disable with notification could enable unsuspecting users to execute potentially malicious macros. (Citation: TechNet Offi

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (5)

- [[DCOM Office Remote Code Execution]]
- [[DOCM Download and Execute via PowerShell]]
- [[Metasploit Scripting with Meterpreter Reverse HTTPS Payload]]
- [[Office Macro-Based Malware]]
- [[XLM Excel 4.0 - SharpShooter Payload Creation]]
