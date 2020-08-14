 
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

        param_name1 = Button(description='persitence_timeHip', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.persitence_timeHip = FloatText(
          value=3000.0,
          step=100,
          style=style, layout=widget_layout)

        param_name2 = Button(description='fracResponse_green', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.fracResponse_green = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='bias_greenResp', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.bias_greenResp = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='hypoxyprobe', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.hypoxyprobe = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name5 = Button(description='sigma_Hp', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.sigma_Hp = FloatText(
          value=7.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='speed_red', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.speed_red = FloatText(
          value=0.2938,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='perst_time_red', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.perst_time_red = FloatText(
          value=15.0,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='bias_red', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.bias_red = FloatText(
          value=0.1719,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='speed_green', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.speed_green = FloatText(
          value=0.4755,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='perst_time_green', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.perst_time_green = FloatText(
          value=15.0,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='bias_green', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.bias_green = FloatText(
          value=0.1791,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.tumor_radius = FloatText(
          value=250.0,
          step=10,
          style=style, layout=widget_layout)

        param_name13 = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.uptake_rate = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='rate_KnToKp', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.rate_KnToKp = FloatText(
          value=0.00363,
          step=0.001,
          style=style, layout=widget_layout)

        param_name15 = Button(description='rate_KpToKn', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.rate_KpToKn = FloatText(
          value=0.00107,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name16 = Button(description='sigma_S', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.sigma_S = FloatText(
          value=38.0,
          step=1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='sigma_T', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.sigma_T = FloatText(
          value=6.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='sigma_H', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.sigma_H = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='production_rate', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.production_rate = FloatText(
          value=4.8e-4,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name20 = Button(description='degradation_rate', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.degradation_rate = FloatText(
          value=6.8e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        units_button1 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'

        desc_button1 = Button(description='phenotype persistence time of GFP+ cells' , tooltip='phenotype persistence time of GFP+ cells', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='fraction of GFP+ cells with different motility bias (bias_greenResp)' , tooltip='fraction of GFP+ cells with different motility bias (bias_greenResp)', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='motility bias for GFP + cells (for fracResponse_green)' , tooltip='motility bias for GFP + cells (for fracResponse_green)', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='mark with hypoxyprobe' , tooltip='mark with hypoxyprobe', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='oxygen pressure threshold to mark hypoxyprobe (> sigma_T and < sigma_H)' , tooltip='oxygen pressure threshold to mark hypoxyprobe (> sigma_T and < sigma_H)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='motility speed for DsRed+ cells' , tooltip='motility speed for DsRed+ cells', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='motility persistence time for DsRed+ cells' , tooltip='motility persistence time for DsRed+ cells', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='motility bias for DsRed+ cells' , tooltip='motility bias for DsRed+ cells', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='motility speed for GFP+ cells' , tooltip='motility speed for GFP+ cells', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='motility persistence time for GFP+ cells' , tooltip='motility persistence time for GFP+ cells', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='motility bias for GFP+ cells' , tooltip='motility bias for GFP+ cells', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='initial tumor radius' , tooltip='initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='uptake rates for the oxygen' , tooltip='uptake rates for the oxygen', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='transition rate from Ki67- to Ki67+ (for saturated signal)' , tooltip='transition rate from Ki67- to Ki67+ (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='transition rate from Ki67+ to Ki67-' , tooltip='transition rate from Ki67+ to Ki67-', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='oxygen pressure threshold to signal proliferation saturation' , tooltip='oxygen pressure threshold to signal proliferation saturation', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='min oxygen pressure to signal proliferation' , tooltip='min oxygen pressure to signal proliferation', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='oxygen pressure threshold to signal hypoxia' , tooltip='oxygen pressure threshold to signal hypoxia', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='protein production rate' , tooltip='protein production rate', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='protein degradation rate' , tooltip='protein degradation rate', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'

        row1 = [param_name1, self.persitence_timeHip, units_button1, desc_button1] 
        row2 = [param_name2, self.fracResponse_green, units_button2, desc_button2] 
        row3 = [param_name3, self.bias_greenResp, units_button3, desc_button3] 
        row4 = [param_name4, self.hypoxyprobe, units_button4, desc_button4] 
        row5 = [param_name5, self.sigma_Hp, units_button5, desc_button5] 
        row6 = [param_name6, self.speed_red, units_button6, desc_button6] 
        row7 = [param_name7, self.perst_time_red, units_button7, desc_button7] 
        row8 = [param_name8, self.bias_red, units_button8, desc_button8] 
        row9 = [param_name9, self.speed_green, units_button9, desc_button9] 
        row10 = [param_name10, self.perst_time_green, units_button10, desc_button10] 
        row11 = [param_name11, self.bias_green, units_button11, desc_button11] 
        row12 = [param_name12, self.tumor_radius, units_button12, desc_button12] 
        row13 = [param_name13, self.uptake_rate, units_button13, desc_button13] 
        row14 = [param_name14, self.rate_KnToKp, units_button14, desc_button14] 
        row15 = [param_name15, self.rate_KpToKn, units_button15, desc_button15] 
        row16 = [param_name16, self.sigma_S, units_button16, desc_button16] 
        row17 = [param_name17, self.sigma_T, units_button17, desc_button17] 
        row18 = [param_name18, self.sigma_H, units_button18, desc_button18] 
        row19 = [param_name19, self.production_rate, units_button19, desc_button19] 
        row20 = [param_name20, self.degradation_rate, units_button20, desc_button20] 

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
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)

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
          box17,
          box18,
          box19,
          box20,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.persitence_timeHip.value = float(uep.find('.//persitence_timeHip').text)
        self.fracResponse_green.value = float(uep.find('.//fracResponse_green').text)
        self.bias_greenResp.value = float(uep.find('.//bias_greenResp').text)
        self.hypoxyprobe.value = ('true' == (uep.find('.//hypoxyprobe').text.lower()) )
        self.sigma_Hp.value = float(uep.find('.//sigma_Hp').text)
        self.speed_red.value = float(uep.find('.//speed_red').text)
        self.perst_time_red.value = float(uep.find('.//perst_time_red').text)
        self.bias_red.value = float(uep.find('.//bias_red').text)
        self.speed_green.value = float(uep.find('.//speed_green').text)
        self.perst_time_green.value = float(uep.find('.//perst_time_green').text)
        self.bias_green.value = float(uep.find('.//bias_green').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.uptake_rate.value = float(uep.find('.//uptake_rate').text)
        self.rate_KnToKp.value = float(uep.find('.//rate_KnToKp').text)
        self.rate_KpToKn.value = float(uep.find('.//rate_KpToKn').text)
        self.sigma_S.value = float(uep.find('.//sigma_S').text)
        self.sigma_T.value = float(uep.find('.//sigma_T').text)
        self.sigma_H.value = float(uep.find('.//sigma_H').text)
        self.production_rate.value = float(uep.find('.//production_rate').text)
        self.degradation_rate.value = float(uep.find('.//degradation_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//persitence_timeHip').text = str(self.persitence_timeHip.value)
        uep.find('.//fracResponse_green').text = str(self.fracResponse_green.value)
        uep.find('.//bias_greenResp').text = str(self.bias_greenResp.value)
        uep.find('.//hypoxyprobe').text = str(self.hypoxyprobe.value)
        uep.find('.//sigma_Hp').text = str(self.sigma_Hp.value)
        uep.find('.//speed_red').text = str(self.speed_red.value)
        uep.find('.//perst_time_red').text = str(self.perst_time_red.value)
        uep.find('.//bias_red').text = str(self.bias_red.value)
        uep.find('.//speed_green').text = str(self.speed_green.value)
        uep.find('.//perst_time_green').text = str(self.perst_time_green.value)
        uep.find('.//bias_green').text = str(self.bias_green.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//uptake_rate').text = str(self.uptake_rate.value)
        uep.find('.//rate_KnToKp').text = str(self.rate_KnToKp.value)
        uep.find('.//rate_KpToKn').text = str(self.rate_KpToKn.value)
        uep.find('.//sigma_S').text = str(self.sigma_S.value)
        uep.find('.//sigma_T').text = str(self.sigma_T.value)
        uep.find('.//sigma_H').text = str(self.sigma_H.value)
        uep.find('.//production_rate').text = str(self.production_rate.value)
        uep.find('.//degradation_rate').text = str(self.degradation_rate.value)
