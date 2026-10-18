# Git コマンド備忘録

## よく使う流れ

```bash
git status

git add .

git commit -m "コミット内容"

git push
```

---

## 状態確認

### 変更状態確認

```bash
git status
```

### 変更内容確認

```bash
git diff
```

### コミット履歴確認

```bash
git log --oneline
```

### 現在のブランチ確認

```bash
git branch
```

### リモートブランチ一覧

```bash
git branch -a
```

### 接続先確認

```bash
git remote -v
```

---

## ファイル操作

### 変更ファイル追加

```bash
git add .
```

### add取り消し

```bash
git restore --staged ファイル名
```

例

```bash
git restore --staged README.md
```

### コミット前の変更を取り消し

```bash
git restore ファイル名
```

例

```bash
git restore README.md
```

---

## コミット

```bash
git commit -m "コミット内容"
```

例

```bash
git commit -m "README更新"
```

---

## GitHub操作

### GitHubへ送信

```bash
git push
```

### 最新取得

```bash
git pull
```

### リモート情報取得

```bash
git fetch
```

---

## ブランチ

### ブランチ作成＋移動

```bash
git switch -c develop
```

または

```bash
git checkout -b develop
```

### ブランチ切り替え

```bash
git switch main
```

または

```bash
git checkout main
```

### ブランチ削除

```bash
git branch -d develop
```

### ブランチをGitHubへPush

```bash
git push -u origin develop
```

※ 初回のみ

---

## Pull Request運用

### developへPush

```bash
git push
```

### GitHubで実施

1. Pull requests
2. New Pull Request
3. develop → main
4. Create Pull Request
5. Merge Pull Request

---

## マージ

### mainへ移動

```bash
git switch main
```

### 最新取得

```bash
git pull
```

### developをマージ

```bash
git merge develop
```

### GitHubへ反映

```bash
git push
```

---

## 初回セットアップ

### Git初期化

```bash
git init
```

### ユーザー設定

```bash
git config --global user.name "ユーザー名"

git config --global user.email "メールアドレス"
```

---

## GitHub接続

```bash
git remote add origin https://github.com/ユーザー名/リポジトリ.git

git branch -M main

git push -u origin main
```

---

## リモートURL変更

```bash
git remote set-url origin URL
```

---

## .gitignore確認

```bash
git check-ignore -v ファイル名
```

例

```bash
git check-ignore -v data/items.db
```

---

## InventoryManager 開発フロー

```bash
git switch develop

# 作業

git add .

git commit -m "機能追加"

git push
```

↓

GitHub

```text
Pull Request
develop → main
Merge
```