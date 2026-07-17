import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Prediction History")

history_path = Path("history/prediction_history.csv")

if not history_path.exists():

    st.info("No prediction history available.")

else:

    df = pd.read_csv(history_path)

    st.success(f"{len(df)} Predictions Found")

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

    st.download_button(
        "⬇ Download History",
        data=df.to_csv(index=False),
        file_name="prediction_history.csv",
        mime="text/csv"
    )

    if st.button("🗑 Clear History"):

        history_path.unlink()

        st.success("History Deleted Successfully")

        st.rerun()