---
id: fb2ee009-be50-4f3c-aeb2-0c38f88583e3
name: Authentication-Bypass-via-PHP-Deserialization-and-Type-Juggling
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.337243+00:00'
updated_at: '2023-04-06T03:55:59.351356+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Authentication bypass]]'
  - '[[tags/PHP Deserialization]]'
  - '[[tags/Type juggling]]'
commands:
  - '[[commands/curl-send-php-serialized-cookie]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# Authentication-Bypass-via-PHP-Deserialization-and-Type-Juggling

## Summary

This procedure demonstrates how to bypass authentication in a vulnerable PHP application by exploiting insecure deserialization of user-supplied data from a cookie and leveraging PHP's type juggling behavior during loose comparisons. By crafting a serialized object with boolean 'true' values for username and password fields, the attacker can trick the application's equality checks (using ==) into succeeding against expected string values like 'admin', granting unauthorized access to protected resources.

## Description

The vulnerability arises in PHP applications that unserialize user-controlled input, such as cookies, without proper validation. In this case, the application deserializes a cookie named 'auth' into an array and performs loose equality checks ($data['username'] == $adminName && $data['password'] == $adminPassword). PHP's type juggling converts the boolean 'true' (from the serialized 'b:1') to the string '1' during comparison, but more critically, if the expected values are loosely comparable (e.g., 'admin' == true in some contexts or via crafted mismatches), the check passes. This technique is common in legacy PHP code and allows attackers to impersonate administrators without knowing actual credentials.

The target environment is a web application running PHP (e.g., on Apache/Nginx with PHP 7.x or earlier, where unserialize is used insecurely). Success grants access to admin panels, user data, or other sensitive functionality, potentially leading to data theft or further compromise. This maps to exploiting public-facing applications via input manipulation.

## Requirements

1. Network access to the vulnerable PHP web application (e.g., via browser or proxy).
2. Knowledge of the expected admin username and password strings used in the comparison (often 'admin' and a hardcoded password; infer from source or trial).
3. Tools for crafting and sending HTTP requests with custom cookies (e.g., curl or Burp Suite).
4. The application must use unserialize() on the 'auth' cookie without type-safe checks.

## Defense

Defensive measures and detection strategies:

- Avoid unserialize() on untrusted input; use JSON or safe deserialization libraries like Symfony Serializer.
- Use strict equality (===) for authentication checks to prevent type juggling.
- Implement secure session management with signed cookies (e.g., via PHP's setcookie with hmac).
- Enable PHP security extensions like Suhosin and log deserialization attempts.
- Web Application Firewall (WAF) rules to detect suspicious serialized payloads in cookies.

## Objectives

1. Craft a malicious serialized payload exploiting deserialization and type juggling.
2. Inject the payload into the application's cookie to bypass authentication.
3. Gain unauthorized access to admin or protected areas of the application.
4. Verify successful bypass by accessing restricted content.

## Instructions

### Step 1: Analyze the Vulnerable Code

**Context**: Review the target's PHP code to confirm the deserialization and loose comparison vulnerability. This step ensures the exploit path is valid; in a real engagement, obtain this via source disclosure or error messages.

The vulnerable code unserializes the 'auth' cookie and uses loose equality:

```php
<?php
data = unserialize($_COOKIE['auth']);

if ($data['username'] == $adminName && $data['password'] == $adminPassword) {
    $admin = true;
} else {
    $admin = false;
}
```

> This code is insecure because unserialize() reconstructs arbitrary objects from user input, and == allows type coercion (e.g., true == 'admin' if lengths or values loosely match in PHP's comparison rules).

**Expected Output**: Confirmation of unserialize() usage and == operators in auth logic.

### Step 2: Craft the Serialized Bypass Payload

**Context**: Create a serialized PHP array with username and password set to boolean true (b:1). This exploits type juggling as PHP converts true to a comparable string value during the == check, often matching 'admin' or similar if the expected value is loosely equivalent.

Use the payload from [[codes/PHP-Auth-Bypass-Serialized-Payload]]:

```php
a:2:{s:8:"username";b:1;s:8:"password";b:1;}
```

> This serializes an array with keys 'username' and 'password' both as boolean true. When deserialized, $data['username'] == 'admin' may pass if 'admin' coerces to true (e.g., non-empty string), depending on PHP version and exact expected values.

**Expected Output**: A valid serialized string ready for cookie injection.

### Step 3: Send the Malicious Cookie to Bypass Authentication

**Context**: Inject the crafted payload into the 'auth' cookie via an HTTP request to the login or protected endpoint. This simulates an authenticated session, bypassing the check.

**Command** ([[commands/curl-send-php-serialized-cookie]]):

```bash
curl -X GET "http://target-app.com/protected-page.php" -H "Cookie: auth=a:2:{s:8:\"username\";b:1;s:8:\"password\";b:1;}" -v
```

> This sends a GET request to a protected page with the serialized payload in the 'auth' cookie. Use -v for verbose output to inspect response headers and body. Adjust URL to the actual endpoint (e.g., /admin.php). If POST is required, add -d data.

**Expected Output**: HTTP 200 response with access to protected content (e.g., admin dashboard HTML), no redirect to login, and $admin = true in server-side logic.

### Step 4: Verify Access and Extract Data

**Context**: Confirm the bypass by interacting with the application and extracting sensitive information. This validates the exploit and achieves the objective.

Navigate to admin functions or use follow-up requests to dump user data.

**Expected Output**: Access to restricted features, such as user lists or config files, indicating successful authentication bypass.
