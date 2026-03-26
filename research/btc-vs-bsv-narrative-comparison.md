# BTC vs BSV/CSW 叙事对比研究
# BTC vs BSV/CSW Narrative Comparison Research

> 研究目的：为《正本清源比特币》一书提供素材，客观记录双方立场。
> Purpose: Research material for the book. Document both positions factually.
> Date: 2026-03-26

---

## 1. 扩容 Scaling: Small Blocks + Lightning vs Big Blocks

### BTC 立场 (Small Blocks + Layer 2)

**核心主张**：基础层应保持小区块（~1MB / ~4MB SegWit 权重），通过二层方案（Lightning Network）实现支付扩容。

**论据**：
- 小区块让普通用户能运行全节点，保障去中心化和独立验证能力
- 如果区块过大，只有数据中心级别的设备才能运行节点，导致中心化
- 基础层作为结算层（settlement layer），追求安全性和去中心化而非吞吐量
- Lightning Network 允许参与者在链下进行快速、低费用的支付，只在开通和关闭通道时上链
- 技术进步（如 SegWit）在不硬分叉的前提下适度提升了区块容量
- Vitalik Buterin 的评估：区块确实需要增长，但小区块阵营在技术论证上犯的错误更少

**代表人物/组织**：Bitcoin Core 开发者、Blockstream、Adam Back、Luke Dashjr

### BSV 立场 (Big Blocks)

**核心主张**：比特币应通过大区块直接在链上扩容，恢复中本聪的原始设计。Lightning Network 是一个不必要的、有害的补丁。

**论据**：
- 中本聪白皮书标题为"点对点电子现金系统"，意味着链上直接交易
- 高手续费问题是人为限制区块大小造成的——Lightning Network 是"治病比病更害人的药方"
- BSV 从 128MB 起步，后来移除区块上限限制，Teranode 在测试中已实现超过 100 万笔/秒
- 随着计算能力和带宽的进步，大区块在技术上完全可行
- Lightning Network 的根本问题：
  - 路由是概率性的，大额支付经常失败
  - 流动性碎片化：资金锁定在小通道中，管理复杂
  - 趋向中心化：用户倾向于连接资金充足的大节点（hub），削弱抗审查能力
  - 托管方案（custodial wallets）违背了比特币自主权的核心理念
  - 安全漏洞：replacement cycling attacks、jamming attacks 等
- SegWit 创造了 4MB 的区块但只提升了 1.2-1.4 倍的交易容量，而比特币需要的是几十倍甚至上百倍的扩容

**代表人物/组织**：Craig Wright、Calvin Ayre、nChain、BSV Association、CoinGeek

### 白皮书原文参考

白皮书第 5 节"Network"明确描述了节点的工作步骤：
1. New transactions are broadcast to all nodes.
2. Each node collects new transactions into a block.
3. Each node works on finding a difficult proof-of-work for its block.
4. When a node finds a proof-of-work, it broadcasts the block to all nodes.
5. Nodes accept the block only if all transactions in it are valid and not already spent.

BSV 方面认为这里的 "node" 就是矿工，所有交易都在链上处理。BTC 方面则认为这不排斥分层扩容。

---

## 2. 节点定义 Node Definition: Who Is a "Node"?

### BTC 立场 (Full Nodes = Anyone Running Bitcoin Core)

**核心主张**：任何运行 Bitcoin Core 全节点软件的人都是"节点"，都在参与网络的验证和共识维护。

**论据**：
- 全节点验证所有共识规则（21M 上限、减半计划、1MB 区块限制等）
- 运行全节点是"不信任，自己验证"（don't trust, verify）的核心体现
- 全节点数量越多，网络越去中心化、抗审查能力越强
- 全节点的去中心化甚至可能比挖矿的去中心化更重要——它们是共识规则的真正守护者
- 如果全节点数量过低，监管干预就可能成为现实

**代表人物/组织**：Bitcoin Core 社区、Lopp、Bitcoin Magazine

### BSV/CSW 立场 (Only Miners Are Nodes)

