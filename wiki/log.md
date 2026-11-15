---
title: Wiki 日誌
type: log
---

# Wiki 日誌

> 只能 append。查詢最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

## [2026-11-15] init | 建立 wiki 骨架
- 建立 `CLAUDE.md`（schema）、`README.md`、目錄結構、5 個模板
- 建立種子頁（status: seed，皆依一般知識撰寫，**尚無 raw 來源支撐**）：
  - 總覽：overview
  - 概念：asset-allocation、diversification、correlation、rebalancing、risk-tolerance、modern-portfolio-theory、sequence-of-returns-risk、asset-location
  - 策略：60-40、three-fund、all-weather、permanent-portfolio、core-satellite、glide-path
  - 資產類別：equities、bonds、cash、gold、reits
  - 實體：harry-markowitz、john-bogle、ray-dalio、harry-browne、brinson-hood-beebower
  - 台灣：taiwan-investor-context、taiwan-etf-landscape
  - 個人：ips、current-allocation、decision-log
- 下一步：ingest 第一批經典來源（見 README「建議的第一批來源」），把 seed 頁升級為 draft/solid

## [2026-11-15] ingest | 證基會：投資理財與風險管理（含虛擬資產商品性質及風險）
- raw：`raw/articles/2026-05-26-sfi-investing-risk-management-slides.pdf`（＋ .txt 文字擷取）
- 新增：sources/sfi-investing-risk-management-2026、sources/web-2026-11-15-tisa-news、taiwan/tisa、taiwan/anti-fraud、asset-classes/virtual-assets、concepts/financial-planning-vs-investing、concepts/stocks-funds-etfs
- 修改：concepts/asset-allocation、concepts/rebalancing、concepts/risk-tolerance、concepts/diversification、strategies/core-satellite、strategies/glide-path、strategies/60-40、asset-classes/cash、taiwan/taiwan-etf-landscape、taiwan/taiwan-investor-context、entities/brinson-hood-beebower、overview、index
- 矛盾：①簡報「90% 績效差異來自配置」vs. Brinson 原研究的變異解釋 → asset-allocation、brinson 標 contested ②TISA 開戶資格：簡報「20 歲中華民國國民」vs. 遠見「外籍人士也可」→ tisa 標 contested
- 發現：簡報第 23 頁積極型建議工具與穩健型相同，疑似誤植
- 網路查證：TISA 現況（工商時報、遠見、新頭殼、今周刊）
- 建議下一步：Brinson 1986 原文或 Ibbotson & Kaplan 2000；金管會 TISA 官方說明；主計總處 CPI 長期資料（查證「通膨 2–3%」）

## [2026-11-15] ingest | 台灣投資稅制網路查證
- raw：無（網路查證依規則不放 raw）→ sources/web-2026-11-15-taiwan-tax
- 新增：taiwan/tax-overview、taiwan/dividend-tax、taiwan/nhi-supplementary-premium、taiwan/overseas-income-amt、taiwan/us-tax-for-taiwan-investors、taiwan/securities-transaction-tax
- 修改：taiwan/taiwan-investor-context（稅務表填入，seed→draft）、concepts/asset-location（seed→draft）、concepts/rebalancing（補證交稅引用，source_count 2，維持 draft：稅制來源只支撐成本一點）、asset-classes/bonds、asset-classes/reits、index
- 矛盾：無；但有兩項制度變動中 ①補充保費改年度累計（暫緩）②債券 ETF 證交稅停徵延長到 2036（財委會初審，三讀未確認）
- 待查：ETF 證交稅 1‰ 法條原文（全國法規資料庫當日無法連線）、國稅局對海外債 ETF 配息的正式說明、證所稅停徵依據、海外虧損扣抵規則
- 建議下一步：2027-01 前確認債券 ETF 停徵三讀；做「海外股票工具稅後成本比較」synthesis

## [2026-11-15] schema | 新增 Research 流程（6.5）
- CLAUDE.md：新增 `research/` 目錄（每個研究一個資料夾：notes.md、slides.md、slides.html）、6.5 Research 流程（兩段式搜尋、只引用有來源的句子、引用格式、對象與難度、HTML 用 reveal.js + KaTeX）、log 動作類型加入 `research`
- 新增模板：templates/research-note.md、templates/slide-outline.md、templates/slides.html；新增 research/README.md

## [2026-11-15] ingest | seed 頁補來源與待查證處理（網路查證）
- 新增來源頁：sources/web-2026-11-15-classic-theory、sources/web-2026-11-15-strategies-evidence、sources/web-2026-11-15-taiwan-market
- seed → draft（14 頁＋overview）：asset-classes/bonds、equities、gold、reits；concepts/correlation、modern-portfolio-theory、sequence-of-returns-risk；entities/harry-browne、harry-markowitz、john-bogle、ray-dalio；strategies/all-weather、permanent-portfolio、three-fund；overview
- contested → draft：concepts/asset-allocation、entities/brinson-hood-beebower（「90%」已釐清為誤讀：Ibbotson & Kaplan 90/40/100）
- 修改：concepts/diversification、rebalancing；strategies/60-40、glide-path；taiwan/taiwan-investor-context、securities-transaction-tax（改引證交稅條例原文）、tax-overview、dividend-tax、overseas-income-amt；index
- 新發現：①「分散是唯一免費午餐」不在 Markowitz 論文中 ②股債正相關是歷史常態 ③黃金通膨避險證據薄弱 ④台積電占 0050 約 60%、台灣占 ACWI 約 3% ⑤新台幣在股災時常貶但 2020 是反例 ⑥Bogle 改用 120 減年齡的理由（殖利率）與證基會說法（壽命）不同
- 仍為（待查證）：41 處，皆為找不到可靠來源的陳述，保留標記；所有頁面目前都是二手轉述，status 最高 draft
- 建議下一步：把 Markowitz 1952、BHB 1986、Ibbotson & Kaplan 2000、Bridgewater All Weather Story、AQR 股債相關論文、Erb & Harvey 原文放進 raw/papers 正式 ingest
