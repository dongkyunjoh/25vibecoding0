import streamlit as st
import datetime
import random

# 1. 운동 리스트
exercises = [
    {"name": "푸쉬업", "description": "상체 근력을 강화하는 기본적인 운동입니다."},
    {"name": "스쿼트", "description": "하체 근력 향상에 효과적인 운동입니다."},
    {"name": "플랭크", "description": "코어 근육을 단련하는 정적인 운동입니다."},
    {"name": "버피 테스트", "description": "전신 근육과 유산소 운동에 효과적입니다."},
    {"name": "런지", "description": "하체와 균형 감각을 함께 향상시켜줍니다."},
    {"name": "점핑잭", "description": "몸을 풀어주는 유산소 워밍업 운동입니다."},
]

# 2. 오늘 날짜 가져오기
today = datetime.date.today()
day_index = today.toordinal() % len(exercises)  # 날짜를 기반으로 인덱스를 생성

# 3. 오늘의 운동 선택
today_exercise = exercises[day_index]

# 4. Streamlit UI
st.title("🏋️ 오늘의 운동 추천")
st.write(f"📅 날짜: {today.strftime('%Y-%m-%d')}")

st.subheader(f"✅ 오늘의 운동: {today_exercise['name']}")
st.write(today_exercise['description'])

# 추가로 이미지나 유튜브 영상 등도 가능
# st.image("image_url")
# st.video("youtube_url")
