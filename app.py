import streamlit as st
from google import genai
from google.genai import types

from prompts import (
    REPORT_REQUEST_PROMPT,
    SYSTEM_PROMPT_TEMPLATE,
    WELCOME_MESSAGE_TEMPLATE,
)

# If you get a "model not found" error, replace with the model name
# shown in Google AI Studio (e.g. "gemini-2.5-flash").
MODEL_NAME = "gemini-3.5-flash"

st.set_page_config(page_title="CropDoc", page_icon="🌿")

if "GEMINI_API_KEY" not in st.secrets or not st.secrets["GEMINI_API_KEY"]:
    st.error("Missing GEMINI_API_KEY. Add it to .streamlit/secrets.toml and restart the app.")
    st.stop()

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

LANGUAGES = ["English", "Hindi", "Gujarati", "Telugu", "Tamil", "Marathi", "Kannada"]
CROPS = ["Tomato", "Potato", "Rice", "Wheat", "Cotton", "Maize", "Groundnut", "Other"]


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)


gemini_client = get_gemini_client()


def render_message(message):
    with st.chat_message(message["role"]):
        if message["kind"] == "text":
            st.write(message["content"])
        elif message["kind"] == "image":
            st.image(message["content"], width=300)


def add_message(role, kind, content):
    st.session_state.messages.append({"role": role, "kind": kind, "content": content})
    render_message(st.session_state.messages[-1])


def ask_gemini(parts):
    try:
        return st.session_state.chat.send_message(parts).text
    except Exception as error:
        return f"Sorry, something went wrong: {error}"


# ---------- Onboarding ----------
if "onboarded" not in st.session_state:
    st.title("🌿 CropDoc")
    st.caption("Snap a leaf. Find the problem. Fix it early.")
    with st.form("onboarding_form"):
        name = st.text_input("Your name")
        crop = st.selectbox("Main crop", CROPS)
        language = st.selectbox("Reply language", LANGUAGES)
        submitted = st.form_submit_button("Start 🚀")
    if submitted:
        if not name.strip():
            st.warning("Please enter your name.")
        else:
            system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
                name=name.strip(), crop=crop, language=language
            )
            st.session_state.name = name.strip()
            st.session_state.crop = crop
            st.session_state.language = language
            st.session_state.chat = gemini_client.chats.create(
                model=MODEL_NAME,
                config=types.GenerateContentConfig(system_instruction=system_prompt),
            )
            st.session_state.messages = []
            st.session_state.onboarded = True
            st.rerun()
    st.stop()

# ---------- Sidebar: report + reset ----------
with st.sidebar:
    st.header("Your report")
    st.caption("Chat first, then create a report you can save.")
    report_disabled = len(st.session_state.messages) <= 2
    if st.button("📄 Create report", disabled=report_disabled, use_container_width=True):
        with st.spinner("Writing your report..."):
            st.session_state.report = ask_gemini([REPORT_REQUEST_PROMPT])
    if "report" in st.session_state:
        st.download_button(
            "⬇️ Download report (.txt)",
            data=st.session_state.report,
            file_name="cropdoc_report.txt",
            use_container_width=True,
        )
    st.divider()
    if st.button("🔄 Start over", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.caption(
        "⚠️ AI estimates only, not a lab test. Confirm with your local "
        "agriculture officer / KVK before spraying."
    )

# ---------- Chat ----------
st.title("🌿 CropDoc")
st.caption(f"{st.session_state.name} · Crop: {st.session_state.crop}")

if not st.session_state.messages:
    add_message(
        "assistant",
        "text",
        WELCOME_MESSAGE_TEMPLATE.format(
            name=st.session_state.name, crop=st.session_state.crop
        ),
    )
else:
    for message in st.session_state.messages:
        render_message(message)

user_input = st.chat_input(
    "Describe the problem, or attach a leaf photo",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)

if user_input:
    photo = user_input.files[0] if user_input.files else None
    text = user_input.text
    parts = []

    if photo is not None:
        photo_bytes = photo.getvalue()
        add_message("user", "image", photo_bytes)
        parts.append(types.Part.from_bytes(data=photo_bytes, mime_type=photo.type))
    if text:
        add_message("user", "text", text)
        parts.append(text)
    elif photo is not None:
        parts.append("Look at this plant photo. What is the likely problem and what should I do?")

    with st.spinner("Checking your plant..."):
        answer = ask_gemini(parts)
    add_message("assistant", "text", answer)