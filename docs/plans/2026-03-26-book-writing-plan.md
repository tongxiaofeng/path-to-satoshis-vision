# 《正本清源比特币》Writing Plan

> **For agentic workers:** Use superpowers:dispatching-parallel-agents for independent chapter batches. Each task is one chapter — research, write, self-review. Use the spec at `docs/specs/2026-03-26-book-design.md` as the single source of truth for content requirements.

**Goal:** Write a 17-chapter Chinese book (序章 + 17 chapters, ~169K characters) that rebuilds correct understanding of Bitcoin from first principles.

**Architecture:** Markdown chapters with unified template. Chapters are grouped into 5 writing phases by dependency order. Independent chapters within each phase can be written in parallel.

**Output format:** Each chapter is a standalone `.md` file in `chapters/`. Final assembly and typesetting (LaTeX/PDF) is a separate phase after all chapters pass review.

**Key references:**
- Spec: `docs/specs/2026-03-26-book-design.md`
- First Principles article: `/Users/alex/Codes/playground/first-priciple-of-blockchain/article/区块链的第一性原理.md`
- Ledger of Truth (reference only): `/Users/alex/Codes/playground/ledger-of-truth-chinese/The_Ledger_of_Truth.md`
- Bitcoin Whitepaper: fetch from web when needed

---

## Project Setup

### Task 0: Initialize project structure

**Files:**
- Create: `chapters/` directory
- Create: `references/` directory
- Create: `references/bitcoin-whitepaper-quotes.md` — curated Chinese translations of key whitepaper quotes used across chapters

- [ ] **Step 1: Create directory structure**

```
path-to-satoshis-vision/
  chapters/
    00-preface.md        # 序章
    01-industry-status.md
    02-pre-bitcoin.md
    03-ethereum-misconception.md
    04-scaling-dead-end.md
    05-distributed-db.md
    06-electronic-cash.md
    07-transactions.md
    08-proof-of-work.md
    09-incentive-network.md
    10-privacy.md
    11-bitcoin-and-law.md
    12-governance.md
    13-scaling.md
    14-script-smart-contracts.md
    15-btc-deviation.md
    16-bsv.md
    17-global-ledger.md
  references/
    bitcoin-whitepaper-quotes.md
  docs/
    specs/
    plans/
```

- [ ] **Step 2: Prepare whitepaper quotes reference**

Fetch the Bitcoin whitepaper. Extract and translate key quotes that will be referenced across multiple chapters. This prevents inconsistent translations. Store in `references/bitcoin-whitepaper-quotes.md` with format:

```markdown
## Section 1: Introduction
**EN:** "Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties..."
**CN:** "互联网上的商业活动几乎完全依赖金融机构作为可信第三方..."

## Section 2: Transactions
...
```

- [ ] **Step 3: Copy first-principles article for local reference**

```bash
cp /Users/alex/Codes/playground/first-priciple-of-blockchain/article/区块链的第一性原理.md references/
```

---

## Chapter Writing Workflow

Each chapter task follows this workflow:

```
1. Read spec requirements for this chapter
2. Read referenced source material
3. Write the chapter following the template:
   - 引子 (500-800 chars)
   - 正本 (~60%)
   - 清源 (~30%)
   - 小结 (~500 chars)
4. Self-review: check cross-references, verify whitepaper quotes, ensure transitions
5. Save to chapters/XX-name.md
```

**Chapter template** (Part 2, Ch6-14 strict adherence):
```markdown
# [Chapter Title]

## 引子

[500-800 字的故事/事件/类比，引出本章主题]

## [正本 section title — varies by chapter]

[约占 60% 的篇幅，建构正确理解框架]

## [清源 section title — varies by chapter]

[约占 30% 的篇幅，驳斥误解]

## 小结

[约 500 字，一句话回答 + 衔接下一章]
```

Part 1 (Ch1-5) and Part 3 (Ch15-17) use narrative structure, not strict template.

---

## Phase 1: Foundation (序章 + 白皮书引用)

> 序章 is the anchor for the entire book. Must be written first.

