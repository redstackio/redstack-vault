---
id: 3b4ee5f1-555c-45de-8508-38d5363f957e
name: Change Default File Association
type: technique
mitre_id: T1042
mitre_url: null
created_at: '2019-08-28T21:17:34.233291+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Change Default File Association

**MITRE ID**: T1042

## Description

When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access [1] [2] or by administrators using the built-in assoc utility. [3] Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.System file associations are listed under HKEY_CLASSES_ROOT.[extension], for example HKEY_CLASSES_ROOT.txt. The entries point to a handler for that extension located at HKEY_CLASSES_ROOT[handler]. The various commands are then listed as subkeys underneath the shell key at HKEY_CLASSES_ROOT[handler]\shell[action]\command. For example: HKEY_CLASSES_ROOT\txtfile\shell\open\command HKEY_CLASSES_ROOT\txtfile\shell\print\command* HKEY_CLASSES_ROOT\txtfile\shell\printto\commandThe values of the keys listed are commands that are executed when the handler opens the file extension. Adversaries can modify these values to continually execute arbitrary commands. [4]

# Detection

Collect and analyze changes to Registry keys that associate file extensions to default applications for execution and correlate with unknown process launch activity or unusual file types for that process. 

User file association preferences are stored under  [HKEY_CURRENT_USER]\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts and override associations configured under [HKEY_CLASSES_ROOT]. Changes to a user's preference will occur under this entry's subkeys.

Also look for abnormal process call trees for execution of other commands that could relate to Discovery actions or other techniques.

# Mitigation

Direct mitigation of this technique is not recommended since it is a legitimate function that can be performed by users for software preferences. Follow Microsoft's best practices for file associations. [5]

Identify and block potentially malicious software that may be executed by this technique using whitelisting [6] tools, like AppLocker, [7] [8] or Software Restriction Policies [9] where appropriate. [10]

# Footnotes

[1] Microsoft. (n.d.). Change which programs Windows 7 uses by default. Retrieved July 26, 2016.

[2] Microsoft. (n.d.). Specifying File Handlers for File Name Extensions. Retrieved November 13, 2014.

[3] Plett, C. et al.. (2017, October 15). assoc. Retrieved August 7, 2018.

[4] Sioting, S. (2012, October 8). TROJ_FAKEAV.GZD. Retrieved August 8, 2018.

[5] Microsoft. (n.d.). Retrieved July 26, 2016.

[6] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[7] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[8] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[9] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[10] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Direct mitigation of this technique is not recommended since it is a legitimate function that can be performed by users for software preferences. Follow Microsoft's best practices for file associations. (Citation: MSDN File Associations)

Identify and blo

## Tactics

- [[Persistence|TA0003 - Persistence]]
