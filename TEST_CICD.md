# CI/CDの実験

目的:家計簿構築しているシステムへCI/CDを構築するための実験を行う。

## 開発の流れ

### 環境
- ローカル（venv）

- ローカル（docker）

- クラウド（Cloud Job Run）

### コマンド

```bash
# ETL
python-etl

# dbt実行
dbt run

# dbt テスト
dbt test --target=xxx

# リネージ生成のためのメタデータ作成
dbt compile
dbt docs generate#
colibri generate

```

### CI/CDのイメージ

### ローカルテストフェーズ
- ローカル（venv）で検証
  実行条件 : 製造が終了した場合
  実施内容 : コマンドを手動実行し正常終了（データの検証など含む）することを確認する。
  python-etl : python main.py
  dbt : dbt run/test/compile

- ローカル（Docker）で検証
  実行条件 : ローカル（venv）での検証が終了した場合
  実施内容 : コマンドを手動実行し正常終了（データの検証など含む）することを確認する。
  python-etl : docker build & docker run
  dbt : docker build & docker run

### CIフェーズ

- PR作成
  実行条件 : ローカル（docker）での検証が終了した場合
  実施内容 : PRを作成する。その際にdbtのみSQLの整合性・参照チェックを行う。
  python-etl : フォーマット(black --check .)、構文チェック(flake8 .)、型チェック(mypy .)、ロジックテスト(pytest tests/)
  dbt : dbt compile

### CDフェーズ

- 本番環境へ反映
  実行条件 : PRが作成され、CIに成功した場合
  実施内容 : mainブランチPush & Artifact RepositryへPush & Cloud Run Job への反映する。
  python-etl : docker build & docker push & gcloud deploy
  dbt : docker build & docker push & gcloud deploy

## 本番
- 本番実行
  実行条件 : 月初に更新データ（CSVファイル）の準備ができた場合
  実施内容 : シェルを実行する。
  python-etl : cloud run jon (python main.py)
  dbt : cloud run job (dbt run)
※将来的にはshellで動かしたい。
