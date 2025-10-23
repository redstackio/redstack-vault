---
id: 4de3fdb5-a29a-4caa-bab3-9b9583ee2d6a
name: Gitlab/Github CI Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.300925+00:00'
updated_at: '2023-04-10T20:34:09.783945+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[CMSTP|T1191 - CMSTP]]'
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Gitlab CI/Github Actions]]'
- '[[Source Code Management & CI/CD Compromise]]'
commands:
- '[[whoami]]'
---

# Gitlab/Github CI Command Execution

## Summary

Gitlab/Github CI/CD pipelines are used by developers to automate their build, test and deployment process. Attackers can exploit these pipelines to execute arbitrary code on the target system, bypassing security controls. By compromising the CI/CD pipeline, an attacker can gain persistence, move la

## Description

# Description

Gitlab/Github CI/CD pipelines are used by developers to automate their build, test and deployment process. Attackers can exploit these pipelines to execute arbitrary code on the target system, bypassing security controls. By compromising the CI/CD pipeline, an attacker can gain persistence, move laterally and exfiltrate sensitive data. This attack can be executed remotely and can be difficult to detect.

 

## Requirements

1. Access to the Gitlab/Github repository

1. Access to the Gitlab/Github CI/CD pipeline

 

## Defense

1. Implement least privilege access control in the CI/CD pipeline

1. Implement code review and testing for the pipeline

1. Implement monitoring and alerting for pipeline activity

 

## Objectives

1. Execute arbitrary code on the target system

1. Gain persistence on the target system

1. Move laterally and exfiltrate sensitive data

 

# Instructions

1. To execute commands using Gitlab-CI, create a `.gitlab-ci.yml` file with the desired stages and commands. In this example, the `whoami` command is executed in parallel on three different virtual machines specified in the `matrix` field.

 



**Code**: [[stages:
    - test

test:
    stage: test
    scri]]



> The `stages` field specifies the order in which the different stages of the pipeline should be executed. In this case, there is only one stage named `test`. The `test` stage has a `script` field which specifies the command(s) to be executed. In this case, the `whoami` command is executed using the pipe (`|`) operator. The `parallel` field specifies that the command should be executed in parallel on multiple virtual machines specified in the `matrix` field. Finally, the `tags` field allows for the specification of tags that can be used to select specific runners for the job.



**Command** ([[whoami]]):

```bash
whoami
```



2. This Github Action workflow executes a single command on a Windows 2019 runner. The command that is executed in this example is `whoami`.

 

> The `name` field is the name of the workflow. The `on` field specifies the events that will trigger the workflow. In this example, the workflow will be triggered on a `workflow_dispatch` event, when code is pushed to the `main` branch, or when a pull request is made to the `main` branch. The `jobs` field specifies the jobs that will be run as part of the workflow. In this example, there is only one job named `build`. The `runs-on` field specifies the type of runner that will be used to run the job. In this example, the job will run on a Windows 2019 runner. The `steps` field specifies the individual steps that will be run as part of the job. In this example, there is only one step named `Execute Command`. The `run` field specifies the command that will be executed in the step. In this example, the command that is executed is `whoami`.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[CMSTP|T1191 - CMSTP]]
- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[whoami]]

## Tags

- [[Gitlab CI/Github Actions]]
- [[Source Code Management & CI/CD Compromise]]


