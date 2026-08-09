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

.stApp {
    background-color: #F8F7F3;
}

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
   航班卡片
================================ */
.flight-card {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid #E8E8E8;
    box-shadow: 0 3px 10px rgba(0,0,0,0.04);
}

.flight-tag {
    font-size: 14px;
    font-weight: 700;
    color: #777777;
    margin-bottom: 8px;
}

.flight-airline {
    font-size: 22px;
    font-weight: 800;
    color: #222222;
    margin-bottom: 2px;
}

.flight-airline-en {
    font-size: 14px;
    color: #888888;
    margin-bottom: 20px;
}

.flight-route {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-top: 12px;
    margin-bottom: 18px;
}

.flight-location {
    width: 38%;
}

.flight-location.right {
    text-align: right;
}

.flight-time {
    font-size: 25px;
    font-weight: 800;
    color: #222222;
}

.flight-code {
    font-size: 20px;
    font-weight: 700;
    margin-top: 3px;
}

.flight-airport {
    font-size: 14px;
    color: #666666;
    margin-top: 3px;
}

.flight-terminal {
    font-size: 13px;
    color: #999999;
    margin-top: 2px;
}

.flight-middle {
    width: 24%;
    text-align: center;
}

.flight-plane {
    font-size: 24px;
}

.flight-duration {
    font-size: 13px;
    color: #888888;
    margin-top: 4px;
}

.flight-line {
    border-top: 1px solid #DDDDDD;
    margin-top: 6px;
    margin-bottom: 6px;
}

.flight-info {
    font-size: 15px;
    color: #444444;
    line-height: 1.9;
}

.passenger-box {
    background-color: #F7F7F7;
    padding: 14px;
    border-radius: 12px;
    margin-top: 15px;
    font-size: 15px;
}


/* ================================
   Sidebar
================================ */
[data-testid="stSidebar"] h1 {
    font-size: 32px !important;
    font-weight: 800 !important;
}

[data-testid="stSidebar"] p {
    font-size: 17px;
}

