---
id: e4f7aca1-c140-41ee-9dd0-f7f5b83c2602
name: http-dos-using-slowloris
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T18:17:44.970363+00:00'
updated_at: '2023-05-26T01:23:52.034781+00:00'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Network Denial of Service]]'
sub_techniques: []
tags:
  - dos
  - web-applications
commands:
  - '[[commands/git-clone-slowloris-repository]]'
  - '[[commands/python-run-slowloris-attack]]'
platforms:
  - Web
tools:
  - '[[tools/slowloris]]'
skill_level: beginner
impact_level: high
detection_risk: high
validated: true
---

# HTTP DoS Using Slowloris

## Summary

This procedure demonstrates how to perform a Denial of Service (DoS) attack on a web server using the Slowloris tool, which opens multiple incomplete HTTP connections to exhaust the server's connection pool and resources, leading to degraded performance or complete unavailability for legitimate users.

## Description

Slowloris is a low-bandwidth DoS attack tool that targets web servers by initiating numerous partial HTTP requests and keeping them open indefinitely through periodic keep-alive headers. This method is effective against servers with limited connection handling capacity, such as Apache on default configurations, as it ties up server threads without requiring high traffic volume. The attack is particularly useful in scenarios where bandwidth is limited but the goal is to disrupt service availability. It works best against HTTP/1.0 or HTTP/1.1 servers without proper connection limits or timeouts. Prerequisites include a Linux environment with Python 3 and internet access for cloning the repository.

## Requirements

1. Linux machine (e.g., Kali or Ubuntu) with git and Python 3 installed.
2. Network access to the target web server (no authentication required, but firewall rules may block outbound connections).
3. Basic understanding of HTTP protocols and DoS concepts.
4. Target must be a web application vulnerable to connection exhaustion (e.g., Apache without mod_reqtimeout).

## Defense

Defensive measures and detection strategies:

- Implement connection rate limiting and timeouts at the web server level (e.g., Apache's mod_evasive or mod_security).
- Use load balancers or reverse proxies (e.g., NGINX) with connection pooling and IP blacklisting.
- Monitor for unusual patterns of incomplete HTTP requests or high connection counts using tools like Fail2Ban or intrusion detection systems (IDS) such as Snort.
- Enable logging of HTTP headers and connection states to identify keep-alive abuse.

## Objectives

1. Exhaust the target web server's available connections to prevent legitimate access.
2. Demonstrate resource exhaustion without high bandwidth usage.
3. Validate the attack by observing increased response times or service denial.

## Instructions

### Step 1: Clone the Slowloris Repository

**Context**: Obtain the Slowloris tool from its GitHub repository to set up the attack environment. This step ensures you have the latest version of the script.

**Command** ([[commands/git-clone-slowloris-repository]]):
```bash
git clone https://github.com/gkbrk/slowloris.git
```

> This command downloads the Slowloris Python script. Navigate to the cloned directory afterward with `cd slowloris`.

### Step 2: Execute the Slowloris Attack

**Context**: Run the Slowloris script against the target URL to initiate the DoS by opening multiple sockets and sending partial requests. Adjust the number of sockets based on the target's capacity (start with 200-500 for testing).

**Command** ([[commands/python-run-slowloris-attack]]):
```bash
python3 slowloris.py $_TARGET_URL -s $_SOCKET_COUNT
```

> Replace $_TARGET_URL with the victim's website (e.g., https://example.com) and $_SOCKET_COUNT with the desired number of connections (e.g., 300). The script will output progress on socket creation and keep-alive sends. Monitor the target site's responsiveness in another terminal or browser to confirm degradation.

### Step 3: Verify the Attack Impact

**Context**: Observe the effects on the target to confirm success. Use tools like curl or a browser to test load times before and during the attack.

**Instructions**: In a separate terminal, run repeated requests to the target:
```bash
while true; do curl -w "%{time_total} seconds\n" $_TARGET_URL; done
```

> Expected increase in response times or timeouts indicates success. Stop the attack with Ctrl+C once verified.
