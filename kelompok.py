import streamlit as st
st.set_page_config(page_title="Substance Analyzer")



add_selectbox = st.sidebar.selectbox(
    "Substance Analyzer",("home","tentang aplikasi","Mengetahui nilai massa atom relatif suatu unsur","perhitungan kadar (b/v)","perhitungan kadar(b/b)","tentang kami","referensi"))

if add_selectbox=="home":
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>Welcome to substance analyzer</h1>", unsafe_allow_html=True)
    st.image("LPK.png",caption=("Selamat datang di web kami"))
    st.markdown("<h1 style= 'image align: center'>LPK.gif</h1>",unsafe_allow_html=true)
elif add_selectbox=="Mengetahui nilai massa atom relatif suatu unsur":
    st.header('Mencari Nilai Ar Suatu Unsur')
    atom=st.text_input('Masukkan Simbol Unsur (cth: Pb)')
    tombol=st.button('Tampilkan Nilai Ar')

    if atom == "H" :
        st.success ("1")
    elif atom == "Li" :
        st.success ("7")
    elif atom == "Na" :
        st.success ("23")
    elif atom == "K" :
        st.success ("39")
    elif atom == "Rb" :
        st.success ("85,5")
    elif atom == "Cs" :
        st.success ("133")
    elif atom == "Fr" :
        st.success ("223")
    elif atom == "Be" :
        st.success ("9")
    elif atom == "Mg" :
        st.success ("24,3")
    elif atom == "Ca" :
        st.success ("40")
    elif atom == "Sr" :
        st.success ("88")
    elif atom == "Ba" :
        st.success ("137")
    elif atom == "Ra" :
        st.success ("226")
    elif atom == "Ra" :
        st.success ("226")
    elif atom == "Sc" :
        st.success ("45")
    elif atom == "Y" :
        st.success ("89")
    elif atom == "Ti" :
        st.success ("48")
    elif atom == "Zr" :
        st.success ("91,2")
    elif atom == "Hf" :
        st.success ("178,5")
    elif atom == "Rf" :
        st.success ("267,1")
    elif atom == "B" :
        st.success ("11")
    elif atom == "Al" :
        st.success ("27")
    elif atom == "Ga" :
        st.success ("70")
    elif atom == "In" :
        st.success ("115")
    elif atom == "Tl" :
        st.success ("204,4")
    elif atom == "Uut" :
        st.success ("289")
    elif atom == "C" :
        st.success ("12")
    elif atom == "Si" :
        st.success ("28,1")
    elif atom == "Ge" :
        st.success ("73")
    elif atom == "Sn" :
        st.success ("119")
    elif atom == "Pb" :
        st.success ("207,2")
    elif atom == "Fl" :
        st.success ("289,2")
    elif atom == "Nh" :
        st.success ("286,2")
    elif atom == "Lu" :
        st.success ("175")
    elif atom == "Lr" :
        st.success ("262,1")
    elif atom == "V" :
        st.success ("51")
    elif atom == "Nb" :
        st.success ("93")
    elif atom == "Ta" :
        st.success ("181")
    elif atom == "Db" :
        st.success ("262")
    elif atom == "Cr" :
        st.success ("52")
    elif atom == "Mo" :
        st.success ("96")
    elif atom == "W" :
        st.success ("184")
    elif atom == "Sg" :
        st.success ("266")
    elif atom == "N" :
        st.success ("14")
    elif atom == "P" :
        st.success ("31")
    elif atom == "As" :
        st.success ("75")
    elif atom == "Sb" :
        st.success ("122")
    elif atom == "Bi" :
        st.success ("209")
    elif atom == "Uup" :
        st.success ("288")
    elif atom == "Mc" :
        st.success ("289,2")
    elif atom == "O" :
        st.success ("16")
    elif atom == "S" :
        st.success ("32")
    elif atom == "Se" :
        st.success ("79")
    elif atom == "Te" :
        st.success ("128")
    elif atom == "Po" :
        st.success ("209")
    elif atom == "Lv" :
        st.success ("293.2")
    elif atom == "Mn" :
        st.success ("55")
    elif atom == "Tc" :
        st.success ("99")
    elif atom == "Re" :
        st.success ("186,2")
    elif atom == "Bh" :
        st.success ("264")
    elif atom == "Fe" :
        st.success ("56")
    elif atom == "Ru" :
        st.success ("101")
    elif atom == "Os" :
        st.success ("190,2")
    elif atom == "Hs" :
        st.success ("269")
    elif atom == "Co" :
        st.success ("59")
    elif atom == "Rh" :
        st.success ("103")
    elif atom == "Ir" :
        st.success ("192,2")
    elif atom == "Mt" :
        st.success ("268")
    elif atom == "Ni" :
        st.success ("59")
    elif atom == "Pd" :
        st.success ("106,4")
    elif atom == "Pt" :
        st.success ("195")
    elif atom == "Ds" :
        st.success ("269")
    elif atom == "F" :
        st.success ("19")
    elif atom == "Cl" :
        st.success ("35,5")
    elif atom == "Br" :
        st.success ("80")
    elif atom == "I" :
        st.success ("127")
    elif atom == "At" :
        st.success ("210")
    elif atom == "Uus" :
        st.success ("292")
    elif atom == "He" :
        st.success ("4")
    elif atom == "Ne" :
        st.success ("20,2")
    elif atom == "Ar" :
        st.success ("40")
    elif atom == "Kr" :
        st.success ("85")
    elif atom == "Xe" :
        st.success ("131,3")
    elif atom == "Rn" :
        st.success ("222")
    elif atom == "Uuo" :
        st.success ("293")
    elif atom == "La" :
        st.success ("139")
    elif atom == "Ce" :
        st.success ("140")
    elif atom == "Pr" :
        st.success ("141")
    elif atom == "Nd" :
        st.success ("144")
    elif atom == "Pm" :
        st.success ("145")
    elif atom == "Sm" :
        st.success ("150")
    elif atom == "Eu" :
        st.success ("152")
    elif atom == "Gd" :
        st.success ("157")
    elif atom == "Td" :
        st.success ("159")
    elif atom == "Dy" :
        st.success ("162")
    elif atom == "Ho" :
        st.success ("165")
    elif atom == "Er" :
        st.success ("167")
    elif atom == "Tm" :
        st.success ("169")
    elif atom == "Yb" :
        st.success ("173")
    elif atom == "Lu" :
        st.success ("175")
    elif atom == "Ac" :
        st.success ("227")
    elif atom == "Th" :
        st.success ("232")
    elif atom == "Pa" :
        st.success ("231")
    elif atom == "U" :
        st.success ("238")
    elif atom == "Np" :
        st.success ("237")
    elif atom == "Pu" :
        st.success ("244")
    elif atom == "Am" :
        st.success ("243")
    elif atom == "Cm" :
        st.success ("247")
    elif atom == "Bk" :
        st.success ("247")
    elif atom == "Cf" :
        st.success ("251")
    elif atom == "Es" :
        st.success ("254")
    elif atom == "Fm" :
        st.success ("257")
    elif atom == "Md" :
        st.success ("258")
    elif atom == "No" :
        st.success ("259")
    elif atom == "Lr" :
        st.success ("262")
    else :
        st.success ("Mohon memasukkan simbol unsur yang sesuai ")


    