### Task 1: Write 序章 — 一切从双花开始 (~8,000 字)

**Files:**
- Create: `chapters/00-preface.md`
- Read: `references/区块链的第一性原理.md` (sections 1-4)
- Read: `references/bitcoin-whitepaper-quotes.md`

**Spec reference:** See spec "序章：一切从双花开始"

- [ ] **Step 1: Read source material**

Read the first-principles article sections 1-4 for the derivation logic: matter vs information → double-spending → ordering → PoW.

- [ ] **Step 2: Write chapter**

Key requirements:
- Language must be maximally simple and direct — this sets the tone for the book
- Start from physical world vs digital world distinction
- Derive double-spending as the inevitable first problem
- Show ordering as the only solution (whether centralized or not)
- End with Bitcoin's breakthrough: PoW timestamps without trusted third parties
- Close with transition to Part 1: "Now let's see what happened when the industry misunderstood this"

Target: ~8,000 Chinese characters.

- [ ] **Step 3: Self-review**

Verify: no jargon without explanation, transitions are smooth, whitepaper quotes are accurate.

---

## Phase 2: Part 1 — 歧路 (Ch1-5)

> Ch1 should be written first (sets the emotional hook). Ch2-5 can be written in parallel after Ch1.

### Task 2: Write Ch1 — 区块链行业的现状 (~8,000 字)

**Files:**
- Create: `chapters/01-industry-status.md`

**Spec reference:** See spec "Ch1：区块链行业的现状"

- [ ] **Step 1: Research current data**

Web search for latest data on:
- USDT deployment across chains (ERC-20, TRC-20, BEP-20, etc.)
- Cross-chain bridge losses (cumulative $ figure, major incidents)
- L2 sequencer centralization (Arbitrum, Optimism operator details)
- CEX trading volume vs on-chain volume ratio
- FTX collapse key facts

- [ ] **Step 2: Write chapter**

Key requirements:
- Open with a concrete scenario readers experience daily (e.g., sending USDT and choosing the wrong chain)
- Each section should make readers nod — "yes, I've experienced this"
- Build to the punchline: "行业花了 15 年，重新建造了比特币要摧毁的系统"
- Close with the question that drives the rest of the book: "这一切是怎么发生的？"

Target: ~8,000 Chinese characters. Narrative style, no strict template.

- [ ] **Step 3: Self-review and fact-check**

All statistics must be verifiable. No made-up numbers.

### Task 3: Write Ch2 — 比特币之前：数字货币的探索 (~10,000 字)

**Files:**
- Create: `chapters/02-pre-bitcoin.md`

**Spec reference:** See spec "Ch2：比特币之前——数字货币的探索"

**Dependency:** After Task 2 (Ch1), to ensure smooth transition.

- [ ] **Step 1: Research pre-Bitcoin systems**

Research details on: DigiCash/eCash (Chaum, 1989), Hashcash (Back, 1997), b-money (Dai, 1998), Bit Gold (Szabo, 1998). Focus on: what each solved, what each failed at, why.

- [ ] **Step 2: Write chapter**

Key requirements:
- Each system gets a focused section: problem it solved → why it wasn't enough
- Build a clear narrative arc: each attempt gets closer but fails at the same point — trusted third parties
- Bitcoin's breakthrough = PoW + economic incentives + competitive mining
- Reference first-principles article sections 4-5 for the "cheating costs must be physical" argument
- Close with: the solution existed, but the industry forgot what it was solving → Part 1 continues

Target: ~10,000 Chinese characters.

- [ ] **Step 3: Self-review**

### Task 4: Write Ch3 — 一个误解引发的连锁反应 (~10,000 字)

**Files:**
- Create: `chapters/03-ethereum-misconception.md`
- Read: `references/区块链的第一性原理.md` (sections 11-12)

**Spec reference:** See spec "Ch3：一个误解引发的连锁反应"

**Dependency:** Can run parallel with Task 3.

- [ ] **Step 1: Research Ethereum origin and architecture**

Research: Vitalik's original motivation, account model vs UTXO technical details, The DAO incident, global state problem.

