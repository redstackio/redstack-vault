---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - api
  - jwt
  - enumeration
  - data-breach
  - django
type: attack_chain
tools:
  - '[[tools/Docker]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Docker
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Set-Up-TalentMAP-API-Environment]]'
  - '[[procedures/Create-Demo-Environment-and-Seeded-Users]]'
  - '[[procedures/Create-Additional-Test-Users]]'
  - '[[procedures/Login-as-Guest-to-Obtain-JWT-Token]]'
  - '[[procedures/Send-GET-Request-to-Vulnerable-Endpoint]]'
  - '[[procedures/Observe-User-Information-Response]]'
  - '[[procedures/Automate-User-ID-Enumeration-with-Burp-Intruder]]'
step_count: 7
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.865Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the TalentMAP API to unauthorizedly access and enumerate
  sensitive user data across all accounts.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in TalentMAP API to Enumerate All User Personal Information

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) in the TalentMAP API's /api/v1/permission/user/{USER_ID}/ endpoint. An attacker logs in as a low-privilege guest user to obtain a JWT token, then manipulates the USER_ID parameter to access personal details of any user without authorization checks, enabling full enumeration of sensitive data like emails and names for all accounts in the database.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Create Test Data]
    B --> C[Obtain JWT Token]
    C --> D[Exploit IDOR]
    D --> E[Observe Data]
    E --> F[Automate Enumeration]
    F --> G[Data Breach Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#1abc9c
    style F fill:#f39c12
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Docker]]
- [[tools/Web-Browser]]
- [[tools/Burp-Suite]]

### Target Environment

- Django-based web application (TalentMAP API)
- Docker for containerization
- Exposed port 8000 for API access
- Local network access to localhost:8000

### Initial Access Requirements

- No prior credentials needed beyond guest login (username: guest, password: guestpassword)
- Localhost access to the running API instance
- Basic knowledge of HTTP requests and JWT tokens

## Detailed Attack Procedures

### Step 1: Set Up Environment
procedure: [[procedures/Set-Up-TalentMAP-API-Environment]]

**Objective**: Build and launch the TalentMAP API in a controlled Docker environment to replicate the vulnerable setup.

**Instructions**: Follow the build instructions from the referenced report to containerize the API.

**Expected Output**: Running Docker container with API accessible at http://localhost:8000.

**Success Indicators**:
- Container starts without errors
- API endpoint responds to basic requests

### Step 2: Create Demo Environment and Seeded Users
procedure: [[procedures/Create-Demo-Environment-and-Seeded-Users]]

**Objective**: Populate the database with initial demo data and predefined test users to enable vulnerability testing.

**Instructions**: Execute Django management commands inside the container to initialize the environment.

```bash
python manage.py create_demo_environment
python manage.py create_seeded_users
```

**Expected Output**: Confirmation messages for demo environment and seeded users creation.

**Success Indicators**:
- Database populated with base data
- Seeded users available for ID reference

### Step 3: Create Additional Test Users
procedure: [[procedures/Create-Additional-Test-Users]]

**Objective**: Add specific test accounts to expand the dataset for enumeration validation.

**Instructions**: Use the create_user command to add new users with known details.

```bash
python manage.py create_user normalUser normaluser@gmail.com normalUser123 Normal User
python manage.py create_user normalUser1 normaluser1@gmail.com normalUser123 Normal User
python manage.py create_user normalUser2 normaluser2@gmail.com normalUser123 Normal User
```

**Expected Output**: Success messages for each user creation.

**Success Indicators**:
- New users added to database
- User IDs increment sequentially (e.g., 1, 2, 3)

### Step 4: Login as Guest to Obtain JWT Token
procedure: [[procedures/Login-as-Guest-to-Obtain-JWT-Token]]

**Objective**: Authenticate as a low-privilege guest to acquire a valid JWT token for API requests.

**Instructions**: Access the login page and capture the token from the response.

**Expected Output**: JWT token in the authentication response.

**Success Indicators**:
- Successful login
- Token copied for use in headers

### Step 5: Send GET Request to Vulnerable Endpoint
procedure: [[procedures/Send-GET-Request-to-Vulnerable-Endpoint]]

**Objective**: Test the IDOR by requesting data for an arbitrary user ID using the guest token.

**Instructions**: Craft a GET request to the endpoint with manipulated USER_ID and JWT header.

**Expected Output**: JSON response with target user's personal details.

**Success Indicators**:
- Unauthorized access granted
- Sensitive data returned without errors

### Step 6: Observe User Information Response
procedure: [[procedures/Observe-User-Information-Response]]

**Objective**: Validate the leaked data to confirm the IDOR impact.

**Instructions**: Inspect the API response for details like email and name.

**Expected Output**: Full user profile data exposed.

**Success Indicators**:
- Personal information visible
- No access denial

### Step 7: Automate User ID Enumeration with Burp Intruder
procedure: [[procedures/Automate-User-ID-Enumeration-with-Burp-Intruder]]

**Objective**: Scale the attack to enumerate all users by automating ID cycling.

**Instructions**: Intercept a request in Burp and use Intruder to brute-force IDs from 1 to 100.

**Expected Output**: Batch of responses containing data for valid user IDs.

**Success Indicators**:
- Multiple user profiles collected
- Potential for complete database dump

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable API environment
2. Exploitation of IDOR to access arbitrary user data
3. Automated enumeration revealing all user sensitive information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T12:00:00Z*
