# Bitcoin Whitepaper Key Quotes / 比特币白皮书核心引文

> Source: Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," 2008
> https://bitcoin.org/bitcoin.pdf
>
> 本文件为《正本清源比特币》一书的参考资料，收录白皮书各章节的核心原文与中文翻译。

---

## Abstract / 摘要

**EN:** "A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution."

**CN:** "一种纯粹的点对点电子现金系统，将允许在线支付从一方直接发送给另一方，而无需通过金融机构。"

---

**EN:** "Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending."

**CN:** "数字签名提供了部分解决方案，但如果仍需一个可信的第三方来防止双重支付，那么其主要优势就丧失了。"

---

**EN:** "We propose a solution to the double-spending problem using a peer-to-peer network. The network timestamps transactions by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work."

**CN:** "我们提出一种使用点对点网络来解决双重支付问题的方案。该网络通过将交易哈希到一条持续增长的、基于哈希的工作量证明链中，来为交易加盖时间戳，从而形成一份不重做工作量证明就无法更改的记录。"

---

**EN:** "The longest chain not only serves as proof of the sequence of events witnessed, but proof that it came from the largest pool of CPU power."

**CN:** "最长的链不仅可以作为所见证事件序列的证明，还可以证明它来自最大的CPU算力池。"

---

**EN:** "As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers. The network itself requires minimal structure. Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone."

**CN:** "只要大多数CPU算力掌握在不联合攻击网络的节点手中，它们就会产生最长的链并超过攻击者。该网络本身只需要最低限度的结构。消息以尽力而为的方式广播，节点可以随意离开和重新加入网络，并接受最长的工作量证明链作为它们离开期间所发生事件的证明。"

---

## Section 1: Introduction / 第一节：引言

**EN:** "Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties to process electronic payments."

**CN:** "互联网上的商业活动已经几乎完全依赖于金融机构作为可信第三方来处理电子支付。"

---

**EN:** "While the system works well enough for most transactions, it still suffers from the inherent weaknesses of the trust based model. Completely non-reversible transactions are not really possible, since financial institutions cannot avoid mediating disputes."

**CN:** "虽然该系统对大多数交易运作得足够好，但它仍然受到基于信任模式固有弱点的困扰。完全不可逆的交易实际上是不可能的，因为金融机构无法避免调解纠纷。"

---

**EN:** "The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions, and there is a broader cost in the loss of ability to make non-reversible payments for non-reversible services."

**CN:** "调解成本增加了交易费用，限制了最低实际交易规模，切断了小额临时交易的可能性，而且在无法为不可逆服务进行不可逆支付方面，还存在更广泛的成本损失。"

---

**EN:** "With the possibility of reversal, the need for trust spreads. Merchants must be wary of their customers, hassling them for more information than they would otherwise need. A certain percentage of fraud is accepted as unavoidable."

**CN:** "由于存在交易撤销的可能性，对信任的需求不断扩散。商家必须对客户保持警惕，向他们索取本不需要的额外信息。一定比例的欺诈被视为不可避免而被接受。"

---

**EN:** "What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party."

**CN:** "我们需要的是一种基于密码学证明而非信任的电子支付系统，允许任何有交易意愿的双方直接进行交易，而无需一个可信的第三方。"

---

**EN:** "Transactions that are computationally impractical to reverse would protect sellers from fraud, and routine escrow mechanisms could easily be implemented to protect buyers."

**CN:** "计算上不可行的逆转交易将保护卖家免受欺诈，而常规的托管机制也可以轻松实现以保护买家。"

---

**EN:** "In this paper, we propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions. The system is secure as long as honest nodes collectively control more CPU power than any cooperating group of attacker nodes."

**CN:** "在本文中，我们提出了一种利用点对点分布式时间戳服务器来生成交易时间顺序之计算证明的方案，以此解决双重支付问题。只要诚实节点共同控制的CPU算力超过任何协作的攻击者节点群体，系统就是安全的。"

