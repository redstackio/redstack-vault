---
id: proc-grab-prepare-target-001
tags:
  - target-prep
  - phone-enumeration
type: procedure
tools:
  - '[[tools/Custom-CSharp-OTP-Tool]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Identity Information]]'
updated_at: '2025-12-14T17:30:27.430Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Prepare-Target-Phone-Number-for-OTP-Brute-Force

## Summary

This procedure configures a custom tool with the victim's phone number and country code to target the Grab App's OTP endpoints for automated brute-force attacks.

## Description

Using a custom C# application, input the target's phone number (e.g., 380xxxxxxxxx for Ukraine with UA country code, omitting the + sign) to initialize connections to the vulnerable API endpoints: https://p.grabtaxi.com/api/passenger/v2/profiles/activationsms for OTP resends and https://p.grabtaxi.com/api/passenger/v2/profiles/activate for code validation. This step prepares the attack by simulating the login initiation without triggering defenses, leveraging the app's global registration allowance. The tool handles HTTP POST requests with JSON payloads containing phone details; outcomes include readiness for cyclic brute-forcing across the 0000-9999 OTP space.

## Requirements

1. Custom C# tool compiled with .NET 4.0
2. Victim's phone number and country code (2-letter ISO)
3. Network access to Grab API (no auth required for initial requests)
4. Basic understanding of API payloads for phone validation

## Defense

Defensive measures and detection strategies:

- Validate phone numbers against known patterns and geolocations
- Log and alert on repeated activation requests from single IP
- Enforce CAPTCHA or device fingerprinting on login attempts

## Objectives

1. Initialize tool targeting for specific victim account
2. Confirm API accessibility without blocks
3. Set up for efficient OTP cycling

## Instructions

### Step 1: Launch Custom Tool

**Context**: Start the C# application to access input interface.

Compile and run the tool using Visual Studio or .NET runtime (requires .NET 4.0).

> Source code includes HTTP client for API calls; launch via executable or debug mode.

### Step 2: Input Phone Details

**Context**: Enter target information to prepare payloads.

In the tool's UI, provide the phone number with country code (e.g., UA380123456789).

> Tool validates format and constructs JSON: {"country": "UA", "phone_number": "380123456789"}; logs confirmation.

### Step 3: Verify Endpoint Readiness

**Context**: Test initial connection to ensure no immediate restrictions.

Tool sends a preliminary request to activationsms endpoint.

> Expected: 200 OK response or cooldown message; no error indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-CSharp-OTP-Tool]]

## Tags

- target-prep
- phone-enumeration
