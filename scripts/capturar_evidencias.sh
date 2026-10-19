#!/usr/bin/env bash
set -euo pipefail
mkdir -p docs/evidencias
adb shell wm size 720x1280
adb shell wm density 280
adb shell input keyevent 82
adb install -r app/build/outputs/apk/debug/app-debug.apk
for mode in no yes; do
  adb shell cmd uimode night "$mode"
  adb shell am force-stop com.example.superheroes
  adb shell am start -W -n com.example.superheroes/.MainActivity
  sleep 5
  if [ "$mode" = no ]; then name=tema_claro; else name=tema_oscuro; fi
  adb exec-out screencap -p > "docs/evidencias/$name.png"
done
adb shell input swipe 360 1080 360 350 500
sleep 2
adb exec-out screencap -p > docs/evidencias/lista_desplazada.png
adb shell uiautomator dump /sdcard/superheroes.xml
adb exec-out cat /sdcard/superheroes.xml > docs/evidencias/jerarquia_lista.xml
