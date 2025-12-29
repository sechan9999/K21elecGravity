# K21 대선 대시보드 - 로컬 실행 가이드

## 📥 1단계: 프로젝트 다운로드

### GitHub에서 다운로드
```bash
git clone https://github.com/sechan9999/K21elecGravity.git
cd K21elecGravity
git checkout claude/review-changes-mjr4v57x1h5a9ius-aQ6jY
```

또는 ZIP 파일로 다운로드:
https://github.com/sechan9999/K21elecGravity/archive/refs/heads/claude/review-changes-mjr4v57x1h5a9ius-aQ6jY.zip

## 🚀 2단계: 로컬 서버 실행

### 방법 A: 간단한 스크립트 (Mac/Linux)
```bash
./start_dashboard.sh
```

### 방법 B: Python 직접 실행 (Windows/Mac/Linux)
```bash
python -m http.server 3000
```

### 방법 C: 향상된 서버
```bash
python start_server.py
```

## 🌐 3단계: 브라우저 접속

브라우저를 열고 다음 주소로 접속:
```
http://localhost:3000/dashboard_nationwide.html
```

## 📊 접속 가능한 페이지

- 전국 대시보드: http://localhost:3000/dashboard_nationwide.html
- 강원 대시보드: http://localhost:3000/dashboard_province_강원.html
- 경기 대시보드: http://localhost:3000/dashboard_province_경기.html
- ... (기타 지역 대시보드)

## 📥 엑셀 다운로드

대시보드에서 직접 다운로드하거나:
- K21_대선_개표결과_상세.xlsx (7개 시트)
- election_results_complete.xlsx (18개 탭)

## ❗ 주의사항

- Python 3.x가 설치되어 있어야 합니다
- 포트 3000이 사용 중이면 다른 포트로 변경하세요:
  ```bash
  python -m http.server 8000
  # http://localhost:8000/dashboard_nationwide.html
  ```

## 🛑 서버 중지

터미널에서 `Ctrl + C` 키를 누르세요.