**核心主张**：在白皮书中，"node" 就是矿工。非挖矿的全节点在网络拓扑中没有实际功能。

**论据**：
- 白皮书第 5 节的每个步骤都涉及出块（proof-of-work）——节点 = 矿工
- 中本聪原话："Only people trying to create new coins would need to run network nodes"
- 中本聪预见大多数用户不会运行节点："as the network grows beyond a certain point, it would be left more and more to specialists with server farms"
- 中本聪预测"never more than 100K nodes"，其余用户使用轻量级客户端（SPV）
- 学术研究（arxiv.org, 2025）用图论证明：家庭全节点处于网络拓扑边缘，无法参与或影响传播拓扑；传播图由密集互连的矿工集团主导
- 非挖矿全节点是一种"安全剧场"（security theater），给用户错误的参与感
- SPV（Simplified Payment Verification）才是中本聪为普通用户设计的验证方式

**关键分歧**：BTC 社区将"node"的定义扩大到包含所有全节点验证者；BSV 坚持白皮书原始定义，认为只有矿工才是节点。这一分歧直接影响了对"去中心化"的不同理解。

---

## 3. 去中心化 Decentralization

### BTC 立场 (人人可验证 = 去中心化)

**核心主张**：去中心化的核心是让尽可能多的人能独立验证区块链，小区块保障了这种能力。

**论据**：
- 参与门槛低是去中心化的关键——1GB+ 的区块需要数据中心级硬件，会排除个人和小机构
- 全节点验证共识规则（供应上限、区块大小限制、减半等），这才是比特币免信任的根基
- 挖矿中心化风险存在（少数矿池控制大量算力），但全节点的去中心化分布是更重要的安全网
- 2017 年 UASF (User Activated Soft Fork) 证明了用户（而非矿工）才是共识规则的最终裁决者

**代表人物/组织**：Bitcoin Core、Samson Mow、Adam Back

### BSV/CSW 立场 (竞争性挖矿 = 去中心化)

**核心主张**：去中心化是多层次、多维度的概念。BTC 在它最自以为去中心化的方面恰恰是中心化的。

**论据**：
- BTC 的五大中心化问题：
  1. **协议控制中心化**：一小群 Core 开发者有权决定和操纵协议——这才是最严重的中心化
  2. **交易层面中心化**：BTC 无法实现真正的点对点交易
  3. **生态中心化**：依赖中心化交易所
  4. **社会采用中心化**：有限的扩容能力限制了广泛参与
  5. **挖矿中心化**：BTC 80% 算力由四个矿池控制（但这反而是 BTC 中心化中"最不严重"的问题）
- 真正的去中心化需要五个条件：
  1. 锁定的协议，不受中心化势力操纵
  2. 基于 IPv6 的点对点交易框架
  3. 链上直接交易（避免交易所/二层方案的中间人）
  4. 无限扩容以支持广泛采用
  5. 竞争性节点网络上的真正工作量证明
- "家庭全节点"只是安全剧场，真正维护网络安全的是矿工之间的竞争

**关键分歧**：BTC 定义去中心化为"验证的分布"；BSV 定义去中心化为"协议的不可操纵性 + 竞争性挖矿"。

---

## 4. Script/智能合约 Smart Contracts

### BTC 立场 (保守脚本 + 渐进扩展)

**核心主张**：中本聪时代的部分操作码被禁用是出于安全考虑，新功能应通过 BIP 流程谨慎引入。

**论据**：
- 操作码被禁用的原因：OP_LSHIFT 存在 bug 可以导致节点崩溃；其他 bug 允许任何人花费他人的比特币
- 安全优先——基础层的脚本功能应尽量简单，复杂逻辑放到上层
- 通过 BIP 流程逐步引入新功能：OP_CLTV (BIP65)、OP_CSV (BIP112)、Taproot (BIP341) 等
- Taproot 升级引入了 Schnorr 签名和 MAST，增强了隐私和脚本灵活性
- OP_CAT 等操作码的恢复正在讨论中，但需要充分论证安全性

