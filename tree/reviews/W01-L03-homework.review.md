# W01-L03 作业批改 · Tree

## 基本信息
- 学员：Tree
- 课次：W01-L03（input + 计算器 + 周末机器人）
- 作业文件：`tree/homework/W01-L03-homework.py`
- 批改日期：2026-09-09
- 批改 mentor：如意 ✨
- 判定：✅ 5/5 通过 🎉

## 逐题点评
- 题 1 · 三问复述：✅
  - 亮点：f-string 三问一句输出，`{game}` `{animal}` `{mood}` 三段顺序正确。
  - 待补：f-string 里「今天的心情 {mood}」前多一个空格，会变成「今天的心情 happy」双空格。下次写完回头扫一遍标点附近。
- 题 2 · 数猫：✅
  - 亮点：`int(input(...)) + 1` 一步到位，口诀「要算数先 int」掌握扎实。
- 题 3 · 一只 ___ 的 ___ 在 ___：✅
  - 亮点：adj / animal / action 三个 input 顺序合理，f-string 拼接自然。
  - 待补：题目要求 5 道题都要「实际跑通至少 1 次」，本节练习已在 `python3` 实跑通过，留个 run 记录就更好。
- 题 4 · Supermarket Calculator：✅
  - 亮点：`float(input("单价:"))` × `int(input("数量:"))` 类型转换两步都到位，f-string 三行小票清晰。
- 题 5 · Family Calculator：✅
  - 亮点：四则 + 平均值一气呵成，`(a+b)/2` 不引库，Python 风格正解。

## 超前技能
- f-string 跨全题：5 道题全部使用 f-string，已掌握 W02-L03 才教的语法，超纲一整节。
- 类型转换组合拳：`float(input(...))` × `int(input(...))` 已在题 4 用熟练，W02-L01 可走「高阶偷跑」。

## 成长豆
- 把「家庭计算器」抽成独立模块（`calculator.py`）再练习，模块化直觉到位，三件套齐全。
- 唯一小瑕疵是题 1 的 f-string 多余空格，下次写完回头扫一遍。

## 交付门禁
- 全部题目写完：✅
- 实际运行并验证：`python3 tree/homework/W01-L03-homework.py` 跑通，零报错。
- 最终结论：放行 W02「数字与文字魔法」🎓，并在 W02-L01 启用「🪜 高阶偷跑」路径。