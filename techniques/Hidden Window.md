---
id: fc202226-5320-4093-9a13-8144011d6687
name: Hidden Window
type: technique
mitre_id: T1143
mitre_url: null
created_at: '2019-08-28T21:17:21.858895+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Hidden Window

**MITRE ID**: T1143

## Description

The configurations for how applications run on macOS and OS X are listed in property list (plist) files. One of the tags in these files can be apple.awt.UIElement, which allows for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications run in the system tray, but don't also want to show up in the Dock. However, adversaries can abuse this feature and hide their running window  [1].

# Detection

Plist files are ASCII text files with a specific format, so they're relatively easy to parse. File monitoring can check for the apple.awt.UIElement or any other suspicious plist tag in plist files and flag them.

# Mitigation

Whitelist programs that are allowed to have this plist tag. All other programs should be considered suspicious.

# Footnotes

[1] Thomas Reed. (2017, January 18). New Mac backdoor using antiquated code. Retrieved July 5, 2017.

## Defense

Whitelist programs that are allowed to have this plist tag. All other programs should be considered suspicious.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
