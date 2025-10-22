---
id: 7a9adb3b-11af-4dc7-b53b-a3fc1c81e9f3
name: Slack API Token Leakage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:52.160581+00:00'
updated_at: '2023-04-06T03:55:52.184799+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[API Key Leaks]]'
- '[[Exploit]]'
- '[[Slack API Token]]'
commands:
- '[[Verify Slack API Authentication]]'
---

# Slack API Token Leakage

## Summary

This procedure involves exploiting leaked Slack API tokens to gain unauthorized access to the target organization's Slack workspace. Slack API tokens are used to authenticate and authorize API requests to Slack, and can be used to perform various actions depending on the scope of the token. Attacke

## Description

# Description

This procedure involves exploiting leaked Slack API tokens to gain unauthorized access to the target organization's Slack workspace. Slack API tokens are used to authenticate and authorize API requests to Slack, and can be used to perform various actions depending on the scope of the token. Attackers can obtain Slack API tokens from various sources such as publicly accessible GitHub repositories, misconfigured servers, or other sources of leaked sensitive information. Once an attacker has obtained a Slack API token, they can use it to read messages, post messages, and perform other actions within the target Slack workspace. This can lead to the theft of sensitive information or the compromise of the target organization's infrastructure.

## Requirements

1. Valid Slack API token

## Defense

1. Ensure that Slack API tokens are properly secured and not leaked through publicly accessible sources

1. Implement access controls and monitoring to detect and prevent unauthorized access to Slack workspaces

1. Regularly review and revoke unused or unnecessary Slack API tokens

## Objectives

1. Gain unauthorized access to the target organization's Slack workspace

1. Read messages and post messages within the target Slack workspace

1. Steal sensitive information or compromise the target organization's infrastructure

# Instructions

1. To test if a Slack API token is valid, run the following command:

**Code**: [[curl -sX POST "https://slack.com/api/auth.test?tok]]

> This command sends a request to Slack's auth.test API endpoint with the provided API token. If the token is valid, the response will include information about the authenticated user and the Slack workspace.

**Command** ([[Verify Slack API Authentication]]):

```bash
curl -sX POST "https://slack.com/api/auth.test?token=xoxp-TOKEN_HERE&pretty=1"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Verify Slack API Authentication]]

## Tags

- [[API Key Leaks]]
- [[Exploit]]
- [[Slack API Token]]