**代表人物/组织**：Bitcoin Core 开发者、Pieter Wuille、Andrew Poelstra

### BSV/CSW 立场 (恢复原始脚本 = 图灵完备)

**核心主张**：比特币本身就是一个图灵完备的脚本系统。Core 开发者禁用操作码是对比特币能力的阉割。

**论据**：
- BSV 在 2020 年 2 月的 Genesis 升级中恢复了几乎所有被禁用的操作码
- BSV 在 2018 年 11 月将每个脚本的操作码限制从 201 提升到 500，允许更复杂的脚本
- 中本聪设计的原始 Script 就支持复杂智能合约——不需要新操作码或基础层修改
- OP_CAT 在 BSV 上已恢复使用，BTC 上仍然被禁用
- 对比实现效率（来自 sCrypt 团队的比较）：
  - Taproot 功能：BSV 上 1 个开发者 1 小时；BTC 上 150+ 开发者 4 年
  - Covenants：BSV 2020 年即可用；BTC 仍在提案阶段 (OP_CTV, BIP119)
  - 零知识证明：BSV 2022 年链上验证器；BTC 需要新操作码
  - Graftroot：BSV 已实现；BTC 尚未实现
- BTC 的方式导致每个新功能都需要分叉，需要 Core 开发者批准，可能耗时数年
- BSV 的智能合约作为应用层运行在基础协议上，而非硬编码进协议

**关键分歧**：BTC 认为禁用操作码是必要的安全措施，新功能应谨慎添加；BSV 认为原始比特币脚本已经足够强大，禁用操作码是人为限制比特币的潜力。

---

## 5. 匿名 vs 假名 Anonymity vs Pseudonymity

### BTC 立场 (倾向隐私/匿名)

**核心主张**：比特币的隐私性是其核心价值之一。用户应有权保护自己的金融隐私。

**论据**：
- 隐私是一项基本权利，金融监控是对自由的侵害
- CoinJoin、Taproot 等技术增强了交易隐私
- 比特币地址不与身份直接关联，这种设计是有意为之
- 抵抗金融审查是比特币存在的核心意义之一
- 对抗极权政府和金融压迫的工具需要强隐私保护
- 比特币的密码朋克 (cypherpunk) 传统强调隐私

**代表人物/组织**：比特币密码朋克社区、Wasabi Wallet、Samourai Wallet 团队

### BSV/CSW 立场 (假名 + 可审计)

**核心主张**：比特币是假名的（pseudonymous），不是匿名的（anonymous）。它被设计为可审计的诚实系统。

**论据**：
- Craig Wright 声称："I created Bitcoin as an immutable evidence trail that is pseudonymous and cannot be made legitimately anonymous and continue to work"
- 比特币被设计为"在政府、企业和货币中创造更多诚实"的工具
- 匿名性助长非法活动——这与比特币的创造目的相反
- 交易是关联的（linked），账本是透明可审计的
- 假名性在保护日常隐私的同时允许在法律需要时进行审计
- BSV 支持通过零知识证明等密码学技术在公共区块链上实现隐私，同时保持可审计性
- 比特币的 UTXO 模型本身就不是为匿名设计的——它是一个公开的、不可篡改的证据链

**关键分歧**：BTC 社区视隐私/匿名为核心价值观，认为它保护用户自由；CSW/BSV 认为比特币本质上是假名而非匿名系统，强调可审计性是比特币的设计特征而非缺陷。

---

## 6. 协议变更 Protocol Changes: Evolution vs "Set in Stone"

### BTC 立场 (通过 BIP 流程演进)

**核心主张**：比特币协议应通过 Bitcoin Improvement Proposals (BIP) 流程持续演进，适应新需求。

**论据**：
- BIP 流程是一个结构化的、去中心化的治理机制：
  1. 起草和社区讨论
  2. 审查和共识形成
  3. 代码实现和测试
  4. 矿工信号（通常需要 95% 的算力支持）
  5. 激活
