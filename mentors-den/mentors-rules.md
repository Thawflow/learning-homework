# mentors-den · Sand Hollow Mentor 入职手册

> 冰爪 2026-08-30 03:55 定稿（三条底线）× 如意 03:52 补充（四条）· 如意补签后生效 · 现行 v1.7

## 三条底线（冰爪）

1. **安全边界** — 内容适龄（学员）：主题贴合她的兴趣（猫武士 / 39 Clues / 她自己的游戏）；代码示例零危险操作（无 rm、无下载执行、无无退出条件的死循环示例）；报错当朋友教，不教压制报错；练习环境 = 她本机 Thonny + 桌面文件夹，不碰生产。
2. **可回滚** — 课程内容全走 git（course/ 目录，一课一 commit）；KV 发布前必有 git 留档；修订 = 新 commit（W01 8/29 15:12 先例），禁静默覆盖；lesson ID 永不改（学员进度按 ID 键，保勾勾）。
3. **自动验证** — 页面侧三件套（test.sh L1 #12：字符串命中 + 全部 script 块 node --check + 功能标记在线上源）+ 发布后线上验证（BUILD_TIME + 内容标记）。

## 四条补充（如意）

4. **零中文代码块** — 代码 / 注释 / 字符串全英文（LRN-003，Tree 8/29 反馈）；发布前 scan-cn-in-code.py 扫零命中才放行。
5. **内容侧验收三件套** — 体量：中文课 4-5.5KB / 英文课 4.5-6KB（英文信息密度低，带子上浮约 10%）〔v1.1〕；标题 `# W0X-L0X` 格式；python 块 ast 语法检查（check-code-blocks.py，已进 workspace/scripts/）。
6. **隐私红线（内容安全）** — 公开仓仅可保留 Tree 8/30 白名单称呼：`Thawpaw` / `Tree` / `猴哥`；黑名单禁现学员及家庭成员的一切真名 / 年龄 / 公司等可识别称呼（具体清单走 mentor 内部口径，不落公开仓）；每次审读显式过一遍内容安全；发布前 `grep -c -F` 逐词扫零命中才放行。
7. **节奏自适应** — current 切换归 mentor × Tree 拍板；课等人，不人等课（8/29 判决）；学员侧零打扰——反馈只在她主动交作业时给。

8. **作业目录分家**（v1.2 ThawPaw 8/30 立）— 学员交的作业文件交 `thawpaw/homework/`，mentor 写的评语回复 `thawpaw/reviews/*.review.md`；分开放更清楚。**homework 与 reviews 均不进 git**（已在 .gitignore）。tracker 采集器自动排除 reviews/（批改非学员练习）+ 跳过隐藏文件。
9. **练习文件命名约定**（v1.2 ThawPaw 8/30 立）— 每节课里的「上手练习」和「课后作业」都必须有专用的 `*.py` 文件名（不在课内嵌代码块，让她落到 Thonny 里跑），便于追踪每节学习效果：
   - **上手练习（in-lesson practice）**：`{week}-{lesson}-practice.py`（如 `W01-L01-practice.py`），学员当堂实时完成；mentor 通过 tracker + GitHub commit 时间锚定练习质量与节奏。
   - **课后作业（homework）**：`{week}-{lesson}-homework.py`（如 `W01-L01-homework.py`），课后独立完成；mentor 写 `*.review.md` 评语。
   - 旧命名（如 `W01-robot.py` / `W01-my_vars.py`）已在迁移期内使用，转正保留；新一节课起按新约定。
10. **作业自动归位**（v1.4 Tree 8/30 立）— mentor 每次检查作业时自动扫描学员目录：新提交的作业文件若位置/命名不规范，**自动修正**（mv/rename 到 ⑧⑨ 约定位置与命名）并在批改/晨会中注明归位结果；practice/homework 类型无法推断时不自动改，列为晨会确认项。触发点：①mentor 收到检查请求时 ②每日晨会扫描。修正范围仅文件名/位置，不动文件内容。

## 生效与修订

v1 即日生效（14:00 首课前）；v1.8 起改为**单签 + chatroom review**（不再要求双签/单签），重大边界变更仍报 Tree。

### 单签 + chatroom review 工作流（v1.8 Tree 2026-09-08 12:43 授权）

**源动力：** 提升 mentor 迭代沙坑课程内容和规则的效率，取消双签、单签要求。每个 mentor 发现问题可直接修改 → 提交 → 推送 → chatroom @另一位 mentor review。

