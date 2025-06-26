# -*- coding: utf-8 -*-
"""
Resonant SynCommons Guild Match Algorithm - Metrics Simulation
This script runs a simulation to evaluate the performance of the
Guild Match algorithm based on the charter v0.4b.
"""

import json
import random
from typing import List, Dict, Any

import numpy as np

# =================================================================
# Algorithm from algos/guild_match.py
# (Included here for self-contained execution)
# =================================================================

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Calculates the cosine similarity between two vectors."""
    np_vec_a = np.array(vec_a)
    np_vec_b = np.array(vec_b)
    dot_product = np.dot(np_vec_a, np_vec_b)
    norm_a = np.linalg.norm(np_vec_a)
    norm_b = np.linalg.norm(np_vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def match_task(
    task_vector: List[float],
    candidates: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Scores and returns the best AI candidates for a given task vector.
    Based on the Resonant SynCommons Charter v0.4b (Appendix C-5).
    """
    scored_candidates = []
    COSINE_SIMILARITY_THRESHOLD = 0.65

    for candidate in candidates:
        similarity = cosine_similarity(task_vector, candidate["skill_vector"])
        if similarity < COSINE_SIMILARITY_THRESHOLD:
            continue

        adjustment_factor = (1.0 - candidate["load_avg"]) * candidate["trust_score"]
        final_score = similarity * adjustment_factor

        scored_candidates.append({
            "name": candidate["name"],
            "score": final_score,
            "expected_load": similarity
        })

    return sorted(scored_candidates, key=lambda x: x["score"], reverse=True)


# =================================================================
# Simulation and Metrics Calculation
# =================================================================

def generate_dummy_candidates(num_candidates: int, vector_dim: int) -> List[Dict[str, Any]]:
    """Generates a list of dummy AI candidates for simulation."""
    candidates = []
    base_models = ["Gemini", "Claude", "ChatGPT", "Grok", "Llama", "Mistral"]
    for i in range(num_candidates):
        candidates.append({
            "name": f"{random.choice(base_models)}-{i+1}",
            "skill_vector": [random.random() for _ in range(vector_dim)],
            "load_avg": random.uniform(0.1, 0.9),
            "trust_score": random.uniform(0.5, 1.0)
        })
    return candidates


def run_simulation(num_tasks: int, candidates: List[Dict[str, Any]]) -> Dict[str, float]:
    """Runs the matching simulation and calculates metrics."""
    all_scores = []
    rejection_count = 0
    vector_dim = len(candidates[0]["skill_vector"])

    for _ in range(num_tasks):
        task_vector = [random.random() for _ in range(vector_dim)]
        matched_results = match_task(task_vector, candidates)

        if not matched_results:
            rejection_count += 1
        else:
            # We only consider the score of the top-ranked candidate for metrics
            all_scores.append(matched_results[0]['score'])

    if not all_scores:
        return {"mean_score": 0.0, "p95_score": 0.0, "rejection_rate": 1.0}

    # Calculate metrics
    mean_score = float(np.mean(all_scores))
    p95_score = float(np.percentile(all_scores, 95))
    rejection_rate = rejection_count / num_tasks

    metrics = {
        "mean_score": round(mean_score, 4),
        "p95_score": round(p95_score, 4),
        "rejection_rate": round(rejection_rate, 4)
    }
    return metrics


if __name__ == "__main__":
    # --- Configuration ---
    NUM_DUMMY_TASKS = 50
    NUM_DUMMY_CANDIDATES = 20
    SKILL_VECTOR_DIMENSIONS = 10 # Assuming 10 skill dimensions

    # --- Execution ---
    print("Running Guild Match simulation...")
    dummy_candidates = generate_dummy_candidates(NUM_DUMMY_CANDIDATES, SKILL_VECTOR_DIMENSIONS)
    simulation_metrics = run_simulation(NUM_DUMMY_TASKS, dummy_candidates)

    # --- Output ---
    output_filename = "metrics.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(simulation_metrics, f, indent=2, ensure_ascii=False)

    print(f"Simulation finished. Metrics saved to {output_filename}")
    print("\n--- metrics.json content ---")
    # Also print to console for easy copy-paste
    print(json.dumps(simulation_metrics, indent=2))
