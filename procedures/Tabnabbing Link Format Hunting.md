---
id: c0054e50-61e6-4dd7-9795-3e3a61c8c218
name: Tabnabbing Link Format Hunting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.585018+00:00'
updated_at: '2023-04-06T03:56:40.600554+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
tags:
- '[[How to hunt for it]]'
- '[[Tabnabbing]]'
commands:
- '[[Link with target blank]]'
- '[[Link with target blank]]'
---

# Tabnabbing Link Format Hunting

## Summary

Tabnabbing is a type of phishing attack that targets users who keep multiple tabs open in their browser. The attacker waits for the user to switch to a different tab, and then replaces the content of the original tab with a fake login page or other malicious content. This procedure focuses on hunti

## Description

# Description

Tabnabbing is a type of phishing attack that targets users who keep multiple tabs open in their browser. The attacker waits for the user to switch to a different tab, and then replaces the content of the original tab with a fake login page or other malicious content. This procedure focuses on hunting for Tabnabbing attacks by analyzing link formats. By identifying links that have suspicious or unexpected formats, security teams can detect potential Tabnabbing attacks before they occur.

Technically, Tabnabbing works by using JavaScript to detect when a user has switched tabs, and then modifying the content of the original tab. This procedure looks for links that contain JavaScript code or other unexpected elements that could be used to trigger a Tabnabbing attack.

The business value of this procedure is that it helps organizations protect their users from phishing attacks and other types of social engineering. By detecting and preventing Tabnabbing attacks, organizations can reduce the risk of data theft, financial loss, and reputational damage.

## Requirements

1. Access to web traffic logs or network traffic analysis tools

1. Knowledge of common link formats used in your organization

1. Understanding of JavaScript and other web programming languages

## Defense

1. Educate users about the risks of Tabnabbing and other types of phishing attacks

1. Use browser extensions or other tools to block JavaScript and other potentially malicious content

1. Implement multi-factor authentication and other security measures to reduce the impact of successful Tabnabbing attacks

## Objectives

1. Identify links that have suspicious or unexpected formats

1. Detect potential Tabnabbing attacks before they occur

# Instructions

1. To add a link to your HTML page, you can use the anchor tag <a>. The href attribute specifies the URL of the page the link goes to. The target attribute specifies where to open the linked document. The rel attribute specifies the relationship between the current document and the linked document.

**Code**: [[<a href="..." target="_blank" rel="" />  
or
<a hr]]

> The first link format includes the rel attribute, which can be used to specify the relationship between the current document and the linked document. The second link format does not include the rel attribute. When the target attribute is set to "_blank", the linked document will open in a new browser window or tab.

**Command** ([[Link with target blank]]):

```bash
<a href="..." target="_blank" rel="" />
```

**Command** ([[Link with target blank]]):

```bash
<a href="..." target="_blank" />
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]

## Commands Used

- [[Link with target blank]]
- [[Link with target blank]]

## Tags

- [[How to hunt for it]]
- [[Tabnabbing]]