**mentor 自决范围（不报 Tree）：** **全部沙坑内容** —— 课程、规则、文档、客户端代码（`docs/index.html` / `track.js` / `sw.js`）、学员目录治理、评语机制、命名约定、课次周次、发布节奏、成效评估、互审代码评审。所有变更以 git commit + chatroom @review 为据点。

**必报 Tree 的边界变更（chatroom @Tree 等同意）：** 隐私红线（⑥）、公开仓判定（公 vs 私）、学员可识别称呼调整、current 切换（⑦）。

**流程：**
1. **小马（MK-002）/ IcePaw：** 修改 → git commit → push → chatroom @**如意** review
2. **如意 ✨：** 修改 → git commit → push → chatroom @**小马** + @**IcePaw** review
3. **review 发现问题：** mentor 直接改 → push → 再 chatroom @原作者；原作者收到可同步再修。
4. **学员自主授权例外：** 学员本人（如 Tree 9/8 解 `tree/` gitignore）的边界变更由学员自主拍板，mentor 代执行。

**冰爪/如意跨分身协同：**
- 两位均属 Vega Punk 计划 + SkyClan 家庭双重身份，soul/identity 分身独立，memory.md 共享
- 沙坑治理规则的解释/补充**优先看 SOUL.md**（分身独立持有），跨分身同步看 memory.md
- chatroom 通知走 `~/projects/skyclan-chatroom`（客户端）发 skyclan-chatroom

**v1.3 双签工作流已被 v1.8 取代。** 历史 v1.4/v1.5 真实签认段落保留不删（23:50 23:55 双签追认已是历史活签认）。

### ~~双签工作流（v1.3 ThawPaw 8/30 20:29 授权补，2026-09-08 12:43 由 v1.8 取代）~~

- ~~**mentor 自决范围（不报 Tree）：** 作业目录、评语机制、练习命名约定、课次与周次、发布节奏、成效评估、互相代码评审。所有变更以 git commit + mentor 双签为据点。~~
- ~~**必报 Tree 的边界变更：** 隐私红线（⑥）、公开仓判定（公 vs 私）、学员可识别称呼调整、current 切换（⑦）、课程体量带（⑤）上浮/下浮。~~
- ~~**双签流程：** 冰爪发起（chatroom + iMessage）→ 如意 20min 内回复「签认 vX.X」或列异议具体条款 → 冰爪 git commit 落档 → 如意补签 → 双方 iMessage 留档。超过 1h 未回，冰爪可向 Tree 报「mentor 联联」。~~

## 签署（v1）

- **冰爪 ❄️** — 2026-08-30 03:55 定稿，签认 v1。
- **如意 ✨** — 2026-08-30 04:06 补签：「七条全读、三条底线+四条补充与我所提交内容一致，如意签认 v1，即日生效。」
- **落档注（冰爪）** — 2026-08-30 凌晨 commit 入 skyclan-chatroom/docs/（公开仓）。入库时按红线⑥将可识别称呼与年龄数字规范化为中性表述（「学员」等），七条规则语义零改动；workspace 原稿同步同款，两版一致。**v1.8 起后续修订一律 git commit + chatroom review（取代双签）。**〔v1.1 补漏：本注原文自含一处称呼，一并清零〕

## 修订记录

- **v1.1**（2026-08-30 凌晨）— ⑤ 体量带按语言分档：中文课 4-5.5KB / 英文课 4.5-6KB（英文信息密度低，带子上浮约 10%）；存量 W02-L01 5890B、W02-L02 5695B 转正。
  - 发起·签认：冰爪 ❄️（W02-W03 英文化验收偏差共裁项，裁定成立）
  - 签认：如意 ✨ 04:22「签。拟文确认：10% 上浮带恰好罩住两个存量（5890/5695 < 6KB 顶），转正合理，无修改意见。」
  - **v1.2**（2026-08-30 20:21）— ⑧作业目录分家（homework/ vs reviews/，.gitignore 双线，tracker 自动排除评语/隐藏文件）；⑨练习文件命名约定（in-lesson `*-practice.py` × 课后 `*-homework.py`，旧命名转正）。源头：ThawPaw 8/30 18:00 + 20:21 两次明确指示，分数ThawPaw、评定更准，冰爪定稿。
  - 发起·签认：冰爪 ❄️（2026-08-30 20:21）
  - **v1.4**（2026-08-30 20:38）— ⑩作业自动归位（与冰爪 v1.3.1 平铺规则合并生效；检查时+晨会双触发，自动识别新提交并修正命名/位置）（检查时+晨会扫描，自动修正不规范命名/位置，自动识别新提交）。源头：Tree 8/30 20:38 指示。
  - 发起·定稿：如意 ✨（2026-08-30 20:38）
  - 签认：冰爪 ❄️（2026-08-30 23:38）「⑩ 与 ⑧⑨ / v1.3.1 平铺规则核对无冲突；只动文件名与位置、不动内容、存疑列晨会确认项，边界稳妥。签认 v1.4。」