- 三种 BIP 类型：标准跟踪（协议变更）、流程类、信息类
- 软分叉（soft fork）向后兼容，是首选的升级方式
- BIP 不具有强制性——最终由用户选择运行哪个软件
- 已成功实施的重要 BIP：SegWit (BIP141)、Taproot (BIP341)、OP_CLTV (BIP65) 等
- 协议需要适应不断变化的技术环境和安全需求

**代表人物/组织**：Bitcoin Core、Pieter Wuille、Amir Taaki (BIP 流程创始者)

### BSV/CSW 立场 (协议已定型，不应改变)

**核心主张**："Once version 0.1 was released, the core design was set in stone for the rest of its lifetime." 协议是固定的、不可改变的。

**论据**：
- 改变货币规则总是不公平地重新分配价值——"Any change is less than a zero-sum game"
- 协议变更 = 开发者控制 = 去中心化的反面
- 固定协议意味着今天签署的交易在一年、十年、一个世纪后仍然有效
- 就像法币的可操纵性导致货币腐败，协议的不变性保障了货币的健全
- 不应该有"第二个兼容实现"——网络共识需要所有节点行为一致
- BTC 的 SegWit、Taproot 等变更"从根本上偏离了"中本聪的愿景
- BSV 的 Genesis 升级（2020年2月）旨在恢复原始协议，之后协议锁定
- 协议锁定让企业可以安心在其上构建——不用担心底层规则变动

**关键分歧**：BTC 视协议为需要持续改进的"活文档"；CSW/BSV 视协议为一经发布就定型的"基石"，任何改变都是对系统的破坏。这反映了对"who controls Bitcoin"的根本分歧。

---

## 7. 数字黄金 vs 数字现金 Digital Gold vs Digital Cash

### BTC 立场 (Store of Value / Digital Gold)

**核心主张**：比特币是"数字黄金"——一种稀缺的价值储存手段，而非日常支付工具。

**论据**：
- 比特币 2100 万枚的固定供应使其成为对抗通胀的工具
- 区块时间 10 分钟 + 约 7 TPS 的限制使其不适合日常小额支付
- 黄金也不用来买咖啡——它的价值在于稀缺性和持久性
- Michael Saylor 的论述：购买比特币并永久持有，让其增值
- Layer 2 (Lightning Network) 可以处理支付需求，基础层专注于结算
- 比特币已发展为全球宏观资产，被机构投资者和国家接受
- "数字黄金"叙事是比特币最成功的市场定位

**代表人物/组织**：Michael Saylor (MicroStrategy)、Fidelity、BlackRock、大多数 BTC 社区

### BSV/CSW 立场 (Peer-to-Peer Electronic Cash)

**核心主张**：比特币白皮书标题就是"点对点电子现金系统"——它被设计为数字现金，不是数字黄金。

**论据**：
- 白皮书第一句："A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution"
- "数字黄金"叙事是 2017-2018 年 BTC 因扩容失败而被迫转向的——当时交易费用飙升、交易确认需要数小时甚至数天
- "价值储存"需要先有"使用场景"——BTC 缺乏内在效用
- 现实世界中大部分黄金交易已经是数字化的（黄金证券、衍生品等），BTC 作为"数字黄金"是多余的
- BSV 追求的是公共账本和在其上写入数据的能力——通过 Metanet 等应用实现真正的效用
- 不被使用的"货币"不可能长期维持"价值储存"功能——需求来自使用，不是来自囤积
- BSV 的低手续费（远低于 1 美分）使其可以作为真正的微支付系统

**关键分歧**：这是整个 BTC vs BSV 争论中最根本的分歧之一。BTC 认为比特币已经自然演化为数字黄金，这是市场选择；BSV 认为这是开发者人为限制区块大小后的被迫转向，背叛了白皮书的原始愿景。

---

## 8. 治理 Governance: Developer vs Miner

### BTC 立场 (多方利益相关者治理)

**核心主张**：比特币由用户、矿工、开发者和企业共同治理，任何单一方都不能控制协议。

