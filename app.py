import streamlit as st

print("page reloaded")
st.set_page_config(
    page_title = "포켓몬 도감",
    page_icon = "./images/monsterball.png"
)
st.markdown("""
<style>
img {
    max-height: 300px;
}
.st-emotion-cache-o1htok div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.st-emotion-cache-1h9usn1 {
    pointer-events: none;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "ㄴ",
    "격투": "ㄱ",
    "비행": "ㅂ",
    "독": "ㄷ",
    "땅": "ㄸ",
    "바위": "ㅂ",
    "벌레": "ㅂ",
    "고스트": "ㄱ",
    "강철": "ㄱ",
    "불꽃": "ㅂ",
    "물": "ㅁ",
    "풀": "ㅍ",
    "전기": "ㅈ",
    "에스퍼": "ㅇ",
    "얼음": "ㅇ",
    "드래곤": "ㄷ",
    "악": "ㅇ",
    "페어리": "ㅍ"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://i.namu.wiki/i/JCiJogyqv-k6Y2jouisseFOoqo1MivXqCnQei4lVgf7LGor5_fcXvl0UDiK182kgfYpt_3WylNtxNz65ZwBqlkjJ1iFtZlmkhYlEQI4l86Yhh5brwDjkqWhAtFBv1gUdpIt29tX_4fQy_6O8kgw2sQ.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://i.namu.wiki/i/JlAbY1VFiicne3bIox15_TrVYtdU0K7x5SL4GsdsI-D6ByonfV09BnCl7uplz8lsblKZKDIDfSEjjva4I-YbZMIUOWe2hpE7CivIhBaQRz1bSDFAsuHis0EDM7uD1HbAwRuaQ7Pmjrdl3hYohjEJ5Q.webp"
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://i.namu.wiki/i/r0-xGLLanGCDlssyEwBhuuToELB05c8bOIR5gsRVYQRaXSph2U9O8Ii9pTPH4lxJDpbZxQfAMAEO7OwsQqW_jwMkY7Fu_1gMdVI9jtYth9AajFsas89m7ExYVLRoQhQyQUAoUsliOeV9Z_Kg4u75NA.webp"
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://i.namu.wiki/i/RUAArIt57WrDwSjfjjF6_1sThbFmfgTuxaETOoFxQlPUqyMQBVmtT61SEU88uReeY0qfU4X6IpTuNLwkWZATGyeTnddwNS0iSKwbGMkngqnH1XEy7plbk2MJzGlpVldsoIEyqMEkIKaIaSOEDS4cCg.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://i.namu.wiki/i/Dqyy9Fp7hD48GtVnuXGzy0_axg-1h8LGJkPQONpXEYGnrtGXW10GUCheEM4HHMo9baFC_vgawkw2PN1AbHDixdm0B9MXuzhEtuLvpHcac_WoscqSLCem-UdNtj3Sj2XkjEIo3s4-x7-lTcSpAr_g3Q.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://i.namu.wiki/i/ZwRo-Ev5KBjh4jN5bHQWBtbPQMCdFbslSWvKQgqJe9NLFt74OIYSuj7KMR4gTOEer17uaaDfqm_XCBr8rBRD4E1NLhV9dowckQYm4iwpAOjbq7cL8ziFsw0EfXwFL_UW8Z8eVjWNC5xl4cu5SzBejA.webp"
    }
]

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://i.namu.wiki/i/hdyNihCFmLpgBDtg_Re5IAW8I4m8osT8lt2xzZHwPEJ0lixOCG0fhR6Mzxj9eS4hF3ieSRTomWOAinNaKg7H0cXNQLBaJi1iNxoqRdQ3SP4WfepLx1nhdDYtU1C6QgkU-95IBOQkbxY71X6tSdhFBA.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="포켓몬 이름",
            value=example_pokemon["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="포켓몬 이미지 URL",
        value=example_pokemon["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i + 3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i + j + 1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i + j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i + j]
                    st.rerun()
