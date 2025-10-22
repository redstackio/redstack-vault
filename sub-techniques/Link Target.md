---
id: 215a679c-b732-44b5-a90d-3453649b777c
name: Link Target
type: sub-technique
mitre_id: T1608.005
mitre_url: null
created_at: '2023-04-06T00:31:26.513142+00:00'
updated_at: '2023-04-06T00:31:26.513142+00:00'
parent_technique: '[[Stage Capabilities|T1608 - Stage Capabilities]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Link Target

**MITRE ID**: T1608.005

**Parent Technique**: [[Stage Capabilities|T1608 - Stage Capabilities]]

This is a sub-technique of T1608 - Stage Capabilities.

## Summary

Adversaries may put in place resources that are referenced by a link that can be used during targeting. An adversary may rely upon a user clicking a malicious link in order to divulge information (including credentials) or to gain execution, as in [Malicious Link](https://attack.mitre.org/techniques

## Description

Adversaries may put in place resources that are referenced by a link that can be used during targeting. An adversary may rely upon a user clicking a malicious link in order to divulge information (including credentials) or to gain execution, as in [Malicious Link](https://attack.mitre.org/techniques/T1204/001). Links can be used for spearphishing, such as sending an email accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser. Prior to a phish for information (as in [Spearphishing Link](https://attack.mitre.org/techniques/T1598/003)) or a phish to gain initial access to a system (as in [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002)), an adversary must set up the resources for a link target for the spearphishing link. 

Typically, the resources for a link target will be an HTML page that may include some client-side script such as [JavaScript](https://attack.mitre.org/techniques/T1059/007) to decide what content to serve to the user. Adversaries may clone legitimate sites to serve as the link target, this can include cloning of login pages of legitimate web services or organization login pages in an effort to harvest credentials during [Spearphishing Link](https://attack.mitre.org/techniques/T1598/003).(Citation: Malwarebytes Silent Librarian October 2020)(Citation: Proofpoint TA407 September 2019) Adversaries may also [Upload Malware](https://attack.mitre.org/techniques/T1608/001) and have the link target point to malware for download/execution by the user.

Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure ([Domains](https://attack.mitre.org/techniques/T1583/001)) to help facilitate [Malicious Link](https://attack.mitre.org/techniques/T1204/001). Link shortening services can also be employed. Adversaries may also use free or paid accounts on Platform-as-a-Service providers to host link targets while taking advantage of the widely trusted domains of those providers to avoid being blocked.(Citation: Netskope GCP Redirection)(Citation: Netskope Cloud Phishing)(Citation: Intezer App Service Phishing)

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
