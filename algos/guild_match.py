# -*- coding: utf-8 -*-
"""
Resonant SynCommons Guild Match Algorithm - Proof of Concept
"""
import math
from typing import List, Dict, Any, Tuple

import numpy as np


def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """2つのベクトル間のコサイン類似度を計算します。

    Args:
        vec_a (List[float]): ベクトルA。
        vec_b (List[float]): ベクトルB。

    Returns:
        float: コサイン類似度 (-1.0 から 1.0)。
    """
    # np.arrayに変換
    np_vec_a = np.array(vec_a)
    np_vec_b = np.array(vec_b)

    # ドット積（内積）
    dot_product = np.dot(np_vec_a, np_vec_b)

    # 各ベクトルのノルム（大きさ）
    norm_a = np.linalg.norm(np_vec_a)
    norm_b = np.linalg.norm(np_vec_b)

    # ゼロ除算を避ける
    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def match_task(
    task_vector: List[float],
    candidates: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    与えられたタスクベクトルに対し、最適なAI候補をスコアリングし、降順で返します。

    このアルゴリズムは、Resonant SynCommons憲章 v0.4b (付録 C-5) に基づいています。
    スコアリングロジックは以下の通りです。

    1.  **Phase 1: スキル適合性フィルタリング**
        - タスクベクトルと各AI候補のスキルベクトルのコサイン類似度を計算します。
        - 類似度が `0.65` 未満の候補は足切りされます。

    2.  **Phase 2: 負荷と信頼性によるスコア調整**
        - 調整係数 = `(1 - 候補者の平均負荷) * 候補者の信頼スコア`
        - 最終スコア = `コサイン類似度 * 調整係数`

    3.  **出力**
        - フィルタリングを通過した候補を、最終スコアの降順でソートして返します。

    Args:
        task_vector (List[float]):
            解決すべきタスクの要求スキルを表すベクトル。
        candidates (List[Dict[str, Any]]):
            AI候補のリスト。各要素は以下のキーを持つ辞書です。
            - "name" (str): AIの名称。
            - "skill_vector" (List[float]): AIのスキルセットを表すベクトル。
            - "load_avg" (float): AIの平均負荷 (0.0 - 1.0)。
            - "trust_score" (float): AIの信頼スコア (0.0 - 1.0)。

    Returns:
        List[Dict[str, Any]]:
            スコアリングされ、ソートされたAI候補のリスト。
            各要素は以下のキーを持つ辞書です。
            - "name" (str): AIの名称。
            - "score" (float): 最終評価スコア。
            - "expected_load" (float): 期待される負荷（コサイン類似度）。
    """
    scored_candidates = []

    # 定数: コサイン類似度の閾値
    COSINE_SIMILARITY_THRESHOLD = 0.65

    for candidate in candidates:
        # 必須キーの存在チェック
        required_keys = ["name", "skill_vector", "load_avg", "trust_score"]
        if not all(key in candidate for key in required_keys):
            # 必須キーが不足している場合はスキップ
            continue

        # Phase 1: コサイン類似度によるスキル適合性評価
        similarity = cosine_similarity(task_vector, candidate["skill_vector"])

        # 閾値未満の候補は足切り
        if similarity < COSINE_SIMILARITY_THRESHOLD:
            continue

        # Phase 2: 負荷と信頼スコアによる調整
        load_avg = candidate["load_avg"]
        trust_score = candidate["trust_score"]
        adjustment_factor = (1.0 - load_avg) * trust_score

        # 最終スコアの計算
        final_score = similarity * adjustment_factor

        scored_candidates.append({
            "name": candidate["name"],
            "score": final_score,
            "expected_load": similarity  # 期待負荷は純粋なスキル適合度とする
        })

    # 最終スコアの降順でソート
    sorted_candidates = sorted(
        scored_candidates,
        key=lambda x: x["score"],
        reverse=True
    )

    return sorted_candidates


# =================================================================
# Test Code
# =================================================================

if __name__ == "__main__":
    # --- テスト用のサンプルデータ ---

    # タスク：日本語での自然言語処理と、Webデザインに関するタスク
    # [日本語, 英語, コーディング, デザイン, 分析]
    sample_task_vector = [0.9, 0.1, 0.5, 0.8, 0.3]

    # AI候補のリスト
    sample_candidates = [
        {
            "name": "Gemini 2.5 Pro",
            "skill_vector": [0.9, 0.8, 0.7, 0.6, 0.9],  # 万能型
            "load_avg": 0.5,
            "trust_score": 0.95,
        },
        {
            "name": "Claude Sonnet 4",
            "skill_vector": [0.95, 0.7, 0.4, 0.5, 0.9], # 分析・言語特化型
            "load_avg": 0.3,
            "trust_score": 0.9,
        },
        {
            "name": "DALL-E 3",
            "skill_vector": [0.1, 0.1, 0.0, 0.95, 0.2], # デザイン特化型
            "load_avg": 0.8,
            "trust_score": 0.85,
        },
        {
            "name": "Code Llama",
            "skill_vector": [0.1, 0.2, 0.9, 0.1, 0.3], # コーディング特化（タスクとの関連性低い）
            "load_avg": 0.4,
            "trust_score": 0.98,
        },
        {
            "name": "Experimental AI",
            "skill_vector": [0.9, 0.8, 0.7, 0.6, 0.9], # Geminiと同じスキルだが負荷と信頼性が低い
            "load_avg": 0.9,
            "trust_score": 0.6,
        },
    ]

    # --- アルゴリズムの実行 ---
    print("--- Guild Match Algorithm POC ---")
    print(f"Task Vector: {sample_task_vector}\n")

    matched_guild = match_task(sample_task_vector, sample_candidates)

    # --- 結果の表示 ---
    print("--- Matched Guild Candidates (Sorted) ---")
    if not matched_guild:
        print("No suitable candidates found.")
    else:
        for i, member in enumerate(matched_guild):
            print(f"Rank {i+1}:")
            print(f"  Name: {member['name']}")
            print(f"  Final Score: {member['score']:.4f}")
            print(f"  Expected Load (Similarity): {member['expected_load']:.4f}")
            print("-" * 20)

    # --- 期待される結果の考察 ---
    # 1. Gemini: スキルベクトルがタスクと全体的に合致。負荷・信頼性も良好で高スコアが期待される。
    # 2. Claude: 言語・分析能力は高いが、デザインとコーディングがやや低め。しかし負荷が低いためスコアは伸びるはず。
    # 3. DALL-E: デザインスキルは完璧だが他が低い。類似度は閾値を超えるか微妙なライン。超えても負荷が高いためスコアは抑えめか。
    # 4. Code Llama: スキルがタスクと合致しないため、コサイン類似度が閾値(0.65)を下回り、足切りされる可能性が高い。
    # 5. Experimental AI: Geminiとスキルは同じだが、負荷が極めて高く信頼性も低いため、スコアは大幅に低くなるはず。
