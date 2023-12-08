import streamlit as st
from api.teaching_materials import TeachingMaterial

def get_teaching_material_color(teachingMaterial_index):
    colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
    return colors[teachingMaterial_index % len(colors)]

st.set_page_config(page_title="List of Teaching Materials",layout='wide')

st.header('List of Teaching Materials')
teaching_materials = TeachingMaterial().get_teaching_materials()

if teaching_materials:
    for index, teaching_material in enumerate(teaching_materials):
        background_color = get_teaching_material_color(index)
    st.markdown(
        f'<div style="padding: 10px; border-radius: 5px; background-color: {background_color}; color: black">'
            f'<div style="display: flex; flex-direction: column; max-width: 60%">'
                f'<h2 style="color: black">ID: {teaching_material.id}</h2>'
                f'<div style="display: flex; flex-direction: column; flex-wrap: wrap; margin-left: 20px;">'
                    f'<p>Description: {teaching_material.description}</p>'
                    f'<p>Category: {teaching_material.category}</p>'
                    f'<p>Date Acquisition: {teaching_material.date_acquisition}</p>'
                    f'<p>Serie Number: {teaching_material.serie_number}</p>'
                    f'<p>Conservation Status: {teaching_material.conservation_status}</p>'
                    f'<p>Physical Location: {teaching_material.physical_location}</p>'
                    f'<p>Material Cover url: {teaching_material.material_cover_url}</p>'
                    f'<p>Status: {teaching_material.status}</p>'
                f'</div>'
            f'</div>'
            f'<img src="{teaching_material.material_cover_url}" alt="Teaching Material Cover" style="height: 40%; max-width: 35%; margin-right: 20px;">'
        f'</div>',
        unsafe_allow_html=True
    )
    st.text('')