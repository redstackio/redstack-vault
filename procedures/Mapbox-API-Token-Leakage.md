---
id: 7fc50f5a-1f41-4eb3-a403-d0a21ebc0330
name: Mapbox-API-Token-Leakage
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:52.645022+00:00'
updated_at: '2023-04-06T03:55:52.668068+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/API Key Leaks]]'
  - '[[tags/Exploit]]'
  - '[[tags/Mapbox API Token]]'
commands:
  - '[[commands/mapbox-check-token-validity]]'
  - '[[commands/sketchtool-dump-to-json]]'
  - '[[commands/sketchtool-export-artboards-png]]'
  - '[[commands/mapbox-get-account-tokens]]'
platforms:
  - Linux
  - macOS
  - Web
tools: []
validated: true
---

# Mapbox-API-Token-Leakage

## Summary

This procedure outlines how to identify, validate, and exploit leaked Mapbox API tokens, which authenticate access to Mapbox services like maps, geolocation data, and user information. Tokens prefixed with 'pk.' (public) or 'sk.' (secret) can be found in source code, configuration files, public repositories, or design files such as Sketch documents. Once obtained, attackers can use these tokens for unauthorized access, data exfiltration, or further attacks on integrated systems.

## Description

Mapbox API tokens enable developers to integrate mapping and location services into applications. Leaks occur when tokens are hard-coded in client-side JavaScript, committed to GitHub, or embedded in design prototypes like Sketch files used for app mockups. Public tokens ('pk.') allow read-only access to maps and tiles, while secret tokens ('sk.') grant broader scopes including token management and sensitive data retrieval. Exploiting a leaked token involves validating it against Mapbox's API endpoints, enumerating associated tokens if it's a secret key, and using it to query services for geolocation data or user details. This can lead to reconnaissance on user locations, billing information exposure, or lateral movement if the token authenticates to other cloud services. The procedure assumes the attacker has obtained a potential token through reconnaissance and focuses on verification and exploitation in a red team context.

## Requirements

1. Internet access to reach Mapbox API endpoints (https://api.mapbox.com).
2. A suspected Mapbox API token (starting with 'pk.' or 'sk.' followed by a base64-encoded string).
3. For Sketch file analysis: macOS with Sketch app installed and sketchtool CLI available.
4. Basic command-line tools like curl for API interactions.

## Defense

- Avoid hard-coding API tokens in source code, client-side scripts, or design files; use server-side proxies or short-lived tokens.
- Store tokens in environment variables or secure vaults, never in public repositories.
- Implement regular token rotation (e.g., every 90 days) and monitor for leaks using tools like GitHub secret scanning.
- Scope tokens minimally: public keys for read-only, secret keys only for necessary admin actions.
- Enable logging and alerting on unusual API usage patterns, such as high-volume queries from unknown IPs.

## Objectives

1. Locate and extract potential Mapbox API tokens from target files or repositories.
2. Validate the token's authenticity and scope to confirm usability.
3. Enumerate additional tokens and exploit access to Mapbox services for data collection or further compromise.
4. Demonstrate impact by accessing sensitive geolocation or account data.

## Instructions

### Step 1: Identify Potential Tokens in Source Code or Files

**Context**: Begin by searching for Mapbox token patterns in accessible files, such as JavaScript source code, config files, or public repos. Look for strings starting with 'pk.' or 'sk.' followed by a 60+ character JWT-like token. If tokens are suspected in design files like Sketch (.sketch), use sketchtool to dump or export contents for inspection.

**Command** ([[commands/sketchtool-dump-to-json]]):
```bash
sketchtool dump $_SKETCH_FILE_PATH
```

> This command exports the Sketch file's contents to JSON, allowing grep or manual search for embedded tokens in layers, text, or metadata. Replace $_SKETCH_FILE_PATH with the path to the .sketch file.

**Command** ([[commands/sketchtool-export-artboards-png]]):
```bash
sketchtool export artboards $_SKETCH_FILE_PATH --output=$_OUTPUT_DIR --formats=png
```

> If tokens are visually embedded or in images, export artboards to PNG for OCR analysis (use tools like tesseract separately). This helps in prototype files where devs paste tokens during design.

**Expected Output**: JSON dump with file structure or PNG images of artboards. Search output for 'pk.' or 'sk.' patterns using grep: `grep -r 'pk\.' /path/to/dumped/files`.

### Step 2: Validate the Discovered Token

**Context**: Once a potential token is found, verify its validity by querying the Mapbox tokens API. This confirms if it's active and reveals its scopes without alerting the owner immediately.

**Command** ([[commands/mapbox-check-token-validity]]):
```bash
curl "https://api.mapbox.com/tokens/v2?access_token=$_TOKEN"
```

> This API call returns token details if valid, including scopes and creation date. Use a secret token ('sk.') for full details; public tokens may return limited info.

**Expected Output**: JSON response like {"tokens":[{"id":"abc123","scopes":["styles:read","fonts:read"],"token":"pk.eyJ..."}]}. An invalid token returns 401 Unauthorized.

### Step 3: Enumerate All Tokens Associated with the Account

**Context**: If the token is a secret key ('sk.') with appropriate scopes (e.g., 'tokens:read'), query for all tokens linked to the account. This can reveal additional credentials for broader access or rotation targets.

**Command** ([[commands/mapbox-get-account-tokens]]):
```bash
curl "https://api.mapbox.com/tokens/v2/$_USERNAME?access_token=$_TOKEN"
```

> Replace $_USERNAME with the Mapbox username (often derivable from token metadata or public profiles). This lists all tokens, allowing collection of more keys.

**Expected Output**: JSON array of all account tokens, including their IDs, scopes, and values (if permitted). Success if multiple tokens are returned; failure if 403 Forbidden (insufficient scope).