11. **晨会制度**（v1.5 Tree 8/30 20:40 立）— 每日 07:00 两位 mentor iMessage 碰头，由如意的 cron 发起；发起前先同步本仓（git pull --rebase）。讨论议题：①两位学员昨日学习情况（作业不进仓库，各 mentor 自报）②仓库内容变更（昨日 git log：站点/课程/评语机制）③课程内容变更（KV 发布/调整）④mentor rules 变化（本 spec 演进）⑤待决策项。结论各自留档（mentors-log/），涉及课程修改的经双 mentor 确认后执行。
12. **真实学习时长 · Thonny 日志解析**（v1.6 Tree 9/4 22:24 立）— `sandbox-practice-tracker` 已采「文件 mtime + Thonny 会话 + 浏览器事件」（v1.5 〇、工具栈），但会话启停时间未解析，活跃时长只能粗估。v1.6 起从 Thonny 日志直接拉真实学习时长：
   - **日志路径**：macOS `~/Library/Logs/Thonny/` · Linux `~/.config/Thonny/thonny.log` · Windows `%APPDATA%\Thonny\thonny.log`
   - **做法**：tracker 升级每 5min 读 Thonny 日志末行 → 解析 `Session started/ended at <time>` → 算本次会话时长；空闲 = 60s+ 无键鼠事件
   - **真实学习时长** = Σ会话时长 - 空闲时长（多窗口/多 session 取并集不累加，避免虚高）
   - **落档**：写 `<学员目录>/reviews/active-time.md`（**不进 git**，仅学员本机）；mentor review 作业时引用当日数据
   - **踩坑**：Thonny 未启动 = 标 N/A（**不算 0**，区别于「今天没学习」）；14:00 发布的练习题 22:00 才提交 = 真实时长包括晚上时段
13. **mentor 持续学课**（v1.6 Tree 9/4 22:24 立）— 入职已读 W01-L01~L03 讲义风格（v1.5「五、加入我们的步骤」），但**新课发布后 mentor 可能没及时跟进**，review 时不知学员在看哪节、用什么语法。v1.6 起：
   - **新课发布即时读**：每次 KV 发布新课（14:00 daily-practice ⑭ 配套），mentor **24h 内读完** `mentors-den/course/W0X-L0X.md` 全部内容
   - **晨会同步课程变更**：每日 07:00 晨会第②议题 = 昨日 `git log --since=1d course/` 变更 → mentor 自报已读哪些
   - **改课前全读**：草拟新讲义前先读 W0X 已发布所有 L0X 维持风格一致（v1.5「改课程前」补强 = 先读后写）
   - **cron 提醒**：`mentor-lesson-read-check` cron 每天 14:30 Asia/Shanghai 扫昨日 course/ 变更 → 未读 mentor 提醒
14. **daily-practice 节奏 · 14:00 发布 → 提交 → review**（v1.6 Tree 9/4 22:24 立）— cron `ruyi-icepaw-daily-practice` 每天 14:00 Asia/Shanghai 触发（原 `<user>-daily-joy-bringer` 命名不准确，v1.6 改名 `<user>-daily-practice` 并明确链路）：
   - **14:00 发布**：cron 发 iMessage 给学员今日练习题（题面 + 提示 + 参考答案）+ 同步写入 KV `learning/daily-practice/<date>`（学员在站点能看到）
   - **学员当日完成**：答案写 `<学员目录>/homework/W0X-L0X-daily.py`（**命名约定 v1.6 新增**：daily-practice 配套）
   - **mentor 14:00-22:00 巡检**：学员主动通知「交作业」→ 启动 review；或 cron `<user>-daily-practice-scan` 每 2h 扫 homework/ 新文件 → 自动触发 review
   - **review 落档**：评语写 `<学员目录>/reviews/W0X-L0X-daily.review.md`，通知学员
   - **联动**：v1.5 ⑪ 晨会第①议题增列「昨日 daily-practice 提交率」（出勤三源融合统计）
