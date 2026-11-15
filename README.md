# 資產配置 LLM Wiki

依 Andrej Karpathy 的「LLM Wiki」模式建立的個人資產配置知識庫。你負責找來源、問問題；LLM 負責摘要、交叉連結和維護。

## 快速開始

1. 用 **Obsidian** 開啟本資料夾作為 vault（推薦外掛：Dataview、Marp、Obsidian Web Clipper）
2. 在本資料夾開啟 **Claude Code**（或其他 agent），它會自動讀取 `CLAUDE.md`
3. 把文章／論文／筆記丟進 `raw/inbox/`
4. 對 agent 說：`ingest inbox`

## 常用指令

| 你說 | agent 會做 |
|---|---|
| `ingest inbox` / `ingest raw/inbox/xxx.md` | 讀來源 → 建摘要頁 → 更新相關頁 → 更新 index 與 log |
| `問：全天候策略在升息期表現如何？` | 讀 index → 找頁 → 附引用回答 → 問你要不要存成 synthesis |
| `lint` | 檢查矛盾、過時資料、孤兒頁、缺來源的陳述 |
| `檢視我的配置` | 對照 IPS 計算偏離、判斷是否再平衡、寫入決策紀錄 |

## 建議的第一批來源

- Markowitz (1952) *Portfolio Selection*
- Brinson, Hood & Beebower (1986) *Determinants of Portfolio Performance*
- Bogleheads Wiki：Three-fund portfolio、Asset allocation
- Bridgewater 對 All Weather 的公開說明
- 財政部：海外所得與最低稅負制；健保署：二代健保補充保費
- 你常用的台灣 ETF 公開說明書／月報（0050、006208、00878、債券 ETF 等）

## Obsidian 設定小技巧

- Settings → Files and links → Attachment folder path 設為 `raw/assets/`
- 綁一個熱鍵給「Download attachments for current file」，剪下文章後一鍵把圖片存到本機
- 用 Graph view 看哪些頁是樞紐、哪些是孤兒

## Git

本資料夾就是一個 markdown repo，建議 `git init` 取得版本紀錄。若要上傳 GitHub，**請把 `wiki/my-portfolio/` 加進 `.gitignore` 或用私人 repo**。

> 本 wiki 僅供個人學習，不構成投資建議。
