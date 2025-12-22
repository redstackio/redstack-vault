---
id: proc-access-twitter-tweets
tags:
  - twitter-ads
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:25.371Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Twitter-Ads-Tweets-Page

## Summary

This procedure outlines logging into the Twitter Ads platform and navigating to the tweets management page for a specific ad account, serving as the entry point for exploiting vulnerabilities in tweet-related features.

## Description

In the context of the stored XSS attack on ads.twitter.com, accessing the tweets page is the initial step to reach the vulnerable compose feature. This requires valid credentials for an ad account with tweet management permissions. The procedure assumes standard web navigation and targets the URL structure https://ads.twitter.com/accounts/{account_id}/tweets. Expected outcomes include loading the interface where scheduled and posted tweets are listed, enabling further actions like composition.

## Requirements

1. Valid Twitter credentials with access to an ad account.
2. Permissions to view and manage tweets in the ad account.
3. Web browser with JavaScript enabled.

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit ad account access.
- Monitor login attempts and unusual navigation patterns in ad platform logs.

## Objectives

1. Establish authenticated access to the vulnerable tweets interface.
2. Prepare for payload injection without triggering alerts.
3. Ensure the session remains active for subsequent steps.

## Instructions

### Step 1: Log In to Twitter Ads

**Context**: Authenticate to the platform to gain access to ad accounts.

Navigate to https://ads.twitter.com and log in with your Twitter credentials associated with the target ad account.

> Upon successful login, the dashboard displays available ad accounts.

### Step 2: Select Ad Account and Navigate to Tweets

**Context**: Target the specific ad account and load the tweets management section.

Select the ad account from the list, then click on the 'Tweets' tab or navigate directly to https://ads.twitter.com/accounts/{account_id}/tweets, replacing {account_id} with the actual ID (e.g., 18-digit numeric ID).

> The page loads with a list of tweets and a 'Compose Tweet' button, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- twitter-ads
- web-access
