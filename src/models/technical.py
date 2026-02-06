from .base import StockRecommender
from ..data.factory import DataLoaderFactory
import pandas as pd
import ta

class TechnicalAnalysisRecommender(StockRecommender):
    """
    기술적 분석(RSI, 이동평균선)을 기반으로 종목을 추천하는 구현체
    """
    
    def __init__(self):
        self.loader_factory = DataLoaderFactory()

    def recommend(self, ticker_dict: dict) -> pd.DataFrame:
        """
        Args:
            ticker_dict (dict): {ticker: name} 형태의 딕셔너리
        """
        results = []
        
        # 딕셔너리 순회
        for ticker, name in ticker_dict.items():
            loader = self.loader_factory.get_loader(ticker)
            df = loader.get_price_data(ticker)
            
            if df.empty or len(df) < 60:
                continue

            try:
                # RSI 및 이평선 계산
                rsi = ta.momentum.RSIIndicator(df['Close'], window=14).rsi().iloc[-1]
                sma20 = ta.trend.SMAIndicator(df['Close'], window=20).sma_indicator().iloc[-1]
                current_price = df['Close'].iloc[-1]
                
                # 점수 로직
                score = 0
                reason = []
                
                if rsi < 30:
                    score += 50
                    reason.append("RSI 과매도")
                elif rsi > 70:
                    score -= 50
                    reason.append("RSI 과매수")
                else:
                    score += (50 - abs(50 - rsi))
                
                if current_price > sma20:
                    score += 30
                    reason.append("상승 추세")
                
                # 등락률
                if len(df) >= 2:
                    prev_close = df['Close'].iloc[-2]
                    change_rate = ((current_price - prev_close) / prev_close) * 100
                else:
                    change_rate = 0.0

                results.append({
                    'Ticker': ticker,
                    'Name': name,  # 종목명 추가
                    'Close': current_price,
                    'Change': round(change_rate, 2),
                    'RSI': round(rsi, 2),
                    'Score': round(score, 2),
                    'Reason': ", ".join(reason) if reason else "중립"
                })
                
            except Exception as e:
                print(f"Error analyzing {ticker}: {e}")
                continue

        result_df = pd.DataFrame(results)
        if not result_df.empty:
            result_df = result_df.sort_values(by='Score', ascending=False).reset_index(drop=True)
            
        return result_df