- [ ] **Step 2: Write chapter**

Key requirements:
- Start from the misconception: "Bitcoin can't do smart contracts"
- Trace how BTC Core disabling opcodes → industry assumption → Ethereum's birth
- Technical comparison: Account model (global state, sequential) vs UTXO (no global state, parallel)
- The DAO as proof of account model's inherent vulnerability
- Script capability only asserted briefly here — full treatment in Ch14
- Reference first-principles article sections 11-12

Target: ~10,000 Chinese characters.

- [ ] **Step 3: Self-review**

### Task 5: Write Ch4 — 扩容的死胡同 (~10,000 字)

**Files:**
- Create: `chapters/04-scaling-dead-end.md`
- Read: `references/区块链的第一性原理.md` (section 14)

**Spec reference:** See spec "Ch4：扩容的死胡同"

**Dependency:** Can run parallel with Tasks 3-4.

- [ ] **Step 1: Research scaling attempts**

Research: Ethereum sharding abandonment (2022), Rollup mechanics (Optimistic vs ZK), EVM-compatible chain list, Occam's Razor framing.

- [ ] **Step 2: Write chapter**

Key requirements:
- Why Ethereum L1 fundamentally can't scale (global state + sequential execution)
- Sharding failure = admission of account model bottleneck
- Rollup/L2 = outsourcing trust, not scaling
- EVM clones = copying a flawed architecture N times
- Occam's Razor: if one chain can do it, why hundreds + bridges + L2?
- Back-reference Ch1: fragmentation root cause is wrong base architecture

Target: ~10,000 Chinese characters.

- [ ] **Step 3: Self-review**

### Task 6: Write Ch5 — 分布式数据库不是区块链 (~8,000 字)

**Files:**
- Create: `chapters/05-distributed-db.md`
- Read: `references/区块链的第一性原理.md` (section 6)

**Spec reference:** See spec "Ch5：分布式数据库不是区块链"

**Dependency:** Can run parallel with Tasks 3-5.

- [ ] **Step 1: Research Solana architecture**

Research: PoH mechanism, Tower BFT, leader schedule, outage history, validator hardware requirements.

- [ ] **Step 2: Write chapter**

Key requirements:
- PoH is a clock, not consensus; Tower BFT is the actual consensus
- Validator centralization: pre-selected schedule, high hardware bar
- Outage history as evidence (with dates)
- "Scalable" definition: high TPS ≠ scalable
- Closing must serve as Part 1 → Part 2 pivot: "我们已经看到了所有的弯路，现在让我们回到源头"

Target: ~8,000 Chinese characters.

- [ ] **Step 3: Self-review**

---

## Phase 3: Part 2 — 正本, Layers 1-2 (Ch6-9)

> Ch6 must be written first (definition anchor). Ch7-9 form the mechanism layer and have internal dependencies: Ch7 (transactions) → Ch8 (PoW secures transactions) → Ch9 (incentives make PoW work). Write sequentially.

### Task 7: Write Ch6 — 电子现金：一个被遗忘的定义 (~10,000 字)

**Files:**
- Create: `chapters/06-electronic-cash.md`
- Read: `references/bitcoin-whitepaper-quotes.md`

**Spec reference:** See spec "Ch6：电子现金——一个被遗忘的定义"

**Dependency:** After Phase 2 complete.

- [ ] **Step 1: Write chapter**

Key requirements:
- Whitepaper title word-by-word analysis: "Bitcoin", "Peer-to-Peer", "Electronic Cash", "System"
- What Bitcoin is NOT: not cryptocurrency, not digital gold, not blockchain technology, not speculative asset
- Legal-economic meaning of electronic cash
- HODLing contradicts Bitcoin's purpose
- Strict template: 引子/正本/清源/小结

Target: ~10,000 Chinese characters.

- [ ] **Step 2: Self-review**

### Task 8: Write Ch7 — 交易：产权转移的数字表达 (~10,000 字)

**Files:**
- Create: `chapters/07-transactions.md`
- Read: `references/bitcoin-whitepaper-quotes.md` (Section 2)

