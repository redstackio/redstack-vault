---
id: 1353162b-cac5-41c1-905c-ba938d0802e2
name: Linux - Backdooring User Startup File
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.070727+00:00'
updated_at: '2023-04-10T20:34:18.923868+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
sub_techniques:
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[Backdooring a user startup file]]'
- '[[Linux - Persistence]]'
commands:
- '[[Autostart Welcome application]]'
---

# Linux - Backdooring User Startup File

## Summary

Backdooring a user startup file is a technique used by attackers to maintain persistence on a Linux system by adding malicious code to a user's startup file. This technique is commonly used because it is an easy way to achieve persistence and is often overlooked by defenders. Attackers can use this

## Description

# Description

Backdooring a user startup file is a technique used by attackers to maintain persistence on a Linux system by adding malicious code to a user's startup file. This technique is commonly used because it is an easy way to achieve persistence and is often overlooked by defenders. Attackers can use this technique to execute code every time the user logs in, allowing them to maintain access to the system even after a reboot. From a technical perspective, this technique involves adding a command to a user's startup file that will execute the attacker's code. From a business value perspective, this technique can be used to maintain a foothold on a compromised system and to exfiltrate sensitive data.

## Requirements

1. Access to the target system

1. Ability to modify a user's startup file

## Defense

1. Monitor for changes to user startup files

1. Implement least privilege access controls to limit the ability to modify user startup files

1. Regularly review and remove unnecessary startup files

## Objectives

1. Maintain persistence on a compromised Linux system

1. Execute code every time the user logs in

1. Maintain access to the system even after a reboot

# Instructions

1. Create a desktop file in the ~/.config/autostart directory to automatically launch a program or script at login.

**Code**: [[~/.config/autostart/NAME_OF_FILE.desktop]]

> The desktop file should have the following format:

[Desktop Entry]
Type=Application
Exec=/path/to/program_or_script
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=NAME_OF_FILE
Comment=DESCRIPTION_OF_FILE

Replace /path/to/program_or_script with the actual path to the program or script you want to launch. Replace NAME_OF_FILE with the desired name for the desktop file, and DESCRIPTION_OF_FILE with a brief description of what the file does. The X-GNOME-Autostart-enabled=true line ensures that the file will actually be executed at login.

2. To autostart the GNOME Welcome Tour, follow these steps:
1. Open the terminal.
2. Type 'nano ~/.config/autostart/gnome-welcome-tour.desktop' and press Enter.
3. Copy and paste the following code into the file:

[Desktop Entry]
Type=Application
Name=Welcome
Exec=/var/lib/gnome-welcome-tour
AutostartCondition=unless-exists ~/.cache/gnome-getting-started-docs/seen-getting-started-guide
OnlyShowIn=GNOME;
X-GNOME-Autostart-enabled=false

4. Save the file by pressing Ctrl+O, then press Enter.
5. Exit nano by pressing Ctrl+X.

The GNOME Welcome Tour will now start automatically when you log in to your GNOME desktop environment.

**Code**: [[In : ~/.config/autostart/*.desktop

[Desktop Entry]]

> This command provides instructions on how to enable the GNOME Welcome Tour to start automatically when you log in to your GNOME desktop environment. The command includes a code snippet that creates a desktop entry file for the GNOME Welcome Tour and sets the AutostartCondition parameter to prevent the tour from starting if the user has already seen the getting started guide. The OnlyShowIn parameter restricts the tour to only run in the GNOME desktop environment. The X-GNOME-Autostart-enabled parameter is set to false to disable the autostart feature by default.

**Command** ([[Autostart Welcome application]]):

```bash
In : ~/.config/autostart/*.desktop

[Desktop Entry]
Type=Application
Name=Welcome
Exec=/var/lib/gnome-welcome-tour
AutostartCondition=unless-exists ~/.cache/gnome-getting-started-docs/seen-getting-started-guide
OnlyShowIn=GNOME;
X-GNOME-Autostart-enabled=false
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Create or Modify System Process|T1543 - Create or Modify System Process]]

### Sub-Techniques

- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[Autostart Welcome application]]

## Tags

- [[Backdooring a user startup file]]
- [[Linux - Persistence]]
