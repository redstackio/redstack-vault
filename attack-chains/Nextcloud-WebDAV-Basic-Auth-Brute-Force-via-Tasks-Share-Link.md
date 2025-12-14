---
tags:
  - nextcloud
  - webdav
  - brute-force
  - authentication-bypass
  - account-takeover
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-Private-Share-Link-from-Nextcloud-Tasks]]'
  - '[[procedures/Capture-and-Decode-WebDAV-Auth-Request-with-Burp-Suite]]'
  - '[[procedures/Prepare-Brute-Force-Payloads-for-Basic-Auth]]'
  - '[[procedures/Execute-Password-Brute-Force-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:43.029Z'
description: >-
  A multi-stage attack exploiting the lack of rate limiting on Basic
  Authentication for WebDAV requests in Nextcloud, allowing brute force password
  guessing to achieve account takeover via a private Tasks share link.
skill_level: intermediate
impact_level: high
id: 28d50ece-c934-4b4d-a8ed-c42dc97e3af4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Nextcloud WebDAV Basic Auth Brute Force via Tasks Share Link

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of rate limiting on Basic Authentication headers for WebDAV requests in Nextcloud. An attacker with access to a private share link from the Tasks feature can extract the username from the URL, capture the authentication request, and perform unrestricted brute force attacks to guess passwords, resulting in full account takeover and unauthorized access to the victim's Nextcloud instance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Obtain Share Link] --> B[Capture Auth Request]
    B --> C[Prepare Payloads]
    C --> D[Brute Force Attack]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Nextcloud instance with Tasks app enabled
- WebDAV services accessible (e.g., /remote.php/dav/ endpoints)
- No rate limiting on Basic Auth for WebDAV

### Initial Access Requirements

- Access to a valid Nextcloud account to generate a private Tasks share link (or social engineering to obtain one)
- Network access to the target Nextcloud host
- Burp Suite proxy configured in the browser

## Detailed Attack Procedures

### Step 1: Obtain Private Share Link
procedure: [[procedures/Obtain-Private-Share-Link-from-Nextcloud-Tasks]]

**Objective**: Extract the target username from a private Tasks share link to initiate the authentication prompt.

**Instructions**: Log in to the target Nextcloud instance, navigate to the Tasks section, create or access a task, and generate a private share link. The link will expose the username in the URL path.

**Expected Output**: A URL like `https://<host>/remote.php/dav/calendars/<username>/<calendar-id>/`.

**Success Indicators**:
- Username visible in the URL (e.g., ha.ckitbharat3@gmail.com)
- Link prompts for credentials when opened in a new browser

### Step 2: Capture and Decode Auth Request
procedure: [[procedures/Capture-and-Decode-WebDAV-Auth-Request-with-Burp-Suite]]

**Objective**: Intercept the failed authentication request to the WebDAV endpoint and decode the Basic Auth header to confirm the username.

**Instructions**: Configure your browser to proxy through Burp Suite, open the private link, enter the username and a random password, and capture the HTTP request. Decode the Base64-encoded Authorization header to reveal the username:password format.

**Expected Output**: Decoded header showing `username:randompassword`, with HTTP 401 response.

**Success Indicators**:
- Request intercepted at WebDAV endpoint (e.g., /remote.php/dav/calendars/...)
- Username confirmed from decoded header

### Step 3: Prepare Brute Force Payloads
procedure: [[procedures/Prepare-Brute-Force-Payloads-for-Basic-Auth]]

**Objective**: Generate a list of Base64-encoded Authorization headers using the known username and potential passwords for the brute force attack.

**Instructions**: Create a wordlist of common passwords, prepend the username to each (e.g., `ha.ckitbharat3@gmail.com:password`), and encode the results as Base64 to form valid Basic Auth headers.

**Expected Output**: A payload list like `Authorization: Basic aGEuY2tpdGJoYXJhdDNAZ21haWwuY29tOnBhc3N3b3Jk`.

**Success Indicators**:
- Payload list ready with 100+ entries
- Each payload correctly formatted for Basic Auth

### Step 4: Execute Brute Force Attack
procedure: [[procedures/Execute-Password-Brute-Force-with-Burp-Intruder]]

**Objective**: Launch the brute force attack to guess the correct password and gain authenticated access.

**Instructions**: Send the captured request to Burp Intruder, mark the password section in the Authorization header as the payload position, load the Base64-encoded payload list, and start the attack. Monitor for successful responses.

**Expected Output**: HTTP 200 response on successful authentication, indicating access to the calendar or account.

**Success Indicators**:
- HTTP 200 status for a payload
- Access to WebDAV resources (e.g., calendar data)
- Full account takeover confirmed by navigating to the Nextcloud dashboard

## Attack Chain Summary

### Key Achievements

1. Exposed username via private Tasks share link
2. Unrestricted brute force on WebDAV Basic Auth due to no rate limiting
3. Achieved full Nextcloud account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---

*Last updated: 2023-10-01T00:00:00Z*
