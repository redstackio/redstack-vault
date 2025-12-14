---
tags:
  - phishing
  - twitter-posting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:31.616Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 57946880-591e-4a28-945f-ab45ce1a431e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Post-and-Execute-Malicious-Link

## Summary

This procedure posts the chained redirect URL as a tweet or DM on Twitter and executes it to confirm the bypass, leading users to forbidden domains without warnings or shortening.

## Description

With the chained URL, posting succeeds because validation sees it as a safe twitter.com/login link. Clicking triggers the full chain: login redirect → analytics redirect → Unicode-resolved forbidden site. Ideal for phishing; requires a Twitter account.

## Requirements

1. Logged-in Twitter account
2. Final chained URL from prior procedure
3. Recipient or public timeline for testing

## Defense

Defensive measures and detection strategies:

- Enhance client-side link scanning for chained redirects and Unicode before posting
- Warn users on clicks to twitter.com/login with external redirects
- Analyze tweet links for encoding anomalies in real-time

## Objectives

1. Successfully post without blocking
2. Execute chain to reach target domain
3. Demonstrate evasion of interstitial warnings

## Instructions

### Step 1: Post the URL

**Context**: Create and submit a tweet with the chained URL.

Log in to Twitter, compose tweet, paste URL, and post.

> Expected: Tweet publishes; URL not shortened to t.co.

### Step 2: Execute and Verify

**Context**: Click the link to test the full chain.

Click in tweet; observe redirects: twitter.com/login → analytics.twitter.com → ddosecrets.com (resolved from Unicode).

> Success if no warning page appears and target loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[Phishing]]
- [[twitter-posting]]
