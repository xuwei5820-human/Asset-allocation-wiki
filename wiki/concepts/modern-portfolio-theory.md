---
title: 現代投資組合理論（Modern Portfolio Theory, MPT）
type: concept
tags: [theory, math]
sources: [[sources/web-2026-11-15-classic-theory]]
source_count: 1
status: draft
as_of: 2026-11-15
updated: 2026-11-15
---

# 現代投資組合理論（MPT）

**一句話定義**：以預期報酬與變異數（風險）為基礎，尋找在給定風險下報酬最高的資產組合的數學框架。

## 重點
- 由 [[entities/harry-markowitz|Harry Markowitz]] 於 1952 年在 *Journal of Finance* 發表〈Portfolio Selection〉提出，1959 年擴充成專書（[[sources/web-2026-11-15-classic-theory]]）
- MPT 是 William Sharpe 資本資產定價模型（CAPM）的基礎；Markowitz、Sharpe、Miller 共同獲得 1990 年諾貝爾經濟學獎（[[sources/web-2026-11-15-classic-theory]]）
- 核心觀念：評估資產要看它對**整體組合**風險的貢獻，而非單獨看（待查證：需原文）
- **效率前緣**（Efficient Frontier）：所有「同風險下報酬最高」組合連成的曲線（待查證）

## 數學核心
- 組合預期報酬：$E[R_p] = \sum_i w_i E[R_i]$
- 組合變異數：$\sigma_p^2 = \sum_i \sum_j w_i w_j \sigma_{ij}$（見 [[concepts/correlation]]）

## 常見誤傳
- 「分散是唯一的免費午餐」**不在 1952 年論文中**，也找不到 Markowitz 說過這句話的原始出處（[[sources/web-2026-11-15-classic-theory]]）

## 限制（待查證：需學術來源）
- 對輸入值（預期報酬、相關性）極度敏感，最佳化結果常集中在少數資產
- 假設報酬呈常態分布，低估肥尾風險
- 用變異數衡量風險，未區分上漲與下跌波動

## 延伸
- Black-Litterman 模型、風險平價（見 [[strategies/all-weather]]）、因子模型

## 相關頁面
- [[concepts/diversification]] ・ [[concepts/correlation]] ・ [[entities/harry-markowitz]]
