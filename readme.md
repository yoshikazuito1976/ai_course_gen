# AI Course Generator API

教育向け教材のアウトラインを自動生成する **プロンプトエンジニアリング API** です。  
OpenAI API を利用し、指定したトピックや対象学年に応じてカリキュラム案を出力します。  
FastAPI によって API 化し、Swagger UI から動作確認できます。  

---

## ✨ Features

- **プロンプトテンプレート化**  
  Jinja2 によるプロンプトテンプレートを利用して、入力値を柔軟に差し込み可能  

- **API化**  
  FastAPI を用いて `/outline` エンドポイントを実装  
  JSON 形式の入力 → 自動生成されたアウトラインを JSON で返却  

- **Swagger/OpenAPI 対応**  
  `http://localhost:8000/docs` にアクセスしてリクエスト/レスポンスをGUIで確認可能  

- **再利用可能**  
  プロンプトをコード上で管理しているため、教育分野以外にも容易に展開可能  

---

## 📦 Requirements

- Python 3.10+  
- OpenAI API Key  
- Poetry または venv 環境  

---

## 🚀 Setup

```bash
# 仮想環境作成
python -m venv .venv
source .venv/bin/activate

# 依存関係インストール
pip install -r requirements.txt

# OpenAI API Key を環境変数に設定
export OPENAI_API_KEY="your_api_key_here"

▶️ Run
bash
コードをコピーする
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
ブラウザで以下にアクセスして Swagger UI を利用できます。

http://localhost:8000/docs
📡 Usage
Endpoint
POST /outline

Request Example
json
コードをコピーする
{
  "topic": "Linux入門",
  "grade": "大学1年生"
}
Response Example


{
  "outline": [
    "1. Linuxの歴史と基本概念",
    "2. コマンドラインの基本操作",
    "3. ファイルとディレクトリ管理",
    "4. プロセスとユーザー管理",
    "5. 演習問題とまとめ"
  ]
}
📂 Project Structure

app/
├── main.py        # FastAPI エントリポイント
├── service.py     # OpenAI API 呼び出し処理
├── prompts/       # プロンプトテンプレート
├── schemas.py     # Pydantic スキーマ定義
├── config.py      # 環境変数・設定管理
🔮 Future Work
RAG (Retrieval Augmented Generation) の導入

追加エンドポイントによる教材の自動生成 (スライド, 小テスト)

Docker コンテナ化によるデプロイ

📄 License
MIT License

