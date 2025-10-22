---
id: 00fbd9f2-93b8-435c-8a75-c5c6443590bc
name: Hidden Users
type: technique
mitre_id: T1147
mitre_url: null
created_at: '2019-08-28T21:17:23.627827+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Linux - Backdoor MOTD Persistence]]'
---

# Hidden Users

**MITRE ID**: T1147

## Description

Every user account in macOS has a userID associated with it. When creating a user, you can specify the userID for that account. There is a property value in /Library/Preferences/com.apple.loginwindow called Hide500Users that prevents users with userIDs 500 and lower from appearing at the login screen. By using the Create Account technique with a userID under 500 and enabling this property (setting it to Yes), an adversary can hide their user accounts much more easily: sudo dscl . -create /Users/username UniqueID 401 [1].

# Detection

This technique prevents the new user from showing up at the log in screen, but all of the other signs of a new user still exist. The user still gets a home directory and will appear in the authentication logs.

# Mitigation

If the computer is domain joined, then group policy can help restrict the ability to create or hide users. Similarly, preventing the modification of the /Library/Preferences/com.apple.loginwindow Hide500Users value will force all users to be visible.

# Footnotes

[1] Amit Serper. (2016). Cybereason Lab Analysis OSX.Pirrit. Retrieved July 8, 2017.

## Defense

If the computer is domain joined, then group policy can help restrict the ability to create or hide users. Similarly, preventing the modification of the <code>/Library/Preferences/com.apple.loginwindow</code> <code>Hide500Users</code> value will force all

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (1)

- [[Linux - Backdoor MOTD Persistence]]
