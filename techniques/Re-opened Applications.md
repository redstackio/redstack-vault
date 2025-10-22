---
id: a6a1e100-1e73-4e90-84db-0a86ccd8b7da
name: Re-opened Applications
type: technique
mitre_id: T1164
mitre_url: null
created_at: '2019-08-28T21:17:29.700116+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Re-opened Applications

**MITRE ID**: T1164

## Description

Starting in Mac OS X 10.7 (Lion), users can specify certain applications to be re-opened when a user reboots their machine. While this is usually done via a Graphical User Interface (GUI) on an app-by-app basis, there are property list files (plist) that contain this information as well located at ~/Library/Preferences/com.apple.loginwindow.plist and ~/Library/Preferences/ByHost/com.apple.loginwindow.* .plist. An adversary can modify one of these files directly to include a link to their malicious executable to provide a persistence mechanism each time the user reboots their machine [1].

# Detection

Monitoring the specific plist files associated with reopening applications can indicate when an application has registered itself to be reopened.

# Mitigation

Holding the Shift key while logging in prevents apps from opening automatically [2]. This feature can be disabled entirely with the following terminal command: defaults write -g ApplePersistence -bool no.

# Footnotes

[1] Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.

[2] Apple. (2016, December 6). Automatically re-open windows, apps, and documents on your Mac. Retrieved July 11, 2017.

## Defense

Holding the Shift key while logging in prevents apps from opening automatically (Citation: Re-Open windows on Mac). This feature can be disabled entirely with the following terminal command: <code>defaults write -g ApplePersistence -bool no</code>.

## Tactics

- [[Persistence|TA0003 - Persistence]]
