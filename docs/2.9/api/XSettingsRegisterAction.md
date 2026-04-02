# XSettingsRegisterAction

     Registers Addons
     
    

  
Parameter | Description  
---|---  
path | 
    
    
    path where the addon is in (..\addon\1.0.0).
      
  
installFile | 
    
    
    or the complete path to the install.xml.
      
  
  
Remarks


  
Example
    
    
     Registering Add-ons with the path in which the addon is located
            
                    XSettingsRegisterAction /Path:c:\MyAddOn
            
     Registering Add-ons with the complete path of the instal.xml file
            
                    XSettingsRegisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml
