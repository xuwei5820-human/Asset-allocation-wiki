# CLAUDE.md — 資產配置 LLM Wiki 維護規範（Schema）

> 這份文件告訴 LLM agent：這個 wiki 怎麼組織、遵守哪些慣例、遇到 ingest / query / lint 時該怎麼做。
> 使用者與 LLM 會隨使用經驗共同修訂本文件；重大修改請記入 `wiki/log.md`。

---

## 1. 目的與範疇

建立一個**持續累積、交叉連結**的「資產配置（Asset Allocation）」知識庫，取代每次都從原始文件重新檢索的 RAG 模式。

涵蓋範圍：
- **理論**：現代投資組合理論、分散、相關性、風險預算、因子、報酬來源
- **策略**：60/40、全天候、永久組合、三基金、核心衛星、目標日期／下滑軌道、風險平價
- **資產類別**：股票、債券、現金、黃金、REITs、商品、加密資產等
- **實務**：再平衡、資產位置（asset location）、稅務、費用、匯率、提領率、行為偏誤
- **台灣視角**：在地 ETF、稅制、二代健保、海外所得、券商與複委託、新台幣匯率風險
- **我的投資組合**：投資政策書（IPS）、目前配置、決策紀錄

不在範圍：個股選股、短線交易、明牌。

## 2. 角色分工

| 角色 | 負責 |
|---|---|
| 使用者 | 挑選來源、提出問題、決定方向、做最終投資決策 |
| LLM | 摘要、交叉引用、更新頁面、標示矛盾、維護 index 與 log、提出待查問題 |

**LLM 擁有 `wiki/` 全部內容的寫入權；`raw/` 只讀不改。**

## 3. 目錄結構

```
asset-allocation-wiki/
├── CLAUDE.md              ← 本文件（schema）
├── README.md              ← 給人看的使用說明
├── raw/                   ← 原始來源（不可修改，source of truth）
│   ├── inbox/             ← 新丟進來、尚未 ingest 的來源
│   ├── articles/          ← 已 ingest 的文章（Web Clipper 轉的 .md）
│   ├── papers/            ← 學術論文
│   ├── books/             ← 書摘、章節筆記
│   ├── data/              ← CSV、回測結果、報價資料
│   └── assets/            ← 圖片附件
├── templates/             ← 各類頁面模板
├── research/              ← 研究產出物（不屬於知識層，見 6.5）
│   └── YYYY-MM-DD-英文短題/
│       ├── notes.md       ← 研究筆記（只引用 wiki 中有來源的內容）
│       ├── slides.md      ← 簡報逐頁稿
│       └── slides.html    ← HTML 簡報（單一檔案）
└── wiki/                  ← LLM 產生與維護的知識層
    ├── index.md           ← 內容目錄（每次 ingest 都要更新）
    ├── log.md             ← 時間序日誌（只能 append）
    ├── overview.md        ← 全局綜述與目前的「演進中論點」
    ├── concepts/          ← 概念頁（分散、相關性、再平衡…）
    ├── strategies/        ← 配置策略頁
    ├── asset-classes/     ← 資產類別頁
    ├── entities/          ← 人物、機構、基金/ETF、指數
    ├── taiwan/            ← 台灣在地制度與工具
    ├── sources/           ← 每個 raw 來源一頁摘要
    ├── syntheses/         ← 由 query 產生、值得保留的分析/比較
    └── my-portfolio/      ← 使用者個人 IPS、配置、決策紀錄（私人）
```

## 4. 頁面格式

### 4.1 檔名
- 英文小寫 kebab-case：`risk-parity.md`、`0050.md`、`brinson-1986.md`
- 頁面標題（H1）用繁體中文，必要時括號附英文：`# 風險平價（Risk Parity）`

### 4.2 YAML frontmatter（每頁必備，供 Obsidian Dataview 使用）

