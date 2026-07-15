"""
=========================================================
CyberShield AI
Global Styles
=========================================================
"""

import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* ---------- Hide Streamlit Default UI ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* ---------- Main Container ---------- */

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }

    /* ---------- Hero ---------- */

    .hero{

        background: linear-gradient(
            135deg,
            #0F172A,
            #1E293B
        );

        border-radius:18px;

        padding:35px;

        border:1px solid #334155;

        margin-bottom:25px;

    }

    .hero h1{

        color:white;

        font-size:42px;

        font-weight:700;

    }

    .hero p{

        color:#CBD5E1;

        font-size:18px;

    }

    /* ---------- Cards ---------- */

    .card{

        background:#1E293B;

        padding:20px;

        border-radius:16px;

        border:1px solid #334155;

        box-shadow:0 0 15px rgba(0,0,0,.15);

    }

    /* ---------- Feature Cards ---------- */

    .feature{

        background:#111827;

        border-radius:16px;

        padding:25px;

        border:1px solid #374151;

        min-height:260px;

    }

    .feature h3{

        color:#38BDF8;

    }

    /* ---------- Footer ---------- */

    .footer{

        text-align:center;

        color:#94A3B8;

        margin-top:35px;

        font-size:14px;

    }

    </style>
    """, unsafe_allow_html=True)