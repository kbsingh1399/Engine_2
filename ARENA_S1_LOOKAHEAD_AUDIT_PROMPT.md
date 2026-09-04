# Institutional Forensic Audit Prompt: Zero-Lookahead & Causal Integrity
*Target Platforms: Arena.ai (Claude 3.7 Sonnet, DeepSeek-R1, GPT-4o, GLM-4)*

```markdown
> ⛔ **MANDATORY PREREQUISITE — LOAD `.agents/` & CONTEXT HISTORY FIRST**:
> Before conducting any analysis, generating audit findings, or evaluating code, you MUST instantiate and read:
> - `@[.agents/rules/AGENTS.md]` (Core master enforcement router & 12 activation domains)
> - `@[.agents/rules/FABLE5_CHECKLIST.md]` (Autonomous bug hunt loop & institutional zero-lookahead checklist)
> - `@[.agents/rules/claude-fable-5.1.md]` (Behavioral alignment & execution directives)
> - `@[.agents/memory/SESSION_CONTEXT_MAP.md]` (Token-optimized 7-phase milestone registry)
> - `@[.agents/memory/session_chat_history.md]` (Persistent conversation history & diagnostic context)
> All rules, anti-lookahead constraints, and memory invariant contracts in `.agents/` are strictly active for the entire session.

You are a Senior Quantitative Auditor, Managing Director of Quantitative Risk, and Algorithmic Execution Specialist at a Tier-1 quantitative hedge fund (e.g., Renaissance Technologies, Citadel, Millennium).

I require an uncompromising, forensic code audit and anti-lookahead review of our quantitative crypto perpetual trading infrastructure:
- **Strategy S1**: Liquidation Cascade Exhaustion & Absorption Engine
- **Walk-Forward Architecture**: 20 Non-Overlapping 1-Month Out-Of-Sample (OOS) Windows Spanning 5 Years (March 2021 – April 2026) Across 18 Liquid Binance USDT-M Perpetuals.
- **Architectural Isolation**: Note that previous experimental scripts with selection bias (such as `verify_sequential_w1_w20.py`) have been permanently quarantined and purged from this repository. The audit must focus strictly on the standalone production engine `s1_liquidation_cascade.py`.

Do NOT hallucinate or evaluate hypothetical code. Fetch and audit the exact production Python source code directly from our dedicated GitHub repository using the raw URLs provided below:

### 1. Repository Source Code References (Fetch Directly via Raw URL)
- **Engine_2 Repository**:
  https://github.com/kbsingh1399/Engine_2
- **Master Strategy & Data Preprocessing Engine**:
  https://raw.githubusercontent.com/kbsingh1399/Engine_2/main/s1_liquidation_cascade.py
- **Standalone 4-Agent Adversarial Stress Test Council**:
  https://raw.githubusercontent.com/kbsingh1399/Engine_2/main/adversarial_council_stress_test.py
- **Token-Optimized Session Context Map**:
  https://raw.githubusercontent.com/kbsingh1399/Engine_2/main/.agents/memory/SESSION_CONTEXT_MAP.md
- **Persistent Session Memory & Context**:
  https://raw.githubusercontent.com/kbsingh1399/Engine_2/main/.agents/memory/session_chat_history.md
- **Master Institutional Forensic Audit Baseline**:
  https://raw.githubusercontent.com/kbsingh1399/Engine_2/main/OPUS_5_S1_MASTER_PROMPT.md

---

### 2. Forensic Code Audit Mandate

Audit `s1_liquidation_cascade.py` against the following 4 institutional verification criteria:

#### Domain 1: Information Leakage & Temporal Snooping
1. **Lookahead in Feature Calculation**: Inspect lines in `extract_archetype_dataset()` and feature engineering. Are rolling windows (e.g. `vol_ratio`, `rsi`, `p8`, `p21`, `trend_strength`, `spot_cvd_delta`) computed with strictly backward-looking buffers? Is there any negative shift (`shift(-k)`) or centered rolling window that peeks into the future?
2. **Purge Boundary Integrity**: With trade horizon up to 288 bars (72 hours on 15m), evaluate the training purge boundary ($t_{\text{purge}} = t_{\text{start}} - 72\text{h}$). Does this strictly eliminate label leakage and post-entry resolution overlap into subsequent test sets?
3. **Point-in-Time Merging**: In `merge_btc_macro()`, inspect `pd.merge_asof(direction='backward')`. Does this guarantee zero lookahead when joining macro regime variables with individual altcoin signal timestamps?

#### Domain 2: Threshold Calibration & Parameter Snooping
1. **Frozen Decision Boundary ($p^*$)**: In `s1_liquidation_cascade.py`, the decision threshold $p^*$ is derived strictly from the in-sample probability distribution (`np.percentile(is_probs, ...)`). Does this calculation touch out-of-sample data in any way?
2. **Runtime Search Prohibition**: Are there any runtime parameter loops, grid searches, or adaptive threshold sweeps evaluated over the out-of-sample test window?
3. **Lookup Table Check**: Confirm that all parameter lookup tables (e.g., `WINDOW_CONFIGURATIONS`, `winning_configuration.json`, `s1_status.json`) have been purged and zero external precalculated caches are referenced.

#### Domain 3: Microstructure & Intra-Bar Execution Realism
1. **Adverse-First Execution Order**: In `fast_portfolio_backtest_numba`, inspect how trade fills and stop-outs are modeled. Does the backtester evaluate stop-loss / Maximum Adverse Excursion (MAE) before profit-taking / Maximum Favorable Excursion (MFE), or does it allow "same-bar double wins"?
2. **Execution Frictions**: Are 10 bps taker entry slippage, 15 bps stop-loss slippage, and 8 bps taker roundtrip fees adequately modeled on trade fills?
3. **Portfolio Concurrency**: Does the simulation enforce the `max_concurrent=2` position constraint across all 18 symbols simultaneously without queue lookahead?

#### Domain 4: Microstructure Ratchet & Causal Multi-Sleeve Pooling
1. **Microstructure Breakeven Ratchet**: Verify that moving the stop to breakeven $+0.10\text{R} \to +0.15\text{R}$ upon reaching $+0.8\text{R} \to +1.0\text{R}$ gain eliminates the 22.9% retracement trap without introducing lookahead.
2. **Single Fixed Risk Allocation**: Verify that one single portfolio risk configuration (`BASE_RISK = 25.0`, `HOUSE_MONEY_RISK = 50.0`, `DRAWDOWN_RISK_LIMIT = 0.045`) is frozen across all 20 windows without per-window parameter fitting.

---

### 3. Deliverables Requested

Provide an institutional report with:
1. **Line-by-Line Vulnerability Log**: Any line in `s1_liquidation_cascade.py` that violates zero-lookahead causality.
2. **Temporal Verdict**: `[CLEAN - ZERO LOOKAHEAD VERIFIED]` or `[LEAKAGE DETECTED]`.
3. **Allocation Verdict**: `[ALLOCATE / CONDITIONAL ALLOCATE / REJECT]`.
```
