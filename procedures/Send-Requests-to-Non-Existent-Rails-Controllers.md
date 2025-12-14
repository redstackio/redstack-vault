---
tags:
  - dos
  - rails
  - object-leak
  - cache-abuse
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.159Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d3eb22fa-fc85-4247-a809-06b9e91623a3
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Send-Requests-to-Non-Existent-Rails-Controllers

## Summary

This procedure sends HTTP requests to non-existent controllers in a vulnerable Rails application to trigger the population of the global controller cache, initiating the object leak that precedes memory exhaustion.

## Description

The Action Pack vulnerability causes Rails to attempt loading controller classes for any ':controller' wildcard match, even if the class doesn't exist. Each such request adds an entry to a global hash mapping URL names to attempted class constants, leaking objects into memory without garbage collection. This step exploits that by targeting invalid paths, setting up for repeated exploitation.

## Requirements

1. Confirmed vulnerable wildcard route from prior reconnaissance
2. HTTP client capable of sending GET requests (e.g., curl, browser)
3. Network access to the target application

## Defense

Defensive measures and detection strategies:

- Apply patches for Rails 4.1 and 4.2
- Configure routes to avoid open wildcards or add existence checks
- Log and alert on high volumes of 404s for controller paths
- Use memory monitoring tools to detect cache growth

## Objectives

1. Trigger initial cache population with invalid controller entries
2. Verify object leak without crashing the server
3. Observe subtle memory increase as precursor to DoS

## Instructions

### Step 1: Craft Invalid Controller Request

**Context**: Select a path that matches the wildcard but points to a non-existent controller.

Send a simple GET request:

```http
GET /nonexistentcontroller HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0
```

> The server will attempt to resolve 'NonexistentcontrollerController', adding it to the cache and returning a 404.

### Step 2: Vary Controller Names

**Context**: Test multiple unique invalid names to build cache entries.

Repeat with different paths like /fake1, /fake2:

```http
GET /fake1 HTTP/1.1
Host: target.com
```

> Each unique name populates a new cache entry, confirming the leak mechanism.

### Step 3: Monitor Initial Impact

**Context**: Check server response times and memory via external tools.

After 10-20 requests, query server metrics if accessible (e.g., via New Relic or logs).

> Expect minor memory uptick and consistent 404s without other errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- rails
- object-leak
- cache-abuse