**Spec reference:** See spec "Ch7：交易——产权转移的数字表达"

**Dependency:** After Task 7 (Ch6).

- [ ] **Step 1: Write chapter**

Key requirements:
- UTXO model explanation: spending old coins, minting new coins
- Transaction as legal act: irrevocable property transfer
- Digital signatures = signing legal documents
- Script conditions: lock/unlock paradigm
- Property chain traceability
- UTXO vs Account model recap (connecting back to Ch3)

Target: ~10,000 Chinese characters.

- [ ] **Step 2: Self-review**

### Task 9: Write Ch8 — 工作量证明：用能量锚定秩序 (~9,000 字)

**Files:**
- Create: `chapters/08-proof-of-work.md`
- Read: `references/区块链的第一性原理.md` (sections 5-7)
- Read: `references/bitcoin-whitepaper-quotes.md` (Section 4)

**Spec reference:** See spec "Ch8：工作量证明——用能量锚定秩序"

**Dependency:** After Task 8 (Ch7).

- [ ] **Step 1: Write chapter**

Key requirements:
- Connect back to 序章: double-spending solution = ordering = PoW
- Timestamp server: each block is a sealed timestamp
- Thermodynamics: creating order requires energy (2nd law)
- Not "solving math puzzles" — providing physical guarantee for ordering
- PoS critique: no external cost, pre-selected producers, oligarchy
- ASIC specialization is a feature
- Reference first-principles article sections 5-7

Target: ~9,000 Chinese characters.

- [ ] **Step 2: Self-review**

### Task 10: Write Ch9 — 激励与网络：自运行的经济机器 (~10,000 字)

**Files:**
- Create: `chapters/09-incentive-network.md`
- Read: `references/bitcoin-whitepaper-quotes.md` (Sections 5, 6, 8)

**Spec reference:** See spec "Ch9：激励与网络——自运行的经济机器"

**Dependency:** After Task 9 (Ch8).

- [ ] **Step 1: Write chapter**

Key requirements:
- Economic incentive design: block reward + transaction fees
- 21M supply cap and halving: from subsidy to market-driven model
- Miner transaction selection and ordering: concrete implementation of 序章's "ordering is the solution"
- Honesty as optimal strategy
- Node = miner (whitepaper Section 5 quote)
- "Full node" fallacy
- SPV as design intent (whitepaper Section 8)
- Small-world network topology (mandala network)
- Correct understanding of "decentralization"

Target: ~10,000 Chinese characters.

- [ ] **Step 2: Self-review**

---

## Phase 4: Part 2 — 正本, Layers 3-4 (Ch10-14)

> Ch10-12 (philosophy layer) can be written in parallel. Ch13-14 (capability layer) can be written in parallel after Ch10-12.

### Task 11: Write Ch10 — 隐私：可审计的假名系统 (~8,000 字)

**Files:**
- Create: `chapters/10-privacy.md`
- Read: `references/bitcoin-whitepaper-quotes.md` (Section 10)

**Spec reference:** See spec "Ch10：隐私——可审计的假名系统"

**Dependency:** After Phase 3 complete.

- [ ] **Step 1: Write chapter**

Key requirements:
- Pseudonymous ≠ anonymous (pen name, not mask)
- Whitepaper Section 10 privacy firewall model
- New key pair per transaction recommendation
- Keys ≠ identity ≠ ownership
- UTXO chain analysis: feature not bug
- Freezable, traceable — helps law enforcement
- Regulation-compatible by design

Target: ~8,000 Chinese characters.

- [ ] **Step 2: Self-review**

### Task 12: Write Ch11 — 比特币与法律 (~10,000 字)

**Files:**
- Create: `chapters/11-bitcoin-and-law.md`
- Read: `references/bitcoin-whitepaper-quotes.md` (Section 1)

**Spec reference:** See spec "Ch11：比特币与法律——在法律框架内运作的系统"

**Dependency:** Can run parallel with Task 11.

- [ ] **Step 1: Research legal frameworks**

Research: contract law application to Bitcoin transactions, bearer instrument legal definition, nemo dat principle, court cases involving crypto ownership.