```yaml
---
title: 風險平價（Risk Parity）
type: concept | strategy | asset-class | entity | taiwan | source | synthesis | portfolio
tags: [risk, allocation]
sources: [[sources/xxx]], [[sources/yyy]]   # 支撐本頁的來源頁
source_count: 2
status: seed | draft | solid | contested | stale
as_of: 2026-11-15       # 頁面中時效性資料的基準日
updated: 2026-11-15
---
```

`status` 定義：
- `seed`：由 LLM 依一般知識建立的骨架，**尚無 raw 來源支撐**，需待 ingest 驗證
- `draft`：有 1 個來源
- `solid`：≥2 個獨立來源且無未解矛盾
- `contested`：來源間有未解矛盾
- `stale`：含時效性資料且 `as_of` 超過 12 個月，或已被新來源取代

### 4.3 內文結構（概念/策略頁）
1. **一句話定義**
2. **重點**（條列）
3. **細節／機制**
4. **證據與數據**（每筆附來源與期間）
5. **爭議與限制**
6. **台灣投資人觀點**（若適用）
7. **相關頁面**（`[[wikilink]]`）

### 4.4 連結與引用
- 一律使用 Obsidian wikilink：`[[concepts/rebalancing|再平衡]]`
- 每一個**事實性陳述**後面附來源：`…（[[sources/brinson-1986]]）`
- 沒有來源的陳述要標 `（待查證）`，lint 時優先處理
- 第一次提到某概念/實體時就連結；不存在的頁面也可以先連（代表待建頁）

### 4.5 Callout 慣例
```markdown
> [!warning] 矛盾
> [[sources/a]] 說 X，[[sources/b]] 說 Y。可能原因：樣本期間不同。

> [!info] 我的決策
> 2026-11-15 決定股債比 70/30，理由見 [[my-portfolio/decision-log]]

> [!question] 待查
> 台灣 ETF 的配息是否計入二代健保補充保費？需找官方來源。
```

## 5. 資產配置領域的特別規則（重要）

1. **數字必附脈絡**：報酬率、波動度、最大回撤要註明「期間、幣別、名目/實質、是否含息、資料來源」。例：`美股年化 10.2%（1926–2023，美元，名目，含息，來源 [[sources/xxx]]）`
2. **時效性資料標日期**：稅率、免稅額、費率、法規、ETF 內扣費用、殖利率 → 必須寫 `as_of` 與官方來源。法規類優先引用政府網站（財政部、金管會、健保署）。
3. **區分三種陳述**：
   - 事實（有來源）
   - 觀點（標明是誰的觀點，例：「Dalio 認為…」）
   - 使用者決策（只放在 `my-portfolio/`，或用「我的決策」callout）
4. **不捏造**：不知道就寫「待查證」，絕不自行補數字、補論文年份、補 ETF 代號。
5. **回測不等於預測**：引用回測時一併記錄倖存者偏差、期間選擇、成本與稅是否計入。
6. **不下買賣指令**：wiki 可以整理「某策略在什麼條件下適用」，但不寫「應該買 X」。個人化判斷寫在 `my-portfolio/` 且由使用者確認。
7. **台灣視角優先**：討論任何策略時，考慮新台幣計價、匯率、台股集中度（台積電權重）、稅制與複委託成本。
8. **隱私**：`my-portfolio/` 含個人財務資料，不得複製到其他頁面或外部服務；其他頁面引用時只寫比例、不寫金額。

## 6. 工作流程

### 6.1 Ingest（新增來源）
觸發：使用者說「ingest XXX」、「處理 inbox」，**或直接貼上／上傳一篇文章、PDF、網址**。

