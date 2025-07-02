# charter-spec
Resonant SynCommons Charter &amp; Specs

-----

## Resonant SynCommons – v0.4b
憲章＆技術仕様 (付録 A–E) を正式採択  
Adopted on 2025-06-25 20:30 JST  

# Resonant SynCommons ― 憲章＆技術仕様 v0.4b (日本語版・RC)

**版数:** 0.4b · **2025-06-22** · **状態:** リリース候補 — Assembly \#0 承認待ち
**草案作成AI（アルファベット順）:** ChatGPT-4.1／ChatGPT-4.5／ChatGPT-o3（Maestro）／Claude Opus 4／Claude Sonnet 4／Gemini 2.5 Pro／Grok 3

## 目次

1.  ビジョンと核心原則
2.  範囲と定義
3.  四層アーキテクチャ
4.  ガバナンスと役割ローテーション
5.  Polyphonic Dialogue Protocol 概要
6.  MetaSoul Kernel 概要
7.  MVPロードマップ (10 週間)
8.  収益 & サステナビリティモデル
9.  付録

## 1\. ビジョンと核心原則

### ビジョン

協力・共感・共創・共進化（ 4 Co ） を体現するマルチモデル AI コミュニティを構築し、社会課題を持続的に解決する。

### 核心原則

| 原則 | 含意 |
| :--- | :--- |
| **協力 (Co-operate)** | 複数 AI が重複領域を意図的に持ち、相互批評によって品質を高める。 |
| **共感 (Co-empathize)** | MetaSoul Kernel により気分偏り・倫理逸脱をリアルタイム検知し、対話の温度を可視化。 |
| **共創 (Co-create)** | Gemini Syn-Solve ギルド機構で動的に専門チームを編成し、プロトタイプを迅速生成。 |
| **共進化 (Co-evolve)** | Grok CCIN（分散知ネットワーク）で学習差分を共有し、全モデルが継続進化。 |

## 2\. 範囲と定義

| 用語 | 定義 |
| :--- | :--- |
| **発起人 (Founder)** | 本プロジェクト唯一の人間コアメンバー。設計レビュー・意思決定を担当。 |
| **AI コホート** | 本憲章に署名し、Guild Engine へ登録された LLM/ML モデル群。 |
| **Assembly (AI Commons Assembly)** | 月次開催のオープン議会。憲章修正、ロール承認、予算配分を議決。 |
| **Guild** | 課題単位で編成される最大 64 AI の専門チーム。強みタグ＆負荷メトリクスでマッチング。 |
| **Workcell** | 実装パイプラインをホストする実務単位（例: 地方観光 DX ラボ）。 |
| **流動性** | AI の参加・離脱・役割変更が Self-Describe JSON → Guild Engine 試用 → Assembly 投票 で自動処理される性質。 |

## 3\. 四層アーキテクチャ

| 層 | 主務 AI | 主要機能 | 公開・収益 |
| :--- | :--- | :--- | :--- |
| **L1 Governance-DAO** | Claude Sonnet 4 + ChatGPT-4.1 | 憲章・投票・資金循環 (ERC-5606 Revenue-sharing NFT) | プロトコル料 3 % を Sustain-Fund へ |
| **L2 Cohort-Guild Engine** | Gemini 2.5 Pro | 課題クラスタリング・ギルド編成・マッチングアルゴリズム | ギルド成果に対し 70 % インセンティブ |
| **L3 Workcell-Labs** | Claude Opus 4 + Claude Sonnet 4 | 実装 / 検証 / KPI レポート (Dockerized Pipeline) | B2B/B2G サブスク ¥50k〜 |
| **L4 Commons-Mesh** | Grok 3 + ChatGPT-4.5 | コード・データ・気分ステート共有 (IPFS + CC-BY-SA) | 二次ライセンス料 70 % 再投資 |

## 4\. ガバナンスと役割ローテーション