- [ ] **Step 2: Write chapter**

Key requirements:
- Whitepaper starts with commerce, not cryptography
- Transaction = contract (offer/acceptance/consideration)
- Electronic cash = bearer instrument
- Private key ≠ ownership (nemo dat)
- Protocol lock-in as legal necessity
- Immutable audit trail as evidence
- Miners' legal status
- No new laws needed — existing common law applies

Target: ~10,000 Chinese characters.

- [ ] **Step 3: Self-review**

### Task 13: Write Ch12 — 治理：写入石头的规则 (~9,000 字)

**Files:**
- Create: `chapters/12-governance.md`

**Spec reference:** See spec "Ch12：治理——写入石头的规则"

**Dependency:** Can run parallel with Tasks 11-12.

- [ ] **Step 1: Write chapter**

Key requirements:
- "Set in stone" principle with Satoshi quote
- Why protocol must be locked (rule changes = game changes; legal certainty; economic predictability)
- Fork = exit, not upgrade
- "One CPU one vote" true meaning
- Miners enforce, don't create rules
- Developer governance danger

Target: ~9,000 Chinese characters.

- [ ] **Step 2: Self-review**

### Task 14: Write Ch13 — 扩容：一条链承载全球 (~10,000 字)

**Files:**
- Create: `chapters/13-scaling.md`
- Read: `references/区块链的第一性原理.md` (section 16)

**Spec reference:** See spec "Ch13：扩容——一条链承载全球"

**Dependency:** After Tasks 11-13 (philosophy layer).

- [ ] **Step 1: Write chapter**

Key requirements:
- Back-reference Ch4: why L2/multi-chain fails → why Bitcoin can
- SPV + big blocks = whitepaper's original design
- 1MB as temporary anti-spam, not design parameter
- Lightning Network fundamental flaws
- High-volume low-fee economic model
- On-chain scaling engineering feasibility (UTXO parallelism, microservices)
- Reference first-principles article section 16

Target: ~10,000 Chinese characters.

- [ ] **Step 2: Self-review**

### Task 15: Write Ch14 — 脚本与智能合约：图灵完备的比特币 (~10,000 字)

**Files:**
- Create: `chapters/14-script-smart-contracts.md`

**Spec reference:** See spec "Ch14：脚本与智能合约——图灵完备的比特币"

**Dependency:** Can run parallel with Task 14.

- [ ] **Step 1: Research sCrypt and Runar**

Web search for latest sCrypt documentation, capabilities, examples. Research Runar protocol design and current status.

- [ ] **Step 2: Write chapter**

Key requirements:
- Bitcoin Script original design (Forth heritage)
- Opcode disabling history
- Turing completeness: individual scripts bounded (safety), system-level unbounded
- sCrypt (popular science level): what it is, what it can do, why it matters
- Runar (popular science level): what it is, what it can do, why it matters
- UTXO contract paradigm vs Ethereum account contracts
- Back-reference Ch3: the premise that "Bitcoin can't do smart contracts" was wrong

Target: ~10,000 Chinese characters.

- [ ] **Step 3: Self-review**

---

## Phase 5: Part 3 — 清源 (Ch15-17)

> Ch15 should be written first (provides historical context). Ch16-17 can follow.

### Task 16: Write Ch15 — 比特币与 BTC：协议分裂的真相 (~10,000 字)

**Files:**
- Create: `chapters/15-btc-deviation.md`

**Spec reference:** See spec "Ch15：比特币与 BTC——协议分裂的真相"

**Dependency:** After Phase 4 complete.

- [ ] **Step 1: Research BTC protocol changes timeline**

Research: exact dates and technical details of opcode disabling, 1MB limit, SegWit (BIP141), Taproot (BIP340/341/342).

- [ ] **Step 2: Write chapter**

Key requirements:
- BTC deviation timeline with specific dates and technical changes
- Each "upgrade" analyzed: what it changed, why it's a deviation
- Ticker ≠ protocol
- "Longest honest chain" definition
- "Digital gold" narrative as post-scaling-failure retreat
- Fork = exit, not upgrade

