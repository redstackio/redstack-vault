---
id: 24f1574a-6475-48d7-b5c1-8ac6cfc4ff71
name: Lan Turtle AutoSSH
type: procedure
verified: true
submitted: true
created_at: '2019-10-15T18:46:55.500836+00:00'
updated_at: '2023-05-26T00:40:47.594183+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
platforms:
- Linux
tags:
- '[[Command & Control]]'
- '[[Network]]'
commands:
- '[[sshuttle Forward all traffic through SSH Tunnel]]'
---

# Lan Turtle AutoSSH

**Status**: ✓ Verified

## Summary

The Lan Turtle AutoSSH module is used to automatically open a Reverse SSH connection to an attacker host right when it is plugged into a target network. When we want a remote foothold into a target network that we have physical access to, we can drop a Lan Turtle into their network and walk away, k

## Description

## Description

The Lan Turtle AutoSSH module is used to automatically open a Reverse SSH connection to an attacker host right when it is plugged into a target network.

When we want a remote foothold into a target network that we have physical access to, we can drop a Lan Turtle into their network and walk away, knowing we will have remote access back into their local network.



## Setup

Install the AutoSSH and SSH Key Manager Modules. Key Manager will assist to generate an RSA key and upload it to the remote attacker host using ssh-copy-id. It will also create the known_hosts file in the Lan Turtle to avoid any human interaction when the Lan Turtle is plugged into a target network later. AutoSSH will open a SSH connection to the attacker host with a reverse ssh port opened, allowing the attacker to gain access back into the target network.



1. Configure a remote host with a public IP for the attacker host. We have a procedure using a Terraform script to configure an EC2 Instance with Kali Linux, this is a solid recommendation.



2. Setup the Module Manager

Modules -> Select -> Configure -> Directory -> "Yes connect to LanTurtle.com"



3. Access the Modules under the main menu, at first you will only have the "modulemanager" installed, select it and there will be an option to download more modules on the next screen (The Lan Turtle needs to be online to download modules). One at a time select and install the AutoSSH & SSH Key Manager modules.





![09bb213b-b213-4564-b9be-6d97c185baec.png](_assets/images/Ermis/09bb213b-b213-4564-b9be-6d97c185baec.png)





4. Next, Configure the RSA key to auto-connect once the device is plugged in, do this using the Key Manager module.

In the key manager configuration: Select generate a new RSA key-pair, this could take a minute or two. Once the key is generated select the option to copy the key-pair over to the Attacker host.  This step will require knowledge of your attacker hosts ip, port, username and password for ssh access. RedStack has a Terraform to create an EC2 instance if needed.



5. Now setup the AutoSSH module. Go back to the Module selection page and select AutoSSH -> Configure.

Fill the form with the Attacker host details configured in step 1.

![5141a965-f044-4d9f-8e9d-f5b8a5d43705.png](_assets/images/Ermis/5141a965-f044-4d9f-8e9d-f5b8a5d43705.png)



6. Arm the device by going back to the AutoSSH menu, select enable the AutoSSH module, this will auto start the AutoSSH module on boot, so the next time it is plugged in, it will auto ssh to the attacker host.



7a. Test the lan turtle on your own network -> Unplug it from the computer and plug it back in to allow it to boot. ensure it connects to the attacker host properly and port 2222 is available as viewed in step 8. Once this has been confirmed we are ready to deploy the Lan Turtle device in a live environment.



7b. Physically drop the Lan Turtle onto a target network. This can be connected to a Computer in their office or in their Data Center, anywhere you find access to an RJ-45 cable connecting to their LAN, and a USB port on one of their local systems. This step might require some level of Social Engineering to obtain access into their office space.



8. SSH to the Attacker host and check the connections on the localhost. You may have to wait a minute for the port :2222 to appear



![ddd819a3-fa2c-4f92-b1f2-9e6766e3b9d4.png](_assets/images/Ermis/ddd819a3-fa2c-4f92-b1f2-9e6766e3b9d4.png)



9. Open a local ssh connection to port 2222, a reverse ssh connection back into the Lan Turtle on the Remote site. This will give you full access to the remote Lan Turtle on the targets Local Network.



![38347587-440e-45aa-b1cc-c503a764513f.png](_assets/images/Ermis/38347587-440e-45aa-b1cc-c503a764513f.png)



10. (Optional to step 9)

To tunnel the Kali Linux EC2 traffic through the Lan Turtle directly into the target network run sshuttle. This will forward all of the traffic from the Attacker EC2 Instance through the SSH Tunnel - serving like a VPN connection. 





**Command** ([[sshuttle Forward all traffic through SSH Tunnel]]):

```bash
sshuttle -r root@localhost:2222 0/0
```



Now that the sshuttle connection is up you may access the targets internal network.





## Platforms

- Linux

## Products

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[sshuttle Forward all traffic through SSH Tunnel]]

## Tags

- [[Command & Control]]
- [[Network]]


