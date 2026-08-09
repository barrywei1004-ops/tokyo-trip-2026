import streamlit as st
import requests


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
# 網站 CSS
# =========================================================
st.markdown("""
<style>

/* ================================
   整體背景
================================ */
.stApp {
    background-color: #F8F7F3;
}


/* ================================
   主內容
================================ */
.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1 {
    font-size: 2rem !important;
    font-weight: 800 !important;
}

h2 {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
}


/* ================================
   行程卡片
================================ */
.travel-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 16px;
    border: 1px solid #E8E8E8;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.travel-time {
    font-size: 15px;
    color: #888888;
    font-weight: 600;
    margin-bottom: 5px;
}

.travel-title {
    font-size: 19px;
    font-weight: 700;
    margin-top: 4px;
    color: #242424;
}

.travel-description {
    font-size: 16px;
    color: #555555;
    margin-top: 6px;
    line-height: 1.6;
}


/* ================================
   Sidebar 側邊欄
================================ */

/* 側邊欄標題 */
[data-testid="stSidebar"] h1 {
    font-size: 32px !important;
    font-weight: 800 !important;
}

/* 側邊欄一般文字 */
[data-testid="stSidebar"] p {
    font-size: 17px;
}

/* 選單標題 */
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    font-size: 18px !important;
    font-weight: 700 !important;
}

/* Radio 選項 */
[data-testid="stSidebar"] div[role="radiogroup"] label p {
    font-size: 19px !important;
    font-weight: 600 !important;
}

/* Radio 選項間距 */
[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding-top: 6px !important;
    padding-bottom: 6px !important;
}

/* Caption */
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    font-size: 16px !important;
}


/* ================================
   手機版
================================ */
@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }

    h1 {
        font-size: 1.7rem !important;
    }

    .travel-card {
        padding: 16px;
    }

    .travel-title {
        font-size: 18px;
    }

    .travel-description {
        font-size: 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 共用函式：行程卡片
# =========================================================
def travel_card(time, title, description):

    st.markdown(
        f"""
        <div class="travel-card">
            <div class="travel-time">{time}</div>
            <div class="travel-title">{title}</div>
            <div class="travel-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 匯率 API
# =========================================================
@st.cache_data(ttl=3600)
def get_exchange_rate():

    url = "https://api.frankfurter.dev/v2/rates"

    try:

        response = requests.get(
            url,
            params={
                "base": "TWD",
                "quotes": "JPY"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if isinstance(data, list) and len(data) > 0:

            rate = float(data[0]["rate"])
            rate_date = data[0]["date"]

            return rate, rate_date

    except requests.RequestException:
        pass

    return None, None


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
            "🗺️ 主要旅程",
            "✈️ 航班資訊",
            "🏨 飯店位置",
            "💱 台幣 / 日幣匯率換算"
        ]
    )

    st.divider()

    st.caption("Tokyo Travel 2026")


# =========================================================
# 主要旅程
# =========================================================
if page == "🗺️ 主要旅程":

    st.title("🗺️ 主要旅程")

    st.caption("Tokyo Itinerary")

    st.divider()

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

    st.divider()


    # =====================================================
    # DAY 1
    # =====================================================
    if selected_day == "Day 1｜8/10":

        st.subheader("Day 1｜8月10日")

        st.caption("抵達東京・淺草")

        travel_card(
            "06:30",
            "✈️ 抵達成田國際機場",
            "入境、領取行李"
        )

        travel_card(
            "上午",
            "🚆 前往淺草",
            "成田機場 → 淺草"
        )

        travel_card(
            "上午",
            "🏨 the b 淺草",
            "飯店寄放行李"
        )


    # =====================================================
    # DAY 2
    # =====================================================
    elif selected_day == "Day 2｜8/11":

        st.subheader("Day 2｜8月11日")

        st.caption("Tokyo Day 2")

        travel_card(
            "Morning",
            "☀️ Day 2 行程",
            "行程內容之後可以加入"
        )


    # =====================================================
    # DAY 3
    # =====================================================
    elif selected_day == "Day 3｜8/12":

        st.subheader("Day 3｜8月12日")

        st.caption("換飯店日")

        travel_card(
            "上午",
            "🧳 Check-out",
            "the b 淺草"
        )

        travel_card(
            "下午",
            "🏨 Hotel Amanek Asakusa Ekimae",
            "第二間飯店入住"
        )


    # =====================================================
    # DAY 4
    # =====================================================
    elif selected_day == "Day 4｜8/13":

        st.subheader("Day 4｜8月13日")

        st.caption("Tokyo Day 4")

        travel_card(
            "All Day",
            "🗼 東京行程",
            "行程內容之後可以加入"
        )


    # =====================================================
    # DAY 5
    # =====================================================
    elif selected_day == "Day 5｜8/14":

        st.subheader("Day 5｜8月14日")

        st.caption("Tokyo → Taiwan")

        travel_card(
            "Morning",
            "🧳 Check-out",
            "Hotel Amanek Asakusa Ekimae"
        )

        travel_card(
            "Today",
            "✈️ 返回台灣",
            "前往機場"
        )


# =========================================================
# 航班資訊
# =========================================================
elif page == "✈️ 航班資訊":

    st.title("✈️ 航班資訊")

    st.caption("Flight Information")

    st.divider()

    st.subheader("🇹🇼 → 🇯🇵 去程")

    travel_card(
        "2026 / 08 / 10",
        "桃園國際機場 → 東京成田機場",
        "🛬 抵達成田機場：06:30"
    )

    st.subheader("🇯🇵 → 🇹🇼 回程")

    travel_card(
        "2026 / 08 / 14",
        "東京 → 桃園國際機場",
        "航班資訊可之後加入"
    )


# =========================================================
# 飯店位置
# =========================================================
elif page == "🏨 飯店位置":

    st.title("🏨 飯店位置")

    st.caption("Hotel Information")

    st.divider()

    # -----------------------------------------------------
    # Hotel 1
    # -----------------------------------------------------
    st.subheader("8/10 ～ 8/12")

    travel_card(
        "Hotel 01",
        "🏨 the b 淺草",
        """
        📍 日本〒111-0035<br>
        Tokyo, Taito City,<br>
        Nishiasakusa, 3 Chome−16−12
        """
    )

    st.link_button(
        "📍 開啟 Google Maps",
        "https://www.google.com/maps/search/?api=1&query=the+b+asakusa+tokyo",
        use_container_width=True
    )

    st.divider()

    # -----------------------------------------------------
    # Hotel 2
    # -----------------------------------------------------
    st.subheader("8/12 ～ 8/14")

    travel_card(
        "Hotel 02",
        "🏨 Hotel Amanek Asakusa Ekimae",
        """
        📍 2 Chome-7-2 Komagata<br>
        Taito City, Tokyo 111-0043<br>
        日本
        """
    )

    st.link_button(
        "📍 開啟 Google Maps",
        "https://www.google.com/maps/search/?api=1&query=Hotel+Amanek+Asakusa+Ekimae",
        use_container_width=True
    )


# =========================================================
# 台幣 / 日幣即時匯率換算
# =========================================================
elif page == "💱 台幣 / 日幣匯率換算":

    st.title("💱 台幣 / 日幣匯率換算")

    st.caption("TWD ↔ JPY Currency Converter")

    st.divider()

    rate, rate_date = get_exchange_rate()


    # -----------------------------------------------------
    # 成功取得匯率
    # -----------------------------------------------------
    if rate is not None:

        jpy_to_twd = 1 / rate

        st.success("✅ 已取得最新可用匯率")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "NT$1 可換",
                f"¥{rate:.3f}"
            )

        with col2:

            st.metric(
                "¥1 約為",
                f"NT${jpy_to_twd:.3f}"
            )

        st.caption(
            f"匯率資料日期：{rate_date}"
        )

        st.caption(
            "※ 此為參考匯率，實際刷卡、換匯與現鈔價格可能因銀行及手續費而不同。"
        )

        st.divider()


        # -------------------------------------------------
        # 換算方向
        # -------------------------------------------------
        mode = st.radio(
            "換算方向",
            [
                "🇯🇵 日幣 → 🇹🇼 台幣",
                "🇹🇼 台幣 → 🇯🇵 日幣"
            ],
            horizontal=True
        )


        # -------------------------------------------------
        # JPY → TWD
        # -------------------------------------------------
        if mode == "🇯🇵 日幣 → 🇹🇼 台幣":

            yen = st.number_input(
                "輸入日幣 ¥",
                min_value=0,
                value=1000,
                step=100
            )

            twd = yen * jpy_to_twd

            st.metric(
                "約為台幣",
                f"NT$ {twd:,.0f}"
            )

            st.markdown("#### 快速換算")

            quick_values = [
                100,
                500,
                1000,
                5000,
                10000
            ]

            for value in quick_values:

                converted = value * jpy_to_twd

                st.write(
                    f"¥{value:,} ≈ NT${converted:,.0f}"
                )


        # -------------------------------------------------
        # TWD → JPY
        # -------------------------------------------------
        else:

            twd = st.number_input(
                "輸入台幣 NT$",
                min_value=0,
                value=1000,
                step=100
            )

            yen = twd * rate

            st.metric(
                "約為日幣",
                f"¥ {yen:,.0f}"
            )

            st.markdown("#### 快速換算")

            quick_values = [
                100,
                500,
                1000,
                3000,
                5000
            ]

            for value in quick_values:

                converted = value * rate

                st.write(
                    f"NT${value:,} ≈ ¥{converted:,.0f}"
                )


        # -------------------------------------------------
        # 更新匯率
        # -------------------------------------------------
        st.divider()

        if st.button(
            "🔄 更新最新匯率",
            use_container_width=True
        ):

            st.cache_data.clear()
            st.rerun()


    # -----------------------------------------------------
    # API 無法取得
    # -----------------------------------------------------
    else:

        st.error(
            "目前無法取得最新匯率資料，請稍後再試。"
        )

        if st.button(
            "🔄 重新取得匯率",
            use_container_width=True
        ):

            st.cache_data.clear()
            st.rerun()
