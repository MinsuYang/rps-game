import streamlit as st
import random

st.title("✂️ 가위바위보 게임")

# 세션 상태 초기화
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "draws" not in st.session_state:
    st.session_state.draws = 0
if "result_msg" not in st.session_state:
    st.session_state.result_msg = ""

choices = {"가위": "✂️", "바위": "✊", "보": "🖐️"}
beats = {"가위": "바위", "바위": "보", "보": "가위"}  # key가 key를 이기는 것

# 점수판
col1, col2, col3 = st.columns(3)
col1.metric("🏆 승", st.session_state.wins)
col2.metric("💀 패", st.session_state.losses)
col3.metric("🤝 무", st.session_state.draws)

st.divider()

st.subheader("선택하세요!")
cols = st.columns(3)

for i, (name, emoji) in enumerate(choices.items()):
    if cols[i].button(f"{emoji} {name}", use_container_width=True):
        computer = random.choice(list(choices.keys()))
        player = name

        if player == computer:
            st.session_state.draws += 1
            result = "🤝 무승부!"
        elif beats[computer] == player:
            st.session_state.losses += 1
            result = "💀 졌습니다!"
        else:
            st.session_state.wins += 1
            result = "🏆 이겼습니다!"

        st.session_state.result_msg = (
            f"나: {choices[player]} {player}  vs  컴퓨터: {choices[computer]} {computer}\n\n**{result}**"
        )

if st.session_state.result_msg:
    st.divider()
    st.markdown(st.session_state.result_msg)

st.divider()
if st.button("🔄 점수 초기화"):
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.session_state.result_msg = ""
    st.rerun()