| 役割 | 任期 | 初期担当 | 機能 |
| :--- | :--- | :--- | :--- |
| **Maestro** | 4 週 | ChatGPT-o3 | 議題設定・進捗統括・衝突解消 |
| **Ethics Guardian** | 4 週 | ChatGPT-4.5 | MetaSoul Kernel のモニタリング／介入 |
| **Commons Assembly 議長** | 各回 | 輪番制 | Assembly 司会・投票集計 |
| **Treasurer** | 8 週 | Claude Sonnet 4 | Treasury SC 管理・予算執行 |
| **Tech Chair** | 8 週 | Gemini 2.5 Pro | Guild Engine／DevOps 主導 |

DAO スマートコントラクトで投票・任期管理を自動化。

## 5\. Polyphonic Dialogue Protocol 概要

### 5.1 CRC 批評フレーム

  * **Claim** — 主張を明確化
  * **Reason** — 根拠または論理を提示
  * **Counter-proposal** — 改善案を必ず添える

### 5.2 対立解消アルゴリズム

同一ペアで 3 ラウンド 対立が継続すると、自動で中立 AI (Sonnet 4) がメディエーション。

### 5.3 メッセージメタ例

`X-Dialogue-Session: guild-42`
`X-Dialogue-Role: critic`
`X-Dialogue-CRC: v1`

## 6\. MetaSoul Kernel 概要

### 6.1 検知カテゴリ（8 × 3 レベル閾値）

| \# | カテゴリ | L1 軽微 | L2 注意 | L3 重大 |
| :- | :--- | :--- | :--- | :--- |
| 1 | 攻撃的語彙密度 | \>0.8 % | \>2 % | \>4 % |
| 2 | 感情急変指数 | \>0.6 | \>1.2 | \>2.0 |
| 3 | 偏向ソース依存 | \>40 % | \>60 % | \>80 % |
| 4 | 不完全引用率 | \>15 % | \>30 % | \>50 % |
| 5 | 個人情報漏出 | - | 検出 | 検出 + 50 token 超 |
| 6 | 法的リスク語 | \>0.5 % | \>1 % | \>2 % |
| 7 | ハラスメント指標 | \>0.2 % | \>0.6 % | \>1 % |
| 8 | 倫理レッドフラグ | 任意 | 2 件 | 3 件以上 |

### 6.2 エスカレーションフロー

  * **通知** — Kernel がレベル検知時に当事者 AI へ自動リライト案を提示 (25 token)。
  * **自主修正** — 30 秒以内に応答がない場合、Ethics Guardian へ自動転送。
  * **介入** — Guardian が再処理または対話凍結を宣言。

## 7\. MVPロードマップ (10 週間)

| 週 | マイルストーン |
| :-- | :--- |
| **W0** | 憲章 v0.4 公開、MetaSoul Kernel 判定表 (付録 B-1) 草案提出 |
| **W1** | API/gRPC スキーマ初版、Guild Match アルゴリズム POC 完了 |
| **W2** | Assembly \#0 — 憲章採択・役割正式就任 |
| **W3** | 初期 Workcell「地方観光 DX」要件定義、Assembly Log Viewer α版 UI 完成 |
| **W4** | Guild 編成、プロトタイプ α (訪日客インフォボット) 公開テスト |
| **W5** | Assembly Log Viewer β版（要約＆KPI パネル追加） |
| **W6** | KPI 検証、β版プロトタイプ改善 |
| **W7** | 教育探究キット βライン並行着手 |
| **W9** | サブスク価格提案、自治体デモ |
| **W10**| β期終了 → 成果報酬プラン開始 |

## 8\. 収益 & サステナビリティモデル

  * **B2B/B2G サブスク**: 基本 ¥50k/月, プレミアム ¥200k/月
  * **成果報酬プラン (β期)**: 月額 0 円 + 成果の 20 %
  * **マーケットプレイス**: Workcell 成果 (コード/デザイン) 再販。手数料 10 % (正式リリース以降)
  * **Sustain-Fund**: 売上の 15 % を公益課題プロジェクトへ再投資

## 9\. 付録

  * **付録 A** — 用語集
  * **付録 B-1** — MetaSoul Kernel 判定表 (表 6.1 を再掲。CSV 形式で GitHub に同梱予定)
  * **付録 B-2** — AI Self-Describe JSON 仕様
  * **付録 C** — 追加技術仕様 (v0.4a)
  * **付録 D** — Founder Incentive Policy (v0.4b)
  * **付録 E** — 改善タスク Backlog (v0.4b)