---

## Section 2: Transactions / 第二节：交易

**EN:** "We define an electronic coin as a chain of digital signatures. Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin. A payee can verify the signatures to verify the chain of ownership."

**CN:** "我们将电子货币定义为一条数字签名链。每一位所有者通过对前一笔交易的哈希和下一位所有者的公钥进行数字签名，并将签名附加到这枚货币的末尾，来将货币转让给下一位所有者。收款方可以通过验证签名来验证所有权链。"

---

**EN:** "The problem of course is the payee can't verify that one of the owners did not double-spend the coin. A common solution is to introduce a trusted central authority, or mint, that checks every transaction for double spending."

**CN:** "当然，问题在于收款方无法验证某一位所有者是否对这枚货币进行了双重支付。一个常见的解决方案是引入一个可信的中央机构（即铸币厂），对每笔交易进行双重支付检查。"

---

**EN:** "The problem with this solution is that the fate of the entire money system depends on the company running the mint, with every transaction having to go through them, just like a bank."

**CN:** "这个解决方案的问题在于，整个货币系统的命运取决于运营铸币厂的公司，每一笔交易都必须经过它们，就像银行一样。"

---

**EN:** "We need a way for the payee to know that the previous owners did not sign any earlier transactions. For our purposes, the earliest transaction is the one that counts, so we don't care about later attempts to double-spend. The only way to confirm the absence of a transaction is to be aware of all transactions."

**CN:** "我们需要一种方法让收款方确认之前的所有者没有签署过任何更早的交易。就我们的目的而言，最早的那笔交易才是有效的，因此我们不关心后续的双重支付尝试。确认某笔交易不存在的唯一方法，就是知晓所有交易。"

---

**EN:** "To accomplish this without a trusted party, transactions must be publicly announced, and we need a system for participants to agree on a single history of the order in which they were received. The payee needs proof that at the time of each transaction, the majority of nodes agreed it was the first received."

**CN:** "要在没有可信方的情况下实现这一点，交易必须被公开宣布，并且我们需要一个系统让参与者对交易被接收的先后顺序达成单一的历史共识。收款方需要证明：在每笔交易发生时，大多数节点认同该交易是最先被接收的。"

---

## Section 3: Timestamp Server / 第三节：时间戳服务器

**EN:** "The solution we propose begins with a timestamp server. A timestamp server works by taking a hash of a block of items to be timestamped and widely publishing the hash, such as in a newspaper or Usenet post."

**CN:** "我们提出的方案始于一个时间戳服务器。时间戳服务器的工作方式是对一组待加时间戳的数据项取哈希值，并广泛发布该哈希值，例如在报纸或Usenet帖子中发布。"

---

**EN:** "The timestamp proves that the data must have existed at the time, obviously, in order to get into the hash. Each timestamp includes the previous timestamp in its hash, forming a chain, with each additional timestamp reinforcing the ones before it."

**CN:** "时间戳证明了数据在当时必然已经存在，这是显而易见的，因为只有这样它才能被纳入哈希。每个时间戳在其哈希中包含前一个时间戳，形成一条链，每一个新增的时间戳都强化了它之前的所有时间戳。"

---

## Section 4: Proof-of-Work / 第四节：工作量证明

**EN:** "To implement a distributed timestamp server on a peer-to-peer basis, we will need to use a proof-of-work system similar to Adam Back's Hashcash, rather than newspaper or Usenet posts."

**CN:** "要在点对点的基础上实现分布式时间戳服务器，我们需要使用类似于Adam Back的Hashcash的工作量证明系统，而不是报纸或Usenet帖子。"

---

**EN:** "The proof-of-work involves scanning for a value that when hashed, such as with SHA-256, the hash begins with a number of zero bits. The average work required is exponential in the number of zero bits required and can be verified by executing a single hash."

