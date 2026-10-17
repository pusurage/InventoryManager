# Git コマンド備忘録

## 状態確認

git status

## 変更ファイル追加

git add .

## コミット

git commit -m "コミット内容"

## GitHubへ送信

git push

## 最新取得

git pull

## ブランチ確認

git branch

## 接続先確認

git remote -v

## ログ確認

git log --oneline

## 初回セットアップ

git init

git config --global user.name "ユーザー名"

git config --global user.email "メールアドレス"

## GitHub接続

git remote add origin https://github.com/ユーザー名/リポジトリ.git

git branch -M main

git push -u origin main
