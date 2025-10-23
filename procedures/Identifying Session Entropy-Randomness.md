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







![5dcf8767-ac1f-4de8-ac29-5441694bcf23.png](_assets/images/Mash/5dcf8767-ac1f-4de8-ac29-5441694bcf23.png)









2. Intercept the login request







![57c19602-e8b5-4664-860b-fbdad621afc0.png](_assets/images/Mash/57c19602-e8b5-4664-860b-fbdad621afc0.png)







3. Right-click and send the request to sequencer





![02d52c85-1631-4fc8-ae94-75ca66f3fdf7.png](_assets/images/Mash/02d52c85-1631-4fc8-ae94-75ca66f3fdf7.png)









4. In the token location, select cookie option and the Session ID







![a0b0642d-fb9c-4d6f-8c96-49608d5d89e4.png](_assets/images/Mash/a0b0642d-fb9c-4d6f-8c96-49608d5d89e4.png)









5. Click on Start Live Capture to start capturing the tokens. Once enough requests are made, click on Analyze now.





![36ceebc9-14e5-442f-abfc-b468893bfb81.png](_assets/images/Mash/36ceebc9-14e5-442f-abfc-b468893bfb81.png)







6. The tokens are then analyzed and overall result can be observed. In the below screenshot, randomness of the session identifier is good.





![712f1a1c-1186-4b42-823b-ac251234681b.png](_assets/images/Mash/712f1a1c-1186-4b42-823b-ac251234681b.png)













## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Session Entropy]]
- [[Session Management]]
- [[Session Randomness]]
- [[Web Applications]]


