---
tags:
  - measurement
  - timing
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.790Z'
sub_techniques: []
id: 41846a0c-8cbb-4320-983a-9d0c323451da
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Measure-Single-Request-Response-Time

## Summary

This procedure measures the response time for a single POST request with the large Unicode payload to quantify the normalization delay.

## Description

Repeat the payload submission using Burp Suite and observe the timing. On Windows, this averages 4.4 seconds due to inefficient NFKC handling of large invalid Unicode strings in UsernameField.

## Requirements

1. Vulnerable Django server running
2. Burp Suite with captured payload request

## Defense

Defensive measures and detection strategies:

- Profile and optimize normalization routines
- Implement timeouts for form processing
- Monitor response times for anomalies

## Objectives

1. Validate delay per request
2. Baseline for concurrent impact assessment
3. Confirm vulnerability presence

## Instructions

### Step 1: Repeat Payload Submission

**Context**: Send the modified request multiple times.

In Burp Repeater, send the payload request 5-10 times, noting the timing for each.

> Expected output: Each request takes approximately 4.4 seconds, shown in Burp's timing panel.

### Step 2: Analyze Timing

**Context**: Calculate average delay.

Review Burp logs or use built-in stats to average response times.

> Confirm delays are consistent and significantly longer than normal requests (<1 second).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- measurement
- timing
- dos
