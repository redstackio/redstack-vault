---
id: eac8518c-3bbf-49ca-afa5-ae25596d6807
name: Tabnabbing Attack with Invalid Noopener Attribute Value and Target Attribute
  Value Contains Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.511190+00:00'
updated_at: '2023-04-06T03:56:40.528253+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[More information about the vulnerability]]'
- '[[Tabnabbing]]'
---

# Tabnabbing Attack with Invalid Noopener Attribute Value and Target Attribute Value Contains Command

## Summary

Tabnabbing is a type of phishing attack where a new tab is opened with a fake login page that looks like a legitimate website. This attack is possible due to a vulnerability in how web browsers handle tab switching. By using an invalid noopener attribute value and target attribute value containing 

## Description

# Description

Tabnabbing is a type of phishing attack where a new tab is opened with a fake login page that looks like a legitimate website. This attack is possible due to a vulnerability in how web browsers handle tab switching. By using an invalid noopener attribute value and target attribute value containing a command, an attacker can execute arbitrary code in the context of the victim's browser. This technique can be used to steal sensitive information, such as login credentials or financial data. It can also be used to install malware or gain access to the victim's system.

 

## Requirements

1. Access to a vulnerable website

1. Knowledge of the target's browsing habits

 

## Defense

1. Use content security policy (CSP) to block inline scripts and restrict the domains from which scripts can be loaded

1. Use the noreferrer attribute in links to prevent phishing attacks

1. Educate users on how to recognize and avoid phishing attacks

 

## Objectives

1. Steal sensitive information

1. Install malware

1. Gain access to the victim's system

 

# Instructions

1. To prevent tabnabbing attacks, always hover over the link to check if it is legitimate before clicking on it. Additionally, ensure that your browser is up to date with the latest security patches.

 



**Code**: [[rel]]



> The attacker takes advantage of the fact that users may have multiple tabs open and may switch between them frequently. When the user switches to a different tab, the attacker's website can change the content of the original tab to display a fake login prompt or other malicious content. This can trick the user into entering sensitive information or downloading malware.

2. Use 'noopener' as the value for the 'rel' attribute in the anchor tag to prevent the newly opened page from being able to access the window.opener property of the opening window.

 



**Code**: [[noopener]]



> When using the target='_blank' attribute in an anchor tag, it is important to add the 'rel' attribute with the value 'noopener' to prevent the newly opened page from being able to access the window.opener property of the opening window. This can prevent potential security vulnerabilities, such as cross-site scripting attacks. If the 'rel' attribute is present but does not have the value 'noopener', it is considered an invalid value and should be corrected.

3. The Target Attribute Value Contains Command is used to identify all elements whose target attribute contains the specified value.

 



**Code**: [[_blank]]



> This command takes one argument:
1. Value: The value that should be contained in the target attribute of the elements to be identified.

Example:
If we want to identify all links that open in a new tab, we can use the following command:
Target Attribute Value Contains '_blank'
This will return all elements whose target attribute contains the value '_blank'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]
- [[User Execution|T1204 - User Execution]]

## Tags

- [[More information about the vulnerability]]
- [[Tabnabbing]]