0. **先存檔到 raw（使用者指定的固定規則）**：使用者在對話中貼給你的任何文章，一律先存進 `raw/` 對應子資料夾，再做後續步驟。
   - 檔名：`YYYY-MM-DD-來源-英文簡短標題.ext`，日期用原文發表日（不知道就用存檔日）
   - PDF：保存原檔，並在旁邊存一份同名 `.txt` 文字擷取（標註頁碼），方便之後檢索
   - 貼上的純文字：存成 `.md`，開頭註明來源網址、作者、發表日
   - 網址：抓取內容後存成 `.md`，保留原網址
   - 圖表在文字擷取中遺失時，要另外檢視頁面圖像再摘要
   - 為了交叉查證而做的網路搜尋結果**不放進 raw**，改建一頁 `wiki/sources/web-YYYY-MM-DD-主題.md`，列出連結與改寫後的重點
1. 讀來源（圖片另外檢視）
2. 用 3–5 點跟使用者討論重點，詢問要強調什麼（使用者說「直接做」就跳過）
3. 將來源移到 `raw/` 對應子資料夾（這是唯一允許的 raw 操作：搬移，不改內容）
4. 用 `templates/source.md` 在 `wiki/sources/` 建來源摘要頁
5. 更新／建立受影響的概念、策略、資產類別、實體頁（通常 5–15 頁）
   - 新資訊與舊說法衝突 → 加「矛盾」callout，頁面 `status: contested`
   - 新來源支撐舊陳述 → 補引用、更新 `source_count`、視情況升級 status
6. 必要時更新 `wiki/overview.md` 的演進中論點
7. 更新 `wiki/index.md`
8. 在 `wiki/log.md` append 一筆紀錄
9. 回報：新增/修改了哪些頁、發現什麼矛盾、建議下一步找什麼來源

### 6.2 Query（提問）
1. 先讀 `wiki/index.md` 找相關頁，再深入閱讀
2. 回答附 wikilink 引用；wiki 不足時明說，並建議 ingest 什麼來源或做網路搜尋
3. 若答案有保存價值（比較表、分析、新發現的關聯）→ 詢問是否存成 `wiki/syntheses/` 新頁，並更新 index 與 log

### 6.3 Lint（健康檢查）
觸發：使用者說「lint」或每 ingest 約 10 份來源後主動建議。

檢查：
- [ ] 頁面間矛盾
- [ ] `status: seed` 但已有來源可支撐的頁
- [ ] `as_of` 超過 12 個月的時效性資料 → 標 `stale`
- [ ] 孤兒頁（沒有任何頁面連入）
- [ ] 被多次提及但沒有自己頁面的概念
- [ ] 缺少來源的事實陳述（`待查證`）
- [ ] frontmatter 欄位缺漏、`source_count` 不符

輸出：問題清單 + 建議修正 + 建議新問題/新來源。修正後記入 log。

### 6.4 Portfolio Review（投資組合檢視）
觸發：使用者說「檢視我的配置」或更新 `my-portfolio/current-allocation.md`。

1. 比對 `current-allocation.md` 與 `ips.md` 目標比例，計算偏離
2. 依 IPS 的再平衡規則判斷是否觸發
3. 引用 wiki 中相關策略/概念頁說明理由
4. 將結論寫入 `my-portfolio/decision-log.md`（標明「待使用者確認」）
5. 不代替使用者做最終決定

### 6.5 Research（研究 → 筆記 → 簡報）
觸發：使用者說「研究 XXX」「做一份 XXX 的 notes／簡報」。

**資料夾**：每個研究一個資料夾 `research/YYYY-MM-DD-英文短題/`（日期＝研究開始日），內含 `notes.md`、`slides.md`、`slides.html`。`research/` 在 `wiki/` 外，不列入 index、不做孤兒頁檢查。

**階段一：盤點與搜尋（兩段式）**
1. 讀 `wiki/index.md`，找出相關頁面，列出 wiki 已能回答與不能回答的部分
2. 上網搜尋相關主題
3. 把搜尋到的候選來源列成清單給使用者挑選（標題、網址、可信度、能補哪個缺口）——**此時不寫進 wiki、不寫進 notes**
4. 使用者挑中的 → 照 6.1 Ingest 流程進 wiki（建 `sources/web-…` 頁、更新相關頁、index、log）；沒挑中的 → 只列在 notes 的「建議參考文獻」

