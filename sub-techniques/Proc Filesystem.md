---
id: 15e6e430-6f5b-42c9-adad-c49af0e53d4f
name: Proc Filesystem
type: sub-technique
mitre_id: T1003.007
mitre_url: null
created_at: '2023-04-06T00:31:25.841241+00:00'
updated_at: '2023-04-06T00:31:25.841241+00:00'
parent_technique: '[[Credential Dumping|T1003 - Credential Dumping]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Proc Filesystem

**MITRE ID**: T1003.007

**Parent Technique**: [[Credential Dumping|T1003 - Credential Dumping]]

This is a sub-technique of T1003 - Credential Dumping.

## Summary

Adversaries may gather credentials from information stored in the Proc filesystem or <code>/proc</code>. The Proc filesystem on Linux contains a great deal of information regarding the state of the running operating system. Processes running with root privileges can use this facility to scrape live 

## Description

Adversaries may gather credentials from information stored in the Proc filesystem or <code>/proc</code>. The Proc filesystem on Linux contains a great deal of information regarding the state of the running operating system. Processes running with root privileges can use this facility to scrape live memory of other running programs. If any of these programs store passwords in clear text or password hashes in memory, these values can then be harvested for either usage or brute force attacks, respectively.

This functionality has been implemented in the MimiPenguin(Citation: MimiPenguin GitHub May 2017), an open source tool inspired by Mimikatz. The tool dumps process memory, then harvests passwords and hashes by looking for text strings and regex patterns for how given applications such as Gnome Keyring, sshd, and Apache use memory to store such authentication artifacts.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
