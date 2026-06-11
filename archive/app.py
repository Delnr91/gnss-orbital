"""Streamlit Web Application for the Keplerian Orbital Dynamics Laboratory.

Provides a clean web interface for the 3D Orbit Simulator and the Space Second Brain,
suitable for free hosting on Streamlit Community Cloud.
"""

import streamlit as st
import numpy as np

from orbital import (
    OrbitalPropagator,
    OrbitPlotter,
    Locale,
    SpaceTeacher,
    create_leo_orbit,
    create_meo_orbit,
    create_geo_orbit,
    create_heo_orbit,
    EARTH_RADIUS,
)

# Page configuration
st.set_page_config(
    page_title="Astrodynamics Laboratory",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Session State for progress
if "completed_actions" not in st.session_state:
    st.session_state.completed_actions = set()

# Sidebar Setup
st.sidebar.title("Mission Control")
lang = st.sidebar.selectbox("Language / Idioma / 语言", ["en", "es", "zh"])
locale = Locale(lang)
teacher = SpaceTeacher()

page = st.sidebar.radio(
    locale.t("ui.orbit_preset"),
    [
        "3D Orbit Simulator",
        "Space Second Brain",
    ]
)

if page == "3D Orbit Simulator":
    st.title(locale.t("ui.title_orbit_simulation"))
    st.write(
        "Interactive orbital mechanics playground. Adjust classical orbital elements "
        "and observe Keplerian trajectories in ECI (Earth-Centered Inertial) frame."
    )

    # Columns layout
    col_ctrl, col_plot = st.columns([1, 2])

    with col_ctrl:
        st.subheader("Orbital Elements")
        
        # Presets
        preset = st.selectbox(
            locale.t("ui.widgets.orbit_preset"),
            ["Custom", "LEO (ISS)", "MEO (GPS)", "GEO (Geostationary)", "HEO (Molniya)"],
        )
        
        # Base values depending on preset
        val_a = 7000.0
        val_e = 0.01
        val_i = 51.6
        val_raan = 0.0
        val_argp = 0.0
        
        if preset == "LEO (ISS)":
            val_a = EARTH_RADIUS + 408.0
            val_e = 0.0006
            val_i = 51.6
        elif preset == "MEO (GPS)":
            val_a = EARTH_RADIUS + 20200.0
            val_e = 0.01
            val_i = 55.0
        elif preset == "GEO (Geostationary)":
            val_a = 42164.0
            val_e = 0.0001
            val_i = 0.01
        elif preset == "HEO (Molniya)":
            val_a = 26560.0
            val_e = 0.74
            val_i = 63.4
            val_argp = 270.0

        a = st.slider(locale.t("ui.widgets.semi_major_axis"), 6500.0, 45000.0, float(val_a), step=100.0)
        e = st.slider(locale.t("ui.widgets.eccentricity"), 0.0, 0.9, float(val_e), step=0.01)
        i = st.slider(locale.t("ui.widgets.inclination"), 0.0, 180.0, float(val_i), step=0.5)
        raan = st.slider(locale.t("ui.widgets.raan"), 0.0, 360.0, float(val_raan), step=1.0)
        argp = st.slider(locale.t("ui.widgets.argument_of_periapsis"), 0.0, 360.0, float(val_argp), step=1.0)

        # Orbit summary calculation
        perigee = a * (1.0 - e)
        if perigee < EARTH_RADIUS:
            st.error(locale.t("errors.subsurface_orbit", perigee=perigee - EARTH_RADIUS, radius=EARTH_RADIUS))
            prop = None
        else:
            prop = OrbitalPropagator(a=a, e=e, i=i, raan=raan, argp=argp, nu0=0.0)

    with col_plot:
        if prop:
            plotter = OrbitPlotter(locale)
            fig = plotter.plot_orbit(prop, color="#00ff88")
            st.plotly_chart(fig, use_container_width=True)

            # Metrics
            period_hrs = prop.period() / 3600.0
            alt_perigee = (a * (1.0 - e)) - EARTH_RADIUS
            alt_apogee = (a * (1.0 + e)) - EARTH_RADIUS
            
            m1, m2, m3 = st.columns(3)
            m1.metric(locale.t("orbit.period"), f"{period_hrs:.2f} hrs")
            m2.metric(locale.t("orbit.perigee_altitude"), f"{alt_perigee:.1f} km")
            m3.metric(locale.t("orbit.apogee_altitude"), f"{alt_apogee:.1f} km")

            # Achievement recording
            if preset != "Custom":
                st.session_state.completed_actions.add(f"simulate_{preset.lower().split()[0]}")

elif page == "Space Second Brain":
    st.title("MIT-Stanford Space Second Brain")
    st.write(
        "Interactive localized knowledge vault covering Keplerian mechanics, GNSS precision, "
        "and 2030 space roadmaps. Uses a deterministic anti-troll filter."
    )

    query = st.text_input("Ask the Space Teacher:", placeholder="e.g. Galileo, IRIS2, Kepler, J2...")
    
    col_btn, col_fallback = st.columns([1, 4])
    with col_btn:
        search_clicked = st.button("Search Knowledge")

    # Document browser dropdown
    doc_options = ["Select document..."] + teacher.get_document_names()
    selected_doc = st.selectbox("Or browse files directly:", doc_options)

    st.write("---")

    if search_clicked and query:
        res = teacher.query_knowledge(query, lang)
        st.markdown(res)
    elif selected_doc != "Select document...":
        doc_content = teacher.get_document(selected_doc)
        st.markdown(f"### Document: {selected_doc.upper()}\n\n---\n\n{doc_content}")
    else:
        st.info("Enter keywords above or select a document to start studying.")
