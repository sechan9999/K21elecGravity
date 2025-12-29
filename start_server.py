#!/usr/bin/env python3
"""
K21 Election Dashboard - Local Web Server
포트 3000에서 대시보드를 실행합니다.
"""

import http.server
import socketserver
import os

# 포트 설정
PORT = 3000

# 현재 디렉토리를 웹 루트로 설정
os.chdir('/home/user/K21elecGravity')

# HTTP 요청 핸들러
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS 헤더 추가 (필요한 경우)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        # 로그 메시지 포맷 개선
        print(f"[{self.log_date_time_string()}] {format % args}")

# 서버 실행
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print("=" * 70)
    print(f"🚀 K21 대선 개표 대시보드 웹 서버 시작")
    print("=" * 70)
    print(f"\n📊 대시보드 접속 URL:")
    print(f"   http://localhost:{PORT}/dashboard_nationwide.html")
    print(f"\n📁 제공되는 파일:")
    print(f"   - 전국 대시보드: /dashboard_nationwide.html")
    print(f"   - 지역 대시보드: /dashboard_province_*.html")
    print(f"   - 엑셀 파일: /K21_대선_개표결과_상세.xlsx")
    print(f"   - 기존 엑셀: /election_results_complete.xlsx")
    print(f"\n⏸️  서버 중지: Ctrl + C")
    print("=" * 70)
    print(f"\n서버가 포트 {PORT}에서 실행 중입니다...")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n서버를 종료합니다...")
        httpd.shutdown()
