---
title: 相關性（Correlation）
type: concept
tags: [core, risk, math]
sources: [[sources/web-2026-11-15-strategies-evidence]], [[sources/web-2026-11-15-classic-theory]], [[sources/web-2026-11-15-taiwan-market]]
source_count: 3
status: draft
as_of: 2026-11-15
updated: 2026-11-15
---

# 相關性（Correlation）

**一句話定義**：衡量兩項資產報酬同向變動程度的指標，範圍 −1 到 +1。

## 重點
- +1：完全同向；0：無線性關係；−1：完全反向（定義）
- 兩資產組合的變異數（定義）：

  $$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2$$

  相關係數 $\rho_{12}$ 越低，組合波動越小 → 分散效果越好
- 再平衡紅利也與 $(1-\rho)$ 成正比（Bernstein，有爭議）（[[sources/web-2026-11-15-classic-theory]]）
- 相關性**不是常數**（見下）

## 股債相關性
- **AQR 的解釋**：股票與債券對成長消息反應相反、對通膨消息反應相同 → 成長不確定性主導時股債負相關，通膨不確定性升高時轉為正相關；通膨風險的解釋力遠大於成長風險（[[sources/web-2026-11-15-strategies-evidence]]）
- **歷史數據**（美國）：2000-01 至 2022-11 月相關約 −0.2；1926–1999 年約 +0.18；AQR 指出正相關其實是歷史常態，2000 年後的負相關才是例外（[[sources/web-2026-11-15-strategies-evidence]]）
- **2022 年**：股債同跌，60/40 全年約 −14% 到 −15%（[[sources/web-2026-11-15-strategies-evidence]]）
- 這是 [[strategies/60-40|60/40]] 能否發揮作用的關鍵假設

## 其他資產
- 黃金 vs. 全球股票：約 0.085（1988–2019）（[[sources/web-2026-11-15-strategies-evidence]]）
- REITs vs. 美股：平均約 0.56，區間 0.10–0.86（[[sources/web-2026-11-15-strategies-evidence]]）

## 爭議與限制
- 歷史相關性不保證未來
- 用月報酬與日報酬算出的相關性可能不同（待查證）

## 台灣投資人觀點
- 匯率會改變以台幣計價的相關性：2022 年台股跌、新台幣貶近 10%；2020 年疫情時新台幣反而升值 → 美元資產的「天然避險」效果時有時無（[[sources/web-2026-11-15-taiwan-market]]）

> [!question] 待查
> 以新台幣計價的台股 vs. 美債長期相關係數：需自行用資料計算（放 `raw/data/`）。

## 相關頁面
- [[concepts/diversification]] ・ [[asset-classes/bonds]] ・ [[strategies/all-weather]]