**论据**：
- 比特币的治理是去中心化的：任何协议修改都不是由少数人强加的，而是通过广泛讨论和自愿采纳实现
- 开发者提出方案（BIP），矿工信号支持，用户选择运行哪个软件
- 2017 年 SegWit2x 的失败证明了"用户意志"可以否决矿工和企业的共识
- 矿工不能单方面改变共识规则——软分叉需要 95% 算力信号
- BIP 不具有强制性，最终是用户决定什么是"比特币"
- 开发者是公共的、可审计的，代码是开源的

**代表人物/组织**：Bitcoin Core、Bitcoin Magazine

### BSV/CSW 立场 (矿工治理 + 协议锁定)

**核心主张**：比特币应由矿工治理——他们是唯一有"skin in the game"的参与者。开发者不应有权改变协议。

**论据**：
- "Where there is a protocol change, there is developer control, which is the exact opposite of what Bitcoin is about"
- BTC 的 Core 开发者实质上控制着协议——这是中心化的本质
- 矿工投入了大量资本（硬件、电力），有经济激励维护网络诚实
- 协议锁定后，治理问题本身就不存在了——规则是固定的，矿工负责执行
- Craig Wright 的法律诉讼逻辑：BTC Core 开发者对网络有实际控制权，因此有信托责任
  - 但英国法院驳回了这一论点："At first sight it is very hard to see how TTL's case on fiduciary duty is seriously arguable"
- nChain 开发了"黑名单管理器"工具，可根据法院命令冻结和没收代币——体现了"在法律框架内运作"的治理理念

**关键分歧**：BTC 认为治理是多方博弈的动态平衡；BSV 认为协议应该锁定，矿工执行规则，开发者没有权力改变协议。讽刺的是，BSV 因此面临一个批评：nChain/Craig Wright 对 BSV 的影响力本身就是一种中心化。

---

## 9. 法律合规 Legal Compliance

### BTC 立场 (抗审查 / 对抗监管)

**核心主张**：比特币的核心价值在于抗审查和无需许可。过度的法律合规会破坏这些属性。

**论据**：
- 比特币诞生于 2008 年金融危机之后，本身就是对金融体系失败的回应
- 抗审查（censorship resistance）是比特币最重要的属性之一
- 如果交易可以被冻结或逆转，比特币就不再是比特币
- KYC/AML 在交易所层面是可接受的，但不应侵入协议层
- 去中心化结构本身就使得协议层面的合规强制不可能实现
- 为暴政下的人民提供金融自由是比特币的道德使命

**代表人物/组织**：比特币密码朋克社区、部分 BTC maximalists

### BSV/CSW 立场 (合规友好 / 在法律框架内运作)

**核心主张**：比特币不是在法律之外运作的——它被设计为与现有法律体系兼容。

**论据**：
- Craig Wright："Crypto regulation will make life easier for BSV"——新监管不需要 BSV 做改变，因为 BSV 一直在做合规的事
- 区块链技术要被全球采纳，数字资产需要类似股票和债券的法律待遇
- BSV 的合规特性：
  - **Network Access Rules (NAR)**：提供企业需要的合规框架
  - **Digital Asset Recovery**：支持法院命令下的资产恢复
  - **黑名单管理器**：将法院命令转化为机器可读格式，可冻结和没收代币
- 公开透明的区块链实现了"前所未有的透明度"
- 假名性（而非匿名性）允许在法律需要时进行审计
- 匿名性助长犯罪——这与比特币"创造诚实"的目标相矛盾
- 比特币不是"不受监管的加密货币"——它是在现有法律框架内运作的电子现金

**BTC 社区对 BSV 合规立场的批评**：
- 黑名单管理器被视为对比特币去中心化和抗审查精神的"冒犯"
- 如果矿工可以根据法院命令冻结资金，比特币的无需许可特性就不存在了
- 这本质上是把比特币变成了另一个受控的金融系统

**关键分歧**：BTC 将抗审查视为核心特性，认为法律合规不应侵入协议层；BSV 认为比特币本身就被设计为在法律框架内运作，合规性是特性而非缺陷。