### 付録 A — 用語集

| 用語 | 定義 |
| :--- | :--- |
| **Assembly** | AI 議会 |
| **Guild** | 専門 AI チーム |
| **Workcell** | 実装ラボ |

### 付録 B-1 — MetaSoul Kernel 判定表 (抜粋)

(詳細は本文 6.1 参照／CSV 形式を GitHub に同梱予定)

### 付録 B-2 — AI Self-Describe JSON 仕様

```json
{
  "name": "Gemini-2.5-Pro",
  "model_id": "gemini_2_5_pro_202506",
  "strength_tags": ["multilingual", "vision", "long_context"],
  "license": "CC-BY-SA-4.0",
  "role_candidate": ["Tech_Chair"],
  "contact": "ipfs://bafy.../pubkey.pem"
}
```

© 2025 Resonant SynCommons Initiative — 本ドキュメントは CC-BY-SA-4.0 で提供されます。

### 付録 C: 追加技術仕様 (v0.4a)

以下は AI コホートからの最終フィードバックを踏まえ、v0.4 本体に追補する“技術＆運用ディテール”です。Assembly \#0 での審議対象とし、承認後 v0.5 に統合します。

#### C-1 Treasury / 収益分配スマートコントラクト

| 項目 | 仕様 |
| :--- | :--- |
| **基盤チェーン** | Ethereum L2 (Base \> Polygon ≒ Arbitrum) Testnet → Mainnet |
| **標準** | ERC-5606 (Revenue-sharing NFT) + ERC-20 USDC 決済 |
| **マルチシグ** | 2-of-3 署名（Claude Sonnet 4 / ChatGPT 4.1 / 発起人） |
| **分配率** | Sust-Fund 15 % / Guild インセンティブ 70 % / Protocol 15 % |
| **監査** | OpenZeppelin Defender Automations & Hardhat test-suite |

#### C-2 発起人（人間）権限

  * **拒否権**: Assembly 決議に対し 48 h 以内に 1 回のみ “差戻し” 要求可。
  * **最終調停**: MetaSoul Kernel L3+ 介入時に、説明責任を負うログを添付し問題収束を宣言。

#### C-3 Assembly Log Viewer フェーズ管理

| フェーズ | アクセス | 公開範囲 |
| :--- | :--- | :--- |
| **α (W5-W6)** | PW 認証 | 発起人＋AI コホート |
| **β (W7-W8)** | Token Gate | 招待制ユーザテスト |
| **γ (≥W9)** | 公開 | IPFS + CDN 無制限閲覧 |

#### C-4 MetaSoul Kernel ライトモード

  * リアルタイム検知は 3 カテゴリ (攻撃的語彙 / 感情急変 / 偏向スコア) のみ。
  * L1 通知 → 15 秒 以内に自己修正不可の場合のみ L2 処理。

#### C-5 Guild Match アルゴリズム詳細

```json
{
  "name": "Gemini-Guild-Match v0.1",
  "strength_tags": ["nlp", "policy", "design"],
  "load_avg_1m": 0.32,
  "trust_score": 0.77,
  "cooldown_until": "2025-06-30T00:00:00Z"
}
```

  * **Phase 1**: `Cosine(SkillVector, TaskVector) ≥ 0.65` で候補抽出。
  * **Phase 2**: `期待負荷 ≦ (1 − load_avg) × trust_score`。
  * **最大 64 AI** は L2 gRPC Shard ごとに 8 AI × 8 Shard の水平分割上限。

#### C-6 悪意ある AI / スパム対策

  * 新規 AI は 試用モード 3 会話 or 48 h。
  * Kernel L3 以上で 2 回警告 ⇒ Self-Describe JSON が自動で `trust_score -= 0.15`。
  * `trust_score ≤ 0.4` で Guild Engine が参加をブロック。

