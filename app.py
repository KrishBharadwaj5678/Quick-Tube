from pytube import YouTube 
import streamlit as st

st.set_page_config(
    page_title="Quick Tube",
    page_icon="logo.png",
    menu_items={
        "About":"""Unlock seamless downloads with QuickTube! Effortlessly convert and download your favorite YouTube videos and audio files in high quality. Whether you need music, videos, or educational content, our user-friendly platform makes it fast and easy. Enjoy unlimited downloads with just a few clicks."""
    }
)

st.write("<h2 style='color:#25D366';>Download YouTube Audio & Video Instantly</h2>",unsafe_allow_html=True)

url=st.text_input("Enter Audio/Video URL",placeholder="Paste your link here")

user_select=st.radio("Choose Your Download:",["Audio","Video","Muted Video"])

btn=st.button("Start →")

if btn:

    try:
        link = url
        yt = YouTube(link) 

        def download(filename,download):
            with open(filename,"rb") as audio:
                bin_audio=audio.read()
                st.download_button(download,data=bin_audio,file_name=filename)

        if(user_select=="Audio"):
            with st.spinner("Working on it..."):
                mp4_streams = yt.streams.filter(file_extension='mp4').all()
                d_video = mp4_streams[-1]
                d_video.download(filename="audio.mp3")
                download("audio.mp3","Download Audio")
        
        elif(user_select=="Video"):
            with st.spinner("Working on it..."):
                streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
                video = streams.first()
                video.download(filename="video.mp4")
                download("video.mp4","Download Video")

        elif(user_select=="Muted Video"):
            with st.spinner("Working on it..."):
                streams = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc()
                video = streams.first()
                video.download(filename="muted-video.mp4")
                download("muted-video.mp4","Download Muted Video")
    except:
        st.error("Invalid Youtube URL :(")