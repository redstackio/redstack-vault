---
id: ac-yelp-idor-locid-001
tags:
  - idor
  - web
  - privacy
  - location-data
  - yelp
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Yelp-Login-and-Profile-Access]]'
  - '[[procedures/Intercept-Yelp-Edit-Request-with-Burp]]'
  - '[[procedures/Modify-locid-for-IDOR-Exploitation]]'
  - '[[procedures/Forward-Modified-Request-to-View-Locations]]'
step_count: 5
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.176Z'
description: >-
  Multi-stage exploitation of an Insecure Direct Object Reference (IDOR)
  vulnerability in Yelp's profile location editing endpoint to unauthorizedly
  view other users' saved locations via manipulation of the locid parameter.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Yelp IDOR in locid Parameter to Access Other Users' Profile Locations

Multi-stage attack chain demonstrating the exploitation of an IDOR vulnerability in Yelp's profile location editing endpoint, allowing unauthorized access to other users' saved locations through parameter manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login to Yelp] --> B[Navigate to Profile Locations]
    B --> C[Intercept Edit Request]
    C --> D[Modify locid Parameter]
    D --> E[Forward Request and View Data]

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

- Web platform (Yelp website)
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to yelp.com

### Initial Access Requirements

- Valid Yelp account credentials
- Network position: External attacker with authenticated session
- Prior access needed: None, but authenticated session required

## Detailed Attack Procedures

### Step 1: Login to Yelp
procedure: [[procedures/Yelp-Login-and-Profile-Access]]

**Objective**: Authenticate to Yelp to establish a session for accessing profile features.

**Instructions**: Access the main login page at https://www.yelp.com/ and enter valid credentials to log in.

**Expected Output**: Successful login redirect to the user dashboard.

**Success Indicators**:
- Authenticated session established
- Access to personal profile granted

### Step 2: Navigate to Profile Locations Page
procedure: [[procedures/Yelp-Login-and-Profile-Access]]

**Objective**: View the user's saved locations to prepare for interception.

**Instructions**: After login, navigate to https://www.yelp.com/profile_location to load the saved locations page.

**Expected Output**: Display of the authenticated user's saved locations.

**Success Indicators**:
- Profile locations page loads successfully
- List of personal locations visible

### Step 3: Intercept Edit Request with Burp Suite
procedure: [[procedures/Intercept-Yelp-Edit-Request-with-Burp]]

**Objective**: Capture the edit request for a location to enable parameter modification.

**Instructions**: Configure Burp Suite as a proxy, click the edit button on a location, and intercept the GET request to /profile_location/add_or_edit?nonce=<nonce>&locid=<locid>.

**Expected Output**: Intercepted request visible in Burp Suite's proxy tab.

**Success Indicators**:
- Request intercepted without errors
- locid parameter present in the query string

### Step 4: Modify locid Parameter for IDOR Exploitation
procedure: [[procedures/Modify-locid-for-IDOR-Exploitation]]

**Objective**: Alter the locid to reference another user's location, exploiting the IDOR.

**Instructions**: In the intercepted request, replace the locid value with one from another account, such as wPhD_XkXv2z4Njqekn-sfg or yqLLfgos2xWB-Y9miJ8YcQ.

**Expected Output**: Modified request ready for forwarding.

**Success Indicators**:
- locid successfully changed to target value
- No immediate server rejection

### Step 5: Forward Modified Request to View Locations
procedure: [[procedures/Forward-Modified-Request-to-View-Locations]]

**Objective**: Send the tampered request to disclose the target user's locations.

**Instructions**: Forward the modified GET request through Burp Suite to the endpoint, observing the response.

**Expected Output**: Server response displaying the targeted user's profile locations.

**Success Indicators**:
- Unauthorized locations displayed
- Personal data (addresses) leaked

## Attack Chain Summary

### Key Achievements

1. Successful authentication and navigation to vulnerable endpoint
2. Interception and manipulation of locid parameter via Burp Suite
3. Unauthorized disclosure of other users' saved location data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
