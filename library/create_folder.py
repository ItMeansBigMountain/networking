#!/usr/bin/python


'''
    Documentation:
        Description: creates folder in parameter specified in FILE.yml parameter
        
        Parameter: [ 'pt' ]
        
    # hint: you cannot use print or use quit!
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
    pt = module.params['pt']                      
    




    #code start -------------------------------------------
    x = os.system(f'mkdir -p {pt}')

        
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