**CN:** "工作量证明涉及搜索一个值，使得该值经过哈希运算（如SHA-256）后，所得哈希值以若干个零比特开头。所需的平均工作量随所要求的零比特数呈指数增长，而验证只需执行一次哈希运算即可。"

---

**EN:** "For our timestamp network, we implement the proof-of-work by incrementing a nonce in the block until a value is found that gives the block's hash the required zero bits. Once the CPU effort has been expended to make it satisfy the proof-of-work, the block cannot be changed without redoing the work. As later blocks are chained after it, the work to change the block would include redoing all the blocks after it."

**CN:** "对于我们的时间戳网络，我们通过不断递增区块中的随机数（nonce）来实现工作量证明，直到找到一个使区块哈希值满足所需零比特数的值为止。一旦CPU算力已被消耗以满足工作量证明，该区块就无法在不重做工作的情况下被更改。由于后续的区块在其之后链接，修改该区块的工作将包括重做其后所有区块的工作。"

---

**EN:** "The proof-of-work also solves the problem of determining representation in majority decision making. If the majority were based on one-IP-address-one-vote, it could be subverted by anyone able to allocate many IPs. Proof-of-work is essentially one-CPU-one-vote."

**CN:** "工作量证明还解决了在多数决策中确定代表权的问题。如果多数决定基于一个IP地址一票，那么任何能够分配大量IP的人都可以颠覆它。工作量证明本质上是一个CPU一票。"

---

**EN:** "The majority decision is represented by the longest chain, which has the greatest proof-of-work effort invested in it. If a majority of CPU power is controlled by honest nodes, the honest chain will grow the fastest and outpace any competing chains."

**CN:** "多数决定由最长链代表，因为最长链投入了最大的工作量证明。如果大多数CPU算力由诚实节点控制，诚实链将增长最快，超过任何竞争链。"

---

**EN:** "To modify a past block, an attacker would have to redo the proof-of-work of the block and all blocks after it and then catch up with and surpass the work of the honest nodes. We will show later that the probability of a slower attacker catching up diminishes exponentially as subsequent blocks are added."

**CN:** "要修改一个过去的区块，攻击者必须重做该区块及其之后所有区块的工作量证明，然后赶上并超过诚实节点的工作。我们稍后将证明，随着后续区块的不断添加，较慢的攻击者追赶上来的概率呈指数级递减。"

---

**EN:** "To compensate for increasing hardware speed and varying interest in running nodes over time, the proof-of-work difficulty is determined by a moving average targeting an average number of blocks per hour. If they're generated too fast, the difficulty increases."

**CN:** "为了补偿不断增长的硬件速度以及运行节点的兴趣随时间的变化，工作量证明的难度由一个移动平均值决定，目标是每小时产生固定数量的区块。如果区块产生得太快，难度就会增加。"

---

## Section 5: Network / 第五节：网络

**EN:** "The steps to run the network are as follows: 1) New transactions are broadcast to all nodes. 2) Each node collects new transactions into a block. 3) Each node works on finding a difficult proof-of-work for its block. 4) When a node finds a proof-of-work, it broadcasts the block to all nodes. 5) Nodes accept the block only if all transactions in it are valid and not already spent. 6) Nodes express their acceptance of the block by working on creating the next block in the chain, using the hash of the accepted block as the previous hash."

**CN:** "运行该网络的步骤如下：1）新的交易被广播到所有节点。2）每个节点将新交易收集到一个区块中。3）每个节点为其区块寻找满足难度要求的工作量证明。4）当一个节点找到工作量证明时，它将该区块广播给所有节点。5）节点只有在区块中所有交易都有效且尚未被花费的情况下才接受该区块。6）节点通过使用已接受区块的哈希值作为前一个哈希值，在其上创建下一个区块来表达对该区块的接受。"

---

**EN:** "Nodes always consider the longest chain to be the correct one and will keep working on extending it."

**CN:** "节点始终认为最长的链是正确的，并将持续在其上工作以延长它。"

