---
id: 76de29e3-fb95-4c59-b15c-831d47c75a38
name: Azure SSRF for VM Metadata Service
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.565150+00:00'
updated_at: '2023-04-10T20:23:56.623795+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Azure]]'
- '[[SSRF URL for Cloud Instances]]'
commands:
- '[[Accessing the VM Metadata service from outside the VM]]'
- '[[Changes to the VM Metadata service]]'
- '[[Conclusion]]'
- '[[Get Instance Metadata]]'
- '[[Get Public IP Address]]'
- '[[Introduction and Overview]]'
- '[[Retrieve instance metadata]]'
- '[[Retrieve Maintenance Data]]'
- '[[What is the VM Metadata service?]]'
---

# Azure SSRF for VM Metadata Service

## Summary

Azure SSRF for VM Metadata Service is an attack that takes advantage of the server-side request forgery vulnerability to exploit the Azure Virtual Machines Instance Metadata Service. This vulnerability allows attackers to send requests to internal endpoints, which can lead to unauthorized access to

## Description

# Description

Azure SSRF for VM Metadata Service is an attack that takes advantage of the server-side request forgery vulnerability to exploit the Azure Virtual Machines Instance Metadata Service. This vulnerability allows attackers to send requests to internal endpoints, which can lead to unauthorized access to sensitive information or resources. By exploiting this vulnerability, an attacker can gain access to the metadata service, which contains sensitive information about the virtual machine instance, such as authentication keys and passwords. This information can be used to escalate privileges, move laterally, or exfiltrate data.

 

## Requirements

1. Access to the vulnerable server

1. Knowledge of the SSRF vulnerability

1. Knowledge of the internal endpoints

 

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks

1. Restrict access to the metadata service to trusted sources only

1. Monitor the metadata service for suspicious activity

 

## Objectives

1. Gain unauthorized access to sensitive information or resources

1. Escalate privileges

1. Move laterally

1. Exfiltrate data

 

# Instructions

1. To retrieve metadata about an Azure VM, use the following command: curl -H Metadata:true 'http://169.254.169.254/metadata/instance?api-version=2020-06-01'

 



**Code**: [[https://azure.microsoft.com/en-us/blog/what-just-h]]



> The Azure VM Metadata Service provides information about a running virtual machine that can be used to configure and manage the VM. The service was recently updated to provide more secure access to metadata. The command provided above can be used to retrieve metadata about an Azure VM. The 'Metadata:true' header is required to access the metadata service, and the 'api-version' parameter specifies the version of the metadata service to use. Additional metadata endpoints are available for network interfaces, disks, and more.



**Command** ([[Introduction and Overview]]):

```bash
Recently, Microsoft Azure has made some changes to the VM Metadata service that may impact some users. This blog post provides an overview of the changes and how they may impact your Azure VMs.
```





**Command** ([[What is the VM Metadata service?]]):

```bash
The VM Metadata service is a RESTful endpoint available on every Azure VM that provides information about the VM itself, such as the VM's name, location, and network configuration. The service is accessible via a well-known URL (http://169.254.169.254) from within the VM.
```





**Command** ([[Changes to the VM Metadata service]]):

```bash
Microsoft has made changes to the VM Metadata service that will prevent access to the service from within the VM itself. This change is intended to improve security by preventing attackers who have gained access to a VM from using the VM Metadata service to obtain sensitive information about the VM or other resources in the same virtual network.
```





**Command** ([[Accessing the VM Metadata service from outside the VM]]):

```bash
Users can still access the VM Metadata service from outside the VM, such as from the Azure portal or from another VM in the same virtual network. However, this requires additional configuration to ensure that the request is authenticated and authorized.
```





**Command** ([[Conclusion]]):

```bash
The changes to the VM Metadata service may impact some users who rely on the service for certain scenarios. However, the changes are intended to improve security and prevent attackers from using the service to obtain sensitive information about Azure VMs.
```



2. Use this command to retrieve the maintenance metadata from the specified URL.

 



**Code**: [[http://169.254.169.254/metadata/v1/maintenance]]



> The 'data' field contains the URL to the maintenance metadata. This metadata provides information about the maintenance events that have occurred and are scheduled for the Azure Virtual Machine. The 'lang' field specifies the language used to execute the command. The 'instruction' field provides a brief description of the command and its usage. The 'explain' field provides additional details about the command and its arguments.



**Command** ([[Retrieve Maintenance Data]]):

```bash
http://169.254.169.254/metadata/v1/maintenance
```



3. To retrieve metadata for an Azure Virtual Machine, send an HTTP request to the metadata service endpoint using the following URL: http://169.254.169.254/metadata/instance?api-version=<api-version>&<parameter1>=<value1>&<parameter2>=<value2>...

 



**Code**: [[https://docs.microsoft.com/en-us/azure/virtual-mac]]



> The Azure Virtual Machines Instance Metadata Service allows you to retrieve information about your virtual machine such as its location, network configuration, and storage details. You can retrieve this information by sending an HTTP request to the metadata service endpoint with the appropriate parameters. The metadata service is available only to the virtual machine and cannot be accessed from outside the virtual machine. To ensure that the request is sent to the metadata service endpoint and not to a different endpoint, you must include the header "Metadata: true" in your request.



**Command** ([[Retrieve instance metadata]]):

```bash
curl -H Metadata:true http://169.254.169.254/metadata/instance?api-version=2021-02-01
```



4. To retrieve instance metadata, use the following commands:

 



**Code**: [[http://169.254.169.254/metadata/instance?api-versi]]



> 1. http://169.254.169.254/metadata/instance?api-version=2017-04-02
This command retrieves metadata about the instance.

2. http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text
This command retrieves the public IP address of the instance.



**Command** ([[Get Instance Metadata]]):

```bash
http://169.254.169.254/metadata/instance?api-version=2017-04-02
```





**Command** ([[Get Public IP Address]]):

```bash
http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Commands Used

- [[Accessing the VM Metadata service from outside the VM]]
- [[Changes to the VM Metadata service]]
- [[Conclusion]]
- [[Get Instance Metadata]]
- [[Get Public IP Address]]
- [[Introduction and Overview]]
- [[Retrieve instance metadata]]
- [[Retrieve Maintenance Data]]
- [[What is the VM Metadata service?]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Azure]]
- [[SSRF URL for Cloud Instances]]


