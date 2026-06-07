import streamlit as st
import pandas as pd

st.set_page_config(page_title="專業足球賽事預測站", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")

# 隱賞側邊欄與選單
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("⚽ 專家足球賽事預測分析榜")
st.write("歡迎來到足球預測站，以下為今日最新精選預測（資料與雲端即時同步）。")
st.markdown("---")

# === 🌟 核心修改：從 Google Sheets 讀取資料 🌟 ===
# 請把下方 '你的Google試算表ID' 替換成你剛剛複製的那串英數字
SHEET_ID = "你的Google試算表ID"
GOOGLE_SHEET_URL = f"https://docs.google.com/spreadsheets/d/1mDvl1jjnXpp3UrUNY0hvqThVWzhnw1UGYiYqLJ2a4l4/gviz/tq?tqx=out:csv"

try:
    # 讀取雲端資料
    df = pd.read_csv(GOOGLE_SHEET_URL)
    
    if df.empty:
        st.info("目前暫無精選賽事預測。")
    else:
        # 將最新的比賽排在最上面顯示
        for index, row in df.iloc[::-1].iterrows():
            with st.container():
                st.markdown(
                    f"""
                    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #007bff; margin-bottom: 20px;">
                        <span style="background-color: #6c757d; color: white; padding: 3px 8px; border-radius: 3px; font-size: 12px;">{row['聯賽']}</span>
                        <span style="color: #6c757d; font-size: 14px; margin-left: 10px;">⏰ 比賽時間: {row['比賽時間']}</span>
                        <h3 style="margin-top: 10px; color: #343a40;">{row['主隊']} <span style="color:red;">VS</span> {row['客隊']}</h3>
                        <p style="font-size: 18px; margin-bottom: 5px;">
                            🎯 <b>預測方向：</b> <span style="color: #d9534f; font-weight: bold; font-size: 20px;">{row['預測賽果']}</span>
                        </p>
                        <p style="font-size: 16px; margin-bottom: 5px;">
                            ⭐ <b>信心指數：</b> {row['信心指數']}
                        </p>
                        <div style="background-color: #ffffff; padding: 10px; border-radius: 5px; border: 1px solid #dee2e6; margin-top: 10px; font-size: 14px; color: #495057;">
                            💡 <b>詳細分析：</b> {row['詳細分析']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
except Exception as e:
    st.error("讀取雲端資料失敗，請確認試算表權限是否已開啟。")

st.markdown("---")
st.caption("⚠️ 免責聲明：本網站數據僅供參考，投注具有風險，請理性博彩。")