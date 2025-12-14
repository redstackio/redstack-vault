---
tags:
  - dos
  - rails
  - action-pack
  - memory-leak
  - object-leak
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-Rails-Routes]]'
  - '[[procedures/Send-Requests-to-Non-Existent-Rails-Controllers]]'
  - '[[procedures/Repeat-Requests-for-Memory-Exhaustion-in-Rails]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.171Z'
description: >-
  A multi-step attack exploiting a vulnerability in Ruby on Rails Action Pack
  that causes unbounded memory growth through requests to non-existent wildcard
  controllers, leading to server resource exhaustion.
skill_level: intermediate
impact_level: high
id: bc420aed-2422-4c57-8ead-4c8e84b24df0
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# DoS via Object Leak in Rails Action Pack Wildcard Routes

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Ruby on Rails Action Pack (versions >=4.0.0 and <5.0.0.beta1) where wildcard routes containing ':controller' lead to object leaks and memory exhaustion via a flawed global caching mechanism.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5-10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Routes] --> B[Request Non-Existent Controllers]
    B --> C[Repeat for Memory Growth]
    C --> D[Resource Exhaustion DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl or browser)

### Target Environment

- Ruby on Rails application (versions >=4.0.0 and <5.0.0.beta1)
- Web server exposing Rails routes
- Wildcard routes configured with ':controller' in routing (e.g., match ':controller(/:action(/:id))', :action => /[^/]+/, :id => /[^/]+/)
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Network access to the target web application
- No credentials needed (public-facing vulnerability)
- Ability to send repeated HTTP requests

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Routes
procedure: [[procedures/Identify-Vulnerable-Rails-Routes]]

**Objective**: Locate routes in the Rails application that use wildcard ':controller' patterns, which are susceptible to the caching flaw.

**Instructions**: Review the application's routing configuration, typically in config/routes.rb, or infer from error responses. Look for patterns like match ':controller(/:action(/:id))' that trigger controller lookup without existence checks.

**Expected Output**: Confirmation of vulnerable route patterns, such as responses indicating controller resolution attempts.

**Success Indicators**:
- Identification of ':controller' in route definitions
- Test request to a known route returns 404 but triggers internal lookup

### Step 2: Send Requests to Non-Existent Controllers
procedure: [[procedures/Send-Requests-to-Non-Existent-Rails-Controllers]]

**Objective**: Trigger the population of the global cache with non-existent controller class names, initiating object leaks.

**Instructions**: Craft HTTP requests to URLs that map to wildcard controllers not present in the application, such as /nonexistentcontroller. Use tools like curl to send GET requests and observe server behavior.

**Expected Output**: Server processes the request, populating the internal cache map with the invalid controller name, but returns a 404 error.

**Success Indicators**:
- 404 response received
- No immediate crash, but subtle increase in memory usage observable via monitoring

### Step 3: Repeat Requests for Memory Exhaustion
procedure: [[procedures/Repeat-Requests-for-Memory-Exhaustion-in-Rails]]

**Objective**: Flood the server with repeated requests to exhaust memory resources through unbounded cache growth.

**Instructions**: Automate multiple requests (e.g., 1000+ iterations) to the same or varied non-existent controllers. Monitor server memory via tools like top or Rails logs for unbounded growth in the controller cache.

**Expected Output**: Progressive memory consumption leading to out-of-memory errors, slowdowns, or server crash.

**Success Indicators**:
- Server memory usage spikes
- Application becomes unresponsive or throws memory-related exceptions
- Logs show repeated controller lookup attempts

## Attack Chain Summary

### Key Achievements

1. Identification of exploitable wildcard routes in Rails Action Pack
2. Triggering of object leaks via non-existent controller requests
3. Achievement of denial of service through resource exhaustion

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
