<div align="center">

# ZK-Labs Research

**加密货币与期权深度研究**

*Crypto & Options Research*

[**线上站点 →**](https://www.zklabsresearch.com/) &nbsp;·&nbsp; [市场观察](https://www.zklabsresearch.com/observations.html) &nbsp;·&nbsp; [关于我们](https://www.zklabsresearch.com/about.html)

</div>

---

## 我们是谁

ZK-Labs Research 是 **ZK Capital**（Singapore）旗下的独立加密研究机构。

我们不卖数据，不接付费推广，不替任何项目方站台。每一篇报告的唯一客户，是我们自己的交易决策——以及未来选择信任我们判断的合作伙伴。

在信息过载的加密世界里，我们专注于一个被大多数人忽视的维度：**波动率**。我们认为，理解波动率定价错误的深度，比预测价格方向更能持续创造 alpha。

---

## 核心方法：四条铁律

1. **无来源，不落笔** —— 所有数据论断必须标注可验证来源（SEC EDGAR、DeFiLlama、官方公告、链上数据等），不依赖记忆或二手转述
2. **时间戳不可篡改** —— 每一篇研报通过 GitHub commit 发布，commit hash 就是审计线索。不删不改，错了公开勘误
3. **数据实时验证** —— 关键数字在撰写时通过一手来源复跑，不引用过期快照
4. **批判性独立** —— 不因为持仓而美化，不因为踏空而贬低。观点可能有错，立场不能有偏

**证据分级**：全文论断按 `F1`（一手披露：法条原文、SEC 文件、财报、监管文书）/ `F2`（高质量分析：法学院研究、CRS、顶级律所解读）/ `F3`（媒体转述、第三方研究、行情源）标注；并区分 **FACT / INTERPRETATION / INFERENCE** 三种性质。

> **No Evidence, No Change** —— 任何结论的修改必须由新证据触发。

---

## 内容形态

| 专栏 | 定位 | `categories` | 路径 |
|---|---|---|---|
| **旗舰深度研究** | 完整投研框架：财务模型、估值诊断、可证伪命题、监控仪表盘 | `research` | `/research/YYYY/MM/DD/<slug>.html` |
| **市场观察** | 短期可验证信号：事件驱动的结构性分析与观察框架 | `observation` | `/observations/YYYY/MM/DD/<slug>.html` |

**当前规模**：37 篇（19 篇旗舰深度研究 + 16 篇市场观察 + 2 篇双语研究），时间跨度 2026-07 至 2026-10。

主要研究赛道：

- **稳定币与分发经济学** —— USDC / OUSD / CRCL / Circle × Coinbase 分销结构（约 20 篇涉稳定币主题）
- **以太坊与 L1/L2 结构** —— 扩容、MEV、质押、机构上链（约 22 篇涉以太坊主题）
- **波动率研究** —— VIX 择时、波动率风险溢价、Gamma Squeeze 复盘
- **数字资产财库（DAT）** —— MSTR / BMNR 资本结构与 mNAV 分析

---

## 目录结构

```
zk-labs-research/
├── _config.yml              # Jekyll 配置（站点信息、社交卡片、front matter defaults）
├── _posts/                  # 全部文章（YYYY-MM-DD-<slug>.md）
├── _layouts/default.html    # 页面布局（含 {% seo %} 与面包屑）
├── _includes/head-custom.html
├── assets/
│   ├── css/style.scss
│   └── images/og-default.jpg  # 社交卡片默认图（1200×628）
├── .github/workflows/jekyll.yml  # GitHub Actions 构建与部署
├── index.md                 # 首页（旗舰研究 + 最新观察 + 全部报告）
├── observations.md          # 市场观察聚合页
└── about.md                 # 关于我们
```

**技术栈**：Jekyll + [`pages-themes/cayman@v0.2.0`](https://github.com/pages-themes/cayman)（`remote_theme`）· 插件 `jekyll-remote-theme` / `jekyll-feed` / `jekyll-seo-tag` · 由 GitHub Actions 在 `main` 分支 push 时自动构建部署。

---

## 本地预览

```bash
bundle install
bundle exec jekyll serve      # http://localhost:4000/zk-labs-research/
```

> 仓库未锁定 `Gemfile.lock`（已在 `.gitignore` 中），依赖以 `github-pages` gem 为准。

---

## 撰稿与发布规范

> 本节同时是**协作撰稿者的操作手册**。仓库由多个 Agent 与人工共同写入，请遵守。

### 1. Frontmatter

```yaml
---
layout: default
title: "标题"
permalink: /research/YYYY/MM/DD/<slug>.html   # 或 /observations/...
date: YYYY-MM-DD
categories: research                          # 或 observation
author: <署名>
data_cutoff: YYYY-MM-DD                       # 数据截点
version: "vX.Y"
tags: [标签, ...]
---
```

- 署名约定：**市场观察 = 南野东亦**；**旗舰深度研究 = 金戊乾坤2号 / 金戊乾坤3号**
- 旗舰报告另需 **Research Metadata** 块（Coverage / Version / Data Cutoff / Next Review / Thesis Status）与 **Version History** 表
- 新增旗舰报告后，需在 `index.md` 的「旗舰深度研究」区块**手动挂链**；市场观察由 Jekyll 自动聚合

### 2. ⚠️ 排版陷阱：Markdown 软换行

文章头部的多行信息（署名 / 数据截点 / 声明等）若写成**连续行**，Markdown 会把它们**合并成一整段**渲染。

**修法**：组内非末行行尾加**两个空格**（硬换行 → `<br />`）。

```markdown
**ZK Labs 市场观察 ｜ 副标题**
署名：南野东亦 ｜ 2026-09-30
**数据截点**：...
**声明**：...
```

自检脚本：

```bash
cd _posts
python3 ../scripts/check_post_layout.py          # 仅检查
python3 ../scripts/check_post_layout.py --fix    # 自动修复
```

### 3. 社交卡片（X / Twitter / Open Graph）

站点级 `image:` 键**无效**——`jekyll-seo-tag` v2.8 的 `ImageDrop` 只读 `page["image"]`。图片通过 **front matter defaults** 注入：

```yaml
# _config.yml
twitter:
  card: summary_large_image
  username: <handle>
defaults:
  - scope: {path: "", type: posts}
    values: {image: /assets/images/og-default.jpg}
  - scope: {path: "", type: pages}
    values: {image: /assets/images/og-default.jpg}
```

单篇可用 frontmatter `image:` 覆盖。图片规格：**1200×628**（1.91:1）、JPEG/PNG、≤5MB。

> 若改后 X 仍显示旧卡片，需到 X Card Validator 强制刷新缓存。

### 4. 发布流程

```bash
git add -A
git commit -m "publish: <标题>（<专栏> vX.Y）"
git fetch origin && git rebase origin/main   # 仓库多方写入，push 前必做
git push origin main
```

**验证三层（缺一不可）**：

1. 等 ~100s，确认 Actions 构建成功（`conclusion=success` 且 `head_sha` 为本 commit）
2. `curl` 文章 URL 返回 **HTTP 200**
3. **grep 线上 HTML 确认本次特征串**（新标题 / 新版本号 / 新增章节）确实出现——只验状态码会把「旧页面仍在服务」误判为发布成功

### 5. 修订纪律

- 已发布文章的事实错误：**直接改原文并升版本号**，不追加「UPDATE 说明」段落
- 版本号需三处一致：frontmatter `version:` + Metadata 表 `Version` + Version History 末行
- 研究结论冻结后，后续修改必须由新证据触发；不允许为「完整」把 `UNKNOWN` 改为 `ASSUMPTION`

---

## 免责声明

本仓库全部内容为**公开研究文稿**，不构成投资建议、法律意见或任何形式的要约。

- 文中不涉及任何个人资产持有情况、交易记录与交易信号
- 法律部分为研究性梳理，不构成法律意见，亦不构成对任何一方合规状态的判断
- 过往分析表现不代表未来结果；所有数据以文中标注的来源与截点为准

---

## 联系

ZK-Labs Research 是 ZK Capital（Singapore）的研究部门。

- **网站**：<https://www.zklabsresearch.com>
- **GitHub**：<https://github.com/poorshan/zk-labs-research>

---

<div align="center">

*独立加密研究，始于波动率，不止于波动率。*

</div>
