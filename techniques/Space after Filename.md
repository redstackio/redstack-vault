---
id: 73734b04-f952-45c8-b3bf-9c8bcf834db9
name: Space after Filename
type: technique
mitre_id: T1151
mitre_url: null
created_at: '2019-08-28T21:17:41.734403+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
---

# Space after Filename

**MITRE ID**: T1151

## Description

Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system. For example, if there is a Mach-O executable file called evil.bin, when it is double clicked by a user, it will launch Terminal.app and execute. If this file is renamed to evil.txt, then when double clicked by a user, it will launch with the default text editing application (not executing the binary). However, if the file is renamed to "evil.txt " (note the space at the end), then when double clicked by a user, the true file type is determined by the OS and handled appropriately and the binary will be executed [1]. Adversaries can use this feature to trick users into double clicking benign-looking files of any format and ultimately executing something malicious.

# Detection

It's not common for spaces to be at the end of filenames, so this is something that can easily be checked with file monitoring. From the user's perspective though, this is very hard to notice from within the Finder.app or on the command-line in Terminal.app. Processes executed from binaries containing non-standard extensions in the filename are suspicious.

# Mitigation

Prevent files from having a trailing space after the extension.

# Footnotes

[1] Dan Goodin. (2016, July 6). After hiatus, in-the-wild Mac backdoors are suddenly back. Retrieved July 8, 2017.

[2] Patrick Wardle. (2017, January 1). Mac Malware of 2016. Retrieved September 21, 2018.

## Defense

Prevent files from having a trailing space after the extension.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
