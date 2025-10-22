---
id: 7ab0f430-7640-4b81-94db-de6fdd0b8bc6
name: AppleScript
type: technique
mitre_id: T1155
mitre_url: null
created_at: '2019-08-28T21:17:23.990684+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
---

# AppleScript

**MITRE ID**: T1155

## Description

macOS and OS X applications send AppleEvent messages to each other for interprocess communications (IPC). These messages can be easily scripted with AppleScript for local or remote IPC. Osascript executes AppleScript and any other Open Scripting Architecture (OSA) language scripts. A list of OSA languages installed on a system can be found by using the osalang program.AppleEvent messages can be sent independently or as part of a script. These events can locate open windows, send keystrokes, and interact with almost any open application locally or remotely. Adversaries can use this to interact with open SSH connection, move to remote machines, and even present users with fake dialog boxes. These events cannot start applications remotely (they can start them locally though), but can interact with applications if they're already running remotely. Since this is a scripting language, it can be used to launch more common techniques as well such as a reverse shell via python  [1]. Scripts can be run from the command-line via osascript /path/to/script or osascript -e "script here".

# Detection

Monitor for execution of AppleScript through osascript that may be related to other suspicious behavior occurring on the system.

# Mitigation

Require that all AppleScript be signed by a trusted developer ID before being executed - this will prevent random AppleScript code from executing  [3]. This subjects AppleScript code to the same scrutiny as other .app files passing through Gatekeeper.

# Footnotes

[1] Yerko Grbic. (2017, February 14). Macro Malware Targets Macs. Retrieved July 8, 2017.

[2] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[3] Steven Sande. (2013, December 23). AppleScript and Automator gain new features in OS X Mavericks. Retrieved September 21, 2018.

## Defense

Require that all AppleScript be signed by a trusted developer ID before being executed - this will prevent random AppleScript code from executing  (Citation: applescript signing). This subjects AppleScript code to the same scrutiny as other .app files pas

## Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
