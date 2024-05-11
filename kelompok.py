import streamlit as st

st.title('Menghitung Jumlah kadar ')

tab1, tab2, tab3=st.tabs(['informasi tentang PPM','kalkulator menghitung Molaritas','kalkulator menghitung ppm dari Molaritas'])

with tab1:
    st.header('informasi tentang PPM')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta") adalah satuan yang dipakai sebagai satuan nirdimensi yang berasal dari pecahan yang sangat kecil, misalnya konsentrasi larutan atau kelimpahan partikel yang sangat kecil. ')

    
with tab2:
    st.header('kalkulator menghitung kadar %(b/v) ')
    y=st.number_input('Masukkan volume dari titran yang digunakan selama titrasi :',value=0.0000)
    x=st.number_input('Masukkan konsenstrasi titran yang digunakan :', min_value=0.0000,format='%.4f')    
    z=st.number_input('Masukkan nilai BE sample :')
    w=st.number_input('masukkan volume titrat dalam erlenmeyer :')
    r=st.number_input('masukkan faktor pengali/pengenceran yang digunakan :',min_value=1)
    st.write('Bila tidak ada fp masukkan nilai fp sebagai:1')
    





    tombol = st.button('Hitung jumlah molaritas')
     
    if tombol:
        jumlahmolaritas=y*x*z*r/w*0.1
        st.success(f'Kadar (b/v) sampel adalah{jumlahmolaritas} %') 





with tab3:
    st.header('kalkulator menghitung PPM dengan diketahui molaritas')
    x=st.number_input('Masukkan molaritas dari sampel yang telah dipilih dalam satuan mg/mmol:')
    y=st.number_input('Masukkan volume titran dalam satuan mL:')    
    z=st.number_input('Masukkan bobot molekul dalam satuan mmol/mL')
    v=st.number_input('Masukkan volume sampel dalam satuan mL')


    tombol = st.button('Hitung jumlah PPM')
     
    if tombol:
        jumlahPPM=x*y*z/v/0.001
        st.success(f'jumlah PPM adalah{jumlahPPM}') 



