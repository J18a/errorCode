import streamlit as st
from PIL import Image

st.set_page_config(page_title="Honeytree Code Search",
                   page_icon=":wrench:", layout='wide')
col1, col2 = st.columns([2, 1])

with col1:
    st.title(body='Honeytree Appliance Repair')
    st.header('Error Code Search')

    st.write('For now this is only good for **Whirlpool Washers**.')
    st.write('Its still a work in progress but you get the basics.')
with col2:
    st.image("C:\\Users\\Honey\\Downloads\\honeytree logos\\Png\\Honeytreesolutions Logo_Dark BCGD-Mark.png")
st.write('---')


topLoad = {
    'F0E2': 'Oversuds',
    'F0E3': 'Overload',
    'F0E4': 'Spin Limited By Water Temperature',
    'F0E5': 'Off Balance Load',
    'F1E1': 'Main Control Fault',
    'F1E2': 'Main Control Fault',
    'F2E1': 'UI Stuck Button',
    'F2E3': 'UI Mismatch',
    'F2E4': 'UI Software Error: Incompatible Parameter File',
    'F2E5': 'UI Software Error: Parameter Memory Invalid',
    'F3E1': 'Pressure System Fault',
    'F3E2': 'Inlet Water Temperature Fault',
    'F4E1': 'Heater Stuck On',
    'F4E2': 'Heater Not Turning On',
    'F5E1': 'Lid Switch Fault – Lid Is Up',
    'F5E2': 'Lid Lock Will Not Lock Or Lid Lock Failure',
    'F5E3': 'Lid Lock Will Not Unlock',
    'F5E4': 'Lid Not Opened Between Cycles',
    'F6E2': 'Communication Error: UI Cannot Hear ACU',
    'F6E3': 'Communication Error: ACU Cannot Hear UI',
    'F7E0': 'Loss of Power',
    'F7E1': 'Loss of Power During Spin',
    'F7E2': 'Motor Drive Module Over Temp',
    'F7E3': 'Motor Drive Module Over Current',
    'F7E4': 'Motor Drive Module Over Voltage',
    'F7E5': 'Shifter Failure',
    'F7E6': 'Motor Circuit Loss of Phase',
    'F7E7': 'Motor Start Failure',
    'F7E8': 'Motor Stator Over Temperature',
    'F7E9': 'Locked Rotor',
    'LF': 'Long Fill',
    'F8E1': 'Long Fill',
    'F8E3': 'Overflow Or Flood Condition',
    'F8E6': 'Water Hazard',
    'F9E1': 'Drain Pump System Problem – Long Drain',
    'drn': 'Drain Pump System Problem – Long Drain',
    'dr': 'Drain Pump System Problem – Long Drain',
}
front_load = {
    'F1E1':
    'ACU ERROR',
    'F1E2':
    'MOTOR CONTROL ERROR',
    'F2E3':
    'UNSUPPORTED CYCLE',
    'F3E1':
    'WATER LEVEL SYSTEM ERROR',
    'F3E2':
    'TEMPERATURE SYSTEM ERROR',
    'F4E0':
    'HEATER IS NOT DETECTED',
    'F5E1':
    'DOOR SWITCH ERROR',
    'F5E2':
    'DOOR LOCK ERROR',
    'F5E3':
    'DOOR UNLOCK ERROR',
    'F5E4':
    'DOOR NOT OPENED BETWEEN CYCLES',
    'F6E2':
    'COMMUNICATION ERROR UI TO ACU',
    'F6E3':
    'COMMUNICATION ERROR ACU TO UI',
    'F7E2':
    'MOTOR DRIVE CIRCUIT OVER TEMPERATURE',
    'F7E8':
    'MOTOR OVER TEMPERATURE',
    'F8E0':
    'STEAM INLET VALVE ERROR',
    'F8E1':
    'NO WATER DETECTED ENTERING WASHER OR WATER LEVEL SENSOR TRIP NOT DETECTED',
    'F8E3':
    'OVERFLOW CONDITION',
    'F9E1':
    'LONG DRAIN',
}
lgError = {
    'IE': 'WATER INLET ERROR',
    'UE': 'UNBALANCE ERROR',
    'OE': 'DRAIN ERROR',
    'FE': 'OVERFLOW ERROR',
    'PE': 'PRESSURE SENSOR ERROR',
    'DE1': 'DOOR OPEN ERROR',
    'DE2': 'DOOR OPEN ERROR',
    'TE': 'HEATING ERROR',
    'LE': 'LOCKED MOTOR ERROR',
    'EE': 'EEPROM ERROR',
    'PF': 'POWER FAILURE',
    'SUD': 'SUDS ERROR'
}


choice = st.selectbox(
    'Select Brand', ('LG', 'Whirlpool', 'More Coming Soon'))

tab1, tab2, tab3, tab4 = st.tabs(
    ['Front Load Washers', 'Top Load Washers', 'Refrigerator', 'Stoves'])

with tab1:

    if choice == 'Whirlpool':
        c = st.text_input('Enter Front Load Code')
        submit = st.button('Search')
        if submit:
            if c.upper() in front_load:
                st.write(front_load[c.upper()])
            else:
                st.write('Code not found.')
    if choice == 'LG':
        e = st.text_input('Enter Front Load Code')
        submit = st.button('Search Code')
        if submit:
            if e.upper() in lgError:
                st.write(lgError[e.upper()])
            else:
                st.write('Code not found.')


with tab2:
    if choice == 'Whirlpool':
        d = st.text_input('Enter Top Load Code',)
        submit = st.button('Search Codes')
        if submit:
            if d.upper() in topLoad:
                st.write(topLoad[d.upper()])
            else:
                st.write('Code not found.')
    if choice == 'LG':
        f = st.text_input('Enter Top Load Code')
        submit = st.button('Search')
        if submit:
            if f.upper() in lgError:
                st.write(lgError[f.upper()])
            else:
                st.write('Code not found.')

with tab3:
    st.header('Coming Soon!!')

with tab4:
    st.header('Coming Soon!!')
