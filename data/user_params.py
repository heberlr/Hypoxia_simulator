 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.tumor_radius = FloatText(
          value=250.0,
          step=10,
          style=style, layout=widget_layout)

        param_name2 = Button(description='persitence_timeHip', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.persitence_timeHip = FloatText(
          value=3000.0,
          step=100,
          style=style, layout=widget_layout)

        param_name3 = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.uptake_rate = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='rate_KnToKp', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.rate_KnToKp = FloatText(
          value=0.00363,
          step=0.001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='rate_KpToKn', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.rate_KpToKn = FloatText(
          value=0.00107,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name6 = Button(description='sigmaS', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.sigmaS = FloatText(
          value=38.0,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='sigmaT', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.sigmaT = FloatText(
          value=6.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='speed_red', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.speed_red = FloatText(
          value=0.2938,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='perst_time_red', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.perst_time_red = FloatText(
          value=15.0,
          step=1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='bias_red', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.bias_red = FloatText(
          value=0.1719,
          step=0.01,
          style=style, layout=widget_layout)

        param_name11 = Button(description='speed_green', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.speed_green = FloatText(
          value=0.4755,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='perst_time_green', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.perst_time_green = FloatText(
          value=15.0,
          step=1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='bias_green', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.bias_green = FloatText(
          value=0.1791,
          step=0.01,
          style=style, layout=widget_layout)

        param_name14 = Button(description='fracResponse_green', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.fracResponse_green = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='bias_greenResp', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.bias_greenResp = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='model_stochastic', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.model_stochastic = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        units_button1 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'

        row1 = [param_name1, self.tumor_radius, units_button1, desc_button1] 
        row2 = [param_name2, self.persitence_timeHip, units_button2, desc_button2] 
        row3 = [param_name3, self.uptake_rate, units_button3, desc_button3] 
        row4 = [param_name4, self.rate_KnToKp, units_button4, desc_button4] 
        row5 = [param_name5, self.rate_KpToKn, units_button5, desc_button5] 
        row6 = [param_name6, self.sigmaS, units_button6, desc_button6] 
        row7 = [param_name7, self.sigmaT, units_button7, desc_button7] 
        row8 = [param_name8, self.speed_red, units_button8, desc_button8] 
        row9 = [param_name9, self.perst_time_red, units_button9, desc_button9] 
        row10 = [param_name10, self.bias_red, units_button10, desc_button10] 
        row11 = [param_name11, self.speed_green, units_button11, desc_button11] 
        row12 = [param_name12, self.perst_time_green, units_button12, desc_button12] 
        row13 = [param_name13, self.bias_green, units_button13, desc_button13] 
        row14 = [param_name14, self.fracResponse_green, units_button14, desc_button14] 
        row15 = [param_name15, self.bias_greenResp, units_button15, desc_button15] 
        row16 = [param_name16, self.model_stochastic, units_button16, desc_button16] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.persitence_timeHip.value = float(uep.find('.//persitence_timeHip').text)
        self.uptake_rate.value = float(uep.find('.//uptake_rate').text)
        self.rate_KnToKp.value = float(uep.find('.//rate_KnToKp').text)
        self.rate_KpToKn.value = float(uep.find('.//rate_KpToKn').text)
        self.sigmaS.value = float(uep.find('.//sigmaS').text)
        self.sigmaT.value = float(uep.find('.//sigmaT').text)
        self.speed_red.value = float(uep.find('.//speed_red').text)
        self.perst_time_red.value = float(uep.find('.//perst_time_red').text)
        self.bias_red.value = float(uep.find('.//bias_red').text)
        self.speed_green.value = float(uep.find('.//speed_green').text)
        self.perst_time_green.value = float(uep.find('.//perst_time_green').text)
        self.bias_green.value = float(uep.find('.//bias_green').text)
        self.fracResponse_green.value = float(uep.find('.//fracResponse_green').text)
        self.bias_greenResp.value = float(uep.find('.//bias_greenResp').text)
        self.model_stochastic.value = ('true' == (uep.find('.//model_stochastic').text.lower()) )


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//persitence_timeHip').text = str(self.persitence_timeHip.value)
        uep.find('.//uptake_rate').text = str(self.uptake_rate.value)
        uep.find('.//rate_KnToKp').text = str(self.rate_KnToKp.value)
        uep.find('.//rate_KpToKn').text = str(self.rate_KpToKn.value)
        uep.find('.//sigmaS').text = str(self.sigmaS.value)
        uep.find('.//sigmaT').text = str(self.sigmaT.value)
        uep.find('.//speed_red').text = str(self.speed_red.value)
        uep.find('.//perst_time_red').text = str(self.perst_time_red.value)
        uep.find('.//bias_red').text = str(self.bias_red.value)
        uep.find('.//speed_green').text = str(self.speed_green.value)
        uep.find('.//perst_time_green').text = str(self.perst_time_green.value)
        uep.find('.//bias_green').text = str(self.bias_green.value)
        uep.find('.//fracResponse_green').text = str(self.fracResponse_green.value)
        uep.find('.//bias_greenResp').text = str(self.bias_greenResp.value)
        uep.find('.//model_stochastic').text = str(self.model_stochastic.value)
