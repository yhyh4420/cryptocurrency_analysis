# 암호화폐 분석 챗봇

이 프로젝트는 OpenAI API와 Taivily API를 사용하여 구현된 간단한 암호화폐 분석 챗봇입니다. 사용자의 입력에 따라 다양한 암호화폐에 대한 정보를 제공하고 분석합니다.

## 주요 기능

- 다양한 암호화폐에 대한 실시간 분석 제공
- 암호화폐 가격, 동향, 최신 뉴스 등에 대한 자연어 질문 지원
- OpenAI의 GPT 모델을 활용한 정확하고 맥락에 맞는 응답 제공
- Taivily API를 사용하여 실시간 암호화폐 데이터를 가져옴

## 설치 방법

이 프로젝트를 시작하려면 아래의 지침을 따르세요:

### 필수 조건

- Python 3.7 이상
- Poetry (의존성 관리 도구)

### 설정

1. **저장소 클론**:

   먼저, 이 저장소를 로컬 환경에 클론합니다.

   ```bash
   git clone https://github.com/yhyh4420/cryptocurrency_analysis.git
   cd cryptocurrency_analysis

2. **의존성 설치**
   Poetry가 설치되어 있는지 확인한 후, 다음 명령어를 실행하여 필요한 패키지를 설치합니다.
   ```bash
   poetry install

3. **.env파일 생성**
   프로젝트 루트 디렉토리에 .env 파일을 생성하고, OpenAI API 키와 Taivily API 키를 추가합니다:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   TAIVILY_API_KEY=your_taivily_api_key_here

4. **챗봇 실행**
   다음 명령어를 사용하여 챗봇을 실행합니다:
   ```bash
   poetry run app.py
   
## 사용 방법

이 프로젝트는 다음과 같은 API를 사용합니다:
- OpenAI API: 자연어 처리 및 이해를 위한 GPT 모델 사용.
- Taivily API: 실시간 암호화폐 데이터 제공.

API 키는 각 서비스의 웹사이트를 통해 발급받을 수 있습니다.