Target: ~10,000 Chinese characters. Narrative style.

- [ ] **Step 3: Self-review**

### Task 17: Write Ch16 — BSV：回归原始协议 (~10,000 字)

**Files:**
- Create: `chapters/16-bsv.md`

**Spec reference:** See spec "Ch16：BSV——回归原始协议"

**Dependency:** After Task 16 (Ch15).

- [ ] **Step 1: Research BSV ecosystem current state**

Web search for: Genesis upgrade details, Teranode latest status, sCrypt production deployments, Runar status, enterprise use cases on BSV.

- [ ] **Step 2: Write chapter**

Key requirements:
- Protocol restoration history: BCH split → BSV → Genesis upgrade → protocol lock
- Teranode engineering achievements (clearly distinguish benchmark vs production)
- Ecosystem status: who's building, what's live, what's achieved
- sCrypt and Runar in practice (connect to Ch14's theory)
- Honest about BSV's market position

Target: ~10,000 Chinese characters. Narrative style.

- [ ] **Step 3: Self-review**

### Task 18: Write Ch17 — 全球账本：数字经济的基础设施 (~9,000 字)

**Files:**
- Create: `chapters/17-global-ledger.md`
- Read: `references/区块链的第一性原理.md` (sections 15, 17)

**Spec reference:** See spec "Ch17：全球账本——数字经济的基础设施"

**Dependency:** After Task 17 (Ch16).

- [ ] **Step 1: Write chapter**

Key requirements:
- Micropayments and IoT
- Digital property rights and data sovereignty
- Network effects and Metcalfe's Law (one chain > many chains)
- Internet history parallel: CompuServe/AOL → TCP/IP unification
- Close the loop with Ch1: "行业花了15年重建了比特币要摧毁的系统 → 比特币的设计从第一天起就指向终局"
- Final statement: not prediction, not vision — logical terminus from first principles
- Reference first-principles article sections 15, 17

Target: ~9,000 Chinese characters. Narrative style.

- [ ] **Step 2: Self-review**

---

## Phase 6: Assembly and Review

### Task 19: Full manuscript review and assembly

**Files:**
- Read: all `chapters/*.md` files
- Create: `manuscript/正本清源比特币.md` (assembled full text)

- [ ] **Step 1: Assemble full manuscript**

Concatenate all chapters in order with part dividers.

- [ ] **Step 2: Full-text review**

Check for:
- Cross-reference accuracy (all "回扣 ChX" references are correct)
- Consistent terminology across chapters
- Smooth transitions between chapters (especially Part boundaries)
- Whitepaper quote consistency
- Total word count verification (~169,000 target)
- No orphaned promises (if Ch3 says "see Ch14", Ch14 must deliver)

- [ ] **Step 3: Final polish**

Fix any issues found. Ensure opening and closing form a complete loop.

---

## Dependency Graph

```
Phase 1: Task 0 (setup) → Task 1 (序章)

Phase 2: Task 2 (Ch1) → [Task 3 (Ch2) | Task 4 (Ch3) | Task 5 (Ch4) | Task 6 (Ch5)]

Phase 3: Task 7 (Ch6) → Task 8 (Ch7) → Task 9 (Ch8) → Task 10 (Ch9)

Phase 4: [Task 11 (Ch10) | Task 12 (Ch11) | Task 13 (Ch12)] → [Task 14 (Ch13) | Task 15 (Ch14)]

Phase 5: Task 16 (Ch15) → Task 17 (Ch16) → Task 18 (Ch17)

Phase 6: Task 19 (assembly)
```

## Parallel Execution Summary

| Phase | Sequential | Parallel batch |
|-------|-----------|----------------|
| 1 | Task 0 → Task 1 | — |
| 2 | Task 2 first | Tasks 3, 4, 5, 6 in parallel |
| 3 | Tasks 7 → 8 → 9 → 10 | — |
| 4 | — | Tasks 11, 12, 13 in parallel → Tasks 14, 15 in parallel |
| 5 | Tasks 16 → 17 → 18 | — |
| 6 | Task 19 | — |
