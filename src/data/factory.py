from .kr_loader import KrLoader
from .us_loader import UsLoader

class DataLoaderFactory:
    """
    종목 코드에 따라 적절한 데이터 로더(KR/US)를 반환하는 팩토리 클래스
    """
    
    @staticmethod
    def get_loader(ticker: str):
        """
        티커 형식을 분석하여 로더 인스턴스를 반환합니다.
        
        Args:
            ticker (str): 종목 코드 또는 티커
            
        Returns:
            KrLoader or UsLoader
        """
        # 간단한 로직: 숫자로만 구성되어 있으면 국내 주식으로 간주
        # 예: 삼성전자 '005930' -> KR, 애플 'AAPL' -> US
        if str(ticker).isdigit():
            return KrLoader()
        else:
            return UsLoader()
