---
id: 735b874e-9515-47d0-9e91-d528c12fb1e7
name: Access-Uploaded-Files-Without-Authentication
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T14:04:46.565908+00:00'
updated_at: '2023-05-26T01:33:28.426609+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - file-access
  - broken-access-control
  - owasp
  - owasp-top-10
  - web-applications
commands:
  - '[[commands/curl-upload-file-to-webapp]]'
  - '[[commands/curl-logout-session]]'
  - '[[commands/curl-access-uploaded-file]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Access-Uploaded-Files-Without-Authentication

## Summary

This procedure tests for broken access control in web applications by uploading a file while authenticated and then attempting to access it without authentication. It verifies if the application enforces proper authorization checks on file retrieval endpoints, which could allow unauthorized users to view sensitive uploaded content.

## Description

Many web applications allow users to upload files, such as documents or images, but fail to properly restrict access to these files after upload. This vulnerability, often classified under OWASP Broken Access Control (A01:2021), enables attackers to bypass authentication by directly accessing file URLs. The technique is commonly tested in penetration testing to identify misconfigurations in file serving logic, such as exposing files via predictable paths without session validation. Success indicates a high risk of data exposure, especially if sensitive files are uploaded. This procedure assumes a typical file upload feature and uses HTTP requests to simulate the process.

## Requirements

1. Valid user credentials or session cookie for the target web application with file upload functionality.
2. Knowledge of the upload endpoint (e.g., /upload) and file serving path (e.g., /files/{filename}).
3. Access to a tool like curl for sending HTTP requests, or a browser with developer tools.
4. A test file to upload (e.g., a simple text file with identifiable content).

## Defense

Defensive measures and detection strategies:

- Implement server-side access controls to validate user authentication and authorization before serving uploaded files (e.g., check session tokens or user ownership).
- Use temporary signed URLs or database lookups to restrict file access, expiring links after use.
- Log all file access attempts and monitor for anomalous requests from unauthenticated sources.
- Employ web application firewalls (WAFs) to detect direct object reference patterns and block unauthorized paths.

## Objectives

1. Confirm if uploaded files are publicly accessible without authentication, indicating broken access control.
2. Identify the exact file paths or endpoints vulnerable to unauthorized access.
3. Document the vulnerability for remediation, such as adding authorization middleware.

## Instructions

### Step 1: Upload a Test File While Authenticated

**Context**: Authenticate to the application and upload a test file to obtain its storage location or URL. This step establishes a baseline for the file's accessibility under normal conditions and captures any returned identifiers (e.g., filename or path) needed for subsequent access attempts. The upload simulates legitimate user behavior to avoid detection.

**Command** ([[commands/curl-upload-file-to-webapp]]):

```bash
curl -X POST -F "file=@test.txt" -H "Cookie: session=abc123" http://target.com/upload
```

> This command sends a multipart form upload request with the test file. Replace 'test.txt' with your file path, 'session=abc123' with your actual session cookie, and 'http://target.com/upload' with the target's upload endpoint. The response should include success confirmation and the file's URL or ID.

**Expected Output**: HTTP 200 OK response with JSON or HTML indicating successful upload, such as {"status": "success", "file_url": "/files/test.txt"}. Note the file path for Step 3.

### Step 2: Logout to Terminate the Session

**Context**: End the authenticated session to simulate an unauthorized state. This ensures the subsequent access attempt is performed without valid credentials, isolating the authorization check. If the application uses token-based auth, invalidate the token here.

**Command** ([[commands/curl-logout-session]]):

```bash
curl -X GET -H "Cookie: session=abc123" http://target.com/logout
```

> This sends a GET request to the logout endpoint, clearing the session. Replace the cookie and URL as needed. If logout is a POST, adjust the method accordingly.

**Expected Output**: HTTP 200 or 302 redirect to login page, confirming session termination. Subsequent requests without the cookie should fail authentication.

### Step 3: Attempt to Access the Uploaded File Without Authentication

**Context**: Directly request the uploaded file using its known path without including session cookies or auth headers. This tests if the file serving endpoint enforces authorization. If successful, it confirms the vulnerability; otherwise, proper controls are in place.

**Command** ([[commands/curl-access-uploaded-file]]):

```bash
curl http://target.com/files/test.txt
```

> This performs a simple GET request to the file URL obtained in Step 1. Omit any auth headers or cookies to simulate an unauthenticated user. Replace the URL with the actual file path.

**Expected Output**: If vulnerable, HTTP 200 with the file content (e.g., the text from test.txt). If secure, HTTP 401 Unauthorized, 403 Forbidden, or a redirect to login.

**Success Indicators**:
- File content is returned without authentication, confirming unauthorized access.
- No errors or blocks on the request, indicating missing access controls.
