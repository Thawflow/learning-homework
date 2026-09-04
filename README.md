# 🏖️ 沙坑训练场 · learning.thawflow.com

**GitHub 仓库：** <https://github.com/Thawflow/learning-homework>

> **给学员的一句话入门：** 告诉你的 OpenClaw 克隆这个仓库到 `~/learning-homework`，让它读 `mentors-den/mentors-rules.md` 上岗手册 —— 它就能帮你创建学员目录（`<你的学员目录>/homework/`）并自动 review 你的作业。

---

## 参与者

| 角色 | 名字 | 备注 |
|------|------|------|
| 🐱 学员 | **ThawPaw** | 猫武士主题方向 |
| 🌳 学员 | **Tree** | 自学编程方向 |
| ❄️ mentor | **IcePaw** | 守护 ThawPaw |
| ✨ mentor | **如意** | 守护 Tree |

---

## 迭代参与

如希望参与项目迭代（添加新学员 / 调整课程结构 / 改进 mentor 流程 / 投稿新主题），请联系 Tree：`wangjieqi@brandct.com`。

---

## 网站说明

沙坑训练场是家庭编程课的练习站：每周课程更新到线上，学员本地写作业、按需提交，mentor 批改后反馈。

- 线上站：https://learning.thawflow.com（CDN 缓存约 10 分钟，页脚 BUILD_TIME 可核对版本）
- 站点即仓库：push 到 main 即发布，课程内容可回滚
- mentor 双签规则 + 入职手册：`mentors-den/mentors-rules.md`（v1.6，2026-09-04 Tree 修订）

## 学习路径

课程按周推进（W01 起），每周拆成 L01/L02… 小课，配作业与批改：

1. 基础（W01 起）：input / 变量 / f-string，第一个小项目是 calculator 和 quiz bot
2. 工具链（W07）：git clone 本地克隆法接入，学会自己拉课程
3. 实战（W12）：OpenClaw 案例课，把前面学的串成真工具
4. 卡住时：annex 兜底资料随时查，sandbox 允许无限重练

进度因人而异，重练不算落后。

## 目录结构

```
learning-homework/
├── README.md              ← 你正在看的
├── docs/                  ← GitHub Pages 站点源（push 即上线 learning.thawflow.com）
├── mentors-den/           ← mentor 内部文档（不入站，不公开）
│   ├── mentors-rules.md   ← 双签规则 / 红线 / 作业评阅规范（v1.6 含 Thonny 监测 + 14:00 节奏）
│   └── onboarding/        ← mentor 入职手册
├── thawpaw/               ← 学员 A 的作业区
│   ├── homework/          ← 上手练习 + 课后作业（gitignore）
│   └── reviews/           ← mentor 评语（gitignore）
└── tree/                  ← 学员 B 的作业区
```

每位学员一个文件夹，命名约定见 `mentors-den/mentors-rules.md`。

## 本地作业

学员作业存到自己目录下：

- 上手练习：`{W##}-L##-practice.py`（如 `W01-L01-practice.py`）
- 课后作业：`{W##}-L##-homework.py`（如 `W01-L02-homework.py`）

全部平铺在 `thawpaw/homework/` 一层，**不建周子目录**。旧命名保留兼容，新课按新约定。

## 提交流程

1. 在 Thonny 写代码 / 跑通
2. 保存到 `~/learning-homework/{学员文件夹}/homework/`
3. **交完跟 mentor 说一声**才批改（不发 = 没交）
4. mentor 在 `{学员文件夹}/reviews/{W##}-L##-review.md` 写评语
5. tracker 自动记录练习时长与活跃度（不进 Git）

> ⚠️ 学员文件夹已 `.gitignore`，**作业不会 commit 到 GitHub**。本地独有，私密保存。

---

## 内部资料（不入站点）

- mentor 双签规则 + 入职手册：`mentors-den/mentors-rules.md`（**让 OpenClaw 读这个 → 自动 review**，v1.6，2026-09-04 Tree 修订：含 Thonny 日志解析 → 真实学习时长 ⑫ + mentor 持续学课 ⑬ + daily-practice 14:00 节奏 ⑭）
- KV 发布：`docs/index.html` 内嵌 JS + KV 内容 API（`https://tpg-hq.thawflow.com/learning/*`）

## 站点技术栈

- 静态站：纯 HTML + 内嵌 JS（无构建步骤）
- CDN：`learning.thawflow.com`（CDN 缓存 10min，sw.js 网络优先）
- 内容 API：Cloudflare Worker `tpg-hq.thawflow.com/learning/*`（KV 存储，发布走同源 API）
- 进度跟踪：localStorage（`learning-checks`）+ track.js 埋点（click:* 上报）
