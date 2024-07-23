def loadData(env, gui = None):
    if not gui == None:
        for i in range(3):
            gui.addElement()
    else:
        for i in range(3):
            env.io.addObject()
    import_result  = [None]*3
    import_result[0] = loadData_0(env.io.import_objects[0])
    import_result[1] = loadData_1(env.io.import_objects[1])
    import_result[2] = loadData_2(env.io.import_objects[2])
    passed = all([all([subelement[0] for subelement in element]) for element in import_result])
    if not gui == None:
        for i in range(3):
            gui.setCurrentElement(i)
            if passed:
                gui.populate()
    else:
        for i in range(3):
            if passed:
                env.io.import_objects[i].processObject()
    return import_result

def loadData_0(import_object):
    #################################
    ########## add element ##########
    current_object  = import_object
    meta_files_found = [True,'']
    data_files_found = [True,'']
    
    ########## The meta info ##########
    try:
        path = ''
        current_object.meta_handler.buildMeta(path)
        selected_meta = [
            ['cbox_0a_fg_freq_value' ,'Hz' ,'Freq. first' ,'1' ,'' ],
            ['cbox_0b_fg_freq_value' ,'Hz' ,'Freq. second' ,'1' ,'' ],
            ['psd_distance_value' ,'m' ,'lsd' ,'1e9' ,'' ],
            ['selector_lambda_value' ,'A' ,'Wavelength' ,'1e-10' ,'8' ],
            ['monitor1' ,'' ,'Monitor' ,'1' ,'' ]]
        current_object.meta_handler.selected_meta = selected_meta
    except:
        meta_files_found = [False,path]
    
    ########## The file paths ##########
    common_path = ''
    path_list = [
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120970.tof',
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120971.tof',
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120972.tof']
    if current_object.file_handler.filesExist([
        os.path.join(common_path,item) for item in path_list]):
        current_object.file_handler.addFiles([
            os.path.join(common_path,item) for item in path_list])
    else:
        data_files_found = [False,common_path]
    ########## The data handler ##########
    current_object.data_handler.dimension = [8, 16, 128, 128]
    current_object.data_handler.parameter = 'ref'
    current_object.data_handler.meas = '0'
    current_object.data_handler.reference = True
    current_object.data_handler.background = False
    return [meta_files_found, data_files_found]

def loadData_1(import_object):
    #################################
    ########## add element ##########
    current_object  = import_object
    meta_files_found = [True,'']
    data_files_found = [True,'']
    
    ########## The meta info ##########
    try:
        path = ''
        current_object.meta_handler.buildMeta(path)
        selected_meta = [
            ['cbox_0a_fg_freq_value' ,'Hz' ,'Freq. first' ,'1' ,'' ],
            ['cbox_0b_fg_freq_value' ,'Hz' ,'Freq. second' ,'1' ,'' ],
            ['psd_distance_value' ,'m' ,'lsd' ,'1e9' ,'' ],
            ['selector_lambda_value' ,'A' ,'Wavelength' ,'1e-10' ,'' ],
            ['monitor1' ,'' ,'Monitor' ,'1' ,'' ]]
        current_object.meta_handler.selected_meta = selected_meta
    except:
        meta_files_found = [False,path]
    
    ########## The file paths ##########
    common_path = ''
    path_list = [
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120954.tof',
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120959.tof',
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120960.tof']
    if current_object.file_handler.filesExist([
        os.path.join(common_path,item) for item in path_list]):
        current_object.file_handler.addFiles([
            os.path.join(common_path,item) for item in path_list])
    else:
        data_files_found = [False,common_path]
    ########## The data handler ##########
    current_object.data_handler.dimension = [8, 16, 128, 128]
    current_object.data_handler.parameter = '5k'
    current_object.data_handler.meas = '0'
    current_object.data_handler.reference = False
    current_object.data_handler.background = False
    return [meta_files_found, data_files_found]

def loadData_2(import_object):
    #################################
    ########## add element ##########
    current_object  = import_object
    meta_files_found = [True,'']
    data_files_found = [True,'']
    
    ########## The meta info ##########
    try:
        path = ''
        current_object.meta_handler.buildMeta(path)
        selected_meta = [
            ['cbox_0a_fg_freq_value' ,'Hz' ,'Freq. first' ,'1' ,'' ],
            ['cbox_0b_fg_freq_value' ,'Hz' ,'Freq. second' ,'1' ,'' ],
            ['psd_distance_value' ,'m' ,'lsd' ,'1e9' ,'' ],
            ['selector_lambda_value' ,'A' ,'Wavelength' ,'1e-10' ,'8' ],
            ['monitor1' ,'' ,'Monitor' ,'1' ,'' ]]
        current_object.meta_handler.selected_meta = selected_meta
    except:
        meta_files_found = [False,path]
    
    ########## The file paths ##########
    common_path = ''
    path_list = [
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120955.tof',
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120961.tof',
        'C:/Users/alexs/PycharmProjects/MIEZEPY/miezepy/tests/ressources/00120964.tof']
    if current_object.file_handler.filesExist([
        os.path.join(common_path,item) for item in path_list]):
        current_object.file_handler.addFiles([
            os.path.join(common_path,item) for item in path_list])
    else:
        data_files_found = [False,common_path]
    ########## The data handler ##########
    current_object.data_handler.dimension = [8, 16, 128, 128]
    current_object.data_handler.parameter = '50k'
    current_object.data_handler.meas = '0'
    current_object.data_handler.reference = False
    current_object.data_handler.background = False
    return [meta_files_found, data_files_found]
