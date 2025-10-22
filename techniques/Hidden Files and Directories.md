---
id: 6a5e46ef-b962-4f44-8d8a-547f93dbaea2
name: Hidden Files and Directories
type: technique
mitre_id: T1158
mitre_url: null
created_at: '2019-08-28T21:17:40.591590+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Hidden Files and Directories

**MITRE ID**: T1158

## Description

To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or when using normal commands on the command line. Users must explicitly ask to show the hidden files either via a series of Graphical User Interface (GUI) prompts or with command line switches (dir /a for Windows and ls –a for Linux and macOS).Adversaries can use this to their advantage to hide files and folders anywhere on the system for persistence and evading a typical user or system analysis that does not incorporate investigation of hidden files.WindowsUsers can mark specific files as hidden by using the attrib.exe binary. Simply do attrib +h filename to mark a file or folder as hidden. Similarly, the "+s" marks a file as a system file and the "+r" flag marks the file as read only. Like most windows binaries, the attrib.exe binary provides the ability to apply these changes recursively "/S".Linux/MacUsers can mark specific files as hidden simply by putting a "." as the first character in the file or folder name  [1] [2]. Files and folder that start with a period, ‘.’, are by default hidden from being viewed in the Finder application and standard command-line utilities like "ls". Users must specifically change settings to have these files viewable. For command line usages, there is typically a flag to see all files (including hidden ones). To view these files in the Finder Application, the following command must be executed: defaults write com.apple.finder AppleShowAllFiles YES, and then relaunch the Finder Application.MacFiles on macOS can be marked with the UF_HIDDEN flag which prevents them from being seen in Finder.app, but still allows them to be seen in Terminal.app [3].Many applications create these hidden files and folders to store information so that it doesn’t clutter up the user’s workspace. For example, SSH utilities create a .ssh folder that’s hidden and contains the user’s known hosts and keys.

# Detection

Monitor the file system and shell commands for files being created with a leading "." and the Windows command-line use of attrib.exe to add the hidden attribute.

# Mitigation

Mitigation of this technique may be difficult and unadvised due to the the legitimate use of hidden files and directories.

# Footnotes

[1] Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.

[2] Thomas Reed. (2017, January 18). New Mac backdoor using antiquated code. Retrieved July 5, 2017.

[3] Claud Xiao. (n.d.). WireLurker: A New Era in iOS and OS X Malware. Retrieved July 10, 2017.

[4] Mercer, W., et al. (2017, October 22). "Cyber Conflict" Decoy Document Used in Real Cyber Conflict. Retrieved November 2, 2018.

[5] Dumont, R.. (2019, April 9). OceanLotus: macOS malware update. Retrieved April 15, 2019.

[6] Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.

[7] Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.

[8] Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.

[9] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[10] Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.

[11] PETER EWANE. (2017, June 9). MacSpy: OS X RAT as a Service. Retrieved September 21, 2018.

[12] Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.

[13] Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.

[14] Horejsi, J., et al. (2018, March 14). Tropic Trooper’s New Strategy. Retrieved November 9, 2018.

[15] Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved March 25, 2019.

## Defense

Mitigation of this technique may be difficult and unadvised due to the the legitimate use of hidden files and directories.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
