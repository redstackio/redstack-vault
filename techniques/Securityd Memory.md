---
id: ced5b176-7587-430f-ab87-76d3e9ab20fa
name: Securityd Memory
type: technique
mitre_id: T1167
mitre_url: null
created_at: '2019-08-28T21:17:44.916438+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Securityd Memory

**MITRE ID**: T1167

## Description

In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords. [1] [2] Apple’s securityd utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an attacker need only iterate over the other values to unlock the final password. [1]If an adversary can obtain root access (allowing them to read securityd’s memory), then they can scan through memory to find the correct sequence of keys in relatively few tries to decrypt the user’s logon keychain. This provides the adversary with all the plaintext passwords for users, WiFi, mail, browsers, certificates, secure notes, etc. [1] [3]

# Footnotes

[1] Juuso Salonen. (2012, September 5). Breaking into the OS X keychain. Retrieved July 15, 2017.

[2] Alex Rymdeko-Harvey, Steve Borosh. (2016, May 14). External to DA, the OS X Way. Retrieved July 3, 2017.

[3] Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July 3, 2017.

[4] Patrick Wardle. (2017, January 1). Mac Malware of 2016. Retrieved September 21, 2018.

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