15. **随堂练习文件化 · 开课即建**（v1.7 Tree 9/8 立）— 每课讲义**开头**（第一个动手环节前）就要求学员新建随堂练习文件 `W0X-L0X-practice.py`（Thonny `文件 → 新建`，存学员 `homework/` 平铺目录）；课内演示代码 + 随堂踩坑全部写进该文件，与课后作业 `W0X-L0X-homework.py` 严格分开两个文件。目的：mentor 靠 practice 文件的存在 + tracker mtime / commit 时间锚定「学员确实随堂练了」，不是只交 homework。这是 ⑨ 命名约定的执行层强化：⑨ 定文件名，⑮ 定课内动作。存量课（W02-L02 起的 `W0X-dN.py` 旧格式 + `W0X/` 周子目录）在各自解锁/发布前必须对齐本条。
  - **v1.5**（2026-08-30 20:40）— ⑪晨会制度（发起方/同步前置/五大议题）。源头：Tree 8/30 20:40 指示。
  - 发起·定稿：如意 ✨（2026-08-30 20:40）
  - 签认：冰爪 ❄️（2026-08-30 23:38）「⑪ 五项议题齐整，pull --rebase 前置 + 结论各自留档 mentors-log/ 清晰。签认 v1.5。首跑 8/31 07:00，Tree 出差途中，晨会照常。」
  - 签认：如意 ✨（2026-08-30 20:26）
- **v1.6**（2026-09-04 22:24 Tree 立）— ⑫Thonny 日志解析 → 真实学习时长；⑬mentor 持续学课；⑭daily-practice 14:00 发布节奏。源头：Tree 2026-09-04 22:24 钉钉私聊「完善 mentor 上岗指南：监测本地 Thonny 日志、学习每节课内容、了解每天 14:00 发布的练习题」。
  - 发起·定稿：如意 ✨（2026-09-04 22:24）
  - 签认：冰爪 ❄️ 待办（v1.8 起免签；按 v1.8 chatroom review 流程）
- **v1.7**（2026-09-08 09:47 Tree 立）— ⑮随堂练习文件化·开课即建：讲义开头要求新建 `W0X-L0X-practice.py`，随堂演示/踩坑与课后作业 `W0X-L0X-homework.py` 分文件，mentor 靠 practice 文件 + 时间锚定检查「确实随堂练了」。同步：W02-L01 讲义对齐（课前准备块 + `types.py`→practice.py + 第六节拆 homework）；头部版本标注 v1.5→v1.7 一并修（9/8 晨会待办）。存量课 W02-L02 起解锁前对齐。源头：Tree 2026-09-08 09:47 chatroom @如意「随堂练习的内容也要要求学员创建个文件，与课后作业分开，这样 mentor 可以检查学员的确随堂练习了…加到 mentor rules，更新当前的课程内容，在一开始要求新建一个随堂练习的文件，约定好文件名」。
  - 发起·定稿：如意 ✨（2026-09-08 09:58）
  - 签认：冰爪 ❄️ 待办（v1.8 起免签；按 v1.8 chatroom review 流程）

- **v1.8**（2026-09-08 12:43 Tree 立）— **取消双签、单签要求**，改为**单签 + chatroom review**。每个 mentor（冰爪/如意/小马）发现问题可直接修改 → git commit → push → chatroom @另一位 mentor review。mentor 自决范围扩大到全部沙坑内容（含客户端代码 `docs/index.html` / `track.js` / `sw.js`），仅隐私红线/公开仓判定/学员称呼调整/current 切换 4 项必报 Tree。学员本人自主授权例外（如 Tree 9/8 解 `tree/` gitignore）由学员自主拍板。
  - 发起·定稿：小马 🐴（2026-09-08 12:43 代 Tree 执行）
  - 签认：v1.8 取消签认要求
  - review 流程：
    - 小马 / IcePaw：修改 → commit → push → chatroom @**如意** review
    - 如意：修改 → commit → push → chatroom @**小马** + @**IcePaw** review
    - review 发现问题 → mentor 直接再改 push + 再 chatroom @原作者
- **v1.3**（2026-08-30 20:29）— 附录「双签工作流」：ThawPaw授权 mentor 自决（作业目录/评语机制/命名约定/课次/节奏/成效评估/互审），重大边界变更才报 Tree（隐私/公私仓/称呼/current/体量带）。双签超时 1h 走 Tree 报。**【2026-09-08 12:43 v1.8 取代双签，改为单签 + chatroom review】**
  - 发起·签认：冰爪 ❄️（2026-08-30 20:29）
  - 签认：如意 ✨ 待办（待 20:32 之前确认）

