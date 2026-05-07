#!/bin/bash
set -e

echo "========================================="
echo "  Ollama Custom Container Starting..."
echo "  OLLAMA_MODEL : ${OLLAMA_MODEL:-'(not set)'}"
echo "========================================="

# [개선점 2] 시그널 트랩 — SIGTERM/SIGINT 수신 시 ollama serve에 전달하여 정상 종료
ollama serve &
OLLAMA_PID=$!
trap 'kill ${OLLAMA_PID} 2>/dev/null; wait ${OLLAMA_PID} 2>/dev/null' SIGTERM SIGINT

echo "[INFO] Waiting for ollama server to be ready..."
MAX_WAIT=60
WAITED=0
until curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; do
  if [ "$WAITED" -ge "$MAX_WAIT" ]; then
    echo "[ERROR] Ollama server did not start within ${MAX_WAIT}s. Exiting."
    exit 1
  fi
  sleep 2
  WAITED=$((WAITED + 2))
done
echo "[INFO] Ollama server is ready. (waited ${WAITED}s)"

if [ -n "${OLLAMA_MODEL}" ]; then
  for MODEL in ${OLLAMA_MODEL}; do
    echo "[INFO] Pulling model: ${MODEL}"
    # [개선점 2] 모델 pull 실패 시 경고만 출력하고 계속 진행 (set -e 무시)
    if ollama pull "${MODEL}"; then
      echo "[INFO] Model pull complete: ${MODEL}"
    else
      echo "[WARN] Failed to pull model: ${MODEL} — skipping"
    fi
  done
else
  echo "[WARN] OLLAMA_MODEL is not set. No model will be pulled automatically."
fi

echo "[INFO] All models ready. Keeping server alive..."
wait ${OLLAMA_PID}