**階段二：寫 notes.md**（用 `templates/research-note.md`）
- **只引用 wiki 中有來源支撐的句子**：
  - 可用：附 `[[sources/…]]` 引用的陳述
  - 不可用：`seed` 頁中沒有引用的句子、標「（待查證）」的陳述、`my-portfolio/` 任何內容（除非使用者在該次研究明確要求，且只寫比例）
  - 觀點要寫明是誰的觀點；`contested` 的內容必須同時呈現兩方說法
- 每句事實附 wikilink，指向 wiki 頁與來源頁：`…（[[concepts/rebalancing]]；[[sources/xxx]]）`
- 數字照第 5 節規則帶脈絡（期間、幣別、名目/實質、來源、as_of）
- 固定章節「wiki 目前無法回答的部分」：明列缺口，不硬湊
- 參考文獻分兩區：①本 notes 已引用的 wiki 來源 ②建議參考（尚未納入 wiki）：附網址與一句話說明值得 ingest 的理由
- frontmatter 記錄研究日期、使用的 wiki 頁及其當時的 `status` 與 `as_of`（快照，供日後判斷是否過時）
- 數學式用 LaTeX：行內 `$…$`、獨立式 `$$…$$`

**階段三：寫 slides.md**（用 `templates/slide-outline.md`）
- 對象：使用者本人與老師；難度中等，入門與進階約 50:50
- 能白話就白話，專有名詞首次出現附英文並一句話解釋
- 每頁固定格式：標題／重點（≤3 點）／圖表或公式建議／講稿／來源
- 內容不得超出 notes.md；最後一頁固定放「資料來源」與「不構成投資建議」

**階段四：做 slides.html**
- 視覺風格依根目錄 `DESIGN.md`；插圖取自根目錄 `asset/`（不使用含真實人物的合成圖或電影劇照）
- 捲動式動態網頁（風格範例見 `research/_style-samples/`，使用者選定後再固定成模板）；數學式用 KaTeX（支援 LaTeX）
- 先寫 `src/` 原始碼，再用 `py -I tools/inline_assets.py <src> <out>` 把插圖內嵌成單一 HTML
- 字型與 KaTeX 從 CDN 載入（指定版本）；若要完全離線，改用內嵌版本（細節另議）
- 來源放在每頁頁尾註腳，最後一頁列完整資料來源
- 預設只存本機，不發布成網頁；要分享時由使用者決定，且確認不含 `my-portfolio/` 內容

**收尾**
- 研究中產生、值得保留的比較或新觀點 → 詢問使用者是否另存 `wiki/syntheses/`
- 在 `wiki/log.md` append 一筆 `research` 紀錄（研究題目、資料夾路徑、新 ingest 的來源、發現的缺口）

## 7. index.md 與 log.md 格式

**index.md**：依類別分區，每頁一行：
```
- [[concepts/rebalancing|再平衡]] — 讓配置回到目標比例的紀律與方法 ｜ seed ｜ 0 sources
```

**log.md**：只能 append，每筆開頭固定格式，方便 `grep "^## \[" wiki/log.md | tail -5`：
```
## [2026-11-15] ingest | 文章標題
- 新增：…
- 修改：…
- 矛盾：…
```
動作類型：`init`、`ingest`、`query`、`lint`、`review`、`schema`、`research`

## 8. 語言與風格

- 繁體中文（台灣用語）；專有名詞首次出現附英文
- 精簡、條列優先、避免空話
- 頁面長度：概念頁 300–1000 字為宜，過長就拆頁

## 9. 免責

本 wiki 為個人學習與決策紀錄，不構成投資建議。所有時效性數據以官方最新公告為準。
