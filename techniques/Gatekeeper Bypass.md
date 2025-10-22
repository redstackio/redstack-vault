---
id: 446d73f2-7214-496e-ac08-cbdd07921817
name: Gatekeeper Bypass
type: technique
mitre_id: T1144
mitre_url: null
created_at: '2019-08-28T21:17:38.433202+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Gatekeeper Bypass

**MITRE ID**: T1144

## Description

In macOS and OS X, when applications or programs are downloaded from the internet, there is a special attribute set on the file called com.apple.quarantine. This attribute is read by Apple's Gatekeeper defense program at execution time and provides a prompt to the user to allow or deny execution. Apps loaded onto the system from USB flash drive, optical disk, external hard drive, or even from a drive shared over the local network won’t set this flag. Additionally, other utilities or events like drive-by downloads don’t necessarily set it either. This completely bypasses the built-in Gatekeeper check. [1] The presence of the quarantine flag can be checked by the xattr command xattr /path/to/MyApp.app for com.apple.quarantine. Similarly, given sudo access or elevated permission, this attribute can be removed with xattr as well, sudo xattr -r -d com.apple.quarantine /path/to/MyApp.app. [2] [3]In typical operation, a file will be downloaded from the internet and given a quarantine flag before being saved to disk. When the user tries to open the file or application, macOS’s gatekeeper will step in and check for the presence of this flag. If it exists, then macOS will then prompt the user to confirmation that they want to run the program and will even provide the URL where the application came from. However, this is all based on the file being downloaded from a quarantine-savvy application. [4]

# Detection

Monitoring for the removal of the com.apple.quarantine flag by a user instead of the operating system is a suspicious action and should be examined further.

# Mitigation

Other tools should be used to supplement Gatekeeper's functionality. Additionally, system settings can prevent applications from running that haven't been downloaded through the Apple Store which can help mitigate some of these issues.

# Footnotes

[1] Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.

[2] Rich Trouton. (2012, November 20). Clearing the quarantine extended attribute from downloaded applications. Retrieved July 5, 2017.

[3] Eddie Lee. (2016, February 17). OceanLotus for OS X - an Application Bundle Pretending to be an Adobe Flash Update. Retrieved July 5, 2017.

[4] Thomas Reed. (2016, March 31). Bypassing Apple's Gatekeeper. Retrieved July 5, 2017.

[5] Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.

## Defense

Other tools should be used to supplement Gatekeeper's functionality. Additionally, system settings can prevent applications from running that haven't been downloaded through the Apple Store which can help mitigate some of these issues.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
