---
id: ab29fd55-0c0a-4f7f-ae0f-903f42f83009
name: Launchctl
type: technique
mitre_id: T1152
mitre_url: null
created_at: '2019-08-28T21:17:44.281732+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Launchctl

**MITRE ID**: T1152

## Description

Launchctl controls the macOS launchd process which handles things like launch agents and launch daemons, but can execute other commands or programs itself. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input. By loading or reloading launch agents or launch daemons, adversaries can install persistence or execute changes they made  [1]. Running a command from launchctl is as simple as launchctl submit -l  -- /Path/to/thing/to/execute "arg" "arg" "arg". Loading, unloading, or reloading launch agents or launch daemons can require elevated privileges. Adversaries can abuse this functionality to execute code or even bypass whitelisting if launchctl is an allowed process.

# Detection

Knock Knock can be used to detect persistent programs such as those installed via launchctl as launch agents or launch daemons. Additionally, every launch agent or launch daemon must have a corresponding plist file on disk somewhere which can be monitored. Monitor process execution from launchctl/launchd for unusual or unknown processes.

# Mitigation

Prevent users from installing their own launch agents or launch daemons and instead require them to be pushed out by group policy.

# Footnotes

[1] Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.

[2] Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.

## Defense

Prevent users from installing their own launch agents or launch daemons and instead require them to be pushed out by group policy.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
