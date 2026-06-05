import streamlit as st
import time
import platform
import socket
import os

st.set_page_config(page_title="TRI-NOVA Operational Interface", page_icon="📡", layout="wide")

# Custom CSS for UI styling
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d0f1c 0%, #020308 100%);
        color: #d1d8f5;
    }
    h1, h2, h3 {
        color: #00f0ff !important;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
    }
    [data-testid="stMetricValue"] {
        color: #b026ff !important;
        text-shadow: 0 0 10px rgba(176, 38, 255, 0.6);
    }
    .stButton>button {
        background: linear-gradient(135deg, #b026ff 0%, #00f0ff 100%);
        color: #ffffff;
        border: none;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.3);
        border-radius: 8px;
        transition: all 0.3s ease;
        font-weight: bold;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        box-shadow: 0 0 30px rgba(176, 38, 255, 0.8);
        transform: translateY(-2px);
    }
    [data-testid="stSidebar"] {
        background: rgba(5, 7, 15, 0.95) !important;
        border-right: 1px solid rgba(0, 240, 255, 0.3);
    }
    code {
        color: #00ffcc !important;
        background: rgba(0, 30, 20, 0.6) !important;
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 4px;
    }
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    .stTabs [data-baseweb="tab"] { color: #8c9eff; }
    .stTabs [aria-selected="true"] { color: #00f0ff !important; border-bottom: 2px solid #00f0ff; }
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "SYSTEM ONLINE. TERMINAL ACTIVE. AWAITING INPUT."}
    ]

st.sidebar.title("📡 Node Array")
st.sidebar.markdown("""
- **NODE_01** (Navigation): `[OK]`
- **NODE_02** (Chemical): `[OK]`
- **NODE_03** (Actuator): `[OK]`
- **NODE_04** (Tectonic): `[OK]`
""")
st.sidebar.markdown("---")
st.sidebar.markdown("### Hardware Status")
st.sidebar.markdown("✅ **ASIC:** Active")
st.sidebar.markdown("🔋 **Power:** 4.2mW")
st.sidebar.markdown("🔆 **Network:** Photonic DDS")

st.title("📡 TRI-NOVA: Operational Interface")

tab1, tab2, tab3, tab4 = st.tabs([
    "Terminal", 
    "Hardware Telemetry", 
    "Sensor Metrics", 
    "System Scan"
])

# ================= TAB 1: TERMINAL =================
with tab1:
    st.markdown("### Terminal")
    st.caption("Direct command line input.")
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter command..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        prompt_lower = prompt.lower()
        if "help" in prompt_lower:
            response = "COMMANDS: STATUS, CONFIGURE, SCAN."
        elif "status" in prompt_lower:
            response = "NODES: 4. POWER: 4.2mW. IDLE."
        elif "configure" in prompt_lower or "setup" in prompt_lower:
            response = "AWAITING TARGET IP."
        elif "scan" in prompt_lower:
            response = "EXECUTE SCAN IN TAB 4."
        else:
            response = "COMMAND RECEIVED."
            
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# ================= TAB 2: TELEMETRY =================
with tab2:
    st.markdown("### Hardware Telemetry")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="ASIC Power", value="4.2 mW", delta="-0.1 mW")
        st.metric(label="CPU Status", value="SLEEP", delta="0W Draw")
        
    with col2:
        st.metric(label="Thermal Core", value="100.2 W", delta="+0.2 W")
        st.metric(label="Battery Level", value="98.5 %", delta="Charging")
        
    with col3:
        st.metric(label="Bus Throughput", value="15.85 GB/s", delta="Active")
        st.metric(label="Hull Pressure", value="16,000 psi", delta="Stable")
        
    st.markdown("---")
    st.markdown("### Sensor Array Power")
    
    chem_toggle = st.toggle("Chemical Array", value=True)
    spin_toggle = st.toggle("X-Ray Array", value=False)
    
    if spin_toggle:
        st.warning("BATTERY DISCHARGE RATE INCREASED.")

# ================= TAB 3: SENSORS =================
with tab3:
    st.markdown("### Sensor Metrics")
    
    st.markdown("#### Navigation Sensors")
    st.code("""
GPS: DENIED
MAGNETIC FIELD: ACQUIRED
COHERENCE: 99.8%
""", language="text")
    
    st.markdown("#### Acoustic Mesh")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Modem Range", "50 km")
    with col2:
        st.metric("Connected Nodes", "5")

# ================= TAB 4: SCAN =================
with tab4:
    st.markdown("### Local System Scan")
    st.caption("Read-only hardware check.")
    
    if st.button("Initiate Scan"):
        st.write("Executing parameter extraction...")
        
        hostname = socket.gethostname()
        os_sys = platform.system()
        os_rel = platform.release()
        cores = os.cpu_count()
        
        layers = [
            ("L1 - Hostname", f"{hostname}"),
            ("L2 - Architecture", f"{os_sys} {os_rel} ({cores} cores)"),
            ("L3 - Ledger", "Not Found."),
            ("L4 - Compliance", "Failed."),
            ("L5 - Vulnerability Status", "Open.")
        ]
        
        progress_bar = st.progress(0)
        
        for i, (name, desc) in enumerate(layers):
            time.sleep(0.4)
            progress_bar.progress((i + 1) / len(layers))
            
            if "Not Found" in desc or "Failed" in desc or "Open" in desc:
                st.error(f"⚠️ **{name}**: {desc}")
            else:
                st.success(f"✅ **{name}**: {desc}")
                
        time.sleep(0.5)
        st.markdown("---")
        st.markdown("### SCAN RESULTS")
        st.error(f"**Target:** {hostname}\n\n**Status:** Non-Compliant.\n\n**Cryptographic execution ledger:** Absent.\n\n**Deterministic rule engine:** Absent.")
        
        if os_sys == "Darwin":
            os_specific_vuln = "Darwin XNU Kernel operates outside verified bounds."
            os_specific_patch = "Inject signed governance kext (Kernel Extension). Apple SIP integration."
        elif os_sys == "Windows":
            os_specific_vuln = "NT Kernel lacks deterministic state verification."
            os_specific_patch = "Deploy Ring-0 governance driver. Zero root takeover."
        else:
            os_specific_vuln = f"{os_sys} lacks deterministic execution bounds."
            os_specific_patch = "Patch target execution bounds. Zero root takeover."

        time.sleep(0.5)
        st.markdown("### EXECUTION GAME PLAN")
        
        col_plan1, col_plan2 = st.columns(2)
        
        with col_plan1:
            st.markdown("#### IDENTIFIED DEFICITS (WHY IT IS REQUIRED)")
            st.markdown(f"- **State Vulnerability:** {os_specific_vuln}")
            st.markdown("- **Audit Failure:** 0 bytes of cryptographic ledger history found.")
            st.markdown("- **Compliance Gap:** No active policy engine detected.")
            
        with col_plan2:
            st.markdown("#### TRI-NOVA DEPLOYMENT (DELIVERABLES)")
            st.markdown(f"- **Injection Protocol:** {os_specific_patch}")
            st.markdown("- **Ledger Integration:** Install 256-bit hashed audit logging.")
            st.markdown("- **Policy Engine:** Bind compliance rules to hardware IO.")
            
        st.info("AWAITING AUTHORIZATION TO EXECUTE INJECTION PROTOCOL.")
