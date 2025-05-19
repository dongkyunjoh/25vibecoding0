import streamlit as st
import datetime
import random

# 1. 운동 데이터 (이름 + 이미지 URL)
exercise_data = {
    "맨몸 운동": {
        "초급": [
            {"name": "푸쉬업", "img": "https://cdn.pixabay.com/photo/2020/06/30/05/24/push-up-5355627_1280.jpg"},
            {"name": "스쿼트", "img": "https://cdn.pixabay.com/photo/2021/03/14/17/55/squat-6093690_1280.jpg"},
            {"name": "크런치", "img": "https://cdn.pixabay.com/photo/2016/11/29/09/15/abdominal-1869265_1280.jpg"},
            {"name": "워킹 런지", "img": "https://cdn.pixabay.com/photo/2021/03/04/08/50/lunge-6067877_1280.jpg"},
            {"name": "점핑잭", "img": "https://www.verywellfit.com/thmb/U7_nylnG7ur9qULqBtiKhrQoSiA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Verywell-02-3567157-JumpingJack-5c46917646e0fb0001bd44a5.gif"},
        ],
        "중급": [
            {"name": "플랭크", "img": "https://cdn.pixabay.com/photo/2020/06/30/05/22/plank-5355624_1280.jpg"},
            {"name": "마운틴 클라이머", "img": "https://www.verywellfit.com/thmb/gClZPRnDwJr8MF-DBAjAUP0he2I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Verywell-04-3567157-MountainClimbers-5c46917546e0fb0001bd44a2.gif"},
            {"name": "버피 테스트", "img": "https://media.tenor.com/Dn8vO1dOGTMAAAAC/burpee-home-workout.gif"},
            {"name": "점프 스쿼트", "img": "https://media.tenor.com/ncVuCioO6PcAAAAC/jump-squat.gif"},
            {"name": "파이크 푸쉬업", "img": "https://cdn.pixabay.com/photo/2021/06/14/19/20/yoga-6336814_1280.jpg"},
        ],
    },
    "헬스장 운동": {
        "초급": [
            {"name": "레그 프레스", "img": "https://cdn.pixabay.com/photo/2021/09/12/14/26/gym-6618727_1280.jpg"},
            {"name": "랫풀다운", "img": "https://cdn.pixabay.com/photo/2016/11/21/15/47/bodybuilding-1849086_1280.jpg"},
            {"name": "체스트 프레스", "img": "https://cdn.pixabay.com/photo/2020/09/01/10/01/bench-5534923_1280.jpg"},
            {"name": "바이셉 컬 (머신)", "img": "https://cdn.pixabay.com/photo/2020/10/14/07/31/sports-5652357_1280.jpg"},
            {"name": "시티드 레그 컬", "img": "https://cdn.pixabay.com/photo/2020/06/30/05/21/fitness-5355618_1280.jpg"},
        ]
    }
}

# 2. 세트/횟수 추천
def get_sets_reps(level):
    if level == "초급":
        return f"{random.randint(2, 3)}세트 × {random.choice(['10~12회', '15회', '30초'])}"
    elif level == "중급":
        return f"{random.randint(3, 4)}세트 × {random.choice(['12~15회', '20회', '45초'])}"
    else:
        return f"{random.randint(4, 5)}세트 × {random.choice(['15~20회', '25회', '1분'])}"

# 3. UI 구성
st.title("🏋️ 오늘의 운동 루틴 추천")

place = st.radio("운동 장소를 선택하세요:", list(exercise_data.keys()))
level = st.radio("운동 난이도를 선택하세요:", list(exercise_data[place].keys()))

# 4. 날짜 기반 추천
today = datetime.date.today()
random.seed(today.toordinal())

routines = random.sample(exercise_data[place][level], k=min(5, len(exercise_data[place][level])))

st.write(f"📅 날짜: {today.strftime('%Y-%m-%d')}")
st.subheader(f"📌 오늘의 운동 루틴 ({place}, {level})")

# 5. 운동 출력
for i, ex in enumerate(routines, 1):
    plan = get_sets_reps(level)
    st.markdown(f"### {i}. {ex['name']}")
    st.image(ex["img"], use_column_width=True)
    st.markdown(f"**권장 운동**: {plan}")
    st.markdown("---")
