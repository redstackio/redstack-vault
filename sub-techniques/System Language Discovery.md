---
id: 19508ecd-1ad9-4521-90a0-82ea23ca3cc1
name: System Language Discovery
type: sub-technique
mitre_id: T1614.001
mitre_url: null
created_at: '2023-04-06T00:31:26.870592+00:00'
updated_at: '2023-04-06T00:31:26.870592+00:00'
parent_technique: '[[System Location Discovery|T1614 - System Location Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# System Language Discovery

**MITRE ID**: T1614.001

**Parent Technique**: [[System Location Discovery|T1614 - System Location Discovery]]

This is a sub-technique of T1614 - System Location Discovery.

## Summary

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision 

## Description

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities.(Citation: Malware System Language Check)

There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [Query Registry](https://attack.mitre.org/techniques/T1012) and calls to [Native API](https://attack.mitre.org/techniques/T1106) functions.(Citation: CrowdStrike Ryuk January 2019) 

For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language</code> or parsing the outputs of Windows API functions <code>GetUserDefaultUILanguage</code>, <code>GetSystemDefaultUILanguage</code>, <code>GetKeyboardLayoutList</code> and <code>GetUserDefaultLangID</code>.(Citation: Darkside Ransomware Cybereason)(Citation: Securelist JSWorm)(Citation: SecureList SynAck Doppelgänging May 2018)

On a macOS or Linux system, adversaries may query <code>locale</code> to retrieve the value of the <code>$LANG</code> environment variable.

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]
