#!/usr/bin/env bash
set +e
./gradlew connectedDebugAndroidTest --console=plain
test_status=$?
bash scripts/capturar_evidencias.sh
capture_status=$?
if [ "$test_status" -ne 0 ]; then exit "$test_status"; fi
exit "$capture_status"
