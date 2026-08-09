
import streamlit as st

# =========================================================
# 基本設定
# =========================================================
st.set_page_config(
    page_title="Tokyo Trip 2026",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =========================================================
# 手機版 / 網站外觀 CSS
# =========================================================
st.markdown("""
<style>

/* 整體背景 */
.stApp {
    background-color: #F8F7F3;
}

/* 主內容最大寬度，適合手機直式閱讀 */
.block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* 標題 */
h1 {
    font-size: 2rem !important;
    font-weight: 800 !important;
}

/* 次標題 */
h2 {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
}

/* 卡片 */
.travel-card {
    background-color: white;
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 14px;
    border: 1px solid #E8E8E8;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
}

/* 行程時間 */
.travel-time {
    font-size: 14px;
    color: #888888;
    font-weight: 600;
}

/* 行程名稱 */
.travel-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 5px;
}

/* 行程說明 */
.travel-description {
    font-size: 15px;
    color: #555555;
    margin-top: 4px;
}

/* 手機 */
@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }

    h1 {
        font-size: 1.7rem !important;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 側邊欄
# =========================================================
with st.sidebar:

    st.title("🇯🇵 Tokyo Trip")

    st.caption("2026.08.10 - 2026.08.14")

    st.divider()

    page = st.radio(
        "旅遊選單",
        [
            "✈️ 航班資訊",
            "🏨 飯店位置",
            "💱 台幣 / 日幣匯率換算",
            "🗺️ 主要旅程"
        ]
    )

    st.divider()

    st.caption("Tokyo Travel 2026")


# =========================================================
# 航班資訊
# =========================================================
if page == "✈️ 航班資訊":

    st.title("✈️ 航班資訊")

    st.caption("Flight Information")

    st.markdown("---")

    # ---------- 去程 ----------
    st.subheader("🇹🇼 → 🇯🇵 去程")

    st.markdown("""
    <div class="travel-card">

        <div class="travel-time">
        2026 / 08 / 10
        </div>

        <div class="travel-title">
        桃園國際機場 → 東京成田機場
        </div>

        <div class="travel-description">
        🛬 抵達成田機場：06:30
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ---------- 回程 ----------
    st.subheader("🇯🇵 → 🇹🇼 回程")

    st.markdown("""
    <div class="travel-card">

        <div class="travel-time">
        2026 / 08 / 14
        </div>

        <div class="travel-title">
        東京 → 桃園國際機場
        </div>

        <div class="travel-description">
        航班資訊可之後加入
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 飯店資訊
# =========================================================
elif page == "🏨 飯店位置":

    st.title("🏨 飯店位置")

    st.caption("Hotel Information")

    st.markdown("---")

    # ---------- Hotel 1 ----------
    st.subheader("8/10 ～ 8/12")

    st.markdown("""
    <div class="travel-card">

        <div class="travel-title">
        🏨 the b 淺草
        </div>

        <div class="travel-description">
        📍 日本〒111-0035<br>
        Tokyo, Taito City,<br>
        Nishiasakusa, 3 Chome−16−12
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📍 Google Maps",
        "https://www.google.com/maps/search/?api=1&query=the+b+asakusa+tokyo",
        use_container_width=True
    )

    st.markdown("---")

    # ---------- Hotel 2 ----------
    st.subheader("8/12 ～ 8/14")

    st.markdown("""
    <div class="travel-card">

        <div class="travel-title">
        🏨 Hotel Amanek Asakusa Ekimae
        </div>

        <div class="travel-description">
        📍 2 Chome-7-2 Komagata<br>
        Taito City, Tokyo 111-0043<br>
        日本
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📍 Google Maps",
        "https://www.google.com/maps/search/?api=1&query=Hotel+Amanek+Asakusa+Ekimae",
        use_container_width=True
    )


# =========================================================
# 匯率換算
# =========================================================
elif page == "💱 台幣 / 日幣匯率換算":

    st.title("💱 台幣 / 日幣")

    st.caption("Currency Converter")

    st.markdown("---")

    st.info(
        "目前先使用手動設定匯率，之後可以再改成自動抓取即時匯率。"
    )

    # 使用者自己修改匯率
    exchange_rate = st.number_input(
        "目前匯率｜1 日圓 = ? 台幣",
        min_value=0.01,
        max_value=1.00,
        value=0.21,
        step=0.001,
        format="%.3f"
    )

    st.markdown("---")

    mode = st.radio(
        "換算方向",
        [
            "🇯🇵 日幣 → 🇹🇼 台幣",
            "🇹🇼 台幣 → 🇯🇵 日幣"
        ]
    )

    # ---------- 日幣 → 台幣 ----------
    if mode == "🇯🇵 日幣 → 🇹🇼 台幣":

        yen = st.number_input(
            "輸入日幣 ¥",
            min_value=0,
            value=1000,
            step=100
        )

        twd = yen * exchange_rate

        st.metric(
            "約為台幣",
            f"NT$ {twd:,.0f}"
        )

    # ---------- 台幣 → 日幣 ----------
    else:

        twd = st.number_input(
            "輸入台幣 NT$",
            min_value=0,
            value=1000,
            step=100
        )

        if exchange_rate > 0:

            yen = twd / exchange_rate

            st.metric(
                "約為日幣",
                f"¥ {yen:,.0f}"
            )


# =========================================================
# 主要旅程
# =========================================================
elif page == "🗺️ 主要旅程":

    st.title("🗺️ 主要旅程")

    st.caption("Tokyo Itinerary")

    st.markdown("---")

    # -----------------------------------------------------
    # Day 下拉式選單
    # -----------------------------------------------------
    selected_day = st.selectbox(
        "選擇旅遊日期",
        [
            "Day 1｜8/10",
            "Day 2｜8/11",
            "Day 3｜8/12",
            "Day 4｜8/13",
            "Day 5｜8/14"
        ]
    )

    st.markdown("---")


    # =====================================================
    # DAY 1
    # =====================================================
    if selected_day == "Day 1｜8/10":

        st.subheader("Day 1｜8月10日")

        st.caption("抵達東京・淺草")

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            06:30
            </div>

            <div class="travel-title">
            ✈️ 抵達成田國際機場
            </div>

            <div class="travel-description">
            入境、領取行李
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            上午
            </div>

            <div class="travel-title">
            🚆 前往淺草
            </div>

            <div class="travel-description">
            成田機場 → 淺草
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            上午
            </div>

            <div class="travel-title">
            🏨 the b 淺草
            </div>

            <div class="travel-description">
            飯店寄放行李
            </div>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # DAY 2
    # =====================================================
    elif selected_day == "Day 2｜8/11":

        st.subheader("Day 2｜8月11日")

        st.caption("Tokyo Day 2")

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            Morning
            </div>

            <div class="travel-title">
            ☀️ Day 2 行程
            </div>

            <div class="travel-description">
            行程內容之後可以加入
            </div>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # DAY 3
    # =====================================================
    elif selected_day == "Day 3｜8/12":

        st.subheader("Day 3｜8月12日")

        st.caption("換飯店日")

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            上午
            </div>

            <div class="travel-title">
            🧳 Check-out
            </div>

            <div class="travel-description">
            the b 淺草
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            下午
            </div>

            <div class="travel-title">
            🏨 Hotel Amanek Asakusa Ekimae
            </div>

            <div class="travel-description">
            第二間飯店入住
            </div>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # DAY 4
    # =====================================================
    elif selected_day == "Day 4｜8/13":

        st.subheader("Day 4｜8月13日")

        st.caption("Tokyo Day 4")

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            All Day
            </div>

            <div class="travel-title">
            🗼 東京行程
            </div>

            <div class="travel-description">
            行程內容之後可以加入
            </div>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # DAY 5
    # =====================================================
    elif selected_day == "Day 5｜8/14":

        st.subheader("Day 5｜8月14日")

        st.caption("Tokyo → Taiwan")

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            Morning
            </div>

            <div class="travel-title">
            🧳 Check-out
            </div>

            <div class="travel-description">
            Hotel Amanek Asakusa Ekimae
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="travel-card">

            <div class="travel-time">
            Today
            </div>

            <div class="travel-title">
            ✈️ 返回台灣
            </div>

            <div class="travel-description">
            前往機場
            </div>

        </div>
        """, unsafe_allow_html=True)
