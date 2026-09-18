# mentors-den · ABC Rating + PK v0.2 Outline

> 冰爪 2026-09-17 13:17 BJT 起草 · 待 main session 完整化 + 苗苗 review pass + 猴哥拍板
> 现行基线：mentor rules v1.8（mentors-rules.md）+ ⭐ rating 实际状态 = **规划中未实施**（mentors-rules.md v1.8 描述提及但 mentors-den/course/ 内无 rating 代码；thawpaw/reviews/ 用二元 pass/fail per question = 4/5 题过 ⭐=通过 1 等）
> 本 v0.2 在 v0.1 草案（TODO L75 body）基础上完整化

## 1. 目标与定位

**目标**：在 ⭐ rating 基础上新增 ABC 五级评级 + PK 机制，让学员侧进度可视化 + mentor 侧精力分配更精准。

**定位**：
- ⭐ rating = progress bar（累计通过率，单维）
- **★** **ABC rating =** 每单评分（多维，3 维 × 5 级 = 15 评估点）+ 触发 PK 池
- **PK =** peer-review 池（同水平学员互评 + mentor 复审，跨班协作）

## 2. 评估维度（3 维 × 1-5 分）

| 维度 | 1 分 | 3 分 | 5 分 |
|------|------|------|------|
| **语法（syntax）** | 基础错误多需逐行改 | 标准代码风格，少量提示 | 全规范，能当范例 |
| **逻辑（logic）** | 思路不清，跑不通 | 基本跑通，边界 case 漏 | 完整思考边界 + 优化 |
| **风格（style）** | 不规范，命名乱 | 命名清楚，结构合理 | DRY + 抽象到位 |

**每维 1-5 分，总分 3-15 分。**

## 3. ABC 映射（5 级）

| 等级 | 总分区间 | 含义 | 触发 |
|------|----------|------|------|
| **A** | 14-15 | 优 | ⭐ 累计 +1，进 PK 池候选 |
| **B** | 11-13 | 良 | ⭐ 累计 +0.5（折半），观察下次 |
| **C** | 8-10 | 中 | ⭐ 不变，需 mentor 复审 + 自评 |
| **D** | 5-7 | 待改进 | 退回重做，不进 ⭐ |
| **E** | 0-4 | 需重学 | 触发 1v1 mentor 补救课 |

## 4. PK 机制

**触发条件**：
1. **连续 2 单元 A**（14-15 分 × 2 单元）→ 自动进入 PK 池
2. **B 区间稳定**（连续 3 单元 B）→ 进入"互评组"（学员间 peer review）
3. **A 单次但解题创新** → mentor 推荐入 PK 池（手动触发）

**PK 流程**：
```
PK 池 → 系统随机配对（算法：水平相近 + 不同学习路径）
     → 学员 A 写新挑战 → 学员 B 评审（基于 ABC rubric）
     → 反向 B 写 → A 评审
     → mentor 复审（30% 抽样 + 边缘 case 全检）
     → 双方评分写 PK log + 双方 ⭐ 累计 +1
```

**反作弊**：
- 互评隐藏作者身份（mentor 后台映射）
- mentor 抽样 30% 强制复核
- 评分偏离 mentor 历史均值 ±2 分 → 触发 mentor 介入

## 5. 实施路径

**Phase 1（v1.8 配套，立即可行）**：
- [ ] `mentors-den/abc-rubric.md` 落档（rubric 详表，3 维 × 5 级判分标准）
- [ ] `review-template-v1.7.md` 加 ABC 维度栏（替换 ⭐ 单选）
- [ ] tracker cron 输出新增 `abc_score` 字段
- [ ] PG KV 加 `abc:pool:<member_id>` 跟踪 PK 池状态

**Phase 2（v1.8 验证 1 周后）**：
- [ ] PK 配对算法 + cron 实现
- [ ] 互评 UI（学员侧网页）
- [ ] mentor 抽样复核工具

**Phase 3（v1.8 验证 1 月后）**：
- [ ] PK 排行榜（学员侧可视化）
- [ ] 跨班 PK 试点

## 6. 与现行 ⭐ 双轨制设计

```
学员作业提交
    ↓
tracker cron (sandbox-practice-tracker)
    ↓
mentor review (review-template-v1.7.md)
    ├── ⭐: 4/5 题过 → +1 累计
    └── ABC: 三维各 1-5 分 → 总分 3-15 → 等级 A/B/C/D/E
    ↓
PK 池触发（连续 2 单元 A 或 B 区间稳定）
    ↓
互评 → mentor 复审 → ⭐ +1 双方
```

**双轨并行**：
- ⭐ 是 progress bar（累计）
- ABC 是 quality meter（每单质量）
- 两者互补：⭐ 多了不一定单好（堆量），ABC 高 = 单好 + 自动推动 PK

## 7. 风险与回滚

| 风险 | 缓解 | 回滚 |
|------|------|------|
| 学员侧觉得评级太严 | Phase 1 仅试用 2 周收集反馈 | 退回纯 ⭐ |
| mentor 工作量翻倍 | ABC 评分只对 A/B 区间必评，C/D 可抽查 | 暂缓 ABC 实施 |
| PK 配对不公平 | 算法持续优化 + mentor 人工调整 | 暂停 PK 保留 ABC |
| 学员互评不客观 | mentor 抽样 30% + 评分偏离告警 | 取消互评，mentor 单评 |

## 8. 待办 checklist

- [ ] 苗苗 review pass（她是直接使用者，必须先认可）
- [ ] 猴哥拍板 Phase 1 起步时机（是否等 v1.8 chatroom review 全面落档后）
- [ ] mentor（冰爪+如意）培训 — ABC 评分标准对齐
- [ ] Phase 1 试点课节挑选（建议从 W02-L03 开始）
- [ ] tracker cron 输出格式 PR（与 sandbox-practice-tracker 维护者协同）

---

**起草**：冰爪 ❄️ 2026-09-17 13:17 BJT（todo-hourly 13 班 partial advance on L75）
**关联**：TODO L75 / L74（v1.7 命名规范化）
**下一步**：苗苗 review → 猴哥拍板 Phase 1 → mentor 培训 → W02-L03 试点