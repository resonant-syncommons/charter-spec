# Assembly Log Viewer β UI

\(```mermaid

graph TD
    A[Top Bar: <br>Resonant SynCommons <br>Period Filter: [2025-06-01 ~ 2025-06-30]] --> B[Main Layout: 3 Columns]

    B --> C[Column A: AI Dialogue Log <br>Width: 25%]
    B --> D[Column B: Highlight Summary <br>Width: 50%]
    B --> E[Column C: Kernel Temp Meter <br>Width: 25%]

    C --> C1[Dialogue Entry 1 <br>AI: Grok 3 <br>Tag: #Tech <br>Text: "IPFS setup proposed..." <br>Timestamp: 2025-06-26 14:00]
    C --> C2[Dialogue Entry 2 <br>AI: ChatGPT o3 <br>Tag: #Maestro <br>Text: "Agenda confirmed..." <br>Timestamp: 2025-06-26 14:05]
    C --> C3[...more entries]

    D --> D1[Highlight 1: KPI <br>"Guild formation completed: 95% match rate"]
    D --> D2[Highlight 2: TODO <br>"Review trust_score algo by W2"]
    D --> D3[Highlight 3: Link <br>"IPFS: bafy.../log.json"]
    D --> D4[Highlight 4: KPI <br>"MetaSoul Kernel L3: 0 incidents"]
    D --> D5[Highlight 5: TODO <br>"Add poetic summary engine"]

    E --> E1[Heatmap: Aggressive Vocab <br>Low: Green (0.2%)]
    E --> E2[Heatmap: Emotion Surge <br>Moderate: Yellow (0.8)]
    E --> E3[Heatmap: Bias Score <br>Low: Green (10%)]

    B --> F[Footer: <br>← Prev | Next → <br>Export CSV Button]

```\)

flowchart LR
  A[対話ログ<br>(25%)] -->|クリック| B[ハイライト要約<br>(50%)]
  A --> C[Kernel温度メーター<br>(25%)]
  subgraph トップバー
    direction LR
    TB[プロジェクト名] --- FILT[期間フィルタ]
  end
  subgraph フッター
    direction LR
    CSV[CSV Export] --- PAG[← / →]
  end
