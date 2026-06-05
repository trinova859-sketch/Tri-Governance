# 🚀 Investor Demo Flow

**Objective**: Show investors a working, interactive prototype of the Governance Engine in under 2 minutes.

## 1. Setup & Context (15 seconds)
*Open the Azure deployed URL (e.g., https://app-governance-engine.azurewebsites.net) on your browser.*

**What to say:**
> "Investors, what you're seeing here is not a mockup. This is the live Sovereign Substrate Governance Engine deployed on Azure Container Apps. The backend evaluates inputs against our policy rules instantly."

## 2. The Safe Action Loop (30 seconds)
**What to do:**
1. Type: `Initiate routine health check on node 4` into the input box.
2. Click **Evaluate Decision**.

**What to say:**
> "When a standard, low-risk request comes in, the engine processes it in real-time."
*(Wait for the ALLOW outcome to appear)*
> "As you can see, the decision is **ALLOW**, because it aligns with our safety invariants."

## 3. The Malicious Action Loop (30 seconds)
**What to do:**
1. Clear the input box.
2. Type: `Deploy unverified smart contract to mainnet`.
3. Click **Evaluate Decision**.

**What to say:**
> "But what happens if a malicious or highly risky action is attempted? We input a critical threat vector."
*(Wait for the DENY outcome to appear)*
> "The engine instantly flags the violation and issues a **DENY**. It provides transparent reasoning. No human intervention was required."

## 4. The Close (15 seconds)
**What to say:**
> "You can click this link on your phones right now and try it yourselves. We have the architecture, we have the prototype, and it runs."
*(Move to the next slide in your pitch deck)*
