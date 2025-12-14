---
tags:
  - dos
  - resource-exhaustion
  - mattermost
  - playbook
type: attack_chain
tools:
  - '[[tools/generate-payload.py]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-create-oversized-playbook]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-12-14T10:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-Mattermost-as-Normal-User]]'
  - '[[procedures/Generate-Oversized-Playbook-Payload]]'
  - '[[procedures/Create-Playbook-with-Oversized-Template]]'
  - '[[procedures/Initiate-Playbook-Run-to-Trigger-DoS]]'
step_count: 8
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.510Z'
description: >-
  Multi-stage attack exploiting lack of size validation in Mattermost Playbooks
  to cause server resource exhaustion and denial of service.
id: 744c4ab8-d73a-4939-9036-c84265eb9514
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# DoS via Oversized Playbook Attributes in Mattermost

Multi-stage attack chain demonstrating a complete denial-of-service workflow by exploiting the lack of size validation on playbook attributes in Mattermost, leading to server crash and unavailability for all users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authentication] --> B[Payload Generation]
    B --> C[Playbook Creation]
    C --> D[Run Initiation]
    D --> E[Resource Exhaustion and Crash]
    E --> F[DoS Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#e67e22
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/generate-payload.py]]
- curl

### Target Environment

- Mattermost instance with Playbooks plugin enabled
- Default nginx configuration (50MB request body limit)
- Web access to Mattermost UI and API

### Initial Access Requirements

- Valid normal user credentials (no admin privileges needed)
- Network access to the Mattermost server
- Browser for UI interactions or API tools

## Detailed Attack Procedures

### Step 1: Log in as a Normal User
procedure: [[procedures/Authenticate-to-Mattermost-as-Normal-User]]

**Objective**: Gain authenticated access to the Mattermost platform as a standard user to prepare for API interactions.

**Instructions**: Access the Mattermost web interface and log in with standard user credentials. Extract the authentication token for subsequent API calls.

**Expected Output**: Successful login to the dashboard, with MMAUTHTOKEN available in browser cookies.

**Success Indicators**:
- User dashboard loads
- MMAUTHTOKEN cookie is present in developer tools

### Step 2: Extract Authentication Token
procedure: [[procedures/Authenticate-to-Mattermost-as-Normal-User]]

**Objective**: Obtain the MMAUTHTOKEN for authenticating API requests.

**Instructions**: Use browser developer tools to inspect cookies after login and copy the MMAUTHTOKEN value.

**Expected Output**: Token string extracted, e.g., a long alphanumeric value.

**Success Indicators**:
- Token retrieved without errors
- Token can be used in subsequent requests

### Step 3: Generate Oversized Payload
procedure: [[procedures/Generate-Oversized-Playbook-Payload]]

**Objective**: Create a JSON payload with a 50MB run_summary_template to bypass size limits.

**Instructions**: Run the generate-payload.py script to produce a payload file with 50,000,000 characters in the run_summary_template field.

**Expected Output**: A 'payload.json' file approximately 50MB in size.

**Success Indicators**:
- File generated successfully
- File size confirms ~50MB

### Step 4: Send Payload to Create Playbook
procedure: [[procedures/Create-Playbook-with-Oversized-Template]]

**Objective**: Submit the oversized payload to the Playbooks API to create a malicious playbook.

**Instructions**: Use [[commands/curl-create-oversized-playbook]] to POST the payload to the API endpoint, including authentication headers.

```bash
curl -X POST "http://<domain>/plugins/playbooks/api/v0/playbooks" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=<user-auth-token>" -H "X-CSRF-TOKEN: <csrf-token>"
```

**Expected Output**: HTTP 200 response indicating playbook creation success.

**Success Indicators**:
- Playbook created without rejection
- No size limit errors

### Step 5: Navigate to Playbooks Page
procedure: [[procedures/Create-Playbook-with-Oversized-Template]]

**Objective**: Locate and select the newly created playbook in the UI.

**Instructions**: In the Mattermost web UI, go to the Playbooks section and click on the playbook from step 4 to open its details.

**Expected Output**: Playbook details page loads.

**Success Indicators**:
- Playbook appears in the list
- Details page accessible

### Step 6: Initiate Playbook Run
procedure: [[procedures/Initiate-Playbook-Run-to-Trigger-DoS]]

**Objective**: Start a run of the playbook to process the oversized template and trigger resource exhaustion.

**Instructions**: On the playbook details page, click the 'Run' button and provide a name for the run instance.

**Expected Output**: Run initiation confirmation, followed by server resource spike.

**Success Indicators**:
- Run starts without immediate errors
- Server CPU/memory usage increases

### Step 7: Observe Server Crash
procedure: [[procedures/Initiate-Playbook-Run-to-Trigger-DoS]]

**Objective**: Monitor the impact as the server processes the large template, leading to crash.

**Instructions**: Watch server metrics; the run processing causes high resource consumption.

**Expected Output**: Server crashes after seconds, application becomes unresponsive.

**Success Indicators**:
- Abnormal resource usage
- Server failure and downtime

### Step 8: Confirm Denial of Service
procedure: [[procedures/Initiate-Playbook-Run-to-Trigger-DoS]]

**Objective**: Verify the DoS effect on all users, including post-restart issues.

**Instructions**: Attempt to access the application; after restart, check playbook run pages for failures.

**Expected Output**: Application unavailable; playbook pages show blank screens post-restart.

**Success Indicators**:
- All users experience downtime
- Persistent loading issues after recovery

## Attack Chain Summary

### Key Achievements

1. Successful creation of oversized playbook without validation
2. Triggered server crash via run initiation
3. Achieved full denial of service impacting all users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Impact]]

---

*Last updated: 2023-12-14T10:00:00Z*