[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    font-size: 18px !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label p {
    font-size: 19px !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding-top: 6px !important;
    padding-bottom: 6px !important;
}

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

    .flight-card {
        padding: 16px;
    }

    .flight-time {
        font-size: 22px;
    }

    .flight-code {
        font-size: 18px;
    }

    .flight-airport {
        font-size: 12px;
    }

    .flight-route {
        gap: 6px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 共用函式：行程卡片
# =========================================================
def travel_card(time, title, description):

    html = f"""
<div class="travel-card">
<div class="travel-time">{time}</div>
<div class="travel-title">{title}</div>
<div class="travel-description">{description}</div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# =========================================================
# 共用函式：航班卡片
# 修正：HTML 不再被 Streamlit 當成程式碼顯示
# =========================================================
def flight_card(
    trip_type,
    date,
    airline,
    airline_en,
    flight_no,
    depart_time,
    depart_code,
    depart_airport,
    depart_terminal,
    arrive_time,
    arrive_code,
    arrive_airport,
    arrive_terminal,
    duration,
    cabin,
    aircraft,
    passengers
):

    html = f"""
<div class="flight-card">
<div class="flight-tag">{trip_type} ｜ {date}</div>

<div class="flight-airline">{flight_no} ｜ {airline}</div>
<div class="flight-airline-en">{airline_en}</div>

<div class="flight-route">

<div class="flight-location">
<div class="flight-time">{depart_time}</div>
<div class="flight-code">{depart_code}</div>
<div class="flight-airport">{depart_airport}</div>
<div class="flight-terminal">{depart_terminal}</div>
</div>

<div class="flight-middle">
<div class="flight-plane">✈️</div>
<div class="flight-line"></div>
<div class="flight-duration">{duration}</div>
</div>

<div class="flight-location right">
<div class="flight-time">{arrive_time}</div>
<div class="flight-code">{arrive_code}</div>
<div class="flight-airport">{arrive_airport}</div>
<div class="flight-terminal">{arrive_terminal}</div>
</div>

</div>

<hr>

<div class="flight-info">
✈️ <b>航班編號：</b>{flight_no}<br>
🏢 <b>航空公司：</b>{airline} {airline_en}<br>
💺 <b>艙等：</b>{cabin}<br>
🛫 <b>機型：</b>{aircraft}<br>
⏱️ <b>飛行時間：</b>{duration}
</div>

<div class="passenger-box">
👥 <b>同班旅客</b><br>
{passengers}
</div>

</div>
"""

    st.markdown(
        html,
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


    # DAY 1
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


    # DAY 2
    elif selected_day == "Day 2｜8/11":

        st.subheader("Day 2｜8月11日")

        st.caption("Tokyo Day 2")

        travel_card(
            "Morning",
            "☀️ Day 2 行程",
            "行程內容之後可以加入"
        )


    # DAY 3
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


    # DAY 4
    elif selected_day == "Day 4｜8/13":

        st.subheader("Day 4｜8月13日")

        st.caption("Tokyo Day 4")

        travel_card(
            "All Day",
            "🗼 東京行程",
            "行程內容之後可以加入"
        )


    # DAY 5
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


    # 旅客選擇
    passenger = st.selectbox(
        "查看旅客",
        [
            "👥 全部旅客",
            "伯燁",
            "伯丞",
            "佳芳"
        ]
    )

    if passenger == "👥 全部旅客":
        passenger_text = "伯燁・伯丞・佳芳"
    else:
        passenger_text = passenger

    st.caption(
        f"目前顯示：{passenger_text}"
    )

    st.divider()


    # =====================================================
    # 去程
    # =====================================================
    st.subheader("🇹🇼 → 🇯🇵 去程")

    flight_card(
        trip_type="去程",
        date="2026 年 8 月 10 日",
        airline="樂桃航空",
        airline_en="Peach Aviation",
        flight_no="MM620",
        depart_time="02:00",
        depart_code="TPE",
        depart_airport="臺灣桃園國際機場",
        depart_terminal="Terminal 1",
        arrive_time="06:30",
        arrive_code="NRT",
        arrive_airport="成田國際機場",
        arrive_terminal="Terminal 1",
        duration="3 小時 30 分",
        cabin="經濟艙",
        aircraft="Airbus A320",
        passengers=passenger_text
    )


    # =====================================================
    # 回程
    # =====================================================
    st.subheader("🇯🇵 → 🇹🇼 回程")

    flight_card(
        trip_type="回程",
        date="2026 年 8 月 14 日",
        airline="泰國獅航",
        airline_en="Thai Lion Air",
        flight_no="SL395",
        depart_time="17:40",
        depart_code="NRT",
        depart_airport="成田國際機場",
        depart_terminal="Terminal 1N",
        arrive_time="20:20",
        arrive_code="TPE",
        arrive_airport="臺灣桃園國際機場",
        arrive_terminal="Terminal 1",
        duration="3 小時 40 分",
        cabin="經濟艙",
        aircraft="Boeing 737-900",
        passengers=passenger_text
    )


    # =====================================================
    # 航班摘要
    # =====================================================
    st.divider()

    st.subheader("📋 航班摘要")

    travel_card(
        "8 / 10",
        "MM620｜樂桃航空",
        "02:00 桃園 T1 → 06:30 成田 T1<br>Airbus A320｜經濟艙｜3 小時 30 分"
    )

    travel_card(
        "8 / 14",
        "SL395｜泰國獅航",
        "17:40 成田 T1N → 20:20 桃園 T1<br>Boeing 737-900｜經濟艙｜3 小時 40 分"
    )

    st.info(
        "⏰ 所有航班時間皆為當地時間。"
    )


# =========================================================
# 飯店位置
# =========================================================
elif page == "🏨 飯店位置":

    st.title("🏨 飯店位置")

    st.caption("Hotel Information")

    st.divider()


    # Hotel 1
    st.subheader("8/10 ～ 8/12")

    travel_card(
        "Hotel 01",
        "🏨 the b 淺草",
        "📍 日本〒111-0035<br>Tokyo, Taito City,<br>Nishiasakusa, 3 Chome−16−12"
    )

    st.link_button(
        "📍 開啟 Google Maps",
        "https://www.google.com/maps/search/?api=1&query=the+b+asakusa+tokyo",
        use_container_width=True
    )

    st.divider()


    # Hotel 2
    st.subheader("8/12 ～ 8/14")

    travel_card(
        "Hotel 02",
        "🏨 Hotel Amanek Asakusa Ekimae",
        "📍 2 Chome-7-2 Komagata<br>Taito City, Tokyo 111-0043<br>日本"
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


        mode = st.radio(
            "換算方向",
            [
                "🇯🇵 日幣 → 🇹🇼 台幣",
                "🇹🇼 台幣 → 🇯🇵 日幣"
            ],
            horizontal=True
        )


        # JPY → TWD
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


        # TWD → JPY
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


        st.divider()

        if st.button(
            "🔄 更新最新匯率",
            use_container_width=True
        ):

            st.cache_data.clear()
            st.rerun()


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