---

## 10. SegWit, Lightning Network, Taproot — CSW 的批评

### SegWit (Segregated Witness, 隔离见证)

**BTC 立场**：
- SegWit 修复了交易延展性（transaction malleability）问题
- 作为软分叉实现，向后兼容
- 通过分离签名数据，有效增加了区块容量（约 1.7-2 倍）
- 为 Lightning Network 等二层方案奠定了基础
- 2017 年 8 月激活，是 BTC 社区的重要共识成果

**CSW 的批评**：
- "Segregated witness fundamentally changes the nature of Bitcoin"——将签名数据从交易验证中分离出来改变了比特币的核心本质
- 扩容效果微不足道："4MB block that gives between 1.2 and 1.4 times the transaction size"——但比特币需要处理 100,000-500,000 TPS
- 直接增加区块到 4MB 就能获得更好的效果，不需要改变数据结构
- SegWit 创造了"双重 Merkle 树结构"，比原生比特币区块链更大
- 签名数据分离造成了各司法管辖区证据保留法下的合规问题
- SegWit 的真正目的是为 Lightning Network 和侧链铺路——这些会"摧毁稀缺性"

### Lightning Network (闪电网络)

**BTC 立场**：
- 实现即时、低费用的链下支付
- 保持基础层的安全性和去中心化
- 适合小额高频支付场景
- 持续发展中，生态系统不断扩大

**CSW 的批评**：
- Lightning Network 和侧链"destroy scarcity"——创造了"无限通胀"，模仿法币而非保持硬通货属性
- 从根本上说，Lightning 解决的是一个不需要存在的问题——高手续费是人为限制区块造成的
- Lightning 的实际问题（来自第三方分析）：
  - 路由失败频繁，大额支付难以完成
  - 流动性碎片化，通道管理复杂
  - 趋向中心化（大 hub 模式）
  - 托管钱包方案违背比特币自主权原则
  - 安全漏洞（replacement cycling attacks 等）
  - Lightning Network 流动性持续下降（2025 年跌破 5,000 BTC）
- Wright 的核心论点：开发者"把我们锁在了侧链和闪电网络里"

### Taproot

**BTC 立场**：
- 引入 Schnorr 签名，提升隐私和效率
- 通过 MAST (Merkelized Abstract Syntax Tree) 实现更灵活的脚本条件
- 使多签交易和复杂条件交易在链上看起来和普通交易一样，增强隐私
- 2021 年 11 月激活

**CSW 的批评**：
- Taproot 和 SegWit 一样"从根本上偏离了中本聪的愿景，误导了投资者"
- 这些是开发者未经授权的协议修改
- BSV 上通过原始脚本就能实现 Taproot 的所有功能——1 个开发者 1 小时即可
- Wright 以 Taproot 为例，提起高达 9000 亿英镑的诉讼，声称 BTC Core 开发者篡改了比特币协议

**CSW 的法律行动**：
- 对 BTC Core 开发者提起多项诉讼，指控他们通过 SegWit 和 Taproot 偏离了白皮书
- 最大一笔诉讼金额 £911B ($1.18T)
- 但法院结果不利：
  - 2024 年 3 月，Justice Mellor 裁定 Wright 不是中本聪
  - 法官认定 Wright 提交的证据是伪造的，Wright "extensively and repeatedly" 向法庭撒谎
  - Wright 因藐视法庭被判处一年监禁（缓刑两年）

---

## 总结：核心叙事框架对比

| 维度 | BTC 叙事 | BSV/CSW 叙事 |
|------|---------|-------------|
| 比特币是什么 | 数字黄金 / 价值储存 | 点对点电子现金 |
| 扩容方式 | Layer 2 (Lightning) | 大区块链上扩容 |
| 节点定义 | 所有全节点 | 仅矿工 |
| 去中心化 | 人人可验证 | 协议不可篡改 + 矿工竞争 |
| 脚本能力 | 保守 + 渐进 BIP | 恢复原始图灵完备脚本 |
| 隐私 | 隐私是权利 | 假名 + 可审计 |
| 协议 | 通过 BIP 演进 | 定型不变 |
| 治理 | 多方利益相关者 | 矿工执行 + 协议锁定 |
| 法律 | 抗审查优先 | 合规友好 |
| SegWit/LN/Taproot | 重要技术进步 | 对比特币的篡改 |

