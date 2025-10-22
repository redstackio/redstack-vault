---
id: fe5b33e5-57dc-4ddf-80c8-381d235b26f6
name: Keychain
type: technique
mitre_id: T1142
mitre_url: null
created_at: '2019-08-28T21:17:44.954208+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Keychain

**MITRE ID**: T1142

## Description

Keychains are the built-in way for macOS to keep track of users' passwords and credentials for many services and features such as WiFi passwords, websites, secure notes, certificates, and Kerberos. Keychain files are located in ~/Library/Keychains/,/Library/Keychains/, and /Network/Library/Keychains/. [1] The security command-line utility, which is built into macOS by default, provides a useful way to manage these credentials.To manage their credentials, users have to use additional credentials to access their keychain. If an adversary knows the credentials for the login keychain, then they can get access to all the other credentials stored in this vault. [2] By default, the passphrase for the keychain is the user’s logon credentials.

# Detection

Unlocking the keychain and using passwords from it is a very common process, so there is likely to be a lot of noise in any detection technique. Monitoring of system calls to the keychain can help determine if there is a suspicious process trying to access it.

# Mitigation

The password for the user's login keychain can be changed from the user's login password. This increases the complexity for an adversary because they need to know an additional password.

# Footnotes

[1] Wikipedia. (n.d.). Keychain (software). Retrieved July 5, 2017.

[2] Alex Rymdeko-Harvey, Steve Borosh. (2016, May 14). External to DA, the OS X Way. Retrieved July 3, 2017.

[3] Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.

[4] Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.

[5] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

## Defense

The password for the user's login keychain can be changed from the user's login password. This increases the complexity for an adversary because they need to know an additional password.

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
