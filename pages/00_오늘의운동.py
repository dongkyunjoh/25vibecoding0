import streamlit as st
import datetime

# 1. 운동 데이터 정의 (장소 + 난이도별)
exercises = {
    "맨몸 운동": {
        "초급": [
            {"name": "푸쉬업", "description": "상체 근력 강화에 좋은 기본 푸쉬업입니다."},
            {"name": "스쿼트", "description": "초보자에게 적합한 맨몸 하체 운동입니다."},
        ],
        "중급": [
            {"name": "플랭크", "description": "코어 근육을 강화하는 정적 운동입니다."},
            {"name": "마운틴 클라이머", "description": "복부와 하체에 동시에 자극을 주는 운동입니다."},
        ],
        "고급": [
            {"name": "버피 테스트", "description": "전신 유산소 및 근력 복합 운동입니다."},
            {"name": "점프 스쿼트", "description": "하체 폭발력과 근지구력을 기르는 운동입니다."},
        ],
    },
    "헬스장 운동": {
        "초급": [
            {"name": "레그 프레스", "description": "기초 하체 근력 운동입니다."},
            {"name": "랫풀다운", "description": "기본적인 등 근육 운동입니다."},
        ],
        "중급": [
            {"name": "벤치프레스", "description": "가슴과 팔 근육을 단련하는 기초 운동입니다."},
            {"name": "시티드 로우", "description": "등과 팔에 자극을 주는 기구 운동입니다."},
        ],
        "고급": [
            {"name": "스쿼트 (바벨)", "description": "복합 근육을 사용하는 고강도 하체 운동입니다."},
            {"name": "데드리프트", "description": "전신 근육 강화에 효과적인 고급 운동입니다."},
        ],
    }
}

# 2. UI 구성
st.title("🏋️ 오늘의 맞춤 운동 추천")

# 사용자 선택
place = st.radio("운동 장소를 선택하세요:", ("맨몸 운동", "헬스장 운동"))
level = st.radio("운동 난이도를 선택하세요:", ("초급", "중급", "고급"))

# 3. 오늘 날짜로 인덱스 계산
today = datetime.date.today()
exercise_list = exercises[place][level]
index = today.toordinal() % len(exercise_list)
selected_exercise = exercise_list[index]

# 4. 추천 운동 출력
st.write(f"📅 날짜: {today.strftime('%Y-%m-%d')}")
st.subheader(f"✅ 오늘의 운동 ({place}, {level})")
st.markdown(f"**{selected_exercise['name']}**")
st.write(selected_exercise["description"])
