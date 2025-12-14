---
tags:
  - cache-control
  - browser-cache
  - sensitive-data-disclosure
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:18.205Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6d205da0-f648-49e6-b367-8900437e515a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Access-Cached-Account-Information-Post-Logout

## Summary

This procedure exploits a cache control vulnerability on the Nextcloud account management page (https://apps.nextcloud.com/account/) by logging in to load sensitive user data into the browser cache, logging out to end the session, and then using the browser's back button to access the cached content without re-authentication, resulting in unauthorized disclosure of personal information such as names and email addresses.

## Description

The vulnerability stems from the absence of proper Cache-Control headers (e.g., no-cache, no-store) on authenticated pages, allowing browsers to cache sensitive content. In a typical scenario, an attacker with temporary access to a shared computer or in a scenario where a user forgets to clear cache can retrieve PII post-logout. This leads to privacy violations and potential GDPR non-compliance, especially in multi-user environments. The procedure requires only valid credentials for initial access and a standard browser, with no advanced tools needed. Expected outcomes include viewing cached user details, highlighting risks of improper session management.

## Requirements

1. Valid Nextcloud account credentials (username and password)
2. Standard web browser with caching enabled (e.g., Chrome, Firefox)
3. Direct internet access to https://apps.nextcloud.com/account/

## Defense

Defensive measures and detection strategies:

- Implement strict Cache-Control headers (e.g., Cache-Control: no-cache, no-store, must-revalidate) on all authenticated pages to prevent caching of sensitive data
- Use Pragma: no-cache and Expires: 0 headers for additional browser compatibility
- Redirect to non-cacheable pages post-logout and invalidate client-side state
- Monitor for anomalous access patterns, such as repeated back-button navigations in logs (though client-side, server logs may show session anomalies)
- Educate users on clearing browser cache and history in shared environments

## Objectives

1. Load and cache sensitive account information during an authenticated session
2. Terminate the session via logout while preserving cache
3. Retrieve and disclose cached data without re-authentication to demonstrate privacy risks

## Instructions

### Step 1: Login and Load Account Page

**Context**: Authenticate to populate the browser cache with sensitive page content.

Navigate to https://apps.nextcloud.com/account/ and enter credentials.

> Upon successful login, the account dashboard will display, caching the HTML content including user details.

### Step 2: Verify Sensitive Data Visibility

**Context**: Confirm the presence of PII to ensure it's cached.

Inspect the page for first name, last name, email, and other details.

> The page source or rendered content will show the sensitive information, which the browser retains in its history and cache.

### Step 3: Perform Logout

**Context**: End the server-side session but rely on client-side caching persistence.

Click the logout button to initiate session termination.

> The browser redirects to a logged-out state, but the back button can still access the local cache.

### Step 4: Use Browser Back Button

**Context**: Exploit the cache to reload the previous page without server interaction.

Press the back button in the browser navigation.

> The cached account page loads locally, bypassing any server checks.

### Step 5: Confirm Data Disclosure

**Context**: Validate that sensitive information is still accessible.

Review the reloaded page for unchanged PII.

> If successful, names and email remain visible, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cache-control
- browser-cache
- sensitive-data-disclosure
- nextcloud
- privacy-violation
