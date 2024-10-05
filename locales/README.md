## Create new translation for specific file

```bash
xgettext -d vdosumry -o locales/vdosumry.pot --no-location vdosumry/main.py
```

## Create new translation for locale

```bash
mkdir -p locales/zh_TW/LC_MESSAGES
msginit -l zh_TW -i locales/vdosumry.pot -o locales/zh_TW/LC_MESSAGES/vdosumry.po
```

## Build translation

```bash
msgfmt locales/zh_TW/LC_MESSAGES/vdosumry.po -o locales/zh_TW/LC_MESSAGES/vdosumry.mo 
```