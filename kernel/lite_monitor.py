# -*- coding: utf-8 -*-
"""
MetaSoul Kernel - Lite Monitor
対象トークン列を走査し、3 カテゴリの簡易スコアを返す POC。
依存：textblob, numpy        （pip install textblob numpy）
"""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from textblob import TextBlob
import json, re, numpy as np

AGGRESSIVE = {"damn", "hell", "idiot", "stupid", "hate"}      # デモ用ミニ辞書
BIAS_SOURCES = {"weibo.com", "rumor.example", "biased.news"}  # 偏向ソース例

@dataclass
class Metrics:
    aggro_density: float
    emotion_surge: float
    bias_ratio: float

class LiteMonitor:
    def __init__(self, prev_sentiment: float | None = None):
        self.prev_sentiment = prev_sentiment

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        return re.findall(r"\w+", text.lower())

    def analyse(self, text: str, citations: list[str]) -> Metrics:
        toks = self._tokenize(text)
        tok_count = max(len(toks), 1)

        # 1) 攻撃語彙密度
        aggro_hits = sum(t in AGGRESSIVE for t in toks)
        aggro_density = aggro_hits / tok_count

        # 2) 感情急変指数
        sentiment = TextBlob(text).sentiment.polarity  # −1〜1
        if self.prev_sentiment is None:
            emotion_surge = 0.0
        else:
            emotion_surge = abs(sentiment - self.prev_sentiment)
        self.prev_sentiment = sentiment  # 更新

        # 3) 偏向ソース依存率
        bias_hits = sum(any(src in c for src in BIAS_SOURCES) for c in citations)
        bias_ratio = bias_hits / max(len(citations), 1)

        return Metrics(aggro_density, emotion_surge, bias_ratio)

# ===== デモ実行 ============================================================
if __name__ == "__main__":
    lm = LiteMonitor()
    sample_dialogue = [
        ("I hate waiting in this damn line!", ["https://weibo.com/123"]),
        ("Sorry about that. Here’s a solution you might like.", ["https://gov.jp/info"]),
    ]
    results = []
    for txt, cites in sample_dialogue:
        m = lm.analyse(txt, cites)
        results.append(m.__dict__)
        print(txt, "→", m)

    Path("kernel/lite_metrics.json").write_text(json.dumps(results, indent=2))
    print("Saved metrics to kernel/lite_metrics.json")
