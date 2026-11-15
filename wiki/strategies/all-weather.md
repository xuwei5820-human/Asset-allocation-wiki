---
title: 全天候策略（All Weather）與風險平價
type: strategy
tags: [strategy, risk-parity]
sources: [[sources/web-2026-11-15-strategies-evidence]]
source_count: 1
status: draft
as_of: 2026-11-15
updated: 2026-11-15
---

# 全天候策略（All Weather）與風險平價

**一句話定義**：依「各資產對組合的風險貢獻相等」而非「金額相等」來配置，目標是在任何經濟環境下都表現尚可。

## 設計邏輯（Bridgewater 官方說法）
- 經濟環境依**成長**與**通膨**相對預期上升或下降，分成四種情境；**對每種情境放相等的風險**（[[sources/web-2026-11-15-strategies-evidence]]）
- Bridgewater 的例子：S&P 500 放 5 元、10 年期公債放 15 元，比各放 10 元更平衡，但報酬較低（[[sources/web-2026-11-15-strategies-evidence]]）
- **槓桿是實施工具**：把低風險的債券放大到與股票相近的風險，讓組合在保持報酬的同時降低風險（[[sources/web-2026-11-15-strategies-evidence]]）
- 1996 年推出，最初用於 [[entities/ray-dalio|Ray Dalio]] 的信託資產；策略本身是被動的（[[sources/web-2026-11-15-strategies-evidence]]）

**風險平價的數學直覺**：讓每個資產的風險貢獻相等

$$w_i \cdot \frac{\partial \sigma_p}{\partial w_i} = \frac{\sigma_p}{N}$$

（公式為定義，非來源數據）

## 散戶簡化版（非 Bridgewater 官方配置）
| 資產 | 比例 |
|---|---|
| 美國股票 | 30% |
| 長期美債 | 40% |
| 中期美債 | 15% |
| 黃金 | 7.5% |
| 商品 | 7.5% |

> [!warning] 來源
> 此比例出自 Tony Robbins《Money: Master the Game》（2014）的「All Seasons」組合，不是 Bridgewater 的實際基金配置；而且**沒有使用槓桿**，與機構版風險平價的特性不同（[[sources/web-2026-11-15-strategies-evidence]]）。

## 證據與數據
- 散戶版 2022 年約 −18.39%（年內最大回撤約 −20.58%）；30 年年化約 7.36%（美元、名目、回測網站、未計稅）（[[sources/web-2026-11-15-strategies-evidence]]）
- 2022 年受傷主因：債券跌幅接近股票（[[sources/web-2026-11-15-strategies-evidence]]）

## 爭議與限制
- 批評：散戶版債券比重過高、過度擬合過去 30 年；只有 30% 股票，拿 S&P 500 當比較基準並不恰當（[[sources/web-2026-11-15-strategies-evidence]]）
- 通膨不確定性升高時股債轉為正相關，削弱分散效果（見 [[concepts/correlation]]）

## 台灣投資人落地方式
- 長天期美債 ETF 在台灣有多檔掛牌（待查證代號、費用、規模）
- 商品類 ETF 選擇少，可考慮以黃金替代或省略（觀點）

## 相關頁面
- [[strategies/permanent-portfolio]] ・ [[concepts/correlation]] ・ [[asset-classes/gold]] ・ [[concepts/modern-portfolio-theory]]
