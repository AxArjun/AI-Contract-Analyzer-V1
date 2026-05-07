import streamlit as st
import requests
import json
import time

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="IA Contract Analyzer",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PREMIUM UI ---
st.markdown("""
<style>
    /* Main Background & Fonts */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }

    /* Titles with Gradients */
    h1 {
        background: linear-gradient(90deg, #2c3e50 0%, #3498db 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }
    
    h2, h3, h4, p, label, .stMarkdown, .stJson {
        color: #2c3e50 !important;
    }
    
    .stCaption {
        color: #555 !important;
    }

    /* Buttons - Premium Gradient */
    .stButton>button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Specific fix for Form Submit Button to ensure visibility */
    [data-testid="stFormSubmitButton"]>button {
        color: #ffffff !important;
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(24, 40, 72, 0.3);
    }
    
    /* Input Fields */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #ffffff;
        color: #333;
        border-radius: 8px;
        border: 1px solid #ddd;
    }

    /* Card-like Containers */
    .css-1r6slb6, .stMarkdown, .stJson {
        background: rgba(255, 255, 255, 0.6);
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    [data-testid="stSidebar"] * {
        color: #333 !important;
    }

</style>
""", unsafe_allow_html=True)

# --- SESSION STATE & HISTORY ---
if 'history' not in st.session_state:
    st.session_state['history'] = []

def main():
    # Header Section
    st.title("⚖️ AI Contract Analyzer")
    st.markdown("""
    <div style='background: rgba(33, 150, 243, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2196F3;'>
        <h4>Professional Automated Legal Analysis</h4>
        <p>Upload your contracts for instant risk assessment, compliance checks, and operational summaries.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # --- SIDEBAR: HISTORY ---
    with st.sidebar:
        st.header("📜 Session History")
        if not st.session_state['history']:
            st.info("No documents analyzed in this session.")
        else:
            for idx, item in enumerate(reversed(st.session_state['history'])):
                with st.expander(f"📄 {item['filename']}"):
                    st.caption(f"Analyzed at: {item['time']}")
                    st.success("Analysis Complete")
        
        # User guide removed

    # --- MAIN UPLOAD AREA ---
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader("📂 Upload Contract (PDF)", type=["pdf"])

        if uploaded_file is not None:
            st.markdown(f"**Selected File:** `{uploaded_file.name}`")
            
            if st.button("🚀 Analyze Contract Now"):
                with st.spinner("🔍 Interpreting Legal Clauses..."):
                    # Simulate slight delay for effect (optional) or just run
                    try:
                        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
                        response = requests.post(f"{BACKEND_URL}/analyze", files=files)
                        
                        if response.status_code == 200:
                            result = response.json()
                            
                            # Add to History
                            st.session_state['history'].append({
                                "filename": uploaded_file.name,
                                "result": result,
                                "time": time.strftime("%H:%M:%S")
                            })
                            
                            display_results(result)
                            st.balloons()
                        else:
                            st.error(f"❌ Error: {response.status_code} - {response.text}")
                    except requests.exceptions.ConnectionError:
                        st.error("🔌 Could not connect to the backend. Is it running?")
                    except Exception as e:
                        st.error(f"⚠️ An unexpected error occurred: {str(e)}")

    with col2:
        # Just a visual spacer or instructional graphic could go here
        st.info("💡 **Tip:** Ensure the PDF is text-selectable for best results.")

    # --- FEEDBACK SECTION ---
    st.divider()
    st.subheader("💬 Feedback")
    
    with st.form("feedback_form"):
        st.write("How was the analysis quality?")
        cols = st.columns(2)
        rating = cols[0].slider("Rating", 1, 5, 5)
        text = cols[1].text_area("Additional Comments")
        
        submitted = st.form_submit_button("Submit Feedback")
        if submitted:
            st.toast("✅ Thank you! Your feedback helps us improve.")
            # Here you would log the feedback to a file/db

def display_results(result):
    st.markdown("### 📊 Analysis Report")
    
    # Check structure
    if isinstance(result, str):
        st.warning(result)
        return

    # Use Tabs for cleaner organization
    tab1, tab2, tab3, tab4 = st.tabs(["🛡️ Legal Risks", "💰 Financial", "⚙️ Operations", "📜 Full Details"])
    
    def extract_content(data):
        """Helper to extract string content from various data structures"""
        # Case 1: List of message objects (LangGraph/LangChain format)
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            # Check for 'type': 'text' and 'text' key
            if 'text' in data[0]:
                return data[0]['text']
            # Fallback for other message types
            elif 'content' in data[0]:
                return data[0]['content']
        
        # Case 2: Direct string
        if isinstance(data, str):
            return data
            
        # Case 3: Simple dictionary (not a list of messages)
        if isinstance(data, dict):
            return data
            
        return str(data)

    def render_section(section_name, data):
        st.markdown(f"#### {section_name}")
        content = extract_content(data)
        
        if isinstance(content, dict):
            for key, value in content.items():
                st.markdown(f"**{key.replace('_', ' ').title()}:**")
                st.markdown(str(value)) # Use markdown to render potential internal markdown
                st.divider()
        else:
            # Render the extracted text as markdown
            st.markdown(content)

    with tab1:
        render_section("Legal & Compliance", result.get("legal", {}))
        
    with tab2:
        render_section("Financial Terms", result.get("financial", {}))

    with tab3:
        render_section("Operational Details", result.get("operations", {}))
        
    with tab4:
        st.json(result)

if __name__ == "__main__":
    main()
