import streamlit as st
import requests

def get_random_dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    return data["message"]

def main():
    st.title("Random Dog Image Viewer")
    random_dog_image = get_random_dog_image()

    if st.button("Generate New Dog Image"):
        st.experimental_rerun()

    st.image(random_dog_image, caption="Random Dog Image", use_column_width=True)

if __name__ == "__main__":
    main()