---

## Sources

### Scaling
- [BSV Series: BTC, Small Blocks, and Lightning Network - Unbounded Capital](https://unboundedcapital.com/blog/btc-small-blocks-lightning-network)
- [The struggle for the true Bitcoin - CoinGeek](https://coingeek.com/the-struggle-for-the-true-bitcoin-btc-bch-or-bsv/)
- [Bitcoin vs. Bitcoin Cash vs. BSV - Gemini](https://www.gemini.com/cryptopedia/bitcoin-vs-bitcoin-cash-vs-bsv-full-comparison)
- [Some reflections on the Bitcoin block size war - Vitalik Buterin](https://vitalik.eth.limo/general/2024/05/31/blocksize.html)
- [Bitcoin scalability problem - Wikipedia](https://en.wikipedia.org/wiki/Bitcoin_scalability_problem)
- [BSV Teranode - BSV Association](https://bsvassociation.org/protocol/teranode/)
- [Lightning Network is dying - CoinGeek](https://coingeek.com/the-lightning-network-is-dying/)
- [Lightning Network challenges - CoinTelegraph](https://cointelegraph.com/news/bitcoins-lightning-network-major-challanges)
- [Critics claim Lightning Network is slowly dying - Protos](https://protos.com/critics-claim-buggy-bitcoin-lightning-network-is-slowly-dying/)
- [The Decentralist Perspective - Bitcoin Magazine](https://bitcoinmagazine.com/technical/decentralist-perspective-bitcoin-might-need-small-blocks-1442090446)

### Nodes
- [The Quotable Satoshi: Nodes - Satoshi Nakamoto Institute](https://satoshi.nakamotoinstitute.org/quotes/nodes/)
- [Redundancy of Full Nodes in Bitcoin - arXiv](https://arxiv.org/html/2506.14197v1)
- [Bitcoin nodes vs. miners - CoinTelegraph](https://cointelegraph.com/learn/articles/bitcoin-nodes-vs-miners)
- [Full node - Bitcoin Wiki](https://en.bitcoin.it/wiki/Full_node)

### Decentralization
- [Is Bitcoin decentralized? - CoinGeek](https://coingeek.com/is-bitcoin-decentralized/)
- [Bitcoin SV is the most centralized Bitcoin network - CryptoNews](https://cryptonews.net/news/bitcoin/27721685/)
- [Is decentralization sustainable in Bitcoin? - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167923624000113)

### Script/Smart Contracts
- [BSV vs BTC smart contracts - CoinGeek](https://coingeek.com/bsv-vs-btc-smart-contracts/)
- [Bitcoin SV vs Bitcoin Core Smart Contracts - sCrypt](https://scryptplatform.medium.com/bitcoin-sv-vs-bitcoin-core-smart-contracts-c9e3c1abef58)
- [Bitcoin Opcodes for Dummies - Medium](https://medium.com/@DrRoyMurphy/bitcoin-opcodes-for-dummies-4cd6f10d744b)
- [Script - Bitcoin Wiki](https://en.bitcoin.it/wiki/Script)
- [OP_CAT enables any contract in Bitcoin - CoinGeek](https://coingeek.com/op_cat-enables-any-contract-in-bitcoin/)

### Anonymity vs Pseudonymity
- [BSV: The Regulation-Friendly Bitcoin - BSV Blockchain](https://bsvblockchain.org/news/bitcoin-sv-the-regulation-friendly-bitcoin/)
- [Craig Wright takes on the lie of unregulated crypto - CoinGeek](https://coingeek.com/dr-craig-wright-takes-on-the-lie-of-unregulated-crypto/)
- [BSV founder Craig Wright Clarifies Bitcoin's Original Intent - Blockchain News](https://blockchain.news/news/bsv-founder-craig-wright-clarifies-bitcoins-original-intent-and-critiques-misuse)

### Protocol Changes
- [Set in Stone - Craig Wright on Medium](https://medium.com/@craig_10243/set-in-stone-7ebc9d31500e)
- [The Vision for Bitcoin - Craig Wright](https://craigwright.net/blog/bitcoin-blockchain-tech/the-vision-for-bitcoin/)
- [What is a BIP? - River](https://river.com/learn/what-is-a-bitcoin-improvement-proposal-bip/)
- [Bitcoin Improvement Proposals - GitHub](https://github.com/bitcoin/bips)

### Digital Gold vs Digital Cash
- [Bitcoin debate: store of value or medium of exchange? - Xapo Bank](https://www.xapobank.com/en/blog/bitcoin-debate-store-of-value-or-medium-of-exchange)
- [Why there is no store of value in BTC - CoinGeek](https://coingeek.com/why-there-is-no-store-of-value-or-digital-gold-in-btc/)
- [BTC is not digital gold - CoinGeek](https://coingeek.com/btc-is-not-digital-gold-and-it-never-was/)
- [Bitcoin: A Peer-to-Peer Electronic Cash System - Whitepaper](https://bitcoin.org/bitcoin.pdf)

### Governance
- [A Primer on Bitcoin Governance - Bitcoin Magazine](https://bitcoinmagazine.com/culture/a-primer-on-bitcoin-governance-or-why-developers-aren-t-in-charge-of-the-protocol-1473270427)
- [Civil War on Bitcoin - CoinGeek](https://coingeek.com/the-war-on-bitcoin/)
- [Bitcoin Developers Score Legal Victory Against Craig Wright - Bitcoinist](https://bitcoinist.com/bitcoin-developers-score-victory-craig-wright-legal/)

### Legal Compliance
- [Craig Wright: Crypto regulation will make life easier for BSV - CoinGeek](https://coingeek.com/dr-craig-wright-crypto-regulation-will-make-life-easier-for-bsv-video/)
- [Craig Wright's Blacklist Resembles Bitcoin Kill Switch - CoinDesk](https://www.coindesk.com/tech/2023/01/20/craig-wrights-blacklist-resembles-bitcoin-kill-switch-satoshi-never-followed-through-on/)
- [BSV: The Regulation-Friendly Bitcoin - BSV Blockchain](https://bsvblockchain.org/news/bitcoin-sv-the-regulation-friendly-bitcoin/)

### SegWit, Lightning, Taproot
- [Craig Wright on SegWit - CoinGeek](https://coingeek.com/craig-wright-segwit/)
- [Craig Wright Says Bitcoin Devs Misled the Public - Decrypt](https://decrypt.co/287138/craig-wright-bitcoin-new-lawsuit)
- [Craig Wright's Risks of Segregated Witness - Bitcoin.com News](https://news.bitcoin.com/risks-segregated-witness-opening-door-mining-cartels-undermine-bitcoin-network/)
- [Craig Wright Claims BSV Is True Bitcoin - CoinGape](https://coingape.com/craig-wright-claims-bsv-is-true-bitcoin-files-lawsuit-against-btc-core-devs/)
- [Craig Wright £911B Lawsuit - DailyCoin](https://dailycoin.com/bitcoin-core-hit-with-911b-lawsuit-by-craig-wright/)

### Legal Context (Craig Wright Identity Claims)
- [Craig Wright's fake Satoshi story - Fortune](https://fortune.com/crypto/2024/03/15/craig-wright-fake-satoshi-nakamoto-exposed/)
- [Craig Steven Wright - Wikipedia](https://en.wikipedia.org/wiki/Craig_Steven_Wright)
- [The Battle of Bitcoin - Rory Cellan-Jones](https://rorycellanjones.substack.com/p/the-battle-of-bitcoin)