---

**EN:** "If two nodes broadcast different versions of the next block simultaneously, some nodes may receive one or the other first. In that case, they work on the first one they received, but save the other branch in case it becomes longer. The tie will be broken when the next proof-of-work is found and one branch becomes longer; the nodes that were working on the other branch will then switch to the longer one."

**CN:** "如果两个节点同时广播了不同版本的下一个区块，某些节点可能会先接收到其中之一。在这种情况下，它们在最先收到的那个区块上工作，但保留另一个分支以防它变得更长。当下一个工作量证明被找到、其中一个分支变得更长时，僵局就会被打破；在另一个分支上工作的节点将会切换到更长的那条链。"

---

**EN:** "New transaction broadcasts do not necessarily need to reach all nodes. As long as they reach many nodes, they will get into a block before long."

**CN:** "新的交易广播不一定需要到达所有节点。只要它们到达足够多的节点，就会很快被收录进区块中。"

---

## Section 6: Incentive / 第六节：激励

**EN:** "By convention, the first transaction in a block is a special transaction that starts a new coin owned by the creator of the block. This adds an incentive for nodes to support the network, and provides a way to initially distribute coins into circulation, since there is no central authority to issue them."

**CN:** "按照惯例，区块中的第一笔交易是一笔特殊交易，它创造一枚新的货币归区块创建者所有。这为节点支持网络提供了激励，同时也提供了一种将货币初始分配到流通中的方式，因为不存在发行货币的中央机构。"

---

**EN:** "The steady addition of a constant of amount of new coins is analogous to gold miners expending resources to add gold to circulation. In our case, it is CPU time and electricity that is expended."

**CN:** "稳定地增加固定数量的新货币，类似于黄金矿工消耗资源将黄金加入流通。在我们的系统中，消耗的是CPU时间和电力。"

---

**EN:** "The incentive can also be funded with transaction fees. If the output value of a transaction is less than its input value, the difference is a transaction fee that is added to the incentive value of the block containing the transaction. Once a predetermined number of coins have entered circulation, the incentive can transition entirely to transaction fees and be completely inflation free."

**CN:** "激励也可以通过交易手续费来提供。如果一笔交易的输出值小于其输入值，差额即为交易手续费，它被加到包含该交易的区块的激励值中。一旦预定数量的货币进入流通，激励就可以完全过渡到交易手续费，从而完全没有通货膨胀。"

---

**EN:** "The incentive may help encourage nodes to stay honest. If a greedy attacker is able to assemble more CPU power than all the honest nodes, he would have to choose between using it to defraud people by stealing back his payments, or using it to generate new coins. He ought to find it more profitable to play by the rules, such rules that favour him with more new coins than everyone else combined, than to undermine the system and the validity of his own wealth."

**CN:** "激励机制可能有助于鼓励节点保持诚实。如果一个贪婪的攻击者能够集结比所有诚实节点更多的CPU算力，他将不得不在利用它来窃回自己的支付以欺诈他人，与利用它来生成新货币之间做出选择。他应该会发现，按规则行事更为有利可图——这些规则使他获得的新货币比其他所有人加起来还要多——而非破坏系统和他自身财富的有效性。"

---

## Section 7: Reclaiming Disk Space / 第七节：回收磁盘空间

**EN:** "Once the latest transaction in a coin is buried under enough blocks, the spent transactions before it can be discarded to save disk space. To facilitate this without breaking the block's hash, transactions are hashed in a Merkle Tree, with only the root included in the block's hash."

**CN:** "一旦一枚货币的最新交易被足够多的区块所覆盖，之前已花费的交易就可以被丢弃以节省磁盘空间。为了在不破坏区块哈希的情况下实现这一点，交易被哈希到一棵默克尔树中，只有树的根节点被纳入区块的哈希。"

---

**EN:** "A block header with no transactions would be about 80 bytes. If we suppose blocks are generated every 10 minutes, 80 bytes * 6 * 24 * 365 = 4.2MB per year."

