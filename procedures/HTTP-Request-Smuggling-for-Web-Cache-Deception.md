---
id: 5eebb632-cba1-4e01-94cb-3ea0bd540fc0
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T14:22:22.651619+00:00'
updated_at: '2023-05-26T18:10:27.854878+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
  - web-cache-deception
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# HTTP-Request-Smuggling-for-Web-Cache-Deception

## Summary

This procedure exploits HTTP request smuggling using chunked transfer encoding to perform web cache deception, tricking the front-end cache into storing sensitive backend responses (like API keys) as static resources accessible to other users.

## Description

HTTP request smuggling occurs when the front-end server (e.g., a reverse proxy or load balancer) and backend server interpret HTTP requests differently, allowing an attacker to smuggle malicious requests to the backend. In this scenario, the front-end does not support chunked encoding properly, enabling the attacker to append a smuggled GET request to a legitimate POST. This poisons the web cache by making the backend's sensitive response (e.g., /apikey endpoint) appear as a cacheable static resource, such as an image or CSS file. Subsequent users loading the page inadvertently fetch and expose the sensitive data. This is effective against applications caching static resources without anti-caching headers.

## Requirements

1. Valid user credentials for the target web application.
2. Access to a proxy tool like [[tools/Burp-Suite]] configured to intercept and modify HTTP requests.
3. The target application must have a front-end server that mishandles chunked encoding and caches static resources.
4. Network access to the application's login and account pages.

## Defense

Defensive measures and detection strategies:

- Normalize HTTP requests at the front-end to enforce consistent parsing (e.g., reject ambiguous Transfer-Encoding).
- Implement strict caching policies with anti-caching headers (Cache-Control: no-store, private) on sensitive endpoints.
- Monitor for anomalous requests with chunked encoding or unexpected methods in bodies.
- Use web application firewalls (WAFs) to detect smuggling patterns like invalid chunk sizes.

## Objectives

1. Authenticate to the application and identify cacheable pages without anti-caching protections.
2. Smuggle a request to a sensitive backend endpoint to poison the cache.
3. Verify cache poisoning by observing sensitive data in static resources served to unauthenticated users.
4. Extract the exposed sensitive information, such as an API key.

## Instructions

### Step 1: Authenticate to the Application

**Context**: Log in to establish a valid session, allowing access to account-related endpoints that may be cacheable.

Use [[tools/Burp-Suite]] to intercept the login request. Submit credentials via the login form.

**Expected Output**: Successful login response (e.g., 200 OK with session cookie or token).

### Step 2: Access Account Details and Verify Caching Behavior

**Context**: Navigate to a page that triggers a backend response without anti-caching headers, confirming the cache is vulnerable to poisoning.

Intercept the request to the "Account Details" page using [[tools/Burp-Suite]]. Observe the response headers for lack of Cache-Control: no-cache or similar.

**Expected Output**: Response headers without anti-caching directives, indicating the content may be cached as static.

### Step 3: Craft and Send Smuggled Request

**Context**: Append a smuggled GET request to the legitimate POST using chunked transfer encoding to bypass front-end parsing and fetch sensitive data from the backend.

In [[tools/Burp-Suite]], modify the request body from Step 2 by adding the smuggling payload. The payload uses a zero-length chunk to terminate the legitimate request early, followed by the smuggled GET.

Reference the smuggling payload: [[codes/Chunked-HTTP-Request-Smuggling-Payload]]

Forward the modified request multiple times (3-5 repetitions) to ensure cache poisoning.

**Expected Output**: Backend responds with the smuggled GET (e.g., API key data), but front-end treats it as part of the POST body.

### Step 4: Verify Cache Poisoning

**Context**: Test if the poisoned response is now cached and served as a static resource to other users.

Open an incognito browser window and load the home page or the targeted static resource URL. Use [[tools/Burp-Suite]]'s search function to query for phrases like "Your API Key" across cached responses.

If not found, repeat Step 3 and force-refresh the page.

**Expected Output**: The sensitive API key appears in a static resource response (e.g., embedded in HTML or as a separate file).

### Step 5: Extract Exposed Sensitive Data

**Context**: Confirm successful deception by retrieving the API key from the poisoned cache.

Inspect the cached static resource in the incognito session or intercepted traffic for the API key value.

**Expected Output**: Full API key string visible in the response body of a static resource.
