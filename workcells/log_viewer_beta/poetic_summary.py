import pandas as pd

def poetic_summary(dialogue_df: pd.DataFrame) -> str:
    """
    Polyphonic Dialogue Protocol 準拠のタグを参考に、120文字程度の詩的要約を生成する。
    ※外部APIは使用しない。各ラウンドの発言から印象語・構文・転調点を抽出し「一日分の響き」を表現
    """
    if dialogue_df.empty or "content" not in dialogue_df.columns:
        return "No dialogue data was provided."

    contents = dialogue_df["content"].tolist()
    # 主要な印象語・動詞・登場語句を抽出（簡易版）
    joined = " ".join(contents)
    keywords = []
    for word in ["共鳴", "問い", "応答", "調和", "葛藤", "気配", "響き", "分岐", "選択", "進化", "感情", "可能性"]:
        if word in joined:
            keywords.append(word)

    # 対話の始点と終点を抽象化
    first = contents[0][:18] if contents else ""
    last = contents[-1][-18:] if contents else ""

    # 詩的組立
    base = (
        f"〈Polyphonic Tag: Resonance〉\n"
        f"今日の対話は「{', '.join(keywords) or '対話'}」を軸に、\n"
        f"“{first}...”から“...{last}”へ。\n"
        f"多層の声が交差し、余白に新たな問いが残る一日だった。"
    )

    # 120文字以内にトリム
    if len(base) > 120:
        base = base[:116] + "…"
    return base
