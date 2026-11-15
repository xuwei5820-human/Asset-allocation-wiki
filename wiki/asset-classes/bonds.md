---
title: 債券（Bonds）
type: asset-class
tags: [asset-class, defensive, income]
sources: [[sources/web-2026-11-15-classic-theory]], [[sources/web-2026-11-15-strategies-evidence]], [[sources/web-2026-11-15-taiwan-tax]], [[sources/web-2026-11-15-taiwan-market]]
source_count: 4
status: draft
as_of: 2026-11-15
updated: 2026-11-15
---

# 債券（Bonds）

**一句話定義**：借錢給政府或企業並收取利息的固定收益資產，在組合中主要扮演穩定器角色。

## 關鍵特性
- **利率風險**：市場利率上升時，固定利率債券價格下跌；票面利率越低的債券，利率風險通常越高（[[sources/web-2026-11-15-classic-theory]]，SEC）
- **存續期間（Duration）**：利率每變動 1 個百分點，價格大約反向變動「存續期間」那麼多％。例如存續期間 10 年的基金，利率升 1% 約跌 10%；2 年的約跌 2%（[[sources/web-2026-11-15-classic-theory]]，FINRA）

  $$\frac{\Delta P}{P} \approx -D \times \Delta y$$

  - 這是近似值：利率下降時的漲幅會大於等幅上升時的跌幅（凸性）；存續期間短也不代表沒有風險（[[sources/web-2026-11-15-classic-theory]]）
- **信用品質**：公債 > 投資等級公司債 > 高收益債；信用越差越像股票（待查證）
- **幣別**：外幣債券對台幣投資人含匯率風險（見 [[taiwan/taiwan-investor-context]]）

## 在組合中的角色
| 類型 | 主要功能（一般認知，待查證） |
|---|---|
| 短期公債 | 類現金、低波動 |
| 中期公債 | 平衡收益與避險 |
| 長期公債 | 對沖通縮與衰退，但利率風險高 |
| 公司債/高收益債 | 提高收益，但危機時與股票同跌 |
| 抗通膨債券（TIPS） | 對沖通膨 |

- [[strategies/permanent-portfolio|永久組合]]用長期公債對應「通縮」情境（[[sources/web-2026-11-15-strategies-evidence]]）

## 證據與數據
- 2022 年股債同跌，60/40 組合全年約跌 14–15%（美元、名目）（[[sources/web-2026-11-15-strategies-evidence]]）
- AQR：通膨不確定性升高時，股債相關性轉正，債券的避險功能減弱（[[sources/web-2026-11-15-strategies-evidence]]）

## 爭議與限制
- 股債相關性不是常數（見 [[concepts/correlation]]）
- 債券 ETF 沒有到期日，與持有單一債券到期的風險特性不同（待查證）

## 台灣投資人觀點
- 台灣掛牌美債 ETF 眾多，需比較內扣費用、追蹤誤差、配息；投資海外債的債券 ETF 配息多屬海外所得，一般不課綜所稅、不扣補充保費（[[sources/web-2026-11-15-taiwan-tax]]；[[taiwan/tax-overview]]）
- 債券 ETF 證交稅停徵到 2026-12-31，槓桿型、反向型不適用（[[sources/web-2026-11-15-taiwan-market]]，證交稅條例第 2-1 條）
- 匯率：2022 年台股下跌時新台幣貶值近 10%，未避險的美元債券以台幣計價的跌幅因此較小；但 2020 年新台幣反而升值，**不是固定關係**（[[sources/web-2026-11-15-taiwan-market]]）

## 相關頁面
- [[strategies/60-40]] ・ [[strategies/all-weather]] ・ [[asset-classes/cash]] ・ [[concepts/correlation]]
