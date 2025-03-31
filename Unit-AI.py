# ** Enginnering Surveying I by Sir Ahmed**
# Convert Quadrantal Bearing to Azimuth Angle
# Convert Azimuth Angle to Quadrantal Bearing
# Gives step by step calculation
# A perfect blend of aesthetic UI and intuitive UX.
# complete short guide of topics 
# made by student of Sir

import streamlit as st
import time
import requests

# Page Configuration
st.set_page_config(
    page_title="Unit AI", 
    page_icon="🇵🇸", 
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://www.google.com/search?q=help",
        "Report a bug": "https://github.com/smaasui",
        "About": """# SMAASU Corporation©️  
        https://g.co/kgs/VvQB8W9
        App Version 0.617"""}
    )

st.sidebar.title("⚖ SMAASU Unit AI Converter")
tabs = st.sidebar.radio("", ["Conversion", "About App", "About Us", "About Me"])

if tabs == "Conversion":
    st.write("# 🌍 SMAASU's Unit Converter ! 🥋")
    # Conversion Functions
    def length_converter(value, from_unit, to_unit):
        conversion_factors = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701, "Yards": 1.09361, "Centimeters": 100, "Millimeters": 1000}
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

    def weight_converter(value, from_unit, to_unit):
        conversion_factors = {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274, "Stones": 0.000157473}
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

    def temperature_converter(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32

    def speed_converter(value, from_unit, to_unit):
        conversion_factors = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Knots": 1.94384}
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

    def time_converter(value, from_unit, to_unit):
        conversion_factors = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400, "Weeks": 1/604800}
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

    def currency_converter(value, from_currency, to_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        try:
            response = requests.get(url).json()
            rates = response.get("rates", {})
            if to_currency in rates:
                return value * rates[to_currency]
            else:
                return "Invalid currency code"
        except Exception as e:
            return f"Error fetching rates: {str(e)}"

    TABS = ["📏 Length", "⚖️ Weight", "🌡 Temperature", "💨 Speed", "🕰 Time", "💲 Currency"]
    tabs = st.tabs(TABS)

    for index, tab in enumerate(tabs):
        with tab:
            unique_key = f"input_{index}"
            value = st.number_input("Enter Value", value=1, key=f"{TABS[index]}_{unique_key}")
            
            if index == 0:
                st.subheader("Length Converter")
                units = ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Yards", "Centimeters", "Millimeters"]
                converter = length_converter
            elif index == 1:
                st.subheader("Weight Converter")
                units = ["Grams", "Kilograms", "Pounds", "Ounces", "Stones"]
                converter = weight_converter
            elif index == 2:
                st.subheader("Temperature Converter")
                units = ["Celsius", "Fahrenheit", "Kelvin"]
                converter = temperature_converter
            elif index == 3:
                st.subheader("Speed Converter")
                units = ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"]
                converter = speed_converter
            elif index == 4:
                st.subheader("Time Converter")
                units = ["Seconds", "Minutes", "Hours", "Days", "Weeks"]
                converter = time_converter
            elif index == 5:
                st.subheader("Currency Converter")
                units = ["USD", "PKR", "EUR", "GBP", "INR", "CAD", "AUD", "CNY"]
                converter = currency_converter
                st.write("**Note : This requires stable internet connection.**")
            
            from_unit = st.selectbox("From", units, key=f"{TABS[index]}_from_{unique_key}")
            to_unit = st.selectbox("To", units, key=f"{TABS[index]}_to_{unique_key}")
            
            result = converter(value, from_unit, to_unit)
            
            with st.spinner("🔄 Converting..."):
                time.sleep(0.2)
            st.success(f"✅ {value} {from_unit} = {result} {to_unit}")

elif tabs == "About App":
    # About App Section
    def about_app():
        st.markdown("""
        # ⚖ **UnitAI - Ultimate Unit Converter**  
        #### **By SMAASU Corporation**
                    
        ## **About App**  

        ### 📌 **Key Features:**  

        ✔️ **Multi-Category Unit Conversion**  
        → Convert **Length, Weight, Temperature, Speed, Time, Area, Volume, Power, Energy, and Currency** seamlessly.  

        ✔️ **Real-time Currency Exchange Rates**  
        → Get up-to-date exchange rates for major global currencies, including **USD, PKR, EUR, GBP, INR, CAD, AUD, CNY, and more**.  

        ✔️ **Fast and Accurate Conversions**  
        → Optimized conversion algorithms ensure instant and precise results for all unit categories.  

        ✔️ **User-Friendly Interface**  
        → Intuitive **Streamlit-powered** UI with easy navigation for an effortless experience.  

        ✔️ **Lightweight and Efficient**  
        → Designed for quick performance with minimal resource usage.  

        **UnitAI is built for professionals, students, and anyone needing quick, reliable unit conversions.**  

        **Convert Anything, Anytime! 🚀**  
        """, unsafe_allow_html=True)

    # Call the function to display the about section
    col1, col2, col3 = st.columns([1.2,7.6,1.2])
    with col2:
        about_app()

elif tabs == "About Me":
    st.write("# 🏅 Syed Muhammad Abdullah Abdulbadeeii")
    col1, col2, col3 = st.columns([4.5,1,4.5])
    with col1:
    # Personal Title 🏅🌟💡🌱🌍👤
        st.write("\n\n")
        st.markdown(
        "<img src='https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg' width='550'>",
        unsafe_allow_html=True)

        # st.image("https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg", use_container_width=True, width=100)
        # Expertise & Interests
        st.write("\n\n")
        st.write("# 🚀 Areas of Expertise")
        st.markdown(
            """
            - 🏗️ **Civil Engineering & Smart Infrastructure** – Engineering sustainable and innovative urban solutions.
            - 💻 **Software & Web Development** – Creating intelligent digital solutions to optimize efficiency.
            - 🤖 **Artificial Intelligence & Data Science** – Harnessing AI-driven technologies for smarter decision-making.
            - 📊 **Data Processing & Automation** – Streamlining complex workflows through advanced automation.
            - 🚀 **Entrepreneurship & Technological Innovation** – Spearheading startups that drive meaningful change.
            - ❤️ **Philanthropy & Social Impact** – Advocating for and supporting communities in need.
            """
        )


    with col3:
        st.write("# 🌱 About Me")
        # Introduction
        st.markdown(
            """
            I am **Syed Muhammad Abdullah Abdulbadeeii**, a **Civil Engineering Student at NED University of Engineering & Technology, Entrepreneur, Innovator, and Philanthropist**. 
            With a deep passion for **Artificial Intelligence, Architecture, and Sustainable Urbanization**, I am committed to pioneering **Transformative Solutions** that seamlessly integrate technology with real-world applications.
            
            My work is driven by a vision to **Build a Smarter, More Sustainable Future**, where cutting-edge innovations enhance efficiency, improve urban living, and empower businesses. 
            Beyond my professional pursuits, I am dedicated to **philanthropy**, striving to **uplift Muslims and support underprivileged communities**, fostering a society rooted in compassion, empowerment, and progress.
            """
        )
        
        # Vision & Journey
        st.write("# 🌍 My Vision & Journey")
        st.markdown(
            """
            As the founder of **SMAASU Corporation**, I have led groundbreaking initiatives such as **Data Duster**, a web-based platform revolutionizing data processing and automation. 
            My entrepreneurial journey is fueled by a relentless drive to **bridge the gap between technology and urban development**, delivering impactful solutions that **redefine the future of cities and industries**.
            
            **I believe in innovation, sustainability, and the power of technology to transform lives.** Through my work, I strive to create solutions that not only drive efficiency but also foster inclusivity and social well-being.
            
            **Let’s collaborate to build a brighter, more progressive future!**
            """
        )
        
    st.write("# 🔗 Engineering connections !")
    st.link_button("🔗 Stay connected on LinkedIn!", "https://www.linkedin.com/in/smaasui/")

elif tabs == "About Us":
    col1, col2, col3 = st.columns([1.5,7,1.5])
    with col2:

        # Company Title
        st.write("# 🏢 About SMAASU Corporation")

        # Introduction
        st.markdown(
            """
            **SMAASU Corporation** is a forward-thinking company committed to innovation in **technology, architecture, and sustainable urbanization**.
            Our vision is to create cutting-edge solutions that simplify workflows, enhance productivity, and contribute to a smarter, more efficient future.
            """
        )

        # Mission Section
        st.header("🌍 Our Mission")
        st.markdown(
            """
            At **SMAASU Corporation**, we aim to:
            - 🚀 **Develop pioneering software solutions** that enhance business efficiency.
            - 🏗️ **Revolutionize architecture and urban planning** with smart, sustainable designs.
            - 🌱 **Promote sustainability** in every project we undertake.
            - 🤝 **Empower businesses and individuals** with next-gen technology.
            """
        )

        # Core Values Section
        st.header("💡 Our Core Values")
        st.markdown(
            """
            - **Innovation** – Continuously pushing boundaries with cutting-edge technology.
            - **Sustainability** – Building a future that is eco-friendly and efficient.
            - **Excellence** – Delivering top-tier solutions with precision and quality.
            - **Integrity** – Upholding transparency and trust in every endeavor.
            """
        )

        # Call to Action
        st.markdown(
            """
            🚀 **Join us on our journey to create a smarter, more sustainable world with SMAASU Corporation!**
            """,
            unsafe_allow_html=True
        )
        st.link_button("🔗 Visit SMAASU Corporation", "https://g.co/kgs/VvQB8W9")

    col1, col2, col3 = st.columns([2,6,2])
    with col2:

        st.write("# **Releasing Coming Soon...** 🚀")
        st.write("#### Stay tuned!")