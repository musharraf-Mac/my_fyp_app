import streamlit as st
 
st.set_page_config(
    page_title='FYP Demo',
    page_icon=':brain:',
    layout='wide',          # 'centered' or 'wide'
    initial_sidebar_state='expanded'
)
 
st.title('Welcome to My FYP Application')
st.write('This is my Proof-of-Concept built with Streamlit 1.56.0')

# Title, header, subheader — semantic hierarchy
st.title('Main Title')           # Largest — use once per page
st.header('Section Header')      # Second level
st.subheader('Sub-section')      # Third level
 
# Body text
st.text('Plain monospaced text')
st.write('Smart write — auto-detects type')  # Most versatile
 
# Markdown (full GFM support)
st.markdown('''
## Markdown Section- **Bold** and *italic* text- `inline code` formatting- [Link text](https://streamlit.io)
''')

st.success('Model training completed successfully!')
st.info('Dataset loaded: 10,000 records found.')
st.warning('Missing values detected in 3 columns.')
st.error('ERROR: Model file not found at models/clf.pkl')
 
# Toast notification (appears temporarily — new in 1.32+)
st.toast('Predictions saved!', icon=':white_check_mark:')
 
# Exception display with traceback

def risky_operation():
    # your code here
    return result
try:
    result = risky_operation()
except Exception as e:
    st.exception(e)   # Shows full Python traceback in UI
    
col1, col2, col3, col4 = st.columns(4)
 
col1.metric(label='Accuracy',  value='94.5%', delta='+2.1%')
col2.metric(label='Precision', value='91.2%', delta='-0.8%')
col3.metric(label='Recall',    value='96.3%', delta='+1.5%')
col4.metric(label='F1 Score',  value='93.7%', delta='+0.6%')
 
# delta_color controls arrow colour
# 'normal' = green up / red down (default)
# 'inverse' = red up / green down (for loss metrics)
# 'off'     = no colour change
st.metric('Loss', '0.082', delta='-0.014', delta_color='inverse')

model_params = {
    'algorithm': 'Random Forest',
    'n_estimators': 200,
    'max_depth': 15,
    'accuracy': 0.945,
    'features': ['age', 'income', 'score']
}
 
# Pretty-printed, collapsible JSON tree
st.json(model_params)
 
# Or use write() — auto-detects dict
st.write(model_params)
