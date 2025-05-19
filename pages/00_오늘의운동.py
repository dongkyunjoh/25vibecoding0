import streamlit as st
import datetime

# 1. 운동 리스트 정의
bodyweight_exercises = [
    {"name": "푸쉬업", "description": "상체 근력 강화에 좋은 맨몸 운동입니다."},
    {"name": "스쿼트", "description": "하체 근력을 키우는 대표적인 맨몸 운동입니다."},
    {"name": "플랭크", "description": "코어를 단련하는 정적인 운동입니다."},
    {"name": "점핑잭", "description": "워밍업이나 유산소에 좋은 맨몸 운동입니다."},
    {"name": "마운틴 클라이머", "description": "유산소와 복근 운동에 동시에 효과적입니다."},
]

gym_exercises = [
    {"name": "벤치프레스", "description": "상체 근육을 집중적으로 키울 수 있는 대표적인 기구 운동입니다."},
    {"name": "레그프레스", "description": "하체 근육을 강화하는 헬스장 운동입니다."},
    {"name": "랫풀다운", "description": "등 근육 강화에 효과적인 머신 운동입니다."},
    {"name": "케이블 크로스오버", "description": "가슴 근육을 조정하여 운동할 수 있습니다."},
    {"name": "스미스 머신 스쿼트", "description": "스미스 머신을 이용한 안정적인 하체 운동입니다."},
]

# 2. 오늘 날짜 기반 인덱스 계산
today = datetime.date.today()
# UI 타이틀
st.title("🏋️ 오늘의 운동 추천")

# 3. 장소 선택
workout_type = st.radio("운동 장소를 선택하세요:", ("맨몸 운동", "헬스장 운동"))

# 4. 운동 추천
if workout_type == "맨몸 운동":
    index = today.toordinal() % len(bodyweight_exercises)
    exercise = bodyweight_exercises[index]
else:
    index = today.toordinal() % len(gym_exercises)
    exercise = gym_exercises[index]

# 5. 결과 출력
st.write(f"📅 오늘 날짜: {today.strftime('%Y-%m-%d')}")
st.subheader(f"✅ 추천 운동: {exercise['name']}")
st.write(exercise["description"])
