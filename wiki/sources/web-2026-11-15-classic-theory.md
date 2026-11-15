---
title: 經典理論查證彙整：MPT、Brinson、再平衡、存續期間（網路查證）
type: source
tags: [theory, mpt, brinson, rebalancing, bonds, web]
raw_path: （無，網路查證；原文以連結為準）
author: CFA Institute、FINRA、SEC、Econlib、Jason Zweig、Advisor Perspectives、Kitces 等
published: 1952 ~ 2025（原始研究）；轉述文章 2012 ~ 2025
source_type: web-search
reliability: medium   # 多為可信二手轉述（CFA Institute、FINRA、SEC 為高可信）；原論文全文未讀
ingested: 2026-11-15
---

# 經典理論查證彙整（2026-11-15 網路查證）

**用途**：為 seed 頁補來源：[[concepts/modern-portfolio-theory]]、[[entities/harry-markowitz]]、[[entities/brinson-hood-beebower]]、[[concepts/asset-allocation]]、[[concepts/diversification]]、[[concepts/rebalancing]]、[[asset-classes/bonds]]。以下皆為改寫。

## 1. Markowitz 與 MPT
- 〈Portfolio Selection〉刊於 *Journal of Finance* 1952 年 3 月號（第 7 卷第 1 期，頁 77–91）；1959 年擴充成同名專書（Econlib、Encyclopedia.com）
- 1990 年與 William Sharpe、Merton Miller 共同獲得諾貝爾經濟學獎；Sharpe 以 CAPM 聞名，而 MPT 是 CAPM 的基礎（Econlib、UBS Nobel Perspectives）
- Markowitz 於 2023 年 6 月過世，享年 95 歲（UBS）
- **「分散是唯一的免費午餐」並不在 1952 年論文中**；找不到 Markowitz 說過這句話的原始出處，屬於流行的轉述（Advisor Perspectives 2017、MDPI 2024 論文）
- **Markowitz 的個人配置**：他在 2009 年接受 *Journal of Investment Consulting* 訪問時說，當初把退休金提撥股債各半，目的是「把未來的後悔降到最低」；Jason Zweig 指出這個 50/50 後來並沒有一直維持（jasonzweig.com、Advisor Perspectives 2024）

## 2. Brinson, Hood & Beebower（1986）與 Ibbotson & Kaplan（2000）
- BHB 1986：分析 91 個美國大型退休基金 1974–1983 年的**季報酬**；政策配置平均解釋單一基金**報酬隨時間變動**的 93.6%（R²）——衡量的是變異，不是報酬水準，也不是基金之間的差距（CFA Institute Enterprising Investor 2012）
- Ibbotson & Kaplan 2000〈Does Asset Allocation Policy Explain 40, 90, or 100 Percent of Performance?〉：
  - 約 90%：單一基金報酬**隨時間的變異**（確認 BHB）
  - 約 40%：**不同基金之間**報酬差異
  - 約 100%：報酬**水準**（平均而言，主動管理無法增加價值）
  - （CFA Institute 2012、Scribd 論文副本）
- 1991 年 BHB 更新研究的數字各來源不一（91.5% 或「90% 以上」）

## 3. 再平衡紅利
- William Bernstein：50/50 組合每年再平衡，比 Markowitz 的預期報酬多出 0.49% 的「再平衡紅利」；紅利大小與 (1 − 相關係數) 成正比，資產波動越大、相關性越低、報酬越接近，紅利越大（Marotta 引述 Bernstein）
- 批評：與**買進持有不再平衡**比較才有意義；在 Bernstein 自己的例子中，不再平衡的組合報酬反而較高（Advisor Perspectives）
- Kitces：在**報酬差很多的資產**之間（如股債）再平衡，通常會**降低**長期報酬，是風險管理工具而非增加報酬的工具；其他研究的報酬提升通常不超過每年 0.5%（Kitces、Advisor Perspectives）

## 4. 債券存續期間（Duration）
- 利率上升時，固定利率債券價格下跌，這就是利率風險；票面利率越低的債券，利率風險通常越高（SEC investor.gov）
- 經驗法則：利率每變動 1 個百分點，債券價格大約反向變動「存續期間」那麼多％；存續期間 10 年的基金在利率升 1% 時約跌 10%，2 年的約跌 2%（FINRA 投資人警示 2013）
- 存續期間雖以「年」表示，但不只是時間長度；存續期間短也不代表沒有風險（FINRA）
- 這是近似值：利率下降時價格漲幅會大於利率等幅上升時的跌幅（凸性）

## 連結
- [Econlib：Harry Markowitz](https://www.econlib.org/library/Enc/bios/Markowitz.html)
- [UBS Nobel Perspectives：Harry Markowitz](https://www.ubs.com/microsites/nobel-perspectives/en/laureates/harry-markowitz.html)
- [Advisor Perspectives：The Myths and Fallacies about Diversified Portfolios（2017）](https://www.advisorperspectives.com/articles/2017/01/09/the-myths-and-fallacies-about-diversified-portfolios)
- [MDPI：diversification 論文（2024）](https://mdpi.com/1911-8074/17/6/225)
- [Jason Zweig：What Harry Markowitz Meant](https://jasonzweig.com/what-harry-markowitz-meant/)
- [Advisor Perspectives：Allan Roth, 50 percent rule（2024）](https://www.advisorperspectives.com/articles/2024/08/29/50-percent-rule-allan-roth)
- [CFA Institute：Setting the Record Straight on Asset Allocation（2012）](https://blogs.cfainstitute.org/investor/2012/02/16/setting-the-record-straight-on-asset-allocation)
- [Ibbotson & Kaplan 2000 副本（Scribd）](https://es.scribd.com/document/276088167/Does-Asset-Allocation-Explain-40-90-100-Performance)
- [Marotta：The Rebalancing Bonus（Bernstein）](https://marottaonmoney.com/wp-content/uploads/2025/07/The-Rebalancing-Bonus.pdf)
- [Advisor Perspectives：Does Rebalancing Really Pay Off](https://www.advisorperspectives.com/newsletters14/Does_Rebalancing_Really_Pay_Off.php)
- [Kitces：How Rebalancing Usually Reduces Long-Term Returns](https://www.kitces.com/blog/how-rebalancing-usually-reduces-long-term-returns-but-is-good-risk-management-anyway/)
- [FINRA：Brush Up on Bonds: Interest Rate Changes and Duration](https://www.finra.org/investors/insights/bonds-interest-rate-changes-duration)
- [SEC investor.gov：Interest Rate Risk](https://www.investor.gov/news-alerts/investor-bulletins/interest-rate-risk-when-interest-rates-go-prices-fixed-rate-bonds-fal)

> [!question] 待查
> 建議把 Markowitz 1952、BHB 1986、Ibbotson & Kaplan 2000 原文 PDF 放進 `raw/papers/` 正式 ingest，可把本頁轉述升級為一手來源。
