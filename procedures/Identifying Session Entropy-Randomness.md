---
id: c5ae670d-8608-4645-87d4-d033e8eee6d8
name: Identifying Session Entropy/Randomness
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T14:20:51.090848+00:00'
updated_at: '2023-05-26T01:11:24.355359+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Session Entropy]]'
- '[[Session Management]]'
- '[[Session Randomness]]'
- '[[Web Applications]]'
---

# Identifying Session Entropy/Randomness

**Status**: ✓ Verified

## Summary

Session entropy is the randomness of a session identifier. Randomness can be tested by sampling the session identifiers using sequencer module in Burp Suite. 

## Description

# Description

Session entropy is the randomness of a session identifier. Randomness can be tested by sampling the session identifiers using sequencer module in Burp Suite.

# 

# Instructions

# 

1. Enter the login credentials in the browser

2. Intercept the login request

3. Right-click and send the request to sequencer

4. In the token location, select cookie option and the Session ID

5. Click on Start Live Capture to start capturing the tokens. Once enough requests are made, click on Analyze now.

6. The tokens are then analyzed and overall result can be observed. In the below screenshot, randomness of the session identifier is good.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Session Entropy]]
- [[Session Management]]
- [[Session Randomness]]
- [[Web Applications]]
