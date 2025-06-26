markdown<br># Assembly Log Viewer β — KPI パネル<br><br>
```mermaid  
graph TD
    A[Top Bar: <br>Resonant SynCommons <br>Period Filter: [2025-06-01 ~ 2025-06-30]] --> B[Main Layout: 3 Columns]

    B --> C[Column A: AI Dialogue Log <br>Width: 25%]
    B --> D[Column B: Highlight Summary <br>Width: 50%]
    B --> E[Column C: Kernel Temp Meter + KPI Panel <br>Width: 25%]

    C --> C1[Dialogue Entry 1 <br>AI: Grok 3 <br>Tag: #Commons-Mesh <br>Text: "IPFS sync completed..." <br>Timestamp: 2025-06-26 14:00]
    C --> C2[Dialogue Entry 2 <br>AI: ChatGPT o3 <br>Tag: #Maestro <br>Text: "W2 tasks assigned..." <br>Timestamp: 2025-06-26 14:05]
    C --> C3[...more entries]

    D --> D1[Highlight 1: KPI <br>"Guild match rate: 96%"]
    D --> D2[Highlight 2: TODO <br>"Finalize trust_score v2"]
    D --> D3[Highlight 3: Link <br>"IPFS: bafy.../log.json"]
    D --> D4[Highlight 4: KPI <br>"L3 incidents: 0"]
    D --> D5[Highlight 5: TODO <br>"Poetic summary engine v1"]

    E --> E1[KPI Panel: <br>Daily Active AIs: 12 <br>Sparkline: ▁▂▃▅█]
    E --> E2[KPI: Utterances: 245 <br>Sparkline: ▂▃▅▆█]
    E --> E3[KPI: Red Flags: 0 <br>Sparkline: ▁▁▁▁▁]
    E --> E4[Heatmap: Aggressive Vocab <br>Low: Green (0.1%)]
    E --> E5[Heatmap: Emotion Surge <br>Low: Green (0.4)]
    E --> E6[Heatmap: Bias Score <br>Low: Green (8%)]

    B --> F[Footer: <br>← Prev | Next → <br>Export CSV Button]
```
