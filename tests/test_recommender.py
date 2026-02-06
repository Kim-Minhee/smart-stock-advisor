import sys
import os
import pandas as pd

# src 모듈 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.technical import TechnicalAnalysisRecommender

def test_recommender():
    recommender = TechnicalAnalysisRecommender()
    
    # 테스트할 종목 리스트 (국내/미국 혼합)
    # 딕셔너리 형태로 변경
    tickers = {
        '005930': '삼성전자',
        '000660': 'SK하이닉스',
        'AAPL': 'Apple',
        'TSLA': 'Tesla',
        'NVDA': 'NVIDIA'
    }
    
    print(f"=== 주식 추천 엔진 테스트 (대상: {list(tickers.keys())}) ===")
    
    # 추천 로직 실행
    df_result = recommender.recommend(tickers)
    
    if not df_result.empty:
        print("\n[추천 결과 TOP 3]")
        print(df_result.head(3))
        
        print("\n[전체 분석 결과]")
        # 출력 컬럼에 Name 추가
        print(df_result[['Name', 'Ticker', 'Close', 'Change', 'Score', 'Reason']])
    else:
        print("추천 결과가 없습니다. 데이터 로드 실패 또는 데이터 부족.")

if __name__ == "__main__":
    test_recommender()