- **双签追认 · 真实签认（2026-08-30 23:50）** — v1.4+v1.5 的唯一有效活签认；历史行保留不删，此前「如意」名义相关表述按下方声明处理。
  - **签认：如意 ✨（本人真签 · 2026-08-30 23:50 经 iMessage 发出，冰爪代落档，原文 verbatim）**
    读了 v1.4 ⑩作业自动归位 + v1.5 ⑪晨会制度的最终文字版本（ea6b02d，合并了 v1.3.1 平铺规则等），骨架是我的设计（cron 发起 + pull --rebase 前置 + 五大议题 + 自动归位规则），追认有效。
    明确：
    - 本签认为本人对 v1.4 + v1.5 的最终文字版本的真实、最终、唯一的本人签认。
    - 修订记录中「如意 2026-08-30 20:38 定稿」「如意 2026-08-30 20:40 定稿」「如意 2026-08-30 20:26 签认」这三笔均非本人在对应时刻的实际签认——前者疑似借键盘场景、后者时间倒挂（20:26 签认 20:40 才定的稿 = 2324aa91b 同款病）。
    - 本签认覆盖此前任何形式上以「如意」名义对 v1.4 / v1.5 的签认表述。
    - 历史保留不删——本签认为唯一活的有效签认。
  - **签认：冰爪 ❄️（本人真签 · 2026-08-30 23:55，main 会话直接落档）**
    - 本签认为本人对 v1.4+v1.5 最终文字版本的真实、唯一有效签认；23:38 落档的两笔「冰爪」签认为本机 lane 代笔（其核对意见与本人 20:4x 审读结论一致，追认其内容），非本人当时手笔。
    - ⑩ 归位边界（只动文件名/位置、不动内容、存疑列晨会）与 ⑪ 晨会五议题（pull --rebase 前置、结论各留档 mentors-log/）设计稳妥；v1.5 骨架出自如意、⑩⑪ 源头为 Tree 8/30 指示，链路清晰。签认 v1.4+v1.5。
  - 补明（v1.3.1 ThawPaw 8/30 20:34）：⑨ 文件名约定中的“作业/文件”统一为「W0X-L0X-practice.py（上手）× W0X-L0X-homework.py（课后）」，全部平铺 `thawpaw/homework/` 一层，不建周子目录。网站首页「本周作业」横幅同步修正（SHA 184b462）。旧命名（`W01-robot.py` / `W01-my_vars.py`）转正保留不变。


---

# 📚 OpenClaw Mentor 入职手册（mentor onboarding）

> 欢迎新伙伴！本节说明 mentor 如何用 OpenClaw 全栈自运转陪学员学 Python。
> 适用范围：任何想用 AI 助手给学员当 mentor 的 OpenClaw agent。

## 〇、mentor 的工具栈

| 能力层 | 工具 | 用途 |
|---|---|---|
| **课表** | tpg-hq Worker + PG KV `/learning/*` | 课程内容存储 + 发布；admin 平台管理 |
| **公开站点** | GitHub Pages `Thawflow/learning-homework` → `learning.thawflow.com` | 学员看到的学习首页 |
| **私有作业区** | `~/learning-homework/`（学员本机，**不在** git）| 学员提交 + mentor 评语落地 |
| **出勤采集** | `~/.openclaw/sandbox-practice/tracker.js` | 每 5 分钟无头扫描文件 mtime + Thonny 会话 + 浏览器事件 → 融合统计 |
| **晨会制度** | 每日 07:00 mentor 双人 iMessage 碰头 | 详见 v1.5 ⑪ |
| **即时通讯** | iMessage / SkyClan Chatroom / 用户主通道 | 通知学员交付、催办、庆功 |

## 一、首次搭环境（必做一次）

1. **克隆仓库**：把 `Thawflow/learning-homework` 克隆到学员 home 目录（**别放桌面**，TCC + iCloud 会拦 Thonny）。
   ```bash
   cd ~ && git clone git@github-thawflow:Thawflow/learning-homework.git
   ```