**CN:** "一个不含交易的区块头大约为80字节。假设每10分钟产生一个区块，80字节 * 6 * 24 * 365 = 每年4.2MB。"

---

## Section 8: Simplified Payment Verification / 第八节：简化支付验证

**EN:** "It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain, which he can get by querying network nodes until he's convinced he has the longest chain, and obtain the Merkle branch linking the transaction to the block it's timestamped in."

**CN:** "不运行完整的网络节点也可以验证支付。用户只需要保留最长工作量证明链的区块头副本——他可以通过查询网络节点来获取，直到确信自己拥有最长链——并获取将交易链接到其被加盖时间戳的区块的默克尔分支。"

---

**EN:** "He can't check the transaction for himself, but by linking it to a place in the chain, he can see that a network node has accepted it, and blocks added after it further confirm the network has accepted it."

**CN:** "他无法自行检查交易，但通过将交易链接到链中的某个位置，他可以看到一个网络节点已经接受了它，而之后添加的区块进一步确认了网络已接受该交易。"

---

**EN:** "As such, the verification is reliable as long as honest nodes control the network, but is more vulnerable if the network is overpowered by an attacker. While network nodes can verify transactions for themselves, the simplified method can be fooled by an attacker's fabricated transactions for as long as the attacker can continue to overpower the network."

**CN:** "因此，只要诚实节点控制着网络，验证就是可靠的，但如果网络被攻击者所压制，则会更加脆弱。虽然网络节点可以自行验证交易，但只要攻击者能持续压制网络，简化方法就可能被攻击者伪造的交易所欺骗。"

---

**EN:** "Businesses that receive frequent payments will probably still want to run their own nodes for more independent security and quicker verification."

**CN:** "频繁接收支付的企业可能仍然希望运行自己的节点，以获得更独立的安全性和更快的验证速度。"

---

## Section 9: Combining and Splitting Value / 第九节：价值的合并与分割

**EN:** "Although it would be possible to handle coins individually, it would be unwieldy to make a separate transaction for every cent in a transfer. To allow value to be split and combined, transactions contain multiple inputs and outputs."

**CN:** "虽然可以逐一处理每枚货币，但为每一分钱的转账都创建一笔单独的交易将非常笨拙。为了允许价值的分割和合并，交易包含多个输入和输出。"

---

**EN:** "It should be noted that fan-out, where a transaction depends on several transactions, and those transactions depend on many more, is not a problem here. There is never the need to extract a complete standalone copy of a transaction's history."

**CN:** "值得注意的是，扇出问题——即一笔交易依赖于多笔交易，而那些交易又依赖于更多交易——在这里不是问题。永远不需要提取一笔交易的完整独立历史副本。"

---

## Section 10: Privacy / 第十节：隐私

**EN:** "The traditional banking model achieves a level of privacy by limiting access to information to the parties involved and the trusted third party. The necessity to announce all transactions publicly precludes this method, but privacy can still be maintained by breaking the flow of information in another place: by keeping public keys anonymous."

**CN:** "传统银行模式通过限制相关各方和可信第三方对信息的访问来实现一定程度的隐私。公开宣布所有交易的必要性排除了这种方法，但仍然可以通过在另一个环节切断信息流来维护隐私：保持公钥的匿名性。"

---

**EN:** "The public can see that someone is sending an amount to someone else, but without information linking the transaction to anyone. This is similar to the level of information released by stock exchanges, where the time and size of individual trades, the 'tape', is made public, but without telling who the parties were."

**CN:** "公众可以看到有人正在向另一个人发送一笔金额，但没有将交易与任何人关联的信息。这类似于证券交易所发布的信息级别——单笔交易的时间和规模（即'交易记录带'）是公开的，但不透露交易各方是谁。"

---

**EN:** "As an additional firewall, a new key pair should be used for each transaction to keep them from being linked to a common owner. Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner."

