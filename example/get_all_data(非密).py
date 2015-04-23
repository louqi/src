'''
Created on 2014-10-20

@author: YangJunwei
'''
import re
import string

class get_all_data:
    
    def __init__(self,file_name):
        self.file_name = file_name
    
    def _read_file(self, path):
        '''read the file,return full text in it
        '''
        fp = open(path)
        try:
            return fp.read()
        except IOError:
            print "%s doesn't exist!" % path
            exit()
        finally:
            fp.close()
                      
    def _get_case_num(self, all_data):
        '''get number of cases
        '''
        pattern =re.compile(r'NUMBER\s+OF\s+CASES,\s+NCASES\s+=\s+\d+')
        case_num = pattern.search(all_data)
        if case_num:
            pattern = re.compile(r'\d+')
            num = pattern.findall(case_num.group())
            if num:
                return num
            else:
                return ['0']
        else:
            return ['0']
        
    def _get_case_context(self, all_data):
        '''get the number of case and the whole context of every case
        '''
        pattern = re.compile(r'SHELL\s+INPUT,\s+CASE\s+NUMBER\s+\d+\s*\n[\w\W]*?END\s+OF\s+CASE\s+NUMBER')
        case_context = pattern.findall(all_data)
        return len(case_context), case_context
    
    def _get_every_case_context(self, case_context):
        '''get the idiographic of every element in every case
        '''
        case_context_dic = {}
        flight_condition = self._get_flight_conditions(case_context)
        if flight_condition != '-':
            case_context_dic['flight_condition'] = flight_condition
        dynamic_character = self._get_dynamic_character(case_context)
        if dynamic_character != '-':
            case_context_dic['dynamic_character'] = dynamic_character
        performance = self._get_performance(case_context)
        if performance != '-':
            case_context_dic['performance'] = performance
        airoperate_load = self._get_airoperated_load(case_context)
        if airoperate_load != '-':
            case_context_dic['aerodynamic_load'] = airoperate_load
        rotor_wake = self._get_rotor_wake(case_context)
        if rotor_wake != '-':
            case_context_dic['rotor_wake'] = rotor_wake
        structrue_load = self._get_structrue_load(case_context)
        if structrue_load != '-':
            case_context_dic['structrue_load'] = structrue_load
        return case_context_dic
        
        
        
 
 
            
    def _get_flight_conditions(self, case_data):
        '''get nine flight conditions of case data
        '''
        pattern = re.compile(r'ROTORCRAFT PERFORMANCE\n[\w\W]*?AERODYNAMIC CONTROLS')
        all_conditions = pattern.findall(case_data)
        if len(all_conditions)>0:
            for condition in all_conditions:
                return self._get_every_condition(condition)
        else:
            return '-'
            
    def _get_every_condition(self, flight_conditions):
        '''get dictionary of flight conditions
        '''
        flight_list = []
        pattern_con = re.compile(r'CONFIGURATION(\s+\w+){4}')
        configuration_list = []
        is_match = 0
        temp_list = []
        for configuration in pattern_con.finditer(flight_conditions):
            is_match = 1
            for value in configuration.group().split('\n'):
                value = value.strip()
                configuration_list.append(value)
        if is_match == 1:
            del configuration_list[0]
            if len(configuration_list) > 2:
                for i in range(2, len(configuration_list)):
                    #the number of element in configuration_list reduce one when delete the element, 
                    #length of configuration_list reduce one, so del 2 every time
                    del configuration_list[2]
            temp_list.append('CONFIGURATION')
            temp_list.append(configuration_list)
            flight_list.append(temp_list)
        
        pattern = re.compile(r'VELOCITY \(\w*/?\w*\)\s+=\s+.?\d+.?\d*')
        velocity = pattern.findall(flight_conditions)
        if velocity:
            vel_value = velocity[0].split('=')
            #flight_dic[vel_value[0].strip()] = vel_value[1].strip()
            temp_list = []
            for i in range(len(vel_value)):
                temp_list.append(vel_value[i].strip())
            flight_list.append(temp_list)
        
        pattern1 = re.compile(r'YAW ANGLE \(DEG\)\s+=\s+.?\d+.?\d*')
        yaw = pattern1.findall(flight_conditions)
        if yaw:
            yaw_value = yaw[0].split('=')
            temp_list = []
            for i in range(len(yaw_value)):
                temp_list.append(yaw_value[i].strip())
            flight_list.append(temp_list)
        
        pattern2 = re.compile(r'PITCH ANGLE \(DEG\)\s+=\s+.?\d+.?\d*')
        pitch = pattern2.findall(flight_conditions)
        if pitch:
            pitch_value = pitch[0].split('=')
            temp_list = []
            for i in range(len(pitch_value)):
                temp_list.append(pitch_value[i].strip())
            flight_list.append(temp_list)
        
        pattern3 = re.compile(r'ROLL ANGLE \(DEG\)\s+=\s+.?\d+.?\d*')
        roll = pattern3.findall(flight_conditions)
        if roll:
            roll_value = roll[0].split('=')
            temp_list = []
            for i in range(len(roll_value)):
                temp_list.append(roll_value[i].strip())
            flight_list.append(temp_list)
        
        pattern4 = re.compile(r'ROTATIONAL SPEED \(RPM\)\s+=\s+.?\d+.?\d*')
        rotational = pattern4.findall(flight_conditions)
        if rotational:
            rotational_value = rotational[0].split('=')
            temp_list = []
            for i in range(len(rotational_value)):
                temp_list.append(rotational_value[i].strip())
            flight_list.append(temp_list)
            
        pattern5 = re.compile(r'COLLECTIVE\s+=\s+.?\d+.?\d*')
        collective = pattern5.findall(flight_conditions)
        if collective:
            collective_value = collective[0].split('=')
            temp_list = []
            for i in range(len(collective_value)):
                temp_list.append(collective_value[i].strip())
            flight_list.append(temp_list)
            
        pattern6 = re.compile(r'LATERAL CYCLIC\s+=\s+.?\d+.?\d*')
        lateral = pattern6.findall(flight_conditions)
        if lateral:  
            lateral_value = lateral[0].split('=')
            temp_list = []
            for i in range(len(lateral_value)):
                temp_list.append(lateral_value[i].strip())
            flight_list.append(temp_list)
      
        pattern7 = re.compile(r'LONGITUDINAL CYCLIC\s+=\s+.?\d+.?\d*')
        longitudinale = pattern7.findall(flight_conditions)
        if longitudinale:  
            longitudinale_value = longitudinale[0].split('=')
            temp_list = []
            for i in range(len(longitudinale_value)):
                temp_list.append(longitudinale_value[i].strip())
            flight_list.append(temp_list)
        
        return flight_list
            


      
    def _get_dynamic_character(self, case_data):
        '''get all data of the paddle structure dynamic chatacter
        '''
        dynamic_character_dic = {}
        pattern = re.compile(r'FLUTTER LOOP ITERATION AND PART SOLUTION\s+[\w+\W+]+DESCRIPTION OF VARIABLES')
        all_character = pattern.findall(case_data)
        if len(all_character) > 0:
            for character in all_character:
                rate = self._get_rate(character)
                dynamic_character_dic['modal_frequency'] = rate
                vibration = self._get_vibration_mode(character)
                dynamic_character_dic['mode_shape'] = vibration
                return dynamic_character_dic
        else:
            return '-'
        
    def _get_rate(self, character_data):
        '''get rate of model
        '''
        rate_list = []
        pattern = re.compile(r'LABEL[\s+\S+]+AXIAL$', re.M)
        for number_data in pattern.finditer(character_data):
            number_temp_list = []
            for element in number_data.group().split(' '):
                filter0 = re.match(r'.+', element)
                if filter0:
                    number_temp_list.append(filter0.group())
        header_list = []
        header_list.append(number_temp_list[0])
        header_list.append(number_temp_list[2]+' '+number_temp_list[3])
        header_list.append(number_temp_list[4])
        header_list.append(number_temp_list[5])
        header_list.append('MASTER MODEL')
        rate_list.append(header_list)
        pattern_num = re.compile(r'M\d+E\d+\s+DYNAMIC\s+[\d+-?.?\d+E?-?\d*\s+]+$', re.M)
        for dynamic in pattern_num.finditer(character_data):
            dynamic_list = []
            for element in dynamic.group().split(' '):
                filter1 = re.match(r'-?.?\d+.?\d+', element)
                if filter1:
                    dynamic_list.append(filter1.group())
            length = len(dynamic_list)
            for i in range(length-4, length):
                if dynamic_list[i] == '1.000':
                    dynamic_list.append(number_temp_list[len(number_temp_list)-(length - i)])
            for i in range(6):
                del dynamic_list[4]
            rate_list.append(dynamic_list)        
        rate_transposition_list = rate_list
        return rate_transposition_list

    def _get_vibration_mode(self, vibration_data):
        '''get the list of wield, shimmy, torsion and stretch in dynamic chatacter
        '''
        vibration_mode_dic = {}
        pattern = re.compile(r'OUT-OF-PLANE COMPONENT OF MODE SHAPE\s+[\w+\W+]+?IN-PLANE COMPONENT OF MODE')
        wield_data = pattern.findall(vibration_data)
        if len(wield_data) > 0:
            for wield in wield_data:
                wield_list = self._get_vibration_mode_list(r'MODE\s+LABEL\s+[M\d+E\d+\s+]+', r'MODE\s+(\S+)\s+(FLAP|LAG)([\w\W]+?$)', wield)
                vibration_mode_dic['FLAP'] = wield_list
                
        pattern1 = re.compile(r'IN-PLANE COMPONENT OF MODE SHAPE\s+[\w+\W+]+?PITCH/TORSION COMPONENT')
        shimmy_data = pattern1.findall(vibration_data)
        if len(shimmy_data) > 0:
            for shimmy in shimmy_data:
                shimmy_list = self._get_vibration_mode_list(r'MODE LABEL\s+[M\d+E\d+\s+]+$', r'MODE +(\S+) +(FLAP|LAG)([\w\W]+?$)', shimmy)
                vibration_mode_dic['LAG'] = shimmy_list
                
        pattern2 = re.compile(r'PITCH/TORSION COMPONENT OF MODE SHAPE\s+[\w+\W+]+?AXIAL COMPONENT OF MODE')
        torsion_data = pattern2.findall(vibration_data)
        if len(torsion_data) > 0:
            for torsion in torsion_data:
                torsion_list = self._get_vibration_mode_list(r'MODE LABEL\s+[M\d+E\d+\s+]+$', r'MODE +(\S+) +(LINK|PITCH)([\w\W]+?$)', torsion)
                vibration_mode_dic['PITCH'] = torsion_list
                
        pattern3 = re.compile(r'AXIAL COMPONENT OF MODE SHAPE\s+[\w+\W+]+?DESCRIPTION OF VARIABLES')
        stretch_data = pattern3.findall(vibration_data)
        if len(stretch_data) > 0:
            for stretch in stretch_data:
                stretch_list = self._get_vibration_mode_list(r'MODE LABEL\s+[M\d+E\d+\s+]+$', r'MODE +(\S+) +(AXIAL)([\w\W]+?$)', stretch)
                vibration_mode_dic['AXIAL'] = stretch_list
        return vibration_mode_dic 
                
    def _get_vibration_mode_list(self, regular1, regular2, data):
        '''get common data in dynamic data
        '''
        pattern = re.compile(regular1, re.M)
        dynamic_list = []
        dynamic_temp_list = []
        for mode_label in pattern.finditer(data):
            for element in mode_label.group().split('  '):
                filter1 = re.match(r'\w+\s?\w*', element.strip())
                if filter1:
                    dynamic_temp_list.append(filter1.group())
            if 'A' in dynamic_temp_list:
                dynamic_temp_list.pop(dynamic_temp_list.index('A')+1)
            dynamic_temp_list.append('A')
        dynamic_filter_temp_list = []
        flag = 0
        for element in dynamic_temp_list:
            if element != 'A':
                dynamic_filter_temp_list.append(element)
            else:
                flag = flag + 1
        dynamic_list.append(dynamic_filter_temp_list)
               
        pattern1 = re.compile(regular2, re.M)
        dynamic_merge_list = []
        for dynamic_data in pattern1.finditer(data):
            dynamic_temp_data = []
            for element in dynamic_data.group().split(' '):
                filter2 = re.match(r'-?\d*\.?\d+R?|JOINT', element)
                if filter2:
                    dynamic_temp_data.append(filter2.group())
            dynamic_merge_list.append(dynamic_temp_data)
        for i in range(len(dynamic_merge_list)/flag):
            dynamic_temp_list = []
            for j in range(flag):
                temp_len = len(dynamic_merge_list)/flag*j+i
                for k in range(len(dynamic_merge_list[temp_len])):
                    if k != 0 or temp_len/(len(dynamic_merge_list)/flag) == 0:
                        dynamic_temp_list.append(dynamic_merge_list[temp_len][k])
            dynamic_list.append(dynamic_temp_list)
        return dynamic_list
     
     
     

    def _get_performance(self, case_data):
        '''get nine performance of case data 
        '''
        pattern = re.compile(r'ROTOR FORCES AND MOMENTS\n[\w\W]*?PERFORMANCE INDICES')
        performance_data = pattern.findall(case_data)
        if len(performance_data) > 0:
            for performance in performance_data:
                return self._get_performance_dic(performance)
        else:
            return '-'
                
    def _get_performance_dic(self, performance):
        '''get dictionary of every performance
        '''
        performance_dic = {}
        performance_dic['THRUST'] = self._get_subperformance('CT\s*=\s+-?\d*.\d*', '\sT\s*=\s+-?\d*.\d*', performance)
        performance_dic['DRAG FORCE'] = self._get_subperformance('CH\s*=\s+-?\d*.\d*', '\sH\s*=\s+-?\d*.\d*', performance)
        performance_dic['SIDE FORCE'] = self._get_subperformance('CY\s*=\s+-?\d*.\d*', '\sY\s*=\s+-?\d*.\d*', performance)
        performance_dic['ROLL MOMENT'] = self._get_subperformance('CMX\s*=\s+-?\d*.\d*', '\sMX\s*=\s+-?\d*.\d*', performance)
        performance_dic['PITCH MOMENT'] = self._get_subperformance('CMY\s*=\s+-?\d*.\d*', '\sMY\s*=\s+-?\d*.\d*', performance)
        performance_dic['YAW MOMENT'] = self._get_subperformance('CMZ\s*=\s+-?\d*.\d*', '\sMZ\s*=\s+-?\d*.\d*', performance)
        performance_dic['LIFT'] = self._get_subperformance('CL\s*=\s+-?\d*.\d*', '\sL\s*=\s+-?\d*.\d*', performance)
        performance_dic['DRAG'] = self._get_subperformance('CX\s*=\s+-?\d*.\d*', '\sX\s*=\s+-?\d*.\d*', performance)
        performance_dic['ROTOR POWER'] = self._get_subperformance(r'CP\s*=\s+-?\d*.\d*', r'\sP\s*=\s+-?\d*.\d*', performance)
        return performance_dic
        
    def _get_subperformance(self, frist_reguler, second_reguler, performance):
        '''get sub data dictionary of performance
        '''
        thrust_lsit = []
        pattern = re.compile(frist_reguler)
        thrust_ct = pattern.findall(performance)
        if thrust_ct:
            thrust_value = thrust_ct[0].split('=')
            temp_list = []
            for i in range(len(thrust_value)):
                temp_list.append(thrust_value[i].strip())
            thrust_lsit.append(temp_list)
        pattern1 = re.compile(second_reguler)
        thrust_t = pattern1.findall(performance)
        if thrust_t:
            thrust_value = thrust_t[0].split('=')
            temp_list = []
            for i in range(len(thrust_value)):
                temp_list.append(thrust_value[i].strip())
            thrust_lsit.append(temp_list)
        return thrust_lsit





    def _get_airoperated_load(self, case_data):
        '''get data of airoperated load
        '''
        pattern = re.compile(r'BLADE SECTION ANGLE OF ATTACK\s+\(DEG\)\s+[\w\W]*BOUND CIRCULATION PEAKS')
        blade_data = pattern.findall(case_data)
        if len(blade_data) > 0:
            for blade in blade_data:
                return self._get_blade_list(blade)
        else:
            return '-'
                
    def _get_blade_list(self, blade_data):
        '''get data list of BLADE SECTION ANGLE OF ATTACK
        '''
        blade_list = []
        pattern = re.compile(r'RADIAL STATION+(\s+)+=+(\s+\d*.\d+)+')
        radial_station_list = []
        radial_temp_list = []
        for radial in pattern.finditer(blade_data):
            radial_list = radial.group().split(' ')
            del radial_list[0]
            del radial_list[0]
            for i in range(len(radial_list)):
                element = radial_list[i]
                filter1 = re.match(r'\.\d+', element)
                if filter1:
                    radial_temp_list.append(filter1.group().strip())
            radial_temp_list.append('A')
        if 'A' in radial_temp_list:
            flag_position = radial_temp_list.index('A')
        radial_station_list.append('PSI')
        for i in range(len(radial_temp_list)-flag_position):
            radial_station_list.append(radial_temp_list[i+flag_position])
        for i in range(flag_position):
            radial_station_list.append(radial_temp_list[i])
        for element in radial_station_list:
            if element == 'A':
                radial_station_list.remove(element)
        blade_list.append(radial_station_list)
        psi0 = self._get_psi('PSI\s+=\s+.0(\s+-?\d*.\d+)+', '.0', blade_data)
        if len(psi0) > 0:
            blade_list.append(psi0)
        psi15 = self._get_psi('PSI\s+=\s+15.0(\s+-?\d*.\d+)+', '15.0', blade_data)
        if len(psi15) > 0:
            blade_list.append(psi15)
        psi30 = self._get_psi('PSI\s+=\s+30.0(\s+-?\d*.\d+)+', '30.0', blade_data)
        if len(psi30) > 0:
            blade_list.append(psi30)
        psi45 = self._get_psi('PSI\s+=\s+45.0(\s+-?\d*.\d+)+', '45.0', blade_data)
        if len(psi45) > 0:
            blade_list.append(psi45)
        psi60 = self._get_psi('PSI\s+=\s+60.0(\s+-?\d*.\d+)+', '60.0', blade_data)
        if len(psi60) > 0:
            blade_list.append(psi60)
        psi75 = self._get_psi('PSI\s+=\s+75.0(\s+-?\d*.\d+)+', '75.0', blade_data)
        if len(psi75) > 0:
            blade_list.append(psi75)
        psi90 = self._get_psi('PSI\s+=\s+90.0(\s+-?\d*.\d+)+', '90.0', blade_data)
        if len(psi90) > 0:
            blade_list.append(psi90)
        psi105 = self._get_psi('PSI\s+=\s+105.0(\s+-?\d*.\d+)+', '105.0', blade_data)
        if len(psi105) > 0:
            blade_list.append(psi105)
        psi120 = self._get_psi('PSI\s+=\s+120.0(\s+-?\d*.\d+)+', '120.0', blade_data)
        if len(psi120) > 0:
            blade_list.append(psi120)
        psi135 = self._get_psi('PSI\s+=\s+135.0(\s+-?\d*.\d+)+', '135.0', blade_data)
        if len(psi135) > 0:
            blade_list.append(psi135)
        psi150 = self._get_psi('PSI\s+=\s+150.0(\s+-?\d*.\d+)+', '150.0', blade_data)
        if len(psi150) > 0:
            blade_list.append(psi150)
        psi165 = self._get_psi('PSI\s+=\s+165.0(\s+-?\d*.\d+)+', '165.0', blade_data)
        if len(psi165) > 0:
            blade_list.append(psi165)
        psi180 = self._get_psi('PSI\s+=\s+180.0(\s+-?\d*.\d+)+', '180.0', blade_data)
        if len(psi180) > 0:
            blade_list.append(psi180)
        psi195 = self._get_psi('PSI\s+=\s+195.0(\s+-?\d*.\d+)+', '195.0', blade_data)
        if len(psi195) > 0:
            blade_list.append(psi195)
        psi210 = self._get_psi('PSI\s+=\s+210.0(\s+-?\d*.\d+)+', '210.0', blade_data)
        if len(psi210) > 0:
            blade_list.append(psi210)
        psi225 = self._get_psi('PSI\s+=\s+225.0(\s+-?\d*.\d+)+', '225.0', blade_data)
        if len(psi225) > 0:
            blade_list.append(psi225)
        psi240 = self._get_psi('PSI\s+=\s+240.0(\s+-?\d*.\d+)+', '240.0', blade_data)
        if len(psi240) > 0:
            blade_list.append(psi240)
        psi255 = self._get_psi('PSI\s+=\s+255.0(\s+-?\d*.\d+)+', '255.0', blade_data)
        if len(psi255) > 0:
            blade_list.append(psi255)
        psi270 = self._get_psi('PSI\s+=\s+270.0(\s+-?\d*.\d+)+', '270.0', blade_data)
        if len(psi270) > 0:
            blade_list.append(psi270)
        psi285 = self._get_psi('PSI\s+=\s+285.0(\s+-?\d*.\d+)+', '285.0', blade_data)
        if len(psi285) > 0:
            blade_list.append(psi285)
        psi300 = self._get_psi('PSI\s+=\s+300.0(\s+-?\d*.\d+)+', '300.0', blade_data)
        if len(psi300) > 0:
            blade_list.append(psi300)
        psi315 = self._get_psi('PSI\s+=\s+315.0(\s+-?\d*.\d+)+', '315.0', blade_data)
        if len(psi315) > 0:
            blade_list.append(psi315)
        psi330 = self._get_psi('PSI\s+=\s+330.0(\s+-?\d*.\d+)+', '330.0', blade_data)
        if len(psi330) > 0:
            blade_list.append(psi330)
        psi345 = self._get_psi('PSI\s+=\s+345.0(\s+-?\d*.\d+)+', '345.0', blade_data)
        if len(psi345) > 0:
            blade_list.append(psi345)
        psi360 = self._get_psi('PSI\s+=\s+360.0(\s+-?\d*.\d+)+', '360.0', blade_data)
        if len(psi360) > 0:
            blade_list.append(psi360)
        return blade_list

    def _get_psi(self, reguler, frist_value, blade_data):
        '''get data of psi
        '''
        pattern = re.compile(reguler)
        psi_data_list = []
        psi_temp_list = []
        for psi in pattern.finditer(blade_data):
            for element in psi.group().split(' '):
                filter1 = re.match(r'-?\d*\.\d+', element)
                if filter1:
                    psi_temp_list.append(filter1.group().strip())
            if 'A' in psi_temp_list:
                psi_temp_list.pop(psi_temp_list.index('A')+1)
            psi_temp_list.append('A')
        psi_temp_list.pop(0)
        if len(psi_temp_list) > 0:
            if 'A' in psi_temp_list:
                flag_position = psi_temp_list.index('A')
            psi_data_list.append(frist_value)
            for i in range(len(psi_temp_list) - flag_position):
                psi_data_list.append(psi_temp_list[i + flag_position])
            for i in range(flag_position):
                psi_data_list.append(psi_temp_list[i])
            for element in psi_data_list:
                if element == 'A':
                    psi_data_list.remove(element)
            return psi_data_list
        else:
            return []
        






    def _get_rotor_wake(self, case_data):
        '''get data of rotor wake
        '''
        rotor_wake_dic = {}
        wake_geometry = []
        pattern = re.compile(r'OUTPUT OF PART = ROTOR \d+ WAKE GEOMETRY DISPLAY\s[\w\W]*?SOLUTION KIND')
        wake_geometry_explain_data =  pattern.findall(case_data)
        if len(wake_geometry_explain_data) > 0:
            for wake_geometry_explain in wake_geometry_explain_data:
                wake_geometry_temp = self._get_wake_geometry_explain_list(wake_geometry_explain)
                if len(wake_geometry_temp) > 0:
                    wake_geometry.append(wake_geometry_temp)
                
        pattern1 = re.compile(r'MOTION = DOF = DIFFERENCE[\s+\S+]+\d+COMPUTATION TIMES')
        wake_geometry_definite_data = pattern1.findall(case_data)
        if len(wake_geometry_definite_data) > 0:
            for wake_geometry_definite in wake_geometry_definite_data:
                wake_geometry.append(self._get_wake_geometry_definite_list(wake_geometry_definite))
                
        if len(wake_geometry) > 0:
            rotor_wake_dic['wake_geometry'] = wake_geometry
         
        pattern2 = re.compile(r'QUANTITY DEFINITION:\s+INDUCED VELOCITY.*?NUMBER OF SPAN STATIONS.*?NUMBER OF SPAN STATIONS', re.S)
        induced_velocity_data = pattern2.findall(case_data)
        if len(induced_velocity_data) > 0:
            for induced_velocity in induced_velocity_data:
                rotor_wake_dic['induced_velocity'] = self._get_induced_velocity_list(induced_velocity)
        
        if len(rotor_wake_dic) > 0:
            return rotor_wake_dic
        else:
            return '-'
            
    def _get_wake_geometry_explain_list(self, geometry_data):
        '''get data of wake geometry
        '''
        wake_geometry_explain_list = []
        l_vortex = self._get_common_geometry(r'RTL\([\S+\s+]+LEFT TIP VORTEX$', geometry_data)
        if len(l_vortex) > 0:
            wake_geometry_explain_list.append(l_vortex)
        r_vortex = self._get_common_geometry(r'RTR\([\S+\s+]+RIGHT TIP VORTEX$', geometry_data)
        if len(r_vortex) > 0:
            wake_geometry_explain_list.append(r_vortex)
        l_sheet = self._get_common_geometry(r'RSL\([\S+\s+]+LEFT EDGE INBOARD SHEET$', geometry_data)
        if len(l_sheet) > 0:
            wake_geometry_explain_list.append(l_sheet)
        r_sheet = self._get_common_geometry(r'RSR\([\S+\s+]+RIGHT EDGE INBOARD SHEET$', geometry_data)
        if len(r_sheet) > 0:
            wake_geometry_explain_list.append(r_sheet)
        stations = self._get_common_geometry(r'RA\([\S+\s+]+WING SPAN STATIONS, I = 0 TO NPANEL\+1$', geometry_data)
        if len(stations) > 0:
            wake_geometry_explain_list.append(stations)
        
        pattern = re.compile(r'KTWG\s+=[\s+\S+]+NTRAIL\s+=\s+\d+')
        var_value_temp_list = []
        for var_value in pattern.finditer(geometry_data):
            for element in var_value.group().split(','):
                element = self._del_space(element)
                var_value_temp_list.append(element)
        if len(var_value_temp_list) > 0:
            wake_geometry_explain_list.append(var_value_temp_list)
        return wake_geometry_explain_list
    
    def _get_common_geometry(self, regular, geometry_data):
        '''get common data of geometry
        '''
        pattern = re.compile(regular, re.M)
        common_list = []
        for common in pattern.finditer(geometry_data):
            for element in common.group().split('  '):
                element = element.strip()
                filter1 = re.match(r'.+', element)
                if filter1:
                    common_list.append(filter1.group())
        return common_list

    def _get_wake_geometry_definite_list(self, wake_geometry_definite_data):
        '''get data list of motion value
        '''
        pattern = re.compile(r'MOTION VALUE\s+[\w+\s+\d+]+$', re.M)
        motion_value = []
        motion_head_list = []
        motion_head_list.append('PSI')
        for motion_value_head in pattern.finditer(wake_geometry_definite_data):
            for element in motion_value_head.group().split(' '):
                head = re.match(r'\d+', element)
                if head:
                    motion_head_list.append(head.group())
        if len(motion_head_list) > 0:
            motion_value.append(motion_head_list)
        psi0 = self._get_value_list(r'PSI =\s+.000[\s+-?\d+.?\d+E?-?\d*]+$', '.000', wake_geometry_definite_data)
        if len(psi0) > 0:
            motion_value.append(psi0)
        psi15 = self._get_value_list(r'PSI =\s+15.000[\s+-?\d+.?\d+E?-?\d*]+$', '15.000', wake_geometry_definite_data)
        if len(psi15) > 0:
            motion_value.append(psi15)
        psi30 = self._get_value_list(r'PSI =\s+30.000[\s+-?\d+.?\d+E?-?\d*]+$', '30.000', wake_geometry_definite_data)
        if len(psi30) > 0:
            motion_value.append(psi30)
        psi45 = self._get_value_list(r'PSI =\s+45.000[\s+-?\d+.?\d+E?-?\d*]+$', '45.000', wake_geometry_definite_data)
        if len(psi45) > 0:
            motion_value.append(psi45)
        psi60 = self._get_value_list(r'PSI =\s+60.000[\s+-?\d+.?\d+E?-?\d*]+$', '60.000', wake_geometry_definite_data)
        if len(psi60) > 0:
            motion_value.append(psi60)
        psi75 = self._get_value_list(r'PSI =\s+75.000[\s+-?\d+.?\d+E?-?\d*]+$', '75.000', wake_geometry_definite_data)
        if len(psi75) > 0:
            motion_value.append(psi75)
        psi90 = self._get_value_list(r'PSI =\s+90.000[\s+-?\d+.?\d+E?-?\d*]+$', '90.000', wake_geometry_definite_data)
        if len(psi90) > 0:
            motion_value.append(psi90)
        psi105 = self._get_value_list(r'PSI =\s+105.000[\s+-?\d+.?\d+E?-?\d*]+$', '105.000', wake_geometry_definite_data)
        if len(psi105) > 0:
            motion_value.append(psi105)
        psi120 = self._get_value_list(r'PSI =\s+120.000[\s+-?\d+.?\d+E?-?\d*]+$', '120.000', wake_geometry_definite_data)
        if len(psi120) > 0:
            motion_value.append(psi120)
        psi135 = self._get_value_list(r'PSI =\s+135.000[\s+-?\d+.?\d+E?-?\d*]+$', '135.000', wake_geometry_definite_data)
        if len(psi135) > 0:
            motion_value.append(psi135)
        psi150 = self._get_value_list(r'PSI =\s+150.000[\s+-?\d+.?\d+E?-?\d*]+$', '150.000', wake_geometry_definite_data)
        if len(psi150) > 0:
            motion_value.append(psi150)
        psi165 = self._get_value_list(r'PSI =\s+165.000[\s+-?\d+.?\d+E?-?\d*]+$', '165.000', wake_geometry_definite_data)
        if len(psi165) > 0:
            motion_value.append(psi165)
        psi180 = self._get_value_list(r'PSI =\s+180.000[\s+-?\d+.?\d+E?-?\d*]+$', '180.000', wake_geometry_definite_data)
        if len(psi180) > 0:
            motion_value.append(psi180)
        psi195 = self._get_value_list(r'PSI =\s+195.000[\s+-?\d+.?\d+E?-?\d*]+$', '195.000', wake_geometry_definite_data)
        if len(psi195) > 0:
            motion_value.append(psi195)
        psi210 = self._get_value_list(r'PSI =\s+210.000[\s+-?\d+.?\d+E?-?\d*]+$', '210.000', wake_geometry_definite_data)
        if len(psi210) > 0:
            motion_value.append(psi210)
        psi225 = self._get_value_list(r'PSI =\s+225.000[\s+-?\d+.?\d+E?-?\d*]+$', '225.000', wake_geometry_definite_data)
        if len(psi225) > 0:
            motion_value.append(psi225)
        psi240 = self._get_value_list(r'PSI =\s+240.000[\s+-?\d+.?\d+E?-?\d*]+$', '240.000', wake_geometry_definite_data)
        if len(psi240) > 0:
            motion_value.append(psi240)
        psi255 = self._get_value_list(r'PSI =\s+255.000[\s+-?\d+.?\d+E?-?\d*]+$', '255.000', wake_geometry_definite_data)
        if len(psi255) > 0:
            motion_value.append(psi255)
        psi270 = self._get_value_list(r'PSI =\s+270.000[\s+-?\d+.?\d+E?-?\d*]+$', '270.000', wake_geometry_definite_data)
        if len(psi270) > 0:
            motion_value.append(psi270)
        psi285 = self._get_value_list(r'PSI =\s+285.000[\s+-?\d+.?\d+E?-?\d*]+$', '285.000', wake_geometry_definite_data)
        if len(psi285) > 0:
            motion_value.append(psi285)
        psi300 = self._get_value_list(r'PSI =\s+300.000[\s+-?\d+.?\d+E?-?\d*]+$', '300.000', wake_geometry_definite_data)
        if len(psi300) > 0:
            motion_value.append(psi300)
        psi315 = self._get_value_list(r'PSI =\s+315.000[\s+-?\d+.?\d+E?-?\d*]+$', '315.000', wake_geometry_definite_data)
        if len(psi315) > 0:
            motion_value.append(psi315)
        psi330 = self._get_value_list(r'PSI =\s+330.000[\s+-?\d+.?\d+E?-?\d*]+$', '330.000', wake_geometry_definite_data)
        if len(psi330) > 0:
            motion_value.append(psi330)
        psi345 = self._get_value_list(r'PSI =\s+345.000[\s+-?\d+.?\d+E?-?\d*]+$', '345.000', wake_geometry_definite_data)
        if len(psi345) > 0:
            motion_value.append(psi345)
        psi360 = self._get_value_list(r'PSI =\s+360.000[\s+-?\d+.?\d+E?-?\d*]+$', '360.000', wake_geometry_definite_data)
        if len(psi360) > 0:
            motion_value.append(psi360)
        return motion_value
    
    def _get_induced_velocity_list(self, induced_velocity_data):
        '''get data of induced velocity
        '''
        induced_velocity_list = []
        pattern = re.compile(r'SPAN STATION\s+.*')
        station_data = pattern.findall(induced_velocity_data)
        station_temp_list = []
        if len(station_data) > 0:
            for station in station_data:
                for element in station.split('  '):
                    filter1 = re.match(r'.+', element)
                    if filter1:
                        station_temp_list.append(filter1.group().strip())
        station_list = sorted(set(station_temp_list),key=station_temp_list.index)
        induced_velocity_list.append(station_list)
        psi0 = self._get_value_list(r'PSI =\s+\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '.000',induced_velocity_data)
        if len(station_list) == len(psi0):
            induced_velocity_list.append(psi0)
        psi15 = self._get_value_list(r'PSI =\s+15\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '15.000',induced_velocity_data)
        if len(station_list) == len(psi15):
            induced_velocity_list.append(psi15)
        psi30 = self._get_value_list(r'PSI =\s+30\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '30.000',induced_velocity_data)
        if len(station_list) == len(psi30):
            induced_velocity_list.append(psi30)
        psi45 = self._get_value_list(r'PSI =\s+45\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '45.000',induced_velocity_data)
        if len(station_list) == len(psi45):
            induced_velocity_list.append(psi45)
        psi60 = self._get_value_list(r'PSI =\s+60\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '60.000',induced_velocity_data)
        if len(station_list) == len(psi60):
            induced_velocity_list.append(psi60)
        psi75 = self._get_value_list(r'PSI =\s+75\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '75.000',induced_velocity_data)
        if len(station_list) == len(psi75):
            induced_velocity_list.append(psi75)
        psi90 = self._get_value_list(r'PSI =\s+90\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '90.000',induced_velocity_data)
        if len(station_list) == len(psi90):
            induced_velocity_list.append(psi90)
        psi105 = self._get_value_list(r'PSI =\s+105\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '105.000',induced_velocity_data)
        if len(station_list) == len(psi105):
            induced_velocity_list.append(psi105)
        psi120 = self._get_value_list(r'PSI =\s+120\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '120.000',induced_velocity_data)
        if len(station_list) == len(psi120):
            induced_velocity_list.append(psi120)
        psi135 = self._get_value_list(r'PSI =\s+135\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '135.000',induced_velocity_data)
        if len(station_list) == len(psi135):
            induced_velocity_list.append(psi135)
        psi150 = self._get_value_list(r'PSI =\s+150\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '150.000',induced_velocity_data)
        if len(station_list) == len(psi150):
            induced_velocity_list.append(psi150)
        psi165 = self._get_value_list(r'PSI =\s+165\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '165.000',induced_velocity_data)
        if len(station_list) == len(psi165):
            induced_velocity_list.append(psi165)
        psi180 = self._get_value_list(r'PSI =\s+180\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '180.000',induced_velocity_data)
        if len(station_list) == len(psi180):
            induced_velocity_list.append(psi180)
        psi195 = self._get_value_list(r'PSI =\s+195\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '195.000',induced_velocity_data)
        if len(station_list) == len(psi195):
            induced_velocity_list.append(psi195)
        psi210 = self._get_value_list(r'PSI =\s+210\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '210.000',induced_velocity_data)
        if len(station_list) == len(psi210):
            induced_velocity_list.append(psi210)
        psi225 = self._get_value_list(r'PSI =\s+225\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '225.000',induced_velocity_data)
        if len(station_list) == len(psi225):
            induced_velocity_list.append(psi225)
        psi240 = self._get_value_list(r'PSI =\s+240\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '240.000',induced_velocity_data)
        if len(station_list) == len(psi240):
            induced_velocity_list.append(psi240)
        psi255 = self._get_value_list(r'PSI =\s+255\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '255.000',induced_velocity_data)
        if len(station_list) == len(psi255):
            induced_velocity_list.append(psi255)
        psi270 = self._get_value_list(r'PSI =\s+270\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '270.000',induced_velocity_data)
        if len(station_list) == len(psi270):
            induced_velocity_list.append(psi270)
        psi285 = self._get_value_list(r'PSI =\s+285\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '285.000',induced_velocity_data)
        if len(station_list) == len(psi285):
            induced_velocity_list.append(psi285)
        psi300 = self._get_value_list(r'PSI =\s+300\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '300.000',induced_velocity_data)
        if len(station_list) == len(psi300):
            induced_velocity_list.append(psi300)
        psi315 = self._get_value_list(r'PSI =\s+315\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '315.000',induced_velocity_data)
        if len(station_list) == len(psi315):
            induced_velocity_list.append(psi315)
        psi330 = self._get_value_list(r'PSI =\s+330\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '330.000',induced_velocity_data)
        if len(station_list) == len(psi330):
            induced_velocity_list.append(psi330)
        psi345 = self._get_value_list(r'PSI =\s+345\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '345.000',induced_velocity_data)
        if len(station_list) == len(psi345):
            induced_velocity_list.append(psi345)
        psi360 = self._get_value_list(r'PSI =\s+360\.000[\s+-?\d*\.?\d+E?-?\d*]+$', '360.000',induced_velocity_data)
        if len(station_list) == len(psi360):
            induced_velocity_list.append(psi360)
        return induced_velocity_list

    def _get_value_list(self, regular, first_value, motion_value_data):
        '''get every data of every angle in motion
        '''
        pattern = re.compile(regular, re.M)
        value_list = []
        value_list.append(first_value)
        for value in pattern.finditer(motion_value_data):
            for element in value.group().split(' '):
                value = re.match(r'-?\d*\.?\d+E?-?\d+', element)
                if value:
                    if not value.group() == first_value:
                        value_list.append(value.group())
        return value_list




    def _get_structrue_load(self, case_data):
        '''get data of structrue load
        '''
        structrue_load_dic = {}
        structrue_load_value_dic = {}
        pattern = re.compile(r'OUTPUT = ROTOR\s+\d+\s+BLADE\s+\d+\s+LOAD\s+\.\d+R.*?WRITING', re.S)
        blade_load_data = pattern.findall(case_data)
        if len(blade_load_data) > 0:
            for blade_load in blade_load_data:
                blade_load_dic = self._get_blade_load_dic(blade_load)
                for key in blade_load_dic:
                    structrue_load_value_dic[key] = blade_load_dic[key]
        if len(structrue_load_value_dic) > 0:
            structrue_load_dic['blade_load'] = structrue_load_value_dic
        if len(structrue_load_dic) > 0:
            return structrue_load_dic
        else:
            return '-'
                
    def _get_blade_load_dic(self, blade_load_data):
        '''get data dictionary of blade load
        '''
        blade_load_dic = {}
        bladu_load_value_dic = {}
        blade_load_key = ''
        blade_load_temp = re.search(r'\d+\s+BLADE\s+\d+\s+LOAD\s+\.?\d+R\s+(D|F)', blade_load_data)
        if blade_load_temp:
            blade_load_key = blade_load_temp.group()
        if len(str(blade_load_key)) != 0:
            pattern = re.compile(r'MOTION VALUE\s+[\w\W]*?F NORM')
            motion_temp_list = []
            average_temp_list = []
            for motion in pattern.finditer(blade_load_data):
                for element in motion.group().split('  '):
                    filter1 = re.match(r'.+', element)
                    if filter1:
                        motion_temp_list.append(filter1.group().strip())
            if len(motion_temp_list) > 0:
                average_temp_list.append(motion_temp_list)
                
            mean = self._get_blade_load_statistics('MEAN\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(mean) > 0:
                average_temp_list.append(mean)
            maximum = self._get_blade_load_statistics('MAXIMUM\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(maximum) > 0:
                average_temp_list.append(maximum)
            minimum = self._get_blade_load_statistics('MINIMUM\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(minimum) > 0:
                average_temp_list.append(minimum)
            bladu_load_value_dic['average'] = average_temp_list
            
            psi_temp_list = []
            if len(motion_temp_list) > 0:
                psi_temp_list.append(motion_temp_list)
            psi0 = self._get_blade_load_psi('PSI =\s+\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi0) > 0:
                psi_temp_list.append(psi0)
            psi15 = self._get_blade_load_psi('PSI =\s+15\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi15) > 0:
                psi_temp_list.append(psi15)
            psi30 = self._get_blade_load_psi('PSI =\s+30\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi30) > 0:
                psi_temp_list.append(psi30)
            psi45 = self._get_blade_load_psi('PSI =\s+45\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi45) > 0:
                psi_temp_list.append(psi45)
            psi60 = self._get_blade_load_psi('PSI =\s+60\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi60) > 0:
                psi_temp_list.append(psi60)
            psi75 = self._get_blade_load_psi('PSI =\s+75\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi75) > 0:
                psi_temp_list.append(psi75)
            psi90 = self._get_blade_load_psi('PSI =\s+90\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi90) > 0:
                psi_temp_list.append(psi90)
            psi105 = self._get_blade_load_psi('PSI =\s+105\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi105) > 0:
                psi_temp_list.append(psi105)
            psi120 = self._get_blade_load_psi('PSI =\s+120\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi120) > 0:
                psi_temp_list.append(psi120)
            psi135 = self._get_blade_load_psi('PSI =\s+135\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi135) > 0:
                psi_temp_list.append(psi135)
            psi150 = self._get_blade_load_psi('PSI =\s+150\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi150) > 0:
                psi_temp_list.append(psi150)
            psi165 = self._get_blade_load_psi('PSI =\s+165\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi165) > 0:
                psi_temp_list.append(psi165)
            psi180 = self._get_blade_load_psi('PSI =\s+180\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi180) > 0:
                psi_temp_list.append(psi180)
            psi195 = self._get_blade_load_psi('PSI =\s+195\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi195) > 0:
                psi_temp_list.append(psi195)
            psi210 = self._get_blade_load_psi('PSI =\s+210\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi210) > 0:
                psi_temp_list.append(psi210)
            psi225 = self._get_blade_load_psi('PSI =\s+225\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi225) > 0:
                psi_temp_list.append(psi225)
            psi240 = self._get_blade_load_psi('PSI =\s+240\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi240) > 0:
                psi_temp_list.append(psi240)
            psi255 = self._get_blade_load_psi('PSI =\s+255\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi255) > 0:
                psi_temp_list.append(psi255)
            psi270 = self._get_blade_load_psi('PSI =\s+270\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi270) > 0:
                psi_temp_list.append(psi270)
            psi285 = self._get_blade_load_psi('PSI =\s+285\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi285) > 0:
                psi_temp_list.append(psi285)
            psi300 = self._get_blade_load_psi('PSI =\s+300\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi300) > 0:
                psi_temp_list.append(psi300)
            psi315 = self._get_blade_load_psi('PSI =\s+315\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi315) > 0:
                psi_temp_list.append(psi315)
            psi330 = self._get_blade_load_psi('PSI =\s+330\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi330) > 0:
                psi_temp_list.append(psi330)
            psi345 = self._get_blade_load_psi('PSI =\s+345\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi345) > 0:
                psi_temp_list.append(psi345)
            psi360 = self._get_blade_load_psi('PSI =\s+360\.000\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(psi360) > 0:
                psi_temp_list.append(psi360)
            bladu_load_value_dic['time_history'] = psi_temp_list
            
            harmonics_temp_list = []
            if len(motion_temp_list) > 0:
                harmonics_temp_list.append(motion_temp_list)
            cos1 = self._get_blade_load_harmonics('COSINE\s+1\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos1) > 0:
                harmonics_temp_list.append(cos1)
            sin1 = self._get_blade_load_harmonics('\sSINE\s+1\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin1) > 0:
                harmonics_temp_list.append(sin1)
            cos2 = self._get_blade_load_harmonics('COSINE\s+2\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos2) > 0:
                harmonics_temp_list.append(cos2)
            sin2 = self._get_blade_load_harmonics('\sSINE\s+2\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin2) > 0:
                harmonics_temp_list.append(sin2)
            cos3 = self._get_blade_load_harmonics('COSINE\s+3\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos3) > 0:
                harmonics_temp_list.append(cos3)
            sin3 = self._get_blade_load_harmonics('\sSINE\s+3\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin3) > 0:
                harmonics_temp_list.append(sin3)
            cos4 = self._get_blade_load_harmonics('COSINE\s+4\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos4) > 0:
                harmonics_temp_list.append(cos4)
            sin4 = self._get_blade_load_harmonics('\sSINE\s+4\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin4) > 0:
                harmonics_temp_list.append(sin4)
            cos5 = self._get_blade_load_harmonics('COSINE\s+5\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos5) > 0:
                harmonics_temp_list.append(cos5)
            sin5 = self._get_blade_load_harmonics('\sSINE\s+5\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin5) > 0:
                harmonics_temp_list.append(sin5)
            cos6 = self._get_blade_load_harmonics('COSINE\s+6\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos6) > 0:
                harmonics_temp_list.append(cos6)
            sin6 = self._get_blade_load_harmonics('\sSINE\s+6\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin6) > 0:
                harmonics_temp_list.append(sin6)
            cos7 = self._get_blade_load_harmonics('COSINE\s+7\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos7) > 0:
                harmonics_temp_list.append(cos7)
            sin7 = self._get_blade_load_harmonics('\sSINE\s+7\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin7) > 0:
                harmonics_temp_list.append(sin7)
            cos8 = self._get_blade_load_harmonics('COSINE\s+8\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos8) > 0:
                harmonics_temp_list.append(cos8)
            sin8 = self._get_blade_load_harmonics('\sSINE\s+8\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin8) > 0:
                harmonics_temp_list.append(sin8)
            cos9 = self._get_blade_load_harmonics('COSINE\s+9\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos9) > 0:
                harmonics_temp_list.append(cos9)
            sin9 = self._get_blade_load_harmonics('\sSINE\s+9\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin9) > 0:
                harmonics_temp_list.append(sin9)
            cos10 = self._get_blade_load_harmonics('COSINE\s+10\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(cos10) > 0:
                harmonics_temp_list.append(cos10)
            sin10 = self._get_blade_load_harmonics('\sSINE\s+10\s+(-?\d*\.?\d+E?[-\+]?\d*\s+)+', blade_load_data)
            if len(sin10) > 0:
                harmonics_temp_list.append(sin10)
            bladu_load_value_dic['harmonics'] = harmonics_temp_list
            
            blade_load_dic[blade_load_key] = bladu_load_value_dic
            return blade_load_dic
        else:
            return '-'
        
    def _get_blade_load_statistics(self, regular, blade_load_data):
        '''get blade load statisticcs list of blade load
        '''
        pattern = re.compile(regular, re.M)
        statistics_data = ''
        for statistics in pattern.finditer(blade_load_data):
            statistics_data = statistics.group()
            break
        if statistics_data != '':
            statistics_temp_list = statistics_data.split(' ')
            statistics_list = []
            for element in statistics_temp_list:
                filter1 = re.match(r'.+', element)
                if filter1:
                    statistics_list.append(filter1.group())
            return statistics_list
        else:
            return []

    def _get_blade_load_psi(self, regular, blade_load_data):
        '''get blade load psi list of blade load
        '''
        pattern = re.compile(regular, re.M)
        psi_data = ''
        for psi in pattern.finditer(blade_load_data):
            psi_data = psi.group()
        if psi_data != '':
            psi_temp_list = psi_data.split(' ')
            psi_list = []
            for element in psi_temp_list:
                filter1 = re.match(r'.+', element)
                if filter1:
                    psi_list.append(filter1.group())
            del psi_list[0]
            del psi_list[0]
            return psi_list
        else:
            return []

    def _get_blade_load_harmonics(self, regular, blade_load_data):
        '''get blade load harmonics list of blade load
        '''
        pattern = re.compile(regular)
        harmonics_list = []
        for harmonics in pattern.finditer(blade_load_data):
            for element in harmonics.group().split(' '):
                filter1 = re.match(r'.*\w$', element)
                if filter1:
                    harmonics_list.append(filter1.group())
        harmonics_list[0] = harmonics_list[0] + "=" + harmonics_list[1]
        del harmonics_list[1]
        return harmonics_list














    def _del_space(self, string):
        '''delete all of space in string
        '''
        string_list = string.split(' ')
        return ''.join(string_list) 



     
    def get_result(self, file_name):
        '''get result of fetching data from file_name file.
        the result is a dictionary, the key is 1,2 up to the number of case and the value is content of case.
        '''
        text = self._read_file(file_name)
        result = {}
        if text != '':
            case_num = self._get_case_num(text)
            is_case_num, all_case_context = self._get_case_context(text)
            i = 1
            if case_num[0] == str(is_case_num):
                for case_context_temp in all_case_context:
                    case_context = self._get_every_case_context(case_context_temp)
                    result[i] = case_context
                    i = i + 1
                return result
            else:
                print 'the number of case is wrong!'
        else:
            print "no data"
            
            
if __name__ == "__main__":
    file_name = 'E:\workspacess\get_data\src\get_all_data\moxing-coll-speed120.out'
    get_data = get_all_data(file_name)
    from time import time
    start = time()
    result = get_data.get_result(get_data.file_name)
    end = time()
    print end - start
    
