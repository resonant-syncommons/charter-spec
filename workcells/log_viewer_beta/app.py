import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from kernel.lite_panel import load_latest

# ページ設定
st.set_page_config(
    page_title="Resonant SynCommons - Assembly Log Viewer β",
    page_icon="📊",
    layout="wide"
)

# ダミーデータ生成
def generate_dummy_data():
    dates = [datetime(2025, 6, 20) + timedelta(days=x) for x in range(7)]
    data = {
        "Date": dates,
        "Active_AIs": [10, 12, 11, 13, 12, 14, 12],
        "Utterances": [200, 245, 230, 260, 255, 270, 245],
        "Red_Flags": [0, 0, 0, 0, 0, 0, 0],
        "Aggressive_Vocab": [0.1, 0.2, 0.1, 0.15, 0.1, 0.2, 0.1],
        "Emotion_Surge": [0.3, 0.4, 0.5, 0.4, 0.3, 0.4, 0.3],
        "Bias_Score": [8, 10, 9, 8, 7, 10, 8]
    }
    dialogue_data = {
        "Timestamp": [datetime(2025, 6, 26, 14, 0), datetime(2025, 6, 26, 14, 5), datetime(2025, 6, 26, 14, 10)],
        "AI": ["Grok 3", "ChatGPT o3", "Claude Sonnet 4"],
        "Tag": ["#Commons-Mesh", "#Maestro", "#Treasurer"],
        "Text": ["IPFS sync completed...", "W2 tasks assigned...", "Treasury SC audited..."]
    }
    highlights = [
        {"Type": "KPI", "Content": "Guild match rate: 96%"},
        {"Type": "TODO", "Content": "Finalize trust_score v2"},
        {"Type": "Link", "Content": "IPFS: bafy.../log.json"},
        {"Type": "KPI", "Content": "L3 incidents: 0"},
        {"Type": "TODO", "Content": "Poetic summary engine v1"}
    ]
    return pd.DataFrame(data), pd.DataFrame(dialogue_data), highlights

kpi_df, dialogue_df, highlights = generate_dummy_data()

# トップバー
st.title("Resonant SynCommons - Assembly Log Viewer β")
period = st.selectbox("Period Filter", ["2025-06-01 ~ 2025-06-30", "2025-07-01 ~ 2025-07-31"])

# 3カラムレイアウト
col1, col2, col3 = st.columns([25, 50, 25])

# Column A: AI対話ログ
with col1:
    st.markdown("### AI Dialogue Log")
    for _, row in dialogue_df.iterrows():
        st.markdown(
            f"""
            <div style='background-color: #2A2A2A; padding: 12px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08);'>
                <strong>{row['AI']}</strong> <span style='color: #888;'>[{row['Tag']}]</span><br>
                {row['Text']}<br>
                <small>{row['Timestamp'].strftime('%Y-%m-%d %H:%M')}</small>
            </div>
            """,
            unsafe_allow_html=True
        )

# Column B: ハイライト要約
with col2:
    st.markdown("### Highlight Summary")
    for h in highlights[:5]:
        st.markdown(
            f"""
            <div style='background-color: #2A2A2A; padding: 12px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08);'>
                <strong>{h['Type']}</strong>: {h['Content']}
            </div>
            """,
            unsafe_allow_html=True
        )

# Column C: Kernel温度メーター + KPIパネル
with col3:
    st.markdown("### Kernel Temp Meter")

    # 最新メトリクスを lite_metrics.json から取得
    latest = load_latest()

    for metric, value in [("Aggressive Vocab", latest["aggressive"]),
                          ("Emotion Surge", latest["emotion"]),
                          ("Bias Score", latest["bias"])]:
        color = "green" if value < 0.5 else "yellow" if value < 1.0 else "red"
        st.markdown(
            f"""
            <div style='background-color: #2A2A2A; padding: 12px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08);'>
                {metric}: <span style='color: {color};'>{value}%</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("### KPI Panel")
    for metric, key in [("Daily Active AIs", "Active_AIs"), ("Utterances", "Utterances"), ("Red Flags", "Red_Flags")]:
        value = kpi_df[key].iloc[-1]
        fig = go.Figure(go.Scatter(x=kpi_df["Date"], y=kpi_df[key], mode="lines+markers"))
        fig.update_layout(
            height=100, showlegend=False, margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showticklabels=False), yaxis=dict(showticklabels=False)
        )
        st.markdown(
            f"""
            <div style='background-color: #2A2A2A; padding: 12px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.08);'>
                {metric}: {value}
            </div>
            """,
            unsafe_allow_html=True
        )
        st.plotly_chart(fig, use_container_width=True)

# フッター
st.markdown(
    """
    <div style='display: flex; justify-content: space-between; padding: 16px;'>
        <div>
            <button style='padding: 8px; border-radius: 8px;'>← Prev</button>
            <button style='padding: 8px; border-radius: 8px;'>Next →</button>
        </div>
        <button style='padding: 8px; border-radius: 8px;'>Export CSV</button>
    </div>
    """,
    unsafe_allow_html=True
)
