---
id: fa71bbc5-8270-40fe-9495-203ca167fe95
name: CSRF AutoSubmit HTML POST
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.169353+00:00'
updated_at: '2023-04-10T20:21:25.450249+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[HTML POST - AutoSubmit - No User Interaction]]'
- '[[Payloads]]'
---

# CSRF AutoSubmit HTML POST

## Summary

This procedure involves exploiting a user's trust in a website to execute unauthorized actions on their behalf. The attacker crafts a malicious HTML POST form with a hidden input field containing the desired payload. When the user visits the attacker's website, the form is automatically submitted t

## Description

# Description

This procedure involves exploiting a user's trust in a website to execute unauthorized actions on their behalf. The attacker crafts a malicious HTML POST form with a hidden input field containing the desired payload. When the user visits the attacker's website, the form is automatically submitted to the target website, without the user's knowledge or consent. This can lead to a wide range of malicious activities, such as changing the user's settings or making unauthorized purchases.

## Requirements

1. Ability to craft and host a malicious HTML form.

1. Victim user must be authenticated to the target website.

## Defense

1. Implement CSRF tokens on the target website to validate the origin of the request.

1. Use SameSite cookies to prevent CSRF attacks from other domains.

1. Educate users on the risks of clicking on links or submitting forms from untrusted sources.

## Objectives

1. Execute unauthorized actions on behalf of the victim user.

1. Gain access to sensitive information.

1. Cause damage to the target system or organization.

# Instructions

1. Craft a malicious HTML form with the desired payload.

**Code**: [[<form id="autosubmit" action="http://www.example.c]]

> The HTML form should contain a hidden input field with the desired payload, and should be submitted automatically using JavaScript.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

## Tags

- [[Cross-Site Request Forgery]]
- [[HTML POST - AutoSubmit - No User Interaction]]
- [[Payloads]]
