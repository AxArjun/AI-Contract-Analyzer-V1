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
        background: linear-gradient(135deg, #0e1117 0%, #1a1c24 100%);
        font-family: 'Inter', sans-serif;
    }

    /* Titles with Gradients */
    h1 {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }
    
    h2, h3 {
        color: #e0e0e0 !important;
    }

    /* Buttons - Premium Gradient */
    .stButton>button {
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(221, 36, 118, 0.4);
    }

    /* Card-like Containers */
    .css-1r6slb6, .stMarkdown, .stJson {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #111;
        border-right: 1px solid #333;
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
    
    with tab1:
        st.markdown("#### Legal & Compliance")
        data = result.get("legal", {})
        if isinstance(data, dict):
            for key, value in data.items():
                st.markdown(f"**{key.replace('_', ' ').title()}:**")
                st.write(str(value)) # Convert to string to handle lists/dicts safely
                st.divider()
        else:
             st.write(str(data))
        
    with tab2:
        st.markdown("#### Financial Terms")
        data = result.get("financial", {})
        if isinstance(data, dict):
            for key, value in data.items():
                st.markdown(f"**{key.replace('_', ' ').title()}:**")
                st.write(str(value))
                st.divider()
        else:
             st.write(str(data))

    with tab3:
        st.markdown("#### Operational Details")
        data = result.get("operations", {})
        if isinstance(data, dict):
            for key, value in data.items():
                st.markdown(f"**{key.replace('_', ' ').title()}:**")
                st.write(str(value))
                st.divider()
        else:
             st.write(str(data))
        
    with tab4:
        st.json(result)

if __name__ == "__main__":
    main()
