import streamlit as st
import datetime
import random

# 1. 운동 데이터 정의
exercises = {
    "맨몸 운동": {
        "초급": [
            {"name": "푸쉬업", "description": "기본 푸쉬업으로 상체 근력 강화"},
            {"name": "스쿼트", "description": "하체 근력을 기르는 기본 맨몸 운동"},
            {"name": "크런치", "description": "복부 코어 강화에 효과적"},
            {"name": "워킹 런지", "description": "하체와 균형 감각 향상"},
            {"name": "점핑잭", "description": "전신 유산소 워밍업 운동"},
        ],
        "중급": [
            {"name": "플랭크", "description": "코어 단련에 좋은 정적 운동"},
            {"name": "마운틴 클라이머", "description": "복부 + 유산소"},
            {"name": "버피 테스트", "description": "고강도 전신 운동"},
            {"name": "점프 스쿼트", "description": "하체 근력과 점프력 향상"},
            {"name": "파이크 푸쉬업", "description": "어깨를 집중적으로 자극"},
        ],
        "고급": [
            {"name": "핸드스탠드 푸쉬업", "description": "고급 어깨/상체 맨몸 운동"},
            {"name": "플로우 버피", "description": "연속적인 전신 고강도 루틴"},
            {"name": "플랭크 투 푸쉬업", "description": "코어 + 팔 근육 집중"},
            {"name": "점프 런지", "description": "하체의 폭발력 강화"},
            {"name": "스파이더 플랭크", "description": "코어와 하체를 동시에 자극"},
        ]
    },
    "헬스장 운동": {
        "초급": [
            {"name": "레그 프레스", "description": "초보자용 하체 기구 운동"},
            {"name": "랫풀다운", "description": "등 근육 강화에 좋음"},
            {"name": "체스트 프레스", "description": "기본 가슴 운동"},
            {"name": "바이셉 컬 (머신)", "description": "팔뚝 근육 발달"},
            {"name": "시티드 레그 컬", "description": "허벅지 뒤쪽 강화"},
        ],
        "중급": [
            {"name": "벤치프레스", "description": "상체 전면 근육 강화"},
            {"name": "스쿼트 (바벨)", "description": "하체 복합 운동"},
            {"name": "시티드 로우", "description": "등/팔 동시 자극"},
            {"name": "숄더 프레스", "description": "어깨 근육 발달"},
            {"name": "사이클 머신", "description": "하체 유산소 운동"},
        ],
        "고급": [
            {"name": "데드리프트", "description": "전신 복합 고강도 운동"},
            {"name": "클린 앤 저크", "description": "올림픽 리프팅 복합 운동"},
            {"name": "바벨 스쿼트", "description": "하체 근육 집중 훈련"},
            {"name": "덤벨 스내치", "description": "전신 폭발력과 밸런스"},
            {"name": "케이블 크로스오버", "description": "가슴 모양 교정 및 강화"},
        ]
    }
}

# 2. UI 구성
st.title("🏋️‍♀️ 오늘의 운동 루틴 추천")

# 사용자 선택
place = st.radio("운동 장소를 선택하세요:", ("맨몸 운동", "헬스장 운동"))
level = st.radio("운동 난이도를 선택하세요:", ("초급", "중급", "고급"))

# 3. 오늘 날짜 기반 시드 설정
today = datetime.date.today()
random.seed(today.toordinal())  # 매일 동일한 루틴 추천

# 4. 운동 루틴 추천
selected_list = exercises[place][level]
routine = random.sample(selected_list, k=min(5, len(selected_list)))  # 최대 5개 추천

# 5. 루틴 출력
st.write(f"📅 오늘 날짜: {today.strftime('%Y-%m-%d')}")
st.subheader(f"🏃 오늘의 운동 루틴 ({place}, {level})")

for i, ex in enumerate(routine, 1):
    st.markdown(f"**{i}. {ex['name']}**  \n{ex['description']}")
