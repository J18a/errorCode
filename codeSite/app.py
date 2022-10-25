
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Honeytree Code Search",
                   page_icon=":wrench:", layout='wide')
col1, col2 = st.columns([2, 1])

with col1:
    st.title(body='Honeytree Appliance Repair Diagnostic Site',)
    with st.container():
        st.header('**Recently Updated**')
        st.write('**_10/24/22_** - Ive organized it out a little ')

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
lgDw = {
    'AE': 'LEAKAGE ERROR',
    'CL': 'CHILD LOCK',
    'CD': 'COOL DOWN, USUALLY MEANS THE DISHWAHER IS DONE',
    'FE': 'FILL ERROR',
    'HE': 'HEAT ERROR',
    'IE': 'INLET ERROR',
    'LE': 'LOCK ERROR',
    'OE': 'OUTLET ERROR',
    'PF': 'POWER FAILURE',
    'DE': 'DOOR ERROR',
    'TE': 'THERMISTOR ERROR'

}
kadw = {
    '1-1': 'PILOT STUCK ON',
    '1-2': 'CONTROL SOFTWARE ISSUE',
    '2-2': 'NO RESPONSE FROM UI',
    '3-1': 'THERMISTOR OPEN',
    '3-2': 'THERMISTOR SHORTED',
    '3-3': 'FAILED CALIBRATION',
    '4-3': 'MOTOR NOT RUNNING',
    '5-1': 'DOOR STUCK OPEN',
    '5-2': 'DOOR STUCK CLOSED',
    '6-1': 'LOW/NO WATER',
    '6-2': 'FILL VALVE PROBLEM',
    '6-3': 'SUDS/AIR IN PUMP',
    '6-4': 'FLOAT SWITCH OPEN',
    '7-1': 'NO HEAT',
    '7-2': 'HEATER STUCK ON',
    '8-2': 'DRAIN MOTOR PROBLEM',
    '8-3': 'DRAIN STUCK ON',
    '9-1': 'CANT FIND POSITION',
    '9-2': 'STUCK ON',
    '9-3': 'DISC MISSING',
    '10-1': 'DISPENSER ELECTRICAL PROBLEM',
    '10-3': 'DRYING FAN ERROR'





}

choice = st.radio(
    'Please Select Brand or Issue', ('', 'LG', 'Whirlpool', 'Sealed System Issue', 'More Coming Soon'),)
if choice == '':
    st.stop()

if choice == 'More Coming Soon':
    st.header('Stay Tuned!!')
    st.stop()

if choice == 'Sealed System Issue':
    with st.container():
        lowSide = st.number_input('Enter Low side pressure', step=1)
        highSide = st.number_input('Enter High side pressure', step=1)
        submit = st.button('Submit Pressures')
        if submit:
            if highSide < 90 and lowSide < -2:
                st.write('You have a **High Side** leak')
            if -2 <= lowSide <= 5 and 90 <= highSide <= 120:
                st.write('These are only normal **IF** the evap is cold')
            if highSide > 125 and lowSide < 0:
                st.write('You have a **low side** leak')
            else:
                st.write('Call Tech Line')
        st.stop()

if choice == 'LG':
    with st.container():
        dw, washer = st.tabs(['Dishwasher', 'Washer'])
        with dw:
            a = st.text_input('Enter Dishwasher Code')
            button = st.button('Search Dishwasher Code')
            if button == True:
                if a.upper() in lgDw:
                    st.write(lgDw[a.upper()])
                else:
                    st.write('Code not found.')
        with washer:
            b = st.text_input('Enter Front Load Code')
            button = st.button('Search Washer Code')
            if button == True:
                if b.upper() in lgError:
                    st.write(lgError[b.upper()])
                else:
                    st.write('Code not found.')

if choice == 'Whirlpool':
    with st.container():
        dw, tWasher, fWasher = st.tabs(
            ['Dishwasher', 'Top Load Washer', 'Front Load Washer'])

        with dw:
            c = st.text_input('Enter Dishwasher Code')
            st.info('Enter code like this 4-3', icon="ℹ️")
            button = st.button('Search Dishwasher Code')
            if button == True:
                if c.upper() in kadw:
                    st.write(kadw[c.upper()])
                else:
                    st.write('Code not found.')

        with tWasher:
            d = st.text_input('Enter Top Load Code',)
            button = st.button('Search Washer Code')
            if button == True:
                if d.upper() in topLoad:
                    st.write(topLoad[d.upper()])
                else:
                    st.write('Code not found.')

        with fWasher:
            e = st.text_input('Enter Front Load Code')
            button = st.button('Search Front Load Washer Code')
            if button == True:
                if e.upper() in front_load:
                    st.write(front_load[e.upper()])
                else:
                    st.write('Code not found.')
