---
id: c21a0cdc-15f1-495f-931b-1e994e88f310
name: Build a Password List for Online Dictionary Attack
type: procedure
verified: true
submitted: true
created_at: '2020-03-18T23:35:23.678761+00:00'
updated_at: '2023-05-25T19:45:40.591068+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Enumeration]]'
- '[[password cracking]]'
commands:
- '[[CEWL Generate a Password List Using a Website''s Content]]'
- '[[Mutate a Wordlist by Appending a Digits]]'
---

# Build a Password List for Online Dictionary Attack

**Status**: ✓ Verified

## Summary

Build a custom wordlist of potential passwords using contextual information to minimize network traffic. Brute forcing passwords over the network is slow and noisy, making lists like rockyou unfit. 

## Description

# Description

Build a custom wordlist of potential passwords using contextual information to minimize network traffic. Brute forcing passwords over the network is slow and noisy, making lists like rockyou unfit.

# Instructions

This procedure will step through a number of strategies for building password lists, which when combined should make a tailored list suitable for online brute force attacks.

## Popular  Passwords

Large password lists are useful for offline brute forcing, but aren't viable when brute forcing over the network due to traffic. It's best to find a curated list of the top passwords rather than something on the scale of rockyou. A good option would be either the 10-million-password-list-top-100.txt or 10-million-password-list-top-500.txt, both available from [SecLists via GitHub](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials).

## Usernames

Lazy administrators may set a user's password to be the username, leaving it up to users to change it themselves. It's always worth including usernames in password lists for this reason.

## cEWL Lists

Use cEWL to crawl any websites related to the target for potential passwords.

**Command** ([[CEWL Generate a Password List Using a Website's Content]]):

```bash
cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
```

## Mutating Wordlists (Optional)

Mutating a wordlist is useful when the password policy is known. For example, if each password must have a digit, many users will simply append one. This tactic should be used sparingly, as  it grows lists exponentially.

**Command** ([[Mutate a Wordlist by Appending a Digits]]):

```bash
hashcat -a 6 --stdout $_WORDLIST ?d > $_WORDLIST.mutated
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[CEWL Generate a Password List Using a Website's Content]]
- [[Mutate a Wordlist by Appending a Digits]]

## Tags

- [[Enumeration]]
- [[password cracking]]