elif add_selectbox=="perhitungan kadar (b/v)":
    st.header('Kalkulator Perhitungan Kadar %(b/v) Dalam Sampel')
    y=st.number_input('Masukkan volume titran yang digunakan untuk titrasi :',value=0.0000)
    x=st.number_input('Masukkan konsentrasi titran yang digunakan :', min_value=0.0000,format='%.4f')    
    z=st.number_input('Masukkan nilai BE sampel :')
    w=st.number_input('Masukkan volume sampel (mL) :')
    r=st.number_input('Masukkan faktor pengali/pengenceran yang digunakan :',min_value=1)
    st.write('Bila tidak ada faktor pengali/pengenceran masukkan nilai=1')
    





    tombol = st.button('Hitung')
     
    if tombol:
        jumlahkadar=y*x*z*r/w*0.1
        st.success(f'Kadar %(b/v) sampel= {jumlahkadar}%') 

elif add_selectbox=="perhitungan kadar(b/b)":
    st.header('Kalkulator Perhitungan Kadar %(b/b) Dalam Sampel')
    a=st.number_input('volume titran yang digunakan untuk titrasi :')
    b=st.number_input('konsenstrasi titran yang digunakan :', min_value=0.0000,format='%.4f')    
    c=st.number_input('nilai BE sampel :')
    d=st.number_input('bobot sampel (mg) :')
    e=st.number_input(' faktor pengali/pengenceran yang digunakan :',min_value=1)
    st.write('Bila tidak ada faktor pengali/pengenceran masukkan nilai=1')


    tombol =st.button('Hitung kadar')
     
    if tombol:
        jumlah=a*b*c*e/d*100
        st.success(f'Kadar %(b/b) sampel= {jumlah}%') 



