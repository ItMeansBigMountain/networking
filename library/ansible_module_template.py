#!/usr/bin/python


'''
    Documentation:
        Description: CHANGE CODE SECTION IN MAIN()
        
        Parameter: FOUND IN YAML FILE
        
    # hint: you cannot use print or use quit!
    
    # within project folder, have a library folder with all python scripts...
    # cd into project folder and run yml playbook who will call on python module

    # make sure ansible is configigured by having host file & ansible.cfg in project folder
    
    # ansible.cfg
        inventory=./hosts
'''

import os,sys

from ansible.module_utils.basic import AnsibleModule        
from ansible.module_utils._text import to_bytes, to_native   

def main():
    
    module_args = dict( pt=dict(required=True, type='str') )

    # CREATE ANSIBLE OBJECT  
    module = AnsibleModule(                             
        argument_spec=module_args,                
        supports_check_mode=False                 
    )

    #  YAML PARAMETERS
    var1 = module.params['var1']                      
    var2 = module.params['var2']                      
    




    #code start -------------------------------------------
    x = os.system(f'ls')

        
    # code end -------------------------------------------
    


    # ERROR CHECK
    if x == 0:
        noerror = True
    else:
        noerror = False

    if noerror:                                   
        result = dict(                           
            changed=True,                            
            Response=f'Success create folder {pt}!'   
        )                                              
        module.exit_json(**result)                    
    else:
        module.fail_json(msg=f'Error create folder with error code {x}!')     
    
    




# calling fucntions down here
if __name__ == '__main__':
    main()