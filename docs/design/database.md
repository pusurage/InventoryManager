# DB設計

## users

ユーザー情報

- id
- name
- image_path

## items

アイテムマスタ

- id
- name
- effect
- default_duration

## user_items

ユーザー所持アイテム

- id
- user_id
- item_id
- expires_at
- created_at