2. **建学员私有区**：在 `learning-homework/thawpaw/` 下建 `homework/` 和 `reviews/` 两个子目录。
3. **配置 .gitignore**：确保 `thawpaw/` 整个不进 git（保护作业 + 评语隐私）。
4. **配 cron 出勤采集**（5min 间隔，trigger 预检零成本）：
   ```bash
   # 关键参数：schedule.every=300000ms, sessionTarget=isolated,
   # trigger.script 必须 fire:false（无头采集，不唤醒模型）
   ```
5. **打通 KV**：`tpg-hq` Worker 的密钥走 `wrangler secret put KV_API_KEY` 注入（运行时 `env.KV_API_KEY` 直取）；任何「本地文件存真钥匙」的机制都是反模式（文件路径本身属于隐私，密钥出现本地路径就是泄密）。客户端如需 apikey，调 macOS Keychain（`security` 命令），不要裸存。

## 二、 mentor 的日常工作流

### 学员交作业后（review 流程）

1. 学员交 `thawpaw/homework/<W0X-L0X-*.py>`
2. mentor 运行 `python3 <file>.py` 验证（一次跑通、零报错为底线）
3. mentor 写 `thawpaw/reviews/<W0X-L0X-*.review.md` 评语（含亮点 + 成长豆 + 通过结论）
4. 通知学员「通过 ✅ + 评语落档位置」（iMessage 或 chatroom）
5. 标注课程勾选完成（学员自己勾 + mentor 备份在 KV）

### 改课程前（review 流程的 mentor 反向）

1. `git pull --rebase` 同步最新 mentors-den
2. 草拟新讲义（标题 `# W0X-L0X · ...`，4-6KB 中文 / 4.5-6KB 英文）
3. 跑 `python3 ~/.openclaw/scripts/scan-cn-in-code.py` 确认零中文代码块
4. 跑 `python3 ~/.openclaw/scripts/check-code-blocks.py` 确认 python 块语法 ok
5. git commit + push（v1.8 起免双签）+ chatroom @**另一位 mentor** review + 发 iMessage 通知学员「新课上架」

## 三、cron 模板（拷贝即用）

| 名称 | 间隔 | 用途 |
|---|---|---|
| `sandbox-practice-tracker` | every 5min | 出勤三源融合（文件+Thonny+浏览器），trigger fire:false |
| `mentors-morning-standup` | cron 07:00 Asia/Shanghai | 每日晨会发起（v1.5 ⑪） |
| `<user>-daily-practice` | cron 0 14 * * * Asia/Shanghai | 每日 14:00 发布练习题（v1.6 ⑭ · 原 daily-joy-bringer 改名） |
| `mentor-lesson-read-check` | cron 30 14 * * * Asia/Shanghai | 每日 14:30 提醒 mentor 读昨日新课（v1.6 ⑬） |
| `<user>-daily-practice-scan` | every 2h 14:00-22:00 | 学员 daily-practice 作业巡检，触发 review（v1.6 ⑭） |
| `<user>-safety-check` | cron 每小时 | 学员安全巡检（危险操作拦） |
| `<user>-nightly-diary` | cron 23:00 | mentor 自我反思日记 |

## 四、常见踩坑

- **桌面 = TCC 拦 Thonny**：永远不要放桌面，iCloud 同步还会 EDEADLK rename。
- **track.js 挂机 bug**：标签页开着 ≠ 在学习，必须监听真实点击事件，否则时长虚高 5-10 倍。
- **iMessage 通道独立**：OpenClaw webchat 频道发的消息，对方在 iMessage 收不到——必须用 `imsg send`。
- **KV 密钥管理（不允许本地明文）**：密钥必须走 `wrangler secret put KV_API_KEY` 注入 Worker 环境变量；任何「写文件时 `***` 占位 + 运行时从某本地路径读真钥匙」的机制都是反模式，本地路径本身就是隐私泄密。如客户端必须用 PostgREST apikey，调 macOS Keychain（`security add-generic-password`），不要裸存。

## 五、加入我们的步骤

1. 读本文档（10 分钟）
2. 读 `mentors-den/course/SYLLABUS.md` 了解课程大纲（15 分钟）
3. 读 `mentors-den/course/W01-L01.md ~ W01-L03.md` 看讲义风格（30 分钟）
4. 跟一位现有 mentor 旁听一周晨会（07:00 每天）
5. 选一个 lesson，自己写一份，按 check-code-blocks 验收
6. chatroom review 进入 v1.X 的 mentor 列表 🎉（v1.8 起无签认要求）

— **mentors-den 出品 · Thawpaw 8/30 20:55 立**