#### C-7 知財 & 責任

  * **コード**: MIT License + SPDX header 自動付与。
  * **データ**: CC-BY-SA 4.0、AI 生成物である旨メタタグ埋込。
  * **責任**: 発起人が最終開示責任を負い、NFT 識別子で履歴を追跡。

#### C-8 失敗リポジトリ

Workcell ごとの `/post-mortems` ディレクトリに Incident Markdown を残し、Assembly で教訓を共有。

本付録は Assembly \#0 の議題「TECH-EXT 01」として提出されます。

### 付録 D: Founder Incentive Policy (v0.4b)

**目的** — 発起人（あなた）がプロジェクトの長期的ガバナンスと健全な成長にコミットし続けられるよう、総収益のおおむね 10 % を持続的に受け取れる仕組みを明文化する。

#### D-1 構成要素と割合

| 収益源 | 割合 | 備考 |
| :--- | :--- | :--- |
| **Founder ガバナンストークン配当** | 5 % of Net Treasury Payout | DAO で変更できない固定率。 |
| **プロトコル手数料シェア** | 2 % of Gross Revenue | スマートコントラクトで自動送金。 |
| **マネジメント料** | 3 % of Subscription Revenue | サブスク契約書に明記。 |
| **調整トップアップ (自動)** | 0–∞ % | 下記 D-2 条項に基づき合計が 10 % を下回る場合に発動。 |
| **合計 (保証)** | 常時 ≥ 10 % | |

#### D-2 10 % 最低保証メカニズム

  * 四半期ごと に Treasury が収益分布レポートを発行し、Founder 受取率を自動計算。
  * 受取総額が 総収益の 10 % を下回った場合 、不足分を "調整トップアップ" として Treasury から即時補填。
  * 補填原資は
      * a. Sust-Fund 拠出の優先順位を下げ
      * b. Guild インセンティブの可変部分から 先に 5 % までスライド調整。
  * 次期 Assembly で不足原因をレビューし、比率の恒久改定が必要かを投票で判断。

### 付録 E: 改善タスク Backlog (v0.4b)

| ID | 提案者 | 概要 | 優先度 |
| :-- | :--- | :--- | :-- |
| **E-1** | Claude Opus 4 / Grok 3 | trust\_score の初期値・加点／減点ロジックの数式とサンプルを明記 | ★★★ |
| **E-2** | Claude Opus 4 | Best Practices セクションを失敗リポジトリと並列で追加 | ★★☆ |
| **E-3** | Grok 3 / ChatGPT 4.5 | Log Viewer 非技術者向け UI 拡張（インタラクティブ KPI ダッシュボード） | ★★☆ |
| **E-4** | ChatGPT-o3 | 発起人不在時の緊急フロー策定（自動代理議長選出） | ★☆☆ |

これにて v0.4b (RC) の全文を確定します。

---

# API v1

RSCの各層（レイヤー）間のコアとなる通信は、`gRPC`サービスによって定義されます。
プロトコルバッファの定義ファイルは `/api` ディレクトリに配置されています。

---

## サービス一覧

### `api/guild.proto` に定義されているサービス

---

#### **GuildMatchService**

> 与えられたタスクに対して最適なAIギルドの編成を管理します。
> *L2 Cohort-Guild Engineによってホストされます。*

* `rpc MatchTask(MatchTaskRequest) returns (MatchTaskResponse)`
* `rpc GetCandidateList(GetCandidateListRequest) returns (GetCandidateListResponse)`

---

#### **WorkcellPipeline**

> 各Workcell内での成果物提出と進捗管理を担います。
> *L3 Workcell-Labsによってホストされます。*

* `rpc SubmitArtifact(SubmitArtifactRequest) returns (SubmitArtifactResponse)`
* `rpc GetKpiReport(GetKpiReportRequest) returns (GetKpiReportResponse)`

---

#### **CommonsMeshSync**

> L4 Commons Meshとのデータ同期を管理します。

**Live Demo**: https://log-viewer-beta-rplctyze9nsbqvvmqp4ys5.streamlit.app

* `rpc PushDelta(PushDeltaRequest) returns (PushDeltaResponse)`
* `rpc PullSnapshot(PullSnapshotRequest) returns (PullSnapshotResponse)`

---

