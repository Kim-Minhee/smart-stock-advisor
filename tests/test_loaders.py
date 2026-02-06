import sys
import os
import pandas as pd

# src 모듈 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data.factory import DataLoaderFactory

def test_loaders():
    factory = DataLoaderFactory()
    
    print("=== 국내 주식 로더 테스트 (삼성전자: 005930) ===")
    kr_loader = factory.get_loader("005930")
    df_kr = kr_loader.get_price_data("005930")
    if not df_kr.empty:
        print(f"데이터 수신 성공! Shape: {df_kr.shape}")
        print(df_kr.tail(3))
    else:
        print("데이터 수신 실패!")

    print("\n=== 미국 주식 로더 테스트 (애플: AAPL) ===")
    us_loader = factory.get_loader("AAPL")
    df_us = us_loader.get_price_data("AAPL")
    if not df_us.empty:
        print(f"데이터 수신 성공! Shape: {df_us.shape}")
        print(df_us.tail(3))
    else:
        print("데이터 수신 실패!")

if __name__ == "__main__":
    test_loaders()
