---
title: 資產配置總覽
type: overview
tags: [overview]
sources: [[sources/sfi-investing-risk-management-2026]], [[sources/web-2026-11-15-classic-theory]], [[sources/web-2026-11-15-strategies-evidence]], [[sources/web-2026-11-15-taiwan-market]], [[sources/web-2026-11-15-taiwan-tax]]
source_count: 5
status: draft
as_of: 2026-11-15
updated: 2026-11-15
---

# 資產配置總覽

> 這頁是整個 wiki 的「演進中論點」。每次 ingest 有重要新發現時由 LLM 更新。
> 目前來源：1 份 raw（[[sources/sfi-investing-risk-management-2026|證基會入門簡報]]）＋ 5 份網路查證彙整。原本的 seed 頁已全部補上來源（2026-11-15），但都仍是二手轉述，建議逐步 ingest 原始論文。

## 最近的發現（2026-11-15，第二輪查證）
- Brinson 的「90%」已釐清：隨時間變異約 90%、基金之間差異約 40%、報酬水準約 100%（Ibbotson & Kaplan 2000）（[[sources/web-2026-11-15-classic-theory]]）
- 股債負相關是 2000 年後的例外，正相關才是歷史常態；關鍵驅動是**通膨不確定性**（AQR）（[[sources/web-2026-11-15-strategies-evidence]]）
- 黃金的「通膨避險」證據薄弱，真正相關的是實質利率（Erb & Harvey）（[[sources/web-2026-11-15-strategies-evidence]]）
- 台股集中度量化：台積電占 0050 約 60%，台灣只占全球股市約 3%（[[sources/web-2026-11-15-taiwan-market]]）
- 新台幣在台股大跌時**經常**貶值（2022），但 2020 是反例 → 美元資產的「天然避險」不可靠（[[sources/web-2026-11-15-taiwan-market]]）

## 最近的發現（2026-11-15，第一輪）
- 台灣官方投資人教育的「標準說法」：理財先於投資 → 依風險屬性選工具 → 分散 + 再平衡 + 核心衛星。跟本 wiki 框架一致，但完全沒談匯率、稅、海外資產
- 連半官方教材都把 Brinson 研究講成「90% 績效差異」→ 這個誤讀在台灣很普遍，引用時要特別小心
- 新的在地工具：[[taiwan/tisa|TISA]]（2025-07 上路），目前誘因只有費率，租稅優惠未定
- 新資產類別：[[asset-classes/virtual-assets|虛擬資產]]，目前只有風險面描述，缺乏配置比例的證據

## 核心問題
資產配置要回答的是：**錢要放在哪些資產類別、各放多少、多久調整一次**——讓投資組合在可承受的風險下，達成自己的財務目標。

## 目前的工作假設（待來源驗證）
1. **配置比選股、擇時更能決定整體波動**。[[entities/brinson-hood-beebower|Brinson 等人（1986）]]的 93.6% 指的是單一基金報酬隨時間的變異；不同投資人之間的差距，配置只解釋約 40%（[[sources/web-2026-11-15-classic-theory]]）。
2. **[[concepts/diversification|分散]]的價值取決於[[concepts/correlation|相關性]]**，而股債相關性會隨通膨環境改變，2022 年就曾轉正（[[sources/web-2026-11-15-strategies-evidence]]）。
3. **成本、稅與行為比策略細節更重要**：多數人的績效落差來自追高殺低，而不是 60/40 和 70/30 的差別。
4. **沒有任何單一策略在所有環境下最好**；[[strategies/all-weather|全天候]]、[[strategies/permanent-portfolio|永久組合]]試圖對沖不同的經濟情境。
5. **台灣投資人有額外的變數**：新台幣匯率、台股高度集中於少數權值股、海外所得稅制、複委託成本（見 [[taiwan/taiwan-investor-context]]）。

## 決策框架（由上而下）
1. 目標與期間 → [[my-portfolio/ips|投資政策書]]
2. [[concepts/risk-tolerance|風險承受度]]（能力 vs. 意願）
3. 股債比（最重要的單一決策）
4. 股票內部：地區分配（台灣 / 美國 / 全球 / 新興）
5. 債券內部：存續期間、信用品質、幣別
6. 另類資產：[[asset-classes/gold|黃金]]、[[asset-classes/reits|REITs]] 是否納入
7. 工具選擇：ETF、費用、稅
8. [[concepts/rebalancing|再平衡]]規則

## 尚未解決的大問題
- [ ] 以新台幣為基準的投資人，海外債券要不要避險匯率？
- [ ] 台股本土偏誤（home bias）該保留多少？
- [ ] 現在的股債相關性環境與 2000–2020 年有何不同？

## 相關頁面
- [[index]]
