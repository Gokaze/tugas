import streamlit as st

st.title('Menghitung Jumlah kadar ')

tab1, tab2, tab3=st.tabs(['informasi tentang PPM','kalkulator menghitung Molaritas','kalkulator menghitung ppm dari Molaritas'])

with tab1:
    st.header('informasi tentang PPM')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta") adalah satuan yang dipakai sebagai satuan nirdimensi yang berasal dari pecahan yang sangat kecil, misalnya konsentrasi larutan atau kelimpahan partikel yang sangat kecil. ')

    
with tab2:
    st.header('kalkulator menghitung kadar %(b/v) dalam sampel')
    y=st.number_input('Masukkan volume dari titran yang digunakan selama titrasi :',value=0.0000)
    x=st.number_input('Masukkan konsenstrasi titran yang digunakan :', min_value=0.0000,format='%.4f')    
    z=st.number_input('Masukkan nilai BE sample :')
    w=st.number_input('masukkan volume sampel (mL) :')
    r=st.number_input('masukkan faktor pengali/pengenceran yang digunakan :',min_value=1)
    st.write('Bila tidak ada fp masukkan nilai fp sebagai:1')
    





    tombol = st.button('Hitung')
     
    if tombol:
        jumlahkadar=y*x*z*r/w*0.1
        st.success(f'Kadar (b/v) sampel adalah= {jumlahkadar}%') 

with tab3:
    st.header('kalkulator menghitung kadar %(b/b) dalam sampel')
    a=st.number_input('volume titran yang digunakan selama titrasi :')
    b=st.number_input('konsenstrasi titran yang digunakan :', min_value=0.0000,format='%.4f')    
    c=st.number_input('nilai BE sample :')
    d=st.number_input('masukkan bobot sampel (mg) :')
    e=st.number_input('faktor pengali/pengenceran yang digunakan :',min_value=1)
    st.write('Bila tidak ada fp masukkan nilai fp sebagai:1')


    tombol = st.button('Hitung')
     
    if tombol:
        jumlahkadar=a*b*c*e/d*0.1
        st.success(f'Kadar (b/b) sampel adalah= {jumlahkadar}%') 



