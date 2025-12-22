---
id: tool-custom-csharp-otp-001
url: ''
tags:
  - brute-force
  - automation
  - api-client
type: tool
verified: false
platforms:
  - Windows
  - .NET
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.415Z'
validated: true
submitted: true
---
# Custom-CSharp-OTP-Tool

**Status**: Unverified

## Overview

A custom C# tool built with .NET 4.0 to automate brute-force attacks on Grab App's OTP login by cycling guesses and resends, targeting the /activate and /activationsms endpoints.

## Description

This Windows executable uses HttpClient for API interactions, implementing a loop to attempt 3 OTP codes per 30-second cycle, resending on failure to exploit weak limits. Input via UI: phone number and country code; outputs logs and session on success. Designed for persistence over hours, it covers 4-digit space efficiently; source available in original report for customization.

## Features

- Feature 1: Automated 30s delay and 3-attempt cycles per OTP
- Feature 2: JSON payload construction for phone/OTP submission
- Feature 3: Logging of attempts and success detection via response codes

## Installation

### Requirements

- .NET Framework 4.0 or later
- Visual Studio for compilation if modifying source

### Install Commands

```bash
# Compile from source
# Use Visual Studio: Build > Build Solution
# Or run pre-built exe
```

## Basic Usage

```bash
# Launch GUI exe; enter phone, click Start
OTPBruteForce.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| Fixed Codes | Pre-set OTPs like 1056-1058; modifiable in code |
| Country Code | 2-letter input (e.g., UA) |

## Examples

### Example 1: Basic Usage

Run tool, input UA380123456789, start; monitors console for progress.

### Example 2: Advanced Usage

Modify source to vary OTP range: Edit loop in C# to increment from 0000-9999 systematically.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Repeated POSTs to OTP endpoints from single IP
- Pattern of 3 failures followed by resend
- Non-mobile User-Agent in requests

## Related Procedures


## Related Tools

- [[tools/Burp-Suite-Intruder]]
- [[tools/Hydra]]

## References

- Related resources: Original HackerOne report source code
