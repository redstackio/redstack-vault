---
id: d9a6e3fc-6319-44f2-a4d9-49953bca2ed8
name: Group Policy Preferences
type: sub-technique
mitre_id: T1552.006
mitre_url: null
created_at: '2023-04-06T00:31:26.550283+00:00'
updated_at: '2023-04-06T00:31:26.550283+00:00'
parent_technique: '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Group Policy Preferences

**MITRE ID**: T1552.006

**Parent Technique**: [[Unsecured Credentials|T1552 - Unsecured Credentials]]

This is a sub-technique of T1552 - Unsecured Credentials.

## Summary

Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts.(Citation: Microsoft GPP 2016)

These group policies are sto

## Description

Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts.(Citation: Microsoft GPP 2016)

These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share and decrypt the password (using the AES key that has been made public).(Citation: Microsoft GPP Key)

The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files:

* Metasploit’s post exploitation module: <code>post/windows/gather/credentials/gpp</code>
* Get-GPPPassword(Citation: Obscuresecurity Get-GPPPassword)
* gpprefdecrypt.py

On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: <code>dir /s * .xml</code>

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
