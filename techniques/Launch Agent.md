---
id: 5294200e-59f6-4150-a331-31288742adff
name: Launch Agent
type: technique
mitre_id: T1159
mitre_url: null
created_at: '2019-08-28T21:17:31.118144+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Launch Agent

**MITRE ID**: T1159

## Description

Per Apple’s developer documentation, when a user logs in, a per-user launchd process is started which loads the parameters for each launch-on-demand user agent from the property list (plist) files found in /System/Library/LaunchAgents, /Library/LaunchAgents, and $HOME/Library/LaunchAgents [1] [2] [3]. These launch agents have property list files which point to the executables that will be launched [4].Adversaries may install a new launch agent that can be configured to execute at login by using launchd or launchctl to load a plist into the appropriate directories  [5]  [6]. The agent name may be disguised by using a name from a related operating system or benign software. Launch Agents are created with user level privileges and are executed with the privileges of the user when they log in [7] [8]. They can be set up to execute when a specific user logs in (in the specific user’s directory structure) or when any user logs in (which requires administrator privileges).

# Detection

Monitor Launch Agent creation through additional plist files and utilities such as Objective-See’s  KnockKnock application. Launch Agents also require files on disk for persistence which can also be monitored via other file monitoring applications.

# Mitigation

Restrict user's abilities to create Launch Agents with group policy.

# Footnotes

[1] Apple. (n.d.). Creating Launch Daemons and Agents. Retrieved July 10, 2017.

[2] Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July 3, 2017.

[3] Thomas Reed. (2017, January 18). New Mac backdoor using antiquated code. Retrieved July 5, 2017.

[4] Thomas Reed. (2017, July 7). New OSX.Dok malware intercepts web traffic. Retrieved July 10, 2017.

[5] Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.

[6] Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.

[7] Patrick Wardle. (2016, February 29). Let's Play Doctor: Practical OS X Malware Detection & Analysis. Retrieved July 10, 2017.

[8] Eddie Lee. (2016, February 17). OceanLotus for OS X - an Application Bundle Pretending to be an Adobe Flash Update. Retrieved July 5, 2017.

[9] Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.

[10] Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.

[11] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[12] Patrick Wardle. (2017, January 1). Mac Malware of 2016. Retrieved September 21, 2018.

[13] Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.

## Defense

Restrict user's abilities to create Launch Agents with group policy.

## Tactics

- [[Persistence|TA0003 - Persistence]]
