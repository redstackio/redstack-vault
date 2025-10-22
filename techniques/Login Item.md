---
id: c6eda7a0-0898-4dec-b490-6879ae9d1727
name: Login Item
type: technique
mitre_id: T1162
mitre_url: null
created_at: '2019-08-28T21:17:40.250904+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Login Item

**MITRE ID**: T1162

## Description

MacOS provides the option to list specific applications to run when a user logs in. These applications run under the logged in user's context, and will be started every time the user logs in. Login items installed using the Service Management Framework are not visible in the System Preferences and can only be removed by the application that created them [1]. Users have direct control over login items installed using a shared file list which are also visible in System Preferences [1]. These login items are stored in the user's ~/Library/Preferences/ directory in a plist file called com.apple.loginitems.plist [2]. Some of these applications can open visible dialogs to the user, but they don’t all have to since there is an option to ‘Hide’ the window. If an adversary can register their own login item or modified an existing one, then they can use it to execute their code for a persistence mechanism each time the user logs in [3] [4]. The API method  SMLoginItemSetEnabled  can be used to set Login Items, but scripting languages like AppleScript can do this as well  [1].

# Detection

All the login items created via shared file lists are viewable by going to the Apple menu -> System Preferences -> Users & Groups -> Login items. This area (and the corresponding file locations) should be monitored and whitelisted for known good applications. Otherwise, Login Items are located in  Contents/Library/LoginItems  within an application bundle, so these paths should be monitored as well  [1]. Monitor process execution resulting from login actions for unusual or unknown applications.

# Mitigation

Restrict users from being able to create their own login items. Additionally, holding the shift key during login prevents apps from opening automatically [6].

# Footnotes

[1] Apple. (2016, September 13). Adding Login Items. Retrieved July 11, 2017.

[2] Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.

[3] Patrick Wardle. (2015). Malware Persistence on OS X Yosemite. Retrieved July 10, 2017.

[4] Thomas Reed. (2017, July 7). New OSX.Dok malware intercepts web traffic. Retrieved July 10, 2017.

[5] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[6] Apple. (2016, December 6). Automatically re-open windows, apps, and documents on your Mac. Retrieved July 11, 2017.

## Defense

Restrict users from being able to create their own login items. Additionally, holding the shift key during login prevents apps from opening automatically (Citation: Re-Open windows on Mac).

## Tactics

- [[Persistence|TA0003 - Persistence]]