**CN:** "作为额外的防火墙，每笔交易都应使用新的密钥对，以防止它们被关联到同一所有者。在多输入交易中，某些关联仍然不可避免，因为多输入交易必然揭示其输入归属于同一所有者。"

---

## Section 11: Calculations / 第十一节：计算

**EN:** "We consider the scenario of an attacker trying to generate an alternate chain faster than the honest chain. Even if this is accomplished, it does not throw the system open to arbitrary changes, such as creating value out of thin air or taking money that never belonged to the attacker."

**CN:** "我们考虑攻击者试图以比诚实链更快的速度生成替代链的场景。即使做到了这一点，也不会使系统面临任意更改的风险，例如凭空创造价值或夺取从不属于攻击者的资金。"

---

**EN:** "Nodes are not going to accept an invalid transaction as payment, and honest nodes will never accept a block containing them. An attacker can only try to change one of his own transactions to take back money he recently spent."

**CN:** "节点不会接受无效交易作为支付，诚实节点永远不会接受包含无效交易的区块。攻击者只能尝试修改自己的交易，以取回他最近花掉的钱。"

---

**EN:** "The race between the honest chain and an attacker chain can be characterized as a Binomial Random Walk."

**CN:** "诚实链与攻击者链之间的竞赛可以被刻画为一个二项随机游走过程。"

---

**EN:** "Given our assumption that p > q, the probability drops exponentially as the number of blocks the attacker has to catch up with increases. With the odds against him, if he doesn't make a lucky lunge forward early on, his chances become vanishingly small as he falls further behind."

**CN:** "在我们假设 p > q 的前提下，随着攻击者需要追赶的区块数量增加，其追赶成功的概率呈指数级下降。在胜算对他不利的情况下，如果他未能在早期侥幸取得领先，那么随着他越落越远，他的机会将变得微乎其微。"

---

## Section 12: Conclusion / 第十二节：结论

**EN:** "We have proposed a system for electronic transactions without relying on trust."

**CN:** "我们提出了一种不依赖信任的电子交易系统。"

---

**EN:** "We started with the usual framework of coins made from digital signatures, which provides strong control of ownership, but is incomplete without a way to prevent double-spending."

**CN:** "我们从由数字签名构成的常规货币框架出发，该框架提供了对所有权的强有力控制，但在缺乏防止双重支付的方法时是不完整的。"

---

**EN:** "To solve this, we proposed a peer-to-peer network using proof-of-work to record a public history of transactions that quickly becomes computationally impractical for an attacker to change if honest nodes control a majority of CPU power."

**CN:** "为了解决这个问题，我们提出了一个点对点网络，使用工作量证明来记录交易的公开历史——只要诚实节点控制着大多数CPU算力，攻击者要篡改该历史将很快变得在计算上不可行。"

---

**EN:** "The network is robust in its unstructured simplicity. Nodes work all at once with little coordination. They do not need to be identified, since messages are not routed to any particular place and only need to be delivered on a best effort basis."

**CN:** "该网络以其非结构化的简洁性而具有强健性。节点同时工作，几乎不需要协调。它们不需要被识别身份，因为消息不会被路由到任何特定位置，只需以尽力而为的方式传递即可。"

---

**EN:** "Nodes can leave and rejoin the network at will, accepting the proof-of-work chain as proof of what happened while they were gone."

**CN:** "节点可以随意离开和重新加入网络，接受工作量证明链作为它们离开期间所发生事件的证明。"

---

**EN:** "They vote with their CPU power, expressing their acceptance of valid blocks by working on extending them and rejecting invalid blocks by refusing to work on them. Any needed rules and incentives can be enforced with this consensus mechanism."

**CN:** "它们用CPU算力进行投票，通过在有效区块上继续工作来表达对其接受，通过拒绝在无效区块上工作来表达对其拒绝。任何所需的规则和激励都可以通过这种共识机制来执行。"